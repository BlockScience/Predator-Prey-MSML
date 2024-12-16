increment_time_mechanism = {
    "name": "Increment Time Mechanism",
    "description": "A mechanism which increments the current timestep",
    "constraints": [],
    "logic": """Add the delta timestep to the current timestep""",
    "domain": ["Timestep Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Timestep", False),
    ],
}

log_simulation_data_mechanism = {
    "name": "Log Simulation Data Mechanism",
    "description": "A mechanism which adds to the simulation log",
    "constraints": [],
    "logic": """Append the space to the simulation log""",
    "domain": ["Simulation Log Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Simulation Log", False),
    ],
}


meta_mechanisms = [increment_time_mechanism, log_simulation_data_mechanism]
