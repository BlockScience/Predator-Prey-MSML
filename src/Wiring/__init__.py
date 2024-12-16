from .Site import site_wiring
from .Agent import agent_wiring
from .Meta import meta_wiring

wiring = []
wiring.extend(site_wiring)
wiring.extend(agent_wiring)
wiring.extend(meta_wiring)
