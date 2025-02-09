from copy import deepcopy

params_base = {
    "Site Size": (5, 5),
    "Maximum Food per Tile": 10,
    "Food Growth Rate": 1,
    "Initial Number of Food Tiles": 5,
    "Initial Number of Predators": 5,
    "Initial Number of Prey": 5,
    "Hunger Threshold": 5,
    "Maximum Age Parameter": 10,
    "Reproduction Food Threshold": 2,
    "Reproduction Probability": 0.25,
    "Reproduction Food Needed": 3,
    "Initial Prey Food": 5,
    "Initial Predator Food": 5,
    "FP Food Growth Policy": "Constant Food Growth Policy",
}


params_test_food_growth = deepcopy(params_base)
params_test_food_growth["Site Size"] = (2, 2)
params_test_food_growth["Maximum Food per Tile"] = 2
params_test_food_growth["Food Growth Rate"] = 1

params_test_food_growth2 = deepcopy(params_test_food_growth)
params_test_food_growth2["FP Food Growth Policy"] = "Poisson Food Growth Policy"

params_test2 = deepcopy(params_base)
params_test2["DUMMY D Probability"] = 0
params_test2["FP DUMMY Length-1 DEF Control Action"] = (
    "DUMMY Length-1 DEF D Probability Option"
)

params_prey_feeding_test = deepcopy(params_base)
params_prey_feeding_test["Site Size"] = (3, 2)
params_prey_feeding_test["Initial Number of Predators"] = 2
params_prey_feeding_test["Initial Number of Prey"] = 3
params_prey_feeding_test["Initial Prey Food"] = 5
params_prey_feeding_test["Initial Predator Food"] = 7
params_prey_feeding_test["Initial Number of Food Tiles"] = 10

params_hunt_prey_test = deepcopy(params_prey_feeding_test)
params_hunt_prey_test["Hunger Threshold"] = 10


params_agent_movement_test = deepcopy(params_prey_feeding_test)


params_agent_reproduction_test = deepcopy(params_base)
params_agent_reproduction_test["Site Size"] = (2, 2)
params_agent_reproduction_test["Initial Number of Predators"] = 0
params_agent_reproduction_test["Initial Number of Prey"] = 2
params_agent_reproduction_test["Initial Prey Food"] = 5

params_mech_test = deepcopy(params_base)
params_mech_test["Site Size"] = (3, 2)
params_mech_test["Initial Number of Predators"] = 2
params_mech_test["Initial Number of Prey"] = 3
params_mech_test["Initial Prey Food"] = 5
params_mech_test["Initial Predator Food"] = 7
params_mech_test["Initial Number of Food Tiles"] = 10
