import pytest
from gameplay import ability_queue as mod

CASES = [
    ("edge", 'm.input_edge(False, True) is True'),
    ("advance", 'm.advance_phase(1, 0.5, 0.5, 1.0) == 2'),
    ("cancel", 'm.cancel_window(5, 2) == 3'),
    ("anim", 'm.anim_event(5, 3) is True'),
    ("cooldown", 'm.cooldown_rollback(5, False) == 0'),
    ("resource", 'm.resource_ok(10, 5) is True'),
    ("interrupt", 'm.interrupt_priority(2, 3) == 3'),
    ("queue", 'm.queue_limit(2, 3) is True'),
    ("device", 'm.device_threshold("gamepad") == 1'),
    ("server", 'm.server_stage(1, 2) == 2'),
    ("idem", 'm.event_idempotent(1, [2]) is True'),
    ("scene", 'm.scene_clear([1]) == []'),
    ("timescale", 'm.time_scaled(0.5, 2.0) == approx(1.0)'),
    ("hold", 'm.hold_repeat(False, True) is False'),
    ("cast", 'm.cast_valid(1, 3) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
