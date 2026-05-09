from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ReviewResult:
    passed: bool
    findings: list[str]


REQUIRED_HEADERS = {
    "PRD.generated.md": "# Generated PRD",
    "TRD.generated.md": "# Generated TRD",
    "DEV_PHASES.generated.md": "# Generated DEV Phases",
    "DESIGN.generated.md": "# Generated Design Brief",
}


def review_spec_bundle(workspace: Path) -> ReviewResult:
    findings: list[str] = []
    for filename, header in REQUIRED_HEADERS.items():
        path = workspace / filename
        if not path.exists():
            findings.append(f"Missing artifact: {filename}")
            continue
        text = path.read_text(encoding="utf-8")
        if header not in text:
            findings.append(f"Missing required header in {filename}: {header}")

    return ReviewResult(passed=not findings, findings=findings)
