grow_food_control_action_option1 = {
    "name": "Food Growth Control Action V1",
    "description": "Simply pick all sites that do not have the maximum food yet",
    "logic": "Filter out sites with maximum food and otherwise pass the rest through",
}


grow_food_control_action = {
    "name": "Food Growth Control Action",
    "description": "Returns a list of locations that might potentially have food growth",
    "constraints": [],
    "control_action_options": [
        grow_food_control_action_option1,
    ],
    "codomain": [
        "Locations Space",
    ],
    "parameters_used": ["Maximum Food per Tile"],
}

site_control_actions = [grow_food_control_action]
