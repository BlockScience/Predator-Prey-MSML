## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EE1[("Global")]
EE2[("Site")]
EES0(["Food"])
EES0 --- EE0
EES1(["Agents"])
EES1 --- EE1
EES2(["Agent"])
EES2 --- EE2
end

subgraph X5["Agent Reproduction Mechanisms"]
direction TB
X1["Create Agents Mechanism"]
X1 --> EES1
X1 --> EES2
X2["Update Food Mechanism"]
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"<a href='Agents Space' class=internal-link>Agents Space</a>"--> X1
X3 --"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"--> X2
end
class X1 internal-link;
class X2 internal-link;
class X4 internal-link;
class EE0 internal-link;
class EE1 internal-link;
class EE2 internal-link;

```

## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EE1[("Global")]
EE2[("Site")]
EES0(["Food"])
EES0 --- EE0
EES1(["Agents"])
EES1 --- EE1
EES2(["Agent"])
EES2 --- EE2
end

subgraph X5["Agent Reproduction Mechanisms"]
direction TB
X1["Create Agents Mechanism"]
X1 --> EES1
X1 --> EES2
X2["Update Food Mechanism"]
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"<a href='Agents Space' class=internal-link>Agents Space</a>"--> X1
X3 --"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"--> X2
end
class X1 internal-link;
class X2 internal-link;
class X4 internal-link;
class EE0 internal-link;
class EE1 internal-link;
class EE2 internal-link;

```

## Description

Block Type: Parallel Block
Wiring for reproduction
## Components
1. [[Create Agents Mechanism]]
2. [[Update Food Mechanism]]

## All Blocks
1. [[Create Agents Mechanism]]
2. [[Update Food Mechanism]]

## Constraints

## Domain Spaces
1. [[Agents Space]]
2. [[Agent Food Delta Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Agent Food Delta Space]]
2. [[Agents Space]]
3. [[Empty Space]]
4. [[Terminating Space]]

## Metrics Used

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Food|Food]]
2. [[Global]].[[Global State-Agents|Agents]]
3. [[Site]].[[Site State-Agent|Agent]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Agent.py](../../../../src/Wiring/Agent.py)

