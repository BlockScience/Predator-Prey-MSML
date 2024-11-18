from .Dummy import dummy_wiring
from .Site import site_wiring
from .Agent import agent_wiring

wiring = []
wiring.extend(dummy_wiring)
wiring.extend(site_wiring)
wiring.extend(agent_wiring)
