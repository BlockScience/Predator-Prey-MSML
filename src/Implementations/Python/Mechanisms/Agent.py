def remove_agents_mechanism(state, params, spaces):
    state["Agents"] = [
        agent for agent in state["Agents"] if agent not in spaces[0]["Agents"]
    ]
