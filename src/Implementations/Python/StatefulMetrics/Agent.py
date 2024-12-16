from statistics import median


def prey_stateful_metric(state, params):
    return [agent for agent in state["Agents"] if agent["Agent Type"] == "Prey"]


def predator_stateful_metric(state, params):
    return [agent for agent in state["Agents"] if agent["Agent Type"] == "Predator"]


def number_of_prey_stateful_metric(state, params):
    return len(state["Stateful Metrics"]["Prey Stateful Metric"](state, params))


def number_of_predators_stateful_metric(state, params):
    return len(state["Stateful Metrics"]["Predator Stateful Metric"](state, params))


def median_predator_food_stateful_metric(state, params):
    predators = [
        x["Food"]
        for x in state["Stateful Metrics"]["Predator Stateful Metric"](state, params)
    ]
    return median(predators) if len(predators) > 0 else None


def median_prey_food_stateful_metric(state, params):
    prey = [
        x["Food"]
        for x in state["Stateful Metrics"]["Prey Stateful Metric"](state, params)
    ]
    return median(prey) if len(prey) > 0 else None


def median_predator_age_stateful_metric(state, params):
    predators = [
        x["Age"]
        for x in state["Stateful Metrics"]["Predator Stateful Metric"](state, params)
    ]
    return median(predators) if len(predators) > 0 else None


def median_prey_age_stateful_metric(state, params):
    prey = [
        x["Age"]
        for x in state["Stateful Metrics"]["Prey Stateful Metric"](state, params)
    ]
    return median(prey) if len(prey) > 0 else None
