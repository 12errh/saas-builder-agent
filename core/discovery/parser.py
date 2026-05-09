from __future__ import annotations

from core.discovery.models import ProjectArchetype, RequirementProfile


KEYWORDS: list[tuple[ProjectArchetype, tuple[str, ...]]] = [
    (ProjectArchetype.ECOMMERCE, ("shop", "cart", "checkout", "store")),
    (ProjectArchetype.API_SERVICE, ("api", "backend", "service")),
    (ProjectArchetype.DESKTOP_UTILITY, ("desktop", "native app", "qt")),
    (ProjectArchetype.PORTFOLIO, ("portfolio", "personal website")),
    (ProjectArchetype.INTERNAL_TOOL, ("admin", "internal", "dashboard")),
    (ProjectArchetype.SAAS, ("saas", "subscription", "multi-tenant")),
]


def classify_prompt(prompt: str) -> RequirementProfile:
    text = prompt.lower().strip()
    for archetype, keywords in KEYWORDS:
        if any(keyword in text for keyword in keywords):
            return RequirementProfile(
                prompt=prompt,
                archetype=archetype,
                confidence=0.8,
                assumptions=[f"Classified as {archetype.value} from keyword match."],
            )

    return RequirementProfile(
        prompt=prompt,
        archetype=ProjectArchetype.UNKNOWN,
        confidence=0.4,
        assumptions=["No strong keyword match found."],
        unresolved_ambiguities=["Project archetype is unclear; ask follow-up questions."],
    )
