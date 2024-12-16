from .Site import site_spaces
from .Agent import agents_spaces
from .Meta import meta_spaces

spaces = []

spaces.extend(site_spaces)
spaces.extend(agents_spaces)
spaces.extend(meta_spaces)
