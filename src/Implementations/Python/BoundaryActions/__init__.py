from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2
from .Agent import (
    prey_feeding_boundary_action_v1,
    hunt_prey_boundary_action_v1,
    all_agents_move,
    reproduction_threshold_reproduction_boundary_action,
)

boundary_action_options = {
    "Length-1 ABC Equal Weight Option": v1_dummy_boundary,
    "DUMMY Length-2 ABC Equal Weight Option": v1_dummy_boundary2,
    "DUMMY Length-2 ABC Equal Weight 2 Option": v2_dummy_boundary2,
    "Prey Feeding Boundary Action V1": prey_feeding_boundary_action_v1,
    "Hunt Prey Boundary Action V1": hunt_prey_boundary_action_v1,
    "All Agents Movement": all_agents_move,
    "Reproduction Threshold Reproduction Boundary Action": reproduction_threshold_reproduction_boundary_action,
}
