from __future__ import annotations

from pathlib import Path

from core.progress.tracker import TaskTracker


def can_enable_phase_button(tasks_path: Path, next_phase: str) -> bool:
    tracker = TaskTracker(tasks_path)
    return tracker.can_start_phase(next_phase)
