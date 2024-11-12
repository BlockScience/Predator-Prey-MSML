def food_growth_control_action_v1(state, params, spaces):
    sites = [
        site
        for site in state["Sites"]
        if site["Food"] < params["Maximum Food per Tile"]
    ]
    return [{"Locations": sites}]
