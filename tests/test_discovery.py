from core.discovery.models import ProjectArchetype
from core.discovery.parser import classify_prompt
from core.discovery.questionnaire import apply_answers, build_questionnaire


def test_classify_prompt_ecommerce() -> None:
    profile = classify_prompt("Build me an ecommerce store with cart and checkout")
    assert profile.archetype == ProjectArchetype.ECOMMERCE
    assert profile.confidence >= 0.8


def test_questionnaire_and_apply_answers() -> None:
    profile = classify_prompt("Build a SaaS subscription app")
    questions = build_questionnaire(profile)
    keys = {q.key for q in questions}
    assert "backend_choice" in keys
    assert "multi_tenant" in keys

    answers = {q.key: q.options[0] for q in questions}
    updated = apply_answers(profile, answers)
    assert updated.unresolved_ambiguities == []
    assert updated.confidence > 0.8
