Description: The list of sites with prey on them

Type: [[Locations Array Type]]

Symbol: None

Domain: None

## Parameters Used

## Variables Used
1. [[Global State]].Sites
2. [[Site State]].Agent

## Python Implementation
```python
def prey_locations_stateful_metric(state, params):

    return [
        site
        for site in state["Sites"]
        if (site["Agent"] is not None) and (site["Agent"]["Agent Type"] == "Prey")
    ]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Site.py](../../../src/Implementations/Python/StatefulMetrics/Site.py)

