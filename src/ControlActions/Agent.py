natural_death_control_action_v1 = {
    "name": "Natural Death Control Action V1",
    "description": "Simply return all agents",
    "logic": "Return all agents",
}


natural_death_control_action = {
    "name": "Natural Death Control Action",
    "description": "Returns a list of potential agents that might die",
    "constraints": [],
    "control_action_options": [
        natural_death_control_action_v1,
    ],
    "codomain": [
        "Agents Space",
    ],
    "parameters_used": [],
}


increase_age_control_action_option1 = {
    "name": "Increase Age Control Action V1",
    "description": "Simply return all agents",
    "logic": "Return all agents",
}


increase_age_control_action = {
    "name": "Increase Age Control Action",
    "description": "Returns a list of potential agents that should have their age increased",
    "constraints": [],
    "control_action_options": [
        increase_age_control_action_option1,
    ],
    "codomain": [
        "Agents Space",
    ],
    "parameters_used": [],
}


agent_control_actions = [natural_death_control_action, increase_age_control_action]
