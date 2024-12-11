from .Agent import (
    prey_feeding_boundary_action_v1,
    hunt_prey_boundary_action_v1,
    all_agents_move,
    reproduction_threshold_reproduction_boundary_action,
)

boundary_action_options = {
                "Prey Feeding Boundary Action V1": prey_feeding_boundary_action_v1,
    "Hunt Prey Boundary Action V1": hunt_prey_boundary_action_v1,
    "All Agents Movement": all_agents_move,
    "Reproduction Threshold Reproduction Boundary Action": reproduction_threshold_reproduction_boundary_action,
}
