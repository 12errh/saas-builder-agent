from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import json


class RunState(str, Enum):
    PROJECT_INIT = "PROJECT_INIT"


@dataclass
class RunSession:
    run_id: str
    state: RunState


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
