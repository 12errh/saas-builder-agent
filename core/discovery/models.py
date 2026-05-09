from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ProjectArchetype(str, Enum):
    SAAS = "saas"
    ECOMMERCE = "ecommerce"
    INTERNAL_TOOL = "internal_tool"
    PORTFOLIO = "portfolio"
    API_SERVICE = "api_service"
    DESKTOP_UTILITY = "desktop_utility"
    UNKNOWN = "unknown"


@dataclass
class RequirementProfile:
    prompt: str
    archetype: ProjectArchetype
    confidence: float
    assumptions: list[str] = field(default_factory=list)
    unresolved_ambiguities: list[str] = field(default_factory=list)
    answers: dict[str, str] = field(default_factory=dict)
