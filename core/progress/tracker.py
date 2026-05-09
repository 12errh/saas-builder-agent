from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json


PHASE_ORDER = ["phase0", "phase1", "phase2", "phase3", "phase4", "phase5", "phase6", "phase7"]


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

    def phase_completion(self) -> dict[str, bool]:
        tasks = self.load()
        by_phase: dict[str, list[TaskItem]] = {}
        for task in tasks:
            by_phase.setdefault(task.phase, []).append(task)
        return {
            phase: bool(items) and all(item.completed for item in items)
            for phase, items in by_phase.items()
        }

    def can_start_phase(self, phase: str) -> bool:
        if phase not in PHASE_ORDER:
            raise ValueError(f"Unknown phase: {phase}")
        completion = self.phase_completion()
        phase_index = PHASE_ORDER.index(phase)
        required_prior = PHASE_ORDER[:phase_index]
        return all(completion.get(item, False) for item in required_prior)
