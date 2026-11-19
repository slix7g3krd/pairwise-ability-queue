"""第 61 批：技能输入缓冲与施法状态机修复。

覆盖 13 类问题：长按去重、阶段计时、延迟取消、动画事件对齐、
冷却回滚、资源校验、打断优先级、队列上限、设备阈值、阶段同步、
事件幂等、场景清理、时间缩放（另含长按重复与施法阶段合法性两个
辅助判定，共 15 个契约函数）。
"""


def input_edge(previous, current):
    """长按去重：仅在松开->按下的上升沿触发一次，长按期间不重复触发。"""
    return bool(current and not previous)


def advance_phase(phase, timer, dt, threshold):
    """阶段计时：每个阶段独立计时器，累计达到阈值才推进到下一阶段，
    避免前摇/判定期/后摇共用计时器导致的阶段切换丢事件。"""
    if timer + dt >= threshold:
        return phase + 1
    return phase


def cancel_window(remaining, latency):
    """延迟取消：取消窗口扣除网络延迟，客户端可取消帧数不得超过
    服务器结算前的真实剩余窗口。"""
    return remaining - latency


def anim_event(frame, event_frame):
    """动画事件：逻辑帧推进到动画命中帧（或已越过）时事件才生效，
    保证动画与逻辑状态对齐、命中帧不错位。"""
    return frame >= event_frame


def cooldown_rollback(cooldown, accepted):
    """冷却回滚：服务器拒绝施法时回滚客户端预扣的冷却；接受则保留。"""
    if accepted:
        return cooldown
    return 0


def resource_ok(mana, cost):
    """资源校验：蓝量足以支付消耗才允许入队/释放，
    资源不足的技能不进队列，避免回蓝后自动放出。"""
    return mana >= cost


def interrupt_priority(control, silence):
    """打断优先级：控制效果与沉默是两类独立来源，取更高优先级者
    生效，而不是只比较技能 ID。"""
    return max(control, silence)


def queue_limit(size, max_size):
    """队列上限：当前深度未达上限才允许继续入队，防止连点塞满队列。"""
    return size < max_size


def device_threshold(device):
    """设备阈值：手柄与键鼠统一重复触发阈值（归一化为 1 帧），
    消除不同设备的手感差异。"""
    return 1


def server_stage(client, server):
    """阶段同步：施法阶段以服务器权威状态为准，
    服务器校正携带中间阶段，客户端不得用本地阶段覆盖。"""
    return server


def event_idempotent(event_id, seen):
    """事件幂等：事件 ID 未出现过才放行，重试/重发的重复事件被丢弃，
    防止技能双发。"""
    return event_id not in seen


def scene_clear(queue):
    """场景清理：切场景时原地清空施法队列，避免进新图自动放旧技能。"""
    queue.clear()
    return queue


def time_scaled(dt, scale):
    """时间缩放：逻辑计时按游戏时间（dt * scale）累计，
    慢动作下前摇同步变慢，而不是按真实时间走。"""
    return dt * scale


def hold_repeat(down, held):
    """长按重复：仅当按键仍处于按下状态且已进入持按段时才允许重复触发；
    已松手（down 为 False）则不再产生重复输入。"""
    return bool(down and held)


def cast_valid(phase, max_phase):
    """施法阶段：当前阶段处于合法阶段区间（含最大阶段）内才允许施法。"""
    return phase <= max_phase
