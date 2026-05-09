from __future__ import annotations

from dataclasses import dataclass

from core.discovery.models import ProjectArchetype, RequirementProfile


@dataclass(frozen=True)
class Question:
    key: str
    prompt: str
    options: tuple[str, ...]


COMMON_QUESTIONS: tuple[Question, ...] = (
    Question("target_users", "Who are the primary users?", ("Consumers", "Businesses", "Internal team")),
    Question("auth", "What authentication model do you want?", ("Email/Password", "OAuth", "SSO")),
    Question("deployment", "Where should it be deployed?", ("Vercel", "Render/Railway", "Custom infra")),
    Question("backend_choice", "Backend preference?", ("Supabase", "Custom backend", "Unsure")),
)

ARCHETYPE_EXTENSION: dict[ProjectArchetype, tuple[Question, ...]] = {
    ProjectArchetype.ECOMMERCE: (
        Question("payments", "Payments provider?", ("Stripe", "PayPal", "Both")),
    ),
    ProjectArchetype.SAAS: (
        Question("multi_tenant", "Need multi-tenant support?", ("Yes", "No", "Not sure")),
    ),
    ProjectArchetype.API_SERVICE: (
        Question("api_style", "Preferred API style?", ("REST", "GraphQL", "Hybrid")),
    ),
}


def build_questionnaire(profile: RequirementProfile) -> list[Question]:
    questions = list(COMMON_QUESTIONS)
    questions.extend(ARCHETYPE_EXTENSION.get(profile.archetype, ()))
    return questions


def apply_answers(profile: RequirementProfile, answers: dict[str, str]) -> RequirementProfile:
    profile.answers.update(answers)
    missing = [q.key for q in build_questionnaire(profile) if q.key not in profile.answers]
    profile.unresolved_ambiguities = [f"Missing answer: {key}" for key in missing]
    if not missing:
        profile.confidence = min(1.0, profile.confidence + 0.15)
    return profile
