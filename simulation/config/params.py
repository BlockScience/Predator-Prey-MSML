from copy import deepcopy

params_base = {
    "DUMMY D Probability": 0.5,
    "DUMMY Length Multiplier": 3,
    "FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF Equal Weight Option",
    "FP DUMMY Length-2 ABC Combo Boundary Action": "DUMMY Length-2 ABC Equal Weight Option",
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
}


params_test_food_growth = deepcopy(params_base)
params_test_food_growth["Site Size"] = (2, 2)
params_test_food_growth["Maximum Food per Tile"] = 2
params_test_food_growth["Food Growth Rate"] = 1


params_test2 = deepcopy(params_base)
params_test2["DUMMY D Probability"] = 0
params_test2["FP DUMMY Length-1 DEF Control Action"] = (
    "DUMMY Length-1 DEF D Probability Option"
)
