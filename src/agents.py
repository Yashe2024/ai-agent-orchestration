from .state import AgentState

def research_agent(state):
    state.findings.append("Research completed: identified relevant business drivers.")
    return state

def data_agent(state):
    state.metrics.update({"revenue_change_pct": -8.4, "customer_change_pct": -3.1})
    return state

def analysis_agent(state):
    if state.metrics.get("revenue_change_pct", 0) < -5:
        state.risks.append("Material revenue decline requires management attention.")
    return state

def reporting_agent(state):
    state.final_answer = (
        f"Revenue changed {state.metrics.get('revenue_change_pct')}%. "
        f"Key findings: {'; '.join(state.findings)}"
    )
    return state
