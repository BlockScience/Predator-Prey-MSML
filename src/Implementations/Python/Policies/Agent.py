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
    space1 = {"Food Deltas": [{"Agent": x, "Delta Food": -1} for x in agents]}
    space2 = {"Age Deltas": [{"Agent": x, "Delta Age": 1} for x in agents]}
    return [space1, space2]


def prey_eat_all_food_policy(state, params, spaces):
    locations = [x["Location"] for x in spaces[0]["Agents"]]
    available_food = state["Metrics"]["Available Food Metric"](
        state, params, [{"Locations": locations}]
    )
    space1 = {
        "Food Locations": [
            {"Location": x, "Food": -y} for x, y in zip(locations, available_food)
        ]
    }
    space2 = {
        "Food Deltas": [
            {"Agent": x, "Delta Food": y}
            for x, y in zip(spaces[0]["Agents"], available_food)
        ]
    }
    return [space1, space2]
