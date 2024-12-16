from .Site import site_policies
from .Agent import agent_policies
from .Meta import meta_policies

policies = []
policies.extend(site_policies)
policies.extend(agent_policies)
policies.extend(meta_policies)
