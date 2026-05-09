from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import json

from core.discovery.models import ProjectArchetype, RequirementProfile
from core.discovery.parser import classify_prompt
from core.discovery.questionnaire import apply_answers, build_questionnaire


class DiscoveryService:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.workspace.mkdir(parents=True, exist_ok=True)

    def initialize_profile(self, prompt: str) -> RequirementProfile:
        return classify_prompt(prompt)

    def get_questions(self, profile: RequirementProfile) -> list[dict[str, object]]:
        questions = build_questionnaire(profile)
        return [{"key": q.key, "prompt": q.prompt, "options": list(q.options)} for q in questions]

    def apply_and_persist(self, profile: RequirementProfile, answers: dict[str, str]) -> RequirementProfile:
        updated = apply_answers(profile, answers)
        self._save_profile(updated)
        return updated

    def _save_profile(self, profile: RequirementProfile) -> None:
        output = self.workspace / "requirement_profile.json"
        payload = asdict(profile)
        payload["archetype"] = profile.archetype.value
        output.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load_profile(self) -> RequirementProfile:
        source = self.workspace / "requirement_profile.json"
        data = json.loads(source.read_text(encoding="utf-8"))
        return RequirementProfile(
            prompt=data["prompt"],
            archetype=ProjectArchetype(data["archetype"]),
            confidence=data["confidence"],
            assumptions=data["assumptions"],
            unresolved_ambiguities=data["unresolved_ambiguities"],
            answers=data["answers"],
        )
