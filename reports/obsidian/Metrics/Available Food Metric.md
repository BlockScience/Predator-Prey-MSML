Description: A metric of the available food at each location.

Type: [[Food Type]]

Symbol: None

## Logic
Query the locations and their foods

## Parameters Used

## Variables Used
1. [[Global State]].[[Global State-Sites|Sites]]
2. [[Site State]].[[Site State-Food|Food]]

## Domain Spaces
1. [[Locations Space]]
## Metrics Used
## Python Implementation
```python
def available_food_metric(state, params, spaces):
    sites = [state["Sites Matrix"][x[0]][x[1]] for x in spaces[0]["Locations"]]
    food = [x["Food"] for x in sites]
    return food
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Metrics/Site.py](../../../src/Implementations/Python/Metrics/Site.py)

