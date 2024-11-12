def constant_food_growth_policy(state, params, spaces):
    space = {"Food Locations": []}
    for loc in spaces[0]["Locations"]:
        delta_food = min(
            params["Maximum Food per Tile"] - loc["Food"], params["Food Growth Rate"]
        )
        space["Food Locations"].append(
            {"Location": loc["Location"], "Food": delta_food}
        )
    return [space]
