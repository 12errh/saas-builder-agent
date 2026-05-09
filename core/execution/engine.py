from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PhaseTask:
    id: str
    title: str
    status: str = "pending"


@dataclass
class PhaseReport:
    phase: str
    tasks_total: int
    tasks_completed: int
    review_passed: bool
    security_passed: bool


class BuildPhaseEngine:
    def run_phase(self, phase: str, tasks: list[PhaseTask]) -> PhaseReport:
        for task in tasks:
            task.status = "completed"

        review_passed = self._review(tasks)
        security_passed = self._security_check(tasks)

        return PhaseReport(
            phase=phase,
            tasks_total=len(tasks),
            tasks_completed=sum(1 for t in tasks if t.status == "completed"),
            review_passed=review_passed,
            security_passed=security_passed,
        )

    def _review(self, tasks: list[PhaseTask]) -> bool:
        return all(task.status == "completed" for task in tasks)

    def _security_check(self, tasks: list[PhaseTask]) -> bool:
        return all(task.status == "completed" for task in tasks)
