def prey_stateful_metric(state, params):
    return [agent for agent in state["Agents"] if agent["Agent Type"] == "Prey"]
