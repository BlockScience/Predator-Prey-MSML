def remove_agents_mechanism(state, params, spaces):
    state["Agents"] = [
        agent for agent in state["Agents"] if agent not in spaces[0]["Agents"]
    ]
    for agent in spaces[0]["Agents"]:
        state["Sites Matrix"][agent["Location"][0]][agent["Location"][1]][
            "Agent"
        ] = None


def update_food_mechanism(state, params, spaces):
    for values in spaces[0]["Food Deltas"]:
        values["Agent"]["Food"] += values["Delta Food"]


def update_agent_age_mechanism(state, params, spaces):
    for values in spaces[0]["Age Deltas"]:
        values["Agent"]["Age"] += values["Delta Age"]


def create_agents_mechanism(state, params, spaces):
    for agent in spaces[0]["Agents"]:
        loc = agent["Location"]
        assert (
            state["Sites Matrix"][loc[0]][loc[1]]["Agent"] is None
        ), "Agent is already at this location!"
        state["Agents"].append(agent)
        state["Sites Matrix"][loc[0]][loc[1]]["Agent"] = agent
