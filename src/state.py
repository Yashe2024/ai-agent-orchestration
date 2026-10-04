from pydantic import BaseModel, Field

class AgentState(BaseModel):
    request: str
    findings: list[str] = Field(default_factory=list)
    metrics: dict = Field(default_factory=dict)
    risks: list[str] = Field(default_factory=list)
    final_answer: str | None = None
