def prey_feeding_boundary_action_v1(state, params, spaces):
    prey = state["Stateful Metrics"]["Prey Stateful Metric"](state, params)
    prey = [x for x in prey if x["Food"] <= params["Hunger Threshold"]]
    return [{"Agents": prey}]


def hunt_prey_boundary_action_v1(state, params, spaces):
    predators = state["Stateful Metrics"]["Predator Stateful Metric"](state, params)
    predators = [x for x in predators if x["Food"] <= params["Hunger Threshold"]]
    return [{"Agents": predators}]
