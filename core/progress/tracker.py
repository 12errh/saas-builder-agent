from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json


@dataclass
class TaskItem:
    id: str
    title: str
    phase: str
    completed: bool = False


class TaskTracker:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[TaskItem]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return [TaskItem(**item) for item in raw]

    def save(self, tasks: list[TaskItem]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps([asdict(t) for t in tasks], indent=2), encoding="utf-8")

    def mark_completed(self, task_id: str) -> bool:
        tasks = self.load()
        updated = False
        for task in tasks:
            if task.id == task_id:
                task.completed = True
                updated = True
        if updated:
            self.save(tasks)
        return updated
