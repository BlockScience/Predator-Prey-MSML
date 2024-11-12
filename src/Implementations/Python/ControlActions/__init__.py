from .Dummy import v1_dummy_control, v2_dummy_control
from .Site import food_growth_control_action_v1

control_action_options = {
    "DUMMY Length-1 DEF Equal Weight Option": v1_dummy_control,
    "DUMMY Length-1 DEF D Probability Option": v2_dummy_control,
    "Food Growth Control Action V1": food_growth_control_action_v1,
}
