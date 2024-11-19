from .Dummy import dummy_stateful_metrics
from .Site import site_stateful_metrics
from .Agent import agent_stateful_metrics

stateful_metrics = []
stateful_metrics.extend(dummy_stateful_metrics)
stateful_metrics.extend(site_stateful_metrics)
stateful_metrics.extend(agent_stateful_metrics)
