## Description

The policy which determines the amount of food that each location will eat.
## Called By
1. [[Prey Feeding Boundary Action]]
## Domain Spaces
1. [[Agents Space]]
## Followed By
1. [[Update Food Locations Mechanism]]
2. [[Update Food Mechanism]]
## Codomain Spaces
1. [[Location Food Delta Space]]
2. [[Agent Food Delta Space]]
## Constraints
## Parameters Used
## Metrics Used
1. [[Available Food Metric]]
## Policy Options
### 1. Prey Eat All Food Policy
#### Description
Eat all the food at the location
#### Logic
For every location the prey eats all the food available
#### Python Implementation
```python
def prey_eat_all_food_policy(state, params, spaces):
    locations = [x["Location"] for x in spaces[0]["Agents"]]
    available_food = state["Metrics"]["Available Food Metric"](
        state, params, [{"Locations": locations}]
    )
    space1 = {
        "Food Locations": [
            {"Location": x, "Food": -y} for x, y in zip(locations, available_food)
        ]
    }
    space2 = {
        "Food Deltas": [
            {"Agent": x, "Delta Food": y}
            for x, y in zip(spaces[0]["Agents"], available_food)
        ]
    }
    return [space1, space2]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Agent.py](../../../src/Implementations/Python/Policies/Agent.py)

