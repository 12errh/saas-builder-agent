from pathlib import Path

from core.discovery.service import DiscoveryService
from core.orchestrator.state_machine import RunSession, RunState


def test_discovery_profile_persistence(tmp_path: Path) -> None:
    service = DiscoveryService(tmp_path)
    profile = service.initialize_profile("Build a SaaS app with subscription")

    questions = service.get_questions(profile)
    answers = {q["key"]: q["options"][0] for q in questions}
    updated = service.apply_and_persist(profile, answers)

    loaded = service.load_profile()

    assert updated.unresolved_ambiguities == []
    assert loaded.answers == updated.answers


def test_state_transition_discovery_to_spec() -> None:
    session = RunSession(run_id="r1", state=RunState.PROJECT_INIT)
    session.transition_to(RunState.DISCOVERY_ACTIVE)
    session.transition_to(RunState.DISCOVERY_RESOLVED)
    session.transition_to(RunState.SPEC_DRAFTING)
    assert session.state == RunState.SPEC_DRAFTING
