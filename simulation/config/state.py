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
