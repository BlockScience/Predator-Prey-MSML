## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EE1[("Site")]
EES0(["Food"])
EES0 --- EE0
EES1(["Food"])
EES1 --- EE1
end

subgraph X8["Prey Feeding Wiring"]
direction TB
X1["Prey Feeding Boundary Action"]
X2["Prey Feeding Policy"]
subgraph X7["Food Eating Mechanisms"]
direction TB
X3["Update Food Locations Mechanism"]
X3 --> EES1
X4["Update Food Mechanism"]
X4 --> EES0
X5[Domain]

direction LR
direction TB
X5 --"Location Food Delta Space"--> X3
X5 --"Agent Food Delta Space"--> X4
end
X1--"Agents Space"--->X2
X2--"Location Food Delta Space
Agent Food Delta Space"---->X7
end
```

## Description

Block Type: Stack Block
Wiring for when prey eats food
## Components
1. [[Prey Feeding Boundary Action]]
2. [[Prey Feeding Policy]]
3. [[Food Eating Mechanisms]]

## All Blocks
1. [[Prey Feeding Boundary Action]]
2. [[Prey Feeding Policy]]
3. [[Update Food Locations Mechanism]]
4. [[Update Food Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Agent Food Delta Space]]
2. [[Agents Space]]
3. [[Empty Space]]
4. [[Location Food Delta Space]]
5. [[Terminating Space]]

## Metrics Used
1. [[Available Food Metric]]
2. [[Prey Stateful Metric]]

## Parameters Used
1. [[Hunger Threshold]]

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Food|Food]]
2. [[Site]].[[Site State-Food|Food]]

