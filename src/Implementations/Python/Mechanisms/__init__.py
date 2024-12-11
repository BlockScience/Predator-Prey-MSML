from .Site import update_food_locations_mechanism, update_agent_locations_mechanism
from .Agent import (
    remove_agents_mechanism,
    update_food_mechanism,
    update_agent_age_mechanism,
    create_agents_mechanism,
)

mechanisms = {
                "Update Food Locations Mechanism": update_food_locations_mechanism,
    "Remove Agents Mechanism": remove_agents_mechanism,
    "Update Food Mechanism": update_food_mechanism,
    "Increase Agent Age Mechanism": update_agent_age_mechanism,
    "Create Agents Mechanism": create_agents_mechanism,
    "Update Agent Locations Mechanism": update_agent_locations_mechanism,
}
