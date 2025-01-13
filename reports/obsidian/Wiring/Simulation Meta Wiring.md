## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Simulation Log"])
EES0 --- EE0
EES1(["Timestep"])
EES1 --- EE0
end

subgraph X3["Simulation Meta Wiring"]
direction TB
X1["Simulation Meta Policy"]
X2["Simulation Meta Mechanisms"]
X2 --"State Update"--> EES0
X2 --"State Update"--> EES1
X1--"<a href='Timestep Space' class=internal-link>Timestep Space</a>
<a href='Simulation Log Space' class=internal-link>Simulation Log Space</a>"---->X2
end
class X1 internal-link;
class X2 internal-link;
class EE0 internal-link;

```

## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Simulation Log"])
EES0 --- EE0
EES1(["Timestep"])
EES1 --- EE0
end

subgraph X7["Simulation Meta Wiring"]
direction TB
X1["Simulation Meta Policy"]
subgraph X6["Simulation Meta Mechanisms"]
direction TB
X2["Increment Time Mechanism"]
X2 --"State Update"--> EES1
X3["Log Simulation Data Mechanism"]
X3 --"State Update"--> EES0
X4[Domain]

direction LR
direction TB
X4 --"<a href='Timestep Space' class=internal-link>Timestep Space</a>"--> X2
X4 --"<a href='Simulation Log Space' class=internal-link>Simulation Log Space</a>"--> X3
end
X1--"<a href='Timestep Space' class=internal-link>Timestep Space</a>
<a href='Simulation Log Space' class=internal-link>Simulation Log Space</a>"---->X6
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class X5 internal-link;
class EE0 internal-link;

```

## Description

Block Type: Stack Block
Wiring for meta simulation steps
## Components
1. [[Simulation Meta Policy]]
2. [[Simulation Meta Mechanisms]]

## All Blocks
1. [[Increment Time Mechanism]]
2. [[Log Simulation Data Mechanism]]
3. [[Simulation Meta Policy]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Simulation Log Space]]
3. [[Terminating Space]]
4. [[Timestep Space]]

## Metrics Used

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Simulation Log|Simulation Log]]
2. [[Global]].[[Global State-Timestep|Timestep]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Meta.py#L5](../../../../src/Wiring/Meta.py#L5)

