from copy import deepcopy

state_base = {
    "Timestep": 0,
    "Simulation Log": [],
    "Agents": None,
    "Sites": None,
}

state_test1 = deepcopy(state_base)
state_test1["Time"] = 100

state_test_natural_death = deepcopy(state_base)
state_test_natural_death["Agents"] = [
    {"Age": 5, "Agent Type": "Predator", "Food": 10, "Location": (0, 0)},
    {"Age": 5, "Agent Type": "Predator", "Food": 0, "Location": (0, 1)},
    {"Age": 10, "Agent Type": "Predator", "Food": 10, "Location": (1, 0)},
    {"Age": 15, "Agent Type": "Predator", "Food": 10, "Location": (1, 1)},
]

state_base_prey_feeding_test = deepcopy(state_base)


state_hunt_prey_test = deepcopy(state_base)

state_agent_movement_test = deepcopy(state_base)

state_agent_reproduction_test = deepcopy(state_base)

state_mech_test = deepcopy(state_base)
