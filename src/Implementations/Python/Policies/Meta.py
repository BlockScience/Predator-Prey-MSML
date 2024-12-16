def simulation_meta_policy_v1(state, params, spaces):
    space1 = {"Timestep": 1}
    space2 = {}

    space2["Timestep"] = state["Timestep"] + 1

    for key in [
        "Open Locations Stateful Metric",
        "Filled Locations Stateful Metric",
        "Prey Locations Stateful Metric",
        "Predator Locations Stateful Metric",
        "Median Site Food Stateful Metric",
        "Prey Stateful Metric",
        "Predator Stateful Metric",
        "Number of Prey Stateful Metric",
        "Number of Predators Stateful Metric",
        "Median Predator Food Stateful Metric",
        "Median Prey Food Stateful Metric",
        "Median Predator Age Stateful Metric",
        "Median Prey Age Stateful Metric",
    ]:
        space2[key] = state["Stateful Metrics"][key](state, params)

    return [space1, space2]
