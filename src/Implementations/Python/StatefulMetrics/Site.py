def open_locations_stateful_metric(state, params):
    return [site for site in state["Sites"] if site["Agent"] is None]