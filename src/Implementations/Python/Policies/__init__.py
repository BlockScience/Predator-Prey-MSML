from .Site import constant_food_growth_policy
from .Agent import (
    natural_death_policy,
    increase_agent_age_policy_plus1,
    prey_eat_all_food_policy,
    random_agent_movement_with_sieve,
    hunt_prey_policy_v1,
    agent_reproduction_policy_v1,
)
from .Meta import simulation_meta_policy_v1

policies = {
    "Constant Food Growth Policy": constant_food_growth_policy,
    "Natural Death Policy V1": natural_death_policy,
    "Increase Agent Age Policy +1": increase_agent_age_policy_plus1,
    "Prey Eat All Food Policy": prey_eat_all_food_policy,
    "Random Agent Movement with Sieve": random_agent_movement_with_sieve,
    "Hunt Prey V1": hunt_prey_policy_v1,
    "Agent Reproduction Policy V1": agent_reproduction_policy_v1,
    "Simulation Meta Policy V1": simulation_meta_policy_v1,
}
