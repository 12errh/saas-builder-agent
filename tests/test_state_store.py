from pathlib import Path

from core.orchestrator.state_machine import RunSession, RunState, StateStore


def test_state_store_roundtrip(tmp_path: Path) -> None:
    target = tmp_path / "run.json"
    store = StateStore(target)
    original = RunSession(run_id="t1", state=RunState.PROJECT_INIT)

    store.save(original)
    loaded = store.load()

    assert loaded.run_id == original.run_id
    assert loaded.state == original.state
