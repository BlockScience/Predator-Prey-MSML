def natural_death_policy(state, params, spaces):
    agents = spaces[0]["Agents"]
    space = {
        "Agents": [
            agent
            for agent in agents
            if agent["Age"] >= params["Maximum Age Parameter"] or agent["Food"] <= 0
        ]
    }
    return [space]
