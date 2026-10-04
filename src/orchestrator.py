from .state import AgentState
from .agents import research_agent, data_agent, analysis_agent, reporting_agent

def run(request: str):
    state = AgentState(request=request)
    for agent in (research_agent, data_agent, analysis_agent):
        state = agent(state)
    return reporting_agent(state)
