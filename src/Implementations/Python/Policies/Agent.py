from random import choice


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


def random_agent_movement_with_sieve(state, params, spaces):
    sieve = spaces[0]["Agents"]
    open_locations = state["Stateful Metrics"]["Open Locations Stateful Metric"](
        state, params
    )
    open_locations = [x["Location"] for x in open_locations]
    out_space = {"Agent Locations": []}
    last = -1

    while len(sieve) > 0 and len(sieve) != last:
        last = len(sieve)
        hold = []
        while len(sieve) > 0:
            curr = sieve.pop()
            options = state["Metrics"]["Neighboring Valid Tiles Metric"](
                state,
                params,
                [{"Locations": [curr["Location"]]}, {"Locations": open_locations}],
            )[0]
            if len(options) == 0:
                hold.append(curr)
            else:
                new = choice(list(options))
                old = curr["Location"]
                open_locations.append(old)
                open_locations.remove(new)
                out_space["Agent Locations"].append({"Agent": curr, "Location": new})

        sieve = hold
    return [out_space]


def hunt_prey_policy_v1(state, params, spaces):
    possible_prey = state["Stateful Metrics"]["Prey Locations Stateful Metric"](
        state, params
    )
    possible_prey = [x["Location"] for x in possible_prey]
    predators = state["Stateful Metrics"]["Predator Stateful Metric"](state, params)

    for predator in predators:
        options = state["Metrics"]["Neighboring Valid Tiles Metric"](
            state,
            params,
            [{"Locations": [predator["Location"]]}, {"Locations": possible_prey}],
        )[0]
        if len(options) > 0:
            prey = choice(list(options))
            possible_prey.remove(prey)
            prey = state["Sites Matrix"][prey[0]][prey[1]]
            print(prey)
