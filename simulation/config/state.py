from copy import deepcopy

state_base = {
    "Dummy": {"Words": "", "Total Length": None},
    "Time": 0,
    "Simulation Log": [],
    "Agents": None,
    "Sites": None,
}

state_test1 = deepcopy(state_base)
state_test1["Time"] = 100

state_test_natural_death = deepcopy(state_base)
state_test_natural_death["Agents"] = [
    {"Age": 5, "Agent Type": "Predator", "Food": 10},
    {"Age": 5, "Agent Type": "Predator", "Food": 0},
    {"Age": 10, "Agent Type": "Predator", "Food": 10},
    {"Age": 15, "Agent Type": "Predator", "Food": 10},
]

state_base_prey_feeding_test = deepcopy(state_base)


state_hunt_prey_test = deepcopy(state_base)

state_agent_movement_test = deepcopy(state_base)

state_agent_reproduction_test = deepcopy(state_base)
