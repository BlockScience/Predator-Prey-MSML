from random import choice, random


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

    space1 = {"Food Deltas": []}
    space2 = {"Agents": []}

    for predator in predators:
        options = state["Metrics"]["Neighboring Valid Tiles Metric"](
            state,
            params,
            [{"Locations": [predator["Location"]]}, {"Locations": possible_prey}],
        )[0]
        if len(options) > 0:
            prey = choice(list(options))
            possible_prey.remove(prey)
            prey = state["Sites Matrix"][prey[0]][prey[1]]["Agent"]
            food = prey["Food"]
            space1["Food Deltas"].append({"Agent": predator, "Delta Food": food})
            space2["Agents"].append(prey)
    return [space1, space2]


def agent_reproduction_policy_v1(state, params, spaces):

    space1 = {"Agents": []}
    space2 = {"Food Deltas": []}

    # Find the agents and open locations
    predators = state["Stateful Metrics"]["Predator Stateful Metric"](state, params)
    prey = state["Stateful Metrics"]["Prey Stateful Metric"](state, params)
    open_locations = state["Stateful Metrics"]["Open Locations Stateful Metric"](
        state, params
    )
    open_locations = [x["Location"] for x in open_locations]

    # Filter to having enough food
    predators = [
        agent
        for agent in predators
        if agent["Food"] >= params["Reproduction Food Threshold"]
    ]
    prey = [
        agent
        for agent in prey
        if agent["Food"] >= params["Reproduction Food Threshold"]
    ]
    for agents in [predators, prey]:
        reproducing_agents = [
            agent_i
            for agent_i in agents
            if random() <= params["Reproduction Probability"]
        ]
        for agent in reproducing_agents:
            if agent not in agents:
                continue
            valid_mates = state["Metrics"]["Is Neighbor Metric"](
                state, params, [{"Agents": [agent]}, {"Agents": agents}]
            )[0]
            if len(valid_mates) == 0:
                continue

            mate = choice(valid_mates)

            # Valid locations for birth on either agent
            valid_locations = state["Metrics"]["Neighboring Valid Tiles Metric"](
                state,
                params,
                [
                    {"Locations": [agent["Location"], mate["Location"]]},
                    {"Locations": open_locations},
                ],
            )
            valid_locations = valid_locations[0].union(valid_locations[1])
            if len(valid_locations) == 0:
                continue
            new_location = choice(list(valid_locations))
            agents.remove(agent)
            agents.remove(mate)
            open_locations.remove(new_location)

            space1["Agents"].append(
                {
                    "Age": 0,
                    "Agent Type": agent["Agent Type"],
                    "Food": params["Reproduction Food Needed"] * 2,
                    "Location": new_location,
                }
            )
            space2["Food Deltas"].append(
                {"Agent": agent, "Delta Food": -params["Reproduction Food Needed"]}
            )
            space2["Food Deltas"].append(
                {"Agent": mate, "Delta Food": -params["Reproduction Food Needed"]}
            )
    return [space1, space2]
