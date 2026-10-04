from src.orchestrator import run

def test_orchestration_produces_answer():
    result = run("Investigate revenue decline")
    assert result.final_answer
    assert result.metrics["revenue_change_pct"] < 0
