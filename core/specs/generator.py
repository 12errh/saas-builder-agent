from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from core.discovery.models import RequirementProfile


@dataclass
class SpecBundle:
    prd_path: Path
    trd_path: Path
    dev_phases_path: Path
    design_path: Path


class SpecGenerator:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.workspace.mkdir(parents=True, exist_ok=True)

    def generate(self, profile: RequirementProfile) -> SpecBundle:
        prd = self.workspace / "PRD.generated.md"
        trd = self.workspace / "TRD.generated.md"
        dev = self.workspace / "DEV_PHASES.generated.md"
        design = self.workspace / "DESIGN.generated.md"

        prd.write_text(self._render_prd(profile), encoding="utf-8")
        trd.write_text(self._render_trd(profile), encoding="utf-8")
        dev.write_text(self._render_dev(profile), encoding="utf-8")
        design.write_text(self._render_design(profile), encoding="utf-8")

        return SpecBundle(prd_path=prd, trd_path=trd, dev_phases_path=dev, design_path=design)

    def _render_prd(self, profile: RequirementProfile) -> str:
        return "\n".join(
            [
                "# Generated PRD",
                f"- Prompt: {profile.prompt}",
                f"- Archetype: {profile.archetype.value}",
                f"- Confidence: {profile.confidence:.2f}",
                "## Clarifications",
                *[f"- {k}: {v}" for k, v in sorted(profile.answers.items())],
                "## Open Questions",
                *([f"- {x}" for x in profile.unresolved_ambiguities] or ["- None"]),
            ]
        )

    def _render_trd(self, profile: RequirementProfile) -> str:
        backend = profile.answers.get("backend_choice", "Unsure")
        return "\n".join(
            [
                "# Generated TRD",
                f"- Project archetype: {profile.archetype.value}",
                f"- Preferred backend: {backend}",
                "## Provider Requirements",
                "- Must support NVIDIA adapter",
                "- Must support OpenRouter adapter",
                "## Architecture Baseline",
                "- Desktop UI: PySide6",
                "- Orchestrator: state-machine driven",
            ]
        )

    def _render_dev(self, profile: RequirementProfile) -> str:
        return "\n".join(
            [
                "# Generated DEV Phases",
                "1. Discovery finalized",
                "2. Specs approved",
                "3. Implementation phase build",
                "4. Review + Security gate",
                "5. Production readiness",
                f"- Source archetype: {profile.archetype.value}",
            ]
        )

    def _render_design(self, profile: RequirementProfile) -> str:
        return "\n".join(
            [
                "# Generated Design Brief",
                "- Style: modern minimal",
                "- Accessibility: WCAG AA baseline",
                "- Core patterns: clear hierarchy, low-noise layout",
                f"- Target archetype: {profile.archetype.value}",
            ]
        )
