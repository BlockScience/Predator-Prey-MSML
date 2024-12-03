## Description

The policy which determines the age increase and the decrease in food.
## Called By
1. [[Increase Age Control Action]]
## Domain Spaces
1. [[Agents Space]]
## Followed By
1. [[Update Food Mechanism]]
2. [[Increase Agent Age Mechanism]]
## Codomain Spaces
1. [[Agent Food Delta Space]]
2. [[Agent Age Delta Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Increase Agent Age Policy +1
#### Description
Simple +1 to age and -1 to food
#### Logic
Return spaces that increase age by 1 and decrease food by 1 for all agents in the domain
#### Python Implementation
```python
def increase_agent_age_policy_plus1(state, params, spaces):
    agents = spaces[0]["Agents"]
    space1 = {"Food Deltas": [{"Agent": x, "Delta Food": -1} for x in agents]}
    space2 = {"Age Deltas": [{"Agent": x, "Delta Age": 1} for x in agents]}
    return [space1, space2]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Agent.py](../../../src/Implementations/Python/Policies/Agent.py)

