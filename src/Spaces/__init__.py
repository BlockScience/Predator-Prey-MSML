from .Dummy import dummy_spaces
from .Site import site_spaces
from .Agent import agents_spaces

spaces = []
spaces.extend(dummy_spaces)
spaces.extend(site_spaces)
spaces.extend(agents_spaces)
