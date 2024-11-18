from .Dummy import (
    dummy_update_dummy_entity_mechanism,
    dummy_increment_time_mechanism,
    dummy_log_simulation_data_mechanism,
)
from .Site import update_food_locations_mechanism
from .Agent import (
    remove_agents_mechanism,
    update_food_mechanism,
    update_agent_age_mechanism,
)

mechanisms = {
    "DUMMY Update Dummy Entity Mechanism": dummy_update_dummy_entity_mechanism,
    "DUMMY Increment Time Mechanism": dummy_increment_time_mechanism,
    "DUMMY Log Simulation Data Mechanism": dummy_log_simulation_data_mechanism,
    "Update Food Locations Mechanism": update_food_locations_mechanism,
    "Remove Agents Mechanism": remove_agents_mechanism,
    "Update Food Mechanism": update_food_mechanism,
    "Increase Agent Age Mechanism": update_agent_age_mechanism,
}
