Description: A metric of the non-busy tiles that are neighbors. The first domain element is the locations to query, the second is the busy tiles (or the free tiles if you want to flip it and have the returned values be the potential mates/tiles where there is a neighboring agent).

Type: [[Location Type]]

Symbol: None

## Logic
Query the location neighbors then filter out any that are busy

## Parameters Used
1. [[Site Size]]

## Variables Used

## Domain Spaces
1. [[Locations Space]]
2. [[Locations Space]]
## Metrics Used
## Python Implementation
```python
def neighboring_valid_tiles_metric(state, params, spaces):
    out = []
    open_locations = spaces[1]["Locations"]
    dim_x = params["Site Size"][0]
    dim_y = params["Site Size"][1]
    for loc in spaces[0]["Locations"]:
        options = [
            ((loc[0] + x) % dim_x, (loc[1] + y) % dim_y)
            for x, y in zip([1, 0, -1, 0], [0, 1, 0, -1])
        ]
        options = set([x for x in options if x in open_locations])
        out.append(options)
    return out
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Metrics/Agent.py#L1](../../../src/Implementations/Python/Metrics/Agent.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Metrics/Site.py#L21](../../../../src/Metrics/Site.py#L21)

