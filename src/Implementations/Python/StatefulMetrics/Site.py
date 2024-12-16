from statistics import median


def open_locations_stateful_metric(state, params):
    return [site for site in state["Sites"] if site["Agent"] is None]


def filled_locations_stateful_metric(state, params):
    return [site for site in state["Sites"] if site["Agent"] is not None]


def prey_locations_stateful_metric(state, params):

    return [
        site
        for site in state["Sites"]
        if (site["Agent"] is not None) and (site["Agent"]["Agent Type"] == "Prey")
    ]


def predator_locations_stateful_metric(state, params):
    return [
        site
        for site in state["Sites"]
        if (site["Agent"] is not None) and (site["Agent"]["Agent Type"] == "Predator")
    ]


def median_site_food_stateful_metric(state, params):
    return median([x["Food"] for x in state["Sites"]])
