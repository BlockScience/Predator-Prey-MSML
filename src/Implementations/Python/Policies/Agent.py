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


def increase_agent_age_policy_plus1(state, params, spaces):
    agents = spaces[0]["Agents"]
    space1 = [{"Agent": x, "Delta Food": -1} for x in agents]
    space2 = [{"Agent": x, "Delta Age": 1} for x in agents]
    return [space1, space2]
