## Description

The policy which determines how and when prey are hunted.
## Called By
## Domain Spaces
1. [[Agents Space]]
## Followed By
## Codomain Spaces
1. [[Agent Food Delta Space]]
2. [[Agents Space]]
## Constraints
## Parameters Used
## Metrics Used
1. [[Neighboring Valid Tiles Metric]]
2. [[Predator Stateful Metric]]
3. [[Prey Locations Stateful Metric]]
## Policy Options
### 1. Hunt Prey V1
#### Description
If a valid prey is in a nearby site then it is eaten. If there are multiple then there is a random choice.
#### Logic

#### Python Implementation
```python
def hunt_prey_policy_v1(state, params, spaces):
    possible_prey = state["Stateful Metrics"]["Prey Locations Stateful Metric"](
        state, params
    )
    possible_prey = [x["Location"] for x in possible_prey]
    predators = state["Stateful Metrics"]["Predator Stateful Metric"]
    print(possible_prey)
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Agent.py](../../../src/Implementations/Python/Policies/Agent.py)

