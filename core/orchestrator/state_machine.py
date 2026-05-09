from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import json


class RunState(str, Enum):
    PROJECT_INIT = "PROJECT_INIT"
    DISCOVERY_ACTIVE = "DISCOVERY_ACTIVE"
    DISCOVERY_RESOLVED = "DISCOVERY_RESOLVED"
    SPEC_DRAFTING = "SPEC_DRAFTING"


ALLOWED_TRANSITIONS: dict[RunState, tuple[RunState, ...]] = {
    RunState.PROJECT_INIT: (RunState.DISCOVERY_ACTIVE,),
    RunState.DISCOVERY_ACTIVE: (RunState.DISCOVERY_RESOLVED,),
    RunState.DISCOVERY_RESOLVED: (RunState.SPEC_DRAFTING,),
    RunState.SPEC_DRAFTING: (),
}


@dataclass
class RunSession:
    run_id: str
    state: RunState

    def transition_to(self, next_state: RunState) -> None:
        allowed = ALLOWED_TRANSITIONS[self.state]
        if next_state not in allowed:
            raise ValueError(f"Invalid state transition: {self.state.value} -> {next_state.value}")
        self.state = next_state


class StateStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def save(self, session: RunSession) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"run_id": session.run_id, "state": session.state.value}
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load(self) -> RunSession:
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return RunSession(run_id=data["run_id"], state=RunState(data["state"]))
