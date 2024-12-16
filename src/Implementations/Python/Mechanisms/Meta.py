def increment_time_mechanism(state, params, spaces):
    state["Timestep"] += spaces[0]["Timestep"]


def log_simulation_data_mechanism(state, params, spaces):
    state["Simulation Log"].append(spaces[0])
