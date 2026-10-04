from src.orchestrator import run
result = run("Why did regional revenue decline?")
print(result.model_dump())
