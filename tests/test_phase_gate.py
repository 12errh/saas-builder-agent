from pathlib import Path

from ui.desktop.phase_gate import can_enable_phase_button


def test_phase_gate_from_seeded_tasks() -> None:
    tasks_path = Path("storage/tasks.json")
    assert can_enable_phase_button(tasks_path, "phase3") is True
    assert can_enable_phase_button(tasks_path, "phase4") is False
