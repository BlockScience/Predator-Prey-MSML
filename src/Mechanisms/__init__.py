from .Dummy import dummy_mechanisms
from .Site import site_mechanisms
from .Agent import agent_mechanisms

mechanisms = []
mechanisms.extend(dummy_mechanisms)
mechanisms.extend(site_mechanisms)
mechanisms.extend(agent_mechanisms)
