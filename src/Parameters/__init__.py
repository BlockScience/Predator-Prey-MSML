from .Dummy import dummy_parameter_sets
from .Site import site_parameter_sets
from .Agent import agent_parameter_sets


parameters = []
parameters.extend(dummy_parameter_sets)
parameters.extend(site_parameter_sets)
parameters.extend(agent_parameter_sets)
