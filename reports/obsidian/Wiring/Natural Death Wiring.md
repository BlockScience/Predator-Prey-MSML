## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Agents"])
EES0 --- EE0
end

subgraph X4["Natural Death Wiring"]
direction TB
X1["Natural Death Control Action"]
X2["Natural Death Policy"]
X3["Remove Agents Mechanism"]
X3 --> EES0
X1--"Agents Space"--->X2
X2--"Agents Space"--->X3
end
```

## Description

Block Type: Stack Block
Wiring for growth of food
## Components
1. [[Natural Death Control Action]]
2. [[Natural Death Policy]]
3. [[Remove Agents Mechanism]]

## All Blocks
1. [[Natural Death Control Action]]
2. [[Natural Death Policy]]
3. [[Remove Agents Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Agents Space]]
2. [[Empty Space]]
3. [[Terminating Space]]

## Parameters Used
1. [[Maximum Age Parameter]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Agents|Agents]]

