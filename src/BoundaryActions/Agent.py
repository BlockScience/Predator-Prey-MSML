prey_feeding_boundary_action_option1 = {
    "name": "Prey Feeding Boundary Action V1",
    "description": "All hungry prey eats",
    "logic": "Filter to just prey and then filter out any prey that are not hungry.",
}

prey_feeding_boundary_action = {
    "name": "Prey Feeding Boundary Action",
    "description": "Boundary action which returns the prey that might eat.",
    "constraints": [],
    "boundary_action_options": [
        prey_feeding_boundary_action_option1,
    ],
    "called_by": ["Agent"],
    "codomain": [
        "Agents Space",
    ],
    "parameters_used": ["Hunger Threshold"],
    "metrics_used": ["Prey Stateful Metric"],
}

hunt_prey_boundary_action_option1 = {
    "name": "Hunt Prey Boundary Action V1",
    "description": "All hungry predators seek out to eat prey",
    "logic": "Filter to just predators and then filter out any predators that are not hungry.",
}

hunt_prey_boundary_action = {
    "name": "Hunt Prey Boundary Action",
    "description": "Boundary action which returns the prey that might eat.",
    "constraints": [],
    "boundary_action_options": [
        hunt_prey_boundary_action_option1,
    ],
    "called_by": ["Agent"],
    "codomain": [
        "Agents Space",
    ],
    "parameters_used": ["Hunger Threshold"],
    "metrics_used": ["Predator Stateful Metric"],
}

agent_movement_boundary_action_option1 = {
    "name": "All Agents Movement",
    "description": "All agents move",
    "logic": "Return all agents after randomly shuffling the order",
}

agent_movement_boundary_action = {
    "name": "Agent Movement Boundary Action",
    "description": "Boundary action which determines which agents can move and also the ordering of which ones move first.",
    "constraints": [],
    "boundary_action_options": [
        agent_movement_boundary_action_option1,
    ],
    "called_by": ["Agent"],
    "codomain": [
        "Agents Space",
    ],
    "parameters_used": [],
    "metrics_used": [],
}

agent_boundary_actions = [
    prey_feeding_boundary_action,
    hunt_prey_boundary_action,
    agent_movement_boundary_action,
]
