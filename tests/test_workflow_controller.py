from pathlib import Path

from core.discovery.parser import classify_prompt
from core.discovery.questionnaire import apply_answers, build_questionnaire
from core.orchestrator.approval import ApprovalStore
from core.orchestrator.workflow import WorkflowController
from core.orchestrator.state_machine import RunState


def test_workflow_through_spec_review(tmp_path: Path) -> None:
    controller = WorkflowController(tmp_path)
    session = controller.start("run-1")

    session = controller.run_discovery_completed(session)
    assert session.state == RunState.DISCOVERY_RESOLVED

    profile = classify_prompt("Build a SaaS app")
    questions = build_questionnaire(profile)
    answers = {q.key: q.options[0] for q in questions}
    profile = apply_answers(profile, answers)

    passed = controller.run_spec_generation(session, profile)
    assert passed

    decisions = ApprovalStore(tmp_path / "approvals.json").load_all()
    assert len(decisions) == 1
    assert decisions[0].stage == "SPEC_REVIEW_INTERNAL"
    assert decisions[0].approved is True
