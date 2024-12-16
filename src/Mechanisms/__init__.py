from .Site import site_mechanisms
from .Agent import agent_mechanisms
from .Meta import meta_mechanisms

mechanisms = []
mechanisms.extend(site_mechanisms)
mechanisms.extend(agent_mechanisms)
mechanisms.extend(meta_mechanisms)
