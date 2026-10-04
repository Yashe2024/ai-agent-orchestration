# AI Agent Orchestration Platform

Reference architecture for controlled multi-agent workflows.

## Example
A business investigation request is decomposed into research, data, analysis and reporting tasks.

```mermaid
flowchart TD
U[User Request] --> O[Orchestrator]
O --> R[Research Agent]
O --> D[Data Agent]
O --> A[Analysis Agent]
R --> C[Shared State]
D --> C
A --> C
C --> V[Validation]
V --> P[Report Agent]
P --> F[Final Response]
```

## Design Principles
- Explicit agent responsibilities
- Tool allow-lists
- Shared state schema
- Validation before final output
- Human escalation for ambiguous/high-risk tasks
- Traceability of agent actions

## Run
```bash
pip install -r requirements.txt
python examples/demo.py
```
