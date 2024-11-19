from random import shuffle, choices


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
            site = {"Location": (i, j), "Food": 0, "Agent": None}
            state["Sites"].append(site)
            state["Sites Matrix"][-1].append(state["Sites"][-1])
    location_indices = list(range(len(state["Sites"])))
    for l in choices(location_indices, k=params["Initial Number of Food Tiles"]):
        state["Sites"][l]["Food"] += 1
    return state


def create_initial_agents(state, params):
    state["Agents"] = []
    agent_types = ["Prey"] * params["Initial Number of Prey"] + ["Predator"] * params[
        "Initial Number of Predators"
    ]
    open_locations = state["Stateful Metrics"]["Open Locations Stateful Metric"](
        state, params
    )
    assert len(agent_types) <= len(open_locations)
    shuffle(agent_types)
    shuffle(open_locations)

    for agent, location in zip(agent_types, open_locations):
        if agent == "Predator":
            food = params["Initial Predator Food"]
        else:
            food = params["Initial Prey Food"]

        agent = {
            "Age": 0,
            "Agent Type": agent,
            "Food": food,
            "Location": location["Location"],
        }
        state["Agents"].append(agent)
        location["Agent"] = agent

    return state
