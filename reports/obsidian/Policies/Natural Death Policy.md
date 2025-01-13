## Description

The policy which determines which agents die.
## Called By
1. [[Natural Death Control Action]]
## Domain Spaces
1. [[Agents Space]]
## Followed By
1. [[Remove Agents Mechanism]]
## Codomain Spaces
1. [[Agents Space]]
## Constraints
## Parameters Used
1. [[Maximum Age Parameter]]
## Metrics Used
## Policy Options
### 1. Natural Death Policy V1
#### Description
Anyone over the maximum age dies and anyone with no food dies
#### Logic
Filter list by the above
#### Python Implementation
```python
def natural_death_policy(state, params, spaces):
    agents = spaces[0]["Agents"]
    space = {
        "Agents": [
            agent
            for agent in agents
            if agent["Age"] >= params["Maximum Age Parameter"] or agent["Food"] <= 0
        ]
    }
    return [space]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Agent.py#L4](../../../src/Implementations/Python/Policies/Agent.py#L4)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Policies/Agent.py#L2](../../../../src/Policies/Agent.py#L2)

