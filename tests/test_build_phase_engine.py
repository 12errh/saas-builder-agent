from core.execution.engine import BuildPhaseEngine, PhaseTask


def test_build_phase_engine_passes() -> None:
    engine = BuildPhaseEngine()
    report = engine.run_phase(
        phase="phase4",
        tasks=[
            PhaseTask(id="1", title="implement endpoint"),
            PhaseTask(id="2", title="add tests"),
        ],
    )

    assert report.tasks_total == 2
    assert report.tasks_completed == 2
    assert report.review_passed is True
    assert report.security_passed is True
