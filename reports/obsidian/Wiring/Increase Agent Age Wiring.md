## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EES0(["Age"])
EES0 --- EE0
EES1(["Food"])
EES1 --- EE0
end

subgraph X8["Increase Agent Age Wiring"]
direction TB
X1["Increase Age Control Action"]
X2["Increase Agent Age Policy"]
subgraph X7["Age & Food Mechanisms"]
direction TB
X3["Update Food Mechanism"]
X3 --> EES1
X4["Increase Agent Age Mechanism"]
X4 --> EES0
X5[Domain]

direction LR
direction TB
X5 --"Agent Food Delta Space"--> X3
X5 --"Agent Age Delta Space"--> X4
end
X1--"Agents Space"--->X2
X2--"Agent Food Delta Space
Agent Age Delta Space"---->X7
end
```

## Description

Block Type: Stack Block
Wiring for updating of the agent age and decreasing their food from aging
## Components
1. [[Increase Age Control Action]]
2. [[Increase Agent Age Policy]]
3. [[Age & Food Mechanisms]]

## All Blocks
1. [[Increase Age Control Action]]
2. [[Increase Agent Age Mechanism]]
3. [[Increase Agent Age Policy]]
4. [[Update Food Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Agent Age Delta Space]]
2. [[Agent Food Delta Space]]
3. [[Agents Space]]
4. [[Empty Space]]
5. [[Terminating Space]]

## Metrics Used

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Age|Age]]
2. [[Agent]].[[Agent State-Food|Food]]

