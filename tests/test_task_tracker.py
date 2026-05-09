from pathlib import Path

from core.progress.tracker import TaskItem, TaskTracker


def test_mark_completed(tmp_path: Path) -> None:
    tracker = TaskTracker(tmp_path / "tasks.json")
    tracker.save([
        TaskItem(id="a", title="Task A", phase="phase0", completed=False),
        TaskItem(id="b", title="Task B", phase="phase0", completed=False),
    ])

    changed = tracker.mark_completed("b")
    assert changed is True

    items = tracker.load()
    by_id = {item.id: item for item in items}
    assert by_id["a"].completed is False
    assert by_id["b"].completed is True


def test_phase_order_gate(tmp_path: Path) -> None:
    tracker = TaskTracker(tmp_path / "tasks.json")
    tracker.save([
        TaskItem(id="p0-a", title="Phase0 A", phase="phase0", completed=True),
        TaskItem(id="p1-a", title="Phase1 A", phase="phase1", completed=False),
    ])

    assert tracker.can_start_phase("phase1") is True
    assert tracker.can_start_phase("phase2") is False
