def update_food_locations_mechanism(state, params, spaces):
    for loc in spaces[0]["Food Locations"]:
        state["Sites Matrix"][loc["Location"][0]][loc["Location"][1]]["Food"] += loc[
            "Food"
        ]


def update_agent_locations_mechanism(state, params, spaces):
    pass
