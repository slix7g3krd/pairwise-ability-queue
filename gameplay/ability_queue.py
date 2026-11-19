"""第 61 批：按住技能键不放，角色在前摇结束瞬间又自动接了一段，松手后技能还在..."""

def input_edge(previous, current):
    """长按去重。"""
    raise NotImplementedError("TODO: input_edge")

def advance_phase(phase, timer, dt, threshold):
    """阶段计时。"""
    raise NotImplementedError("TODO: advance_phase")

def cancel_window(remaining, latency):
    """延迟取消。"""
    raise NotImplementedError("TODO: cancel_window")

def anim_event(frame, event_frame):
    """动画事件。"""
    raise NotImplementedError("TODO: anim_event")

def cooldown_rollback(cooldown, accepted):
    """冷却回滚。"""
    raise NotImplementedError("TODO: cooldown_rollback")

def resource_ok(mana, cost):
    """资源校验。"""
    raise NotImplementedError("TODO: resource_ok")

def interrupt_priority(control, silence):
    """打断优先级。"""
    raise NotImplementedError("TODO: interrupt_priority")

def queue_limit(size, max_size):
    """队列上限。"""
    raise NotImplementedError("TODO: queue_limit")

def device_threshold(device):
    """设备阈值。"""
    raise NotImplementedError("TODO: device_threshold")

def server_stage(client, server):
    """阶段同步。"""
    raise NotImplementedError("TODO: server_stage")

def event_idempotent(event_id, seen):
    """事件幂等。"""
    raise NotImplementedError("TODO: event_idempotent")

def scene_clear(queue):
    """场景清理。"""
    raise NotImplementedError("TODO: scene_clear")

def time_scaled(dt, scale):
    """时间缩放。"""
    raise NotImplementedError("TODO: time_scaled")

def hold_repeat(down, held):
    """长按重复。"""
    raise NotImplementedError("TODO: hold_repeat")

def cast_valid(phase, max_phase):
    """施法阶段。"""
    raise NotImplementedError("TODO: cast_valid")
