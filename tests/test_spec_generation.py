from pathlib import Path

from core.discovery.parser import classify_prompt
from core.discovery.questionnaire import apply_answers, build_questionnaire
from core.specs.generator import SpecGenerator
from core.specs.review import review_spec_bundle


def test_spec_generation_and_review(tmp_path: Path) -> None:
    profile = classify_prompt("Build a SaaS internal dashboard app")
    questions = build_questionnaire(profile)
    answers = {q.key: q.options[0] for q in questions}
    profile = apply_answers(profile, answers)

    bundle = SpecGenerator(tmp_path).generate(profile)

    assert bundle.prd_path.exists()
    assert bundle.trd_path.exists()
    assert bundle.dev_phases_path.exists()
    assert bundle.design_path.exists()

    result = review_spec_bundle(tmp_path)
    assert result.passed
    assert result.findings == []
