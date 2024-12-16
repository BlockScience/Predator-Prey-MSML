from .Site import (
    open_locations_stateful_metric,
    filled_locations_stateful_metric,
    prey_locations_stateful_metric,
    predator_locations_stateful_metric,
    median_site_food_stateful_metric,
)
from .Agent import (
    prey_stateful_metric,
    predator_stateful_metric,
    number_of_prey_stateful_metric,
    number_of_predators_stateful_metric,
    median_predator_food_stateful_metric,
    median_prey_food_stateful_metric,
    median_predator_age_stateful_metric,
    median_prey_age_stateful_metric,
)

stateful_metrics = {
    "Open Locations Stateful Metric": open_locations_stateful_metric,
    "Prey Stateful Metric": prey_stateful_metric,
    "Predator Stateful Metric": predator_stateful_metric,
    "Filled Locations Stateful Metric": filled_locations_stateful_metric,
    "Prey Locations Stateful Metric": prey_locations_stateful_metric,
    "Predator Locations Stateful Metric": predator_locations_stateful_metric,
    "Number of Prey Stateful Metric": number_of_prey_stateful_metric,
    "Number of Predators Stateful Metric": number_of_predators_stateful_metric,
    "Median Predator Food Stateful Metric": median_predator_food_stateful_metric,
    "Median Prey Food Stateful Metric": median_prey_food_stateful_metric,
    "Median Predator Age Stateful Metric": median_predator_age_stateful_metric,
    "Median Prey Age Stateful Metric": median_prey_age_stateful_metric,
    "Median Site Food Stateful Metric": median_site_food_stateful_metric,
}
