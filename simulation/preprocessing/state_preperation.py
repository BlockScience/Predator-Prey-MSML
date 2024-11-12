def compute_starting_total_length(state, params):
    state["Dummy"]["Total Length"] = params["DUMMY Length Multiplier"] * len(
        state["Dummy"]["Words"]
    )
    return state


def create_sites(state, params):
    state["Sites"] = []
    state["Sites Matrix"] = []
    for i in range(params["Site Size"][0]):
        state["Sites Matrix"].append([])
        for j in range(params["Site Size"][1]):
            site = {"Location": (i, j), "Food": 0}
            state["Sites"].append(site)
            state["Sites Matrix"][-1].append(state["Sites"][-1])
    return state
