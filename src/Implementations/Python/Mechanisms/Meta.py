def increment_time_mechanism(state, params, spaces):
    state["Timestep"] += spaces[0]["Timestep"]
