from __future__ import annotations

from pathlib import Path

from core.discovery.models import RequirementProfile
from core.execution.engine import BuildPhaseEngine, PhaseTask
from core.orchestrator.approval import ApprovalMode, ApprovalStore, new_decision
from core.orchestrator.state_machine import RunSession, RunState, StateStore
from core.specs.generator import SpecGenerator
from core.specs.review import review_spec_bundle


class WorkflowController:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.state_store = StateStore(workspace / "run_session.json")
        self.approval_store = ApprovalStore(workspace / "approvals.json")
        self.phase_engine = BuildPhaseEngine()

    def start(self, run_id: str) -> RunSession:
        session = RunSession(run_id=run_id, state=RunState.PROJECT_INIT)
        self.state_store.save(session)
        return session

    def run_discovery_completed(self, session: RunSession) -> RunSession:
        session.transition_to(RunState.DISCOVERY_ACTIVE)
        session.transition_to(RunState.DISCOVERY_RESOLVED)
        self.state_store.save(session)
        return session

    def run_spec_generation(self, session: RunSession, profile: RequirementProfile) -> bool:
        session.transition_to(RunState.SPEC_DRAFTING)
        self.state_store.save(session)
        SpecGenerator(self.workspace).generate(profile)
        result = review_spec_bundle(self.workspace)
        self.approval_store.append(
            new_decision(
                stage="SPEC_REVIEW_INTERNAL",
                approved=result.passed,
                mode=ApprovalMode.MANUAL_EVERY_GATE,
                reason="; ".join(result.findings) if result.findings else "Internal review passed",
            )
        )
        return result.passed

    def run_build_phase(self, phase: str, task_titles: list[str]) -> bool:
        tasks = [PhaseTask(id=f"{phase}-{i+1}", title=title) for i, title in enumerate(task_titles)]
        report = self.phase_engine.run_phase(phase=phase, tasks=tasks)
        passed = report.review_passed and report.security_passed
        self.approval_store.append(
            new_decision(
                stage=f"BUILD_{phase}",
                approved=passed,
                mode=ApprovalMode.MANUAL_EVERY_GATE,
                reason="Build phase checks passed" if passed else "Build phase checks failed",
            )
        )
        return passed
