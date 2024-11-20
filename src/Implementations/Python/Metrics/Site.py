def available_food_metric(state, params, spaces):
    sites = [state["Sites Matrix"][x[0]][x[1]] for x in spaces[0]["Locations"]]
    food = [x["Food"] for x in sites]
    return food
