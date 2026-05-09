from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from enum import Enum
from pathlib import Path
import json


class ApprovalMode(str, Enum):
    MANUAL_EVERY_GATE = "manual_every_gate"
    NOTIFY_ONLY = "notify_only"
    AUTO_CONTINUE = "auto_continue"


@dataclass
class ApprovalDecision:
    stage: str
    approved: bool
    mode: ApprovalMode
    reason: str
    timestamp: str


class ApprovalStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def append(self, decision: ApprovalDecision) -> None:
        history = self.load_all()
        history.append(decision)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [asdict(item) for item in history]
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load_all(self) -> list[ApprovalDecision]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return [
            ApprovalDecision(
                stage=item["stage"],
                approved=item["approved"],
                mode=ApprovalMode(item["mode"]),
                reason=item["reason"],
                timestamp=item["timestamp"],
            )
            for item in raw
        ]


def new_decision(stage: str, approved: bool, mode: ApprovalMode, reason: str = "") -> ApprovalDecision:
    return ApprovalDecision(
        stage=stage,
        approved=approved,
        mode=mode,
        reason=reason,
        timestamp=datetime.now(UTC).isoformat(),
    )
