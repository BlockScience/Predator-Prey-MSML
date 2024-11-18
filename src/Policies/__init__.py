from .Dummy import dummy_policies
from .Site import site_policies
from .Agent import agent_policies

policies = []
policies.extend(dummy_policies)
policies.extend(site_policies)
policies.extend(agent_policies)
