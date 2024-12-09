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
