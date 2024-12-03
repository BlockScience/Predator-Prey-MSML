def update_food_locations_mechanism(state, params, spaces):
    for loc in spaces[0]["Food Locations"]:
        state["Sites Matrix"][loc["Location"][0]][loc["Location"][1]]["Food"] += loc[
            "Food"
        ]


def update_agent_locations_mechanism(state, params, spaces):
    for entry in spaces[0]["Agent Locations"]:
        agent = entry["Agent"]
        old_loc = agent["Location"]
        loc = entry["Location"]
        assert (
            state["Sites Matrix"][loc[0]][loc[1]]["Agent"] is None
        ), "Agent is already at this location!"
        state["Sites Matrix"][old_loc[0]][old_loc[1]]["Agent"] = None
        agent["Location"] = loc
        state["Sites Matrix"][loc[0]][loc[1]]["Agent"] = agent
