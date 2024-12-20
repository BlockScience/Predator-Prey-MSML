import numpy as np


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


def poisson_food_growth_policy(state, params, spaces):
    space = {"Food Locations": []}
    for loc in spaces[0]["Locations"]:
        delta_food = min(
            params["Maximum Food per Tile"] - loc["Food"],
            np.random.poisson(["Food Growth Rate"]),
        )
        space["Food Locations"].append(
            {"Location": loc["Location"], "Food": delta_food}
        )
    return [space]
