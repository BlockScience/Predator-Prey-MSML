from .Dummy import dummy_multiplied_length_metric
from .Site import available_food_metric
from .Agent import neighboring_valid_tiles_metric, is_neighbor_metric

metrics = {
    "DUMMY Multiplied Length Metric": dummy_multiplied_length_metric,
    "Available Food Metric": available_food_metric,
    "Neighboring Valid Tiles Metric": neighboring_valid_tiles_metric,
    "Is Neighbor Metric": is_neighbor_metric,
}
