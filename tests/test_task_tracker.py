from pathlib import Path

from core.progress.tracker import TaskItem, TaskTracker


def test_mark_completed(tmp_path: Path) -> None:
    tracker = TaskTracker(tmp_path / "tasks.json")
    tracker.save([
        TaskItem(id="a", title="Task A", phase="p1", completed=False),
        TaskItem(id="b", title="Task B", phase="p1", completed=False),
    ])

    changed = tracker.mark_completed("b")
    assert changed is True

    items = tracker.load()
    by_id = {item.id: item for item in items}
    assert by_id["a"].completed is False
    assert by_id["b"].completed is True
