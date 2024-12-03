## Description

Randomly returns either A, B, C
## Called By
1. [[DUMMY Entity]]

## Followed By
1. [[DUMMY Letter Count Policy]]

## Constraints

## Codomain Spaces
1. [[DUMMY ABCDEF Space]]

## Metrics Used

## Parameters Used

## Boundary Action Options:
### 1. Length-1 ABC Equal Weight Option
#### Description
Equal weighted probability of choosing A, B or C
#### Logic
Select A, B, C with equal probabilities
#### Python Implementation
```python
def v1_dummy_boundary(state, params, spaces):
    return [{"string": choice(["A", "B", "C"])}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/BoundaryActions/Dummy.py](../../../src/Implementations/Python/BoundaryActions/Dummy.py)

