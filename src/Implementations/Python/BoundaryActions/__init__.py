from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2
from .Agent import prey_feeding_boundary_action_v1

boundary_action_options = {
    "Length-1 ABC Equal Weight Option": v1_dummy_boundary,
    "DUMMY Length-2 ABC Equal Weight Option": v1_dummy_boundary2,
    "DUMMY Length-2 ABC Equal Weight 2 Option": v2_dummy_boundary2,
    "Prey Feeding Boundary Action V1": prey_feeding_boundary_action_v1,
}
