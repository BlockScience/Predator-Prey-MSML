## Description

The policy determines the amount of food growth per site.
## Called By
1. [[Food Growth Control Action]]
## Domain Spaces
1. [[Locations Space]]
## Followed By
1. [[Update Food Locations Mechanism]]
## Codomain Spaces
1. [[Location Food Delta Space]]
## Constraints
## Parameters Used
1. [[Food Growth Rate]]
2. [[Maximum Food per Tile]]
## Metrics Used
## Policy Options
### 1. Constant Food Growth Policy
#### Description
Add a constant rate of food growth to each location up to the maximum
#### Logic
For each location, the delta is equal to min(Food + params["Food Growth Rate"], params["Maximum Food per Tile"])
#### Python Implementation
```python
def constant_food_growth_policy(state, params, spaces):
    space = {"Food Locations": []}
    for loc in spaces[0]["Locations"]:
        delta_food = min(
            params["Maximum Food per Tile"] - loc["Food"], params["Food Growth Rate"]
        )
        space["Food Locations"].append(
            {"Location": loc["Location"], "Food": delta_food}
        )
    return [space]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Site.py](../../../src/Implementations/Python/Policies/Site.py)

### 2. Poisson Food Growth Policy
#### Description
Food growth is based on the Poisson distribution
#### Logic
For each location, the delta is equal to min(Food + POISSON(params["Food Growth Rate"]), params["Maximum Food per Tile"])

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Policies/Site.py](../../../../src/Policies/Site.py)

