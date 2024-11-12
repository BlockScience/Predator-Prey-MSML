from .Dummy import dummy_control_actions
from .Site import site_control_actions

control_actions = []
control_actions.extend(dummy_control_actions)
control_actions.extend(site_control_actions)
