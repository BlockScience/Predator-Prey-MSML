from .Dummy import dummy_letter_count_policy
from .Site import constant_food_growth_policy
from .Agent import natural_death_policy


policies = {
    "DUMMY Letter Count Policy V1": dummy_letter_count_policy,
    "Constant Food Growth Policy": constant_food_growth_policy,
    "Natural Death Policy V1": natural_death_policy,
}
