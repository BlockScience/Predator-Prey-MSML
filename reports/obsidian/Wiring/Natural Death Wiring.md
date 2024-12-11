## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
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
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X3
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class EE0 internal-link;

```

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
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X3
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class EE0 internal-link;

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

## Metrics Used

## Parameters Used
1. [[Maximum Age Parameter]]

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Agents|Agents]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Agent.py](../../../../src/Wiring/Agent.py)

