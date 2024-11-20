from .Dummy import dummy_metrics
from .Site import site_metrics

metrics = []
metrics.extend(dummy_metrics)
metrics.extend(site_metrics)
