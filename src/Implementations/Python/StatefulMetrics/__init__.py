from .Dummy import dummy_metric
from .Site import open_locations_stateful_metric
from .Agent import prey_stateful_metric

stateful_metrics = {
    "DUMMY Nominal Length Stateful Metric": dummy_metric,
    "Open Locations Stateful Metric": open_locations_stateful_metric,
    "Prey Stateful Metric": prey_stateful_metric,
}
