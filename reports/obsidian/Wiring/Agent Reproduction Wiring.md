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

subgraph X4["Agent Reproduction Wiring"]
direction TB
X1["Agent Reproduction Boundary Action"]
X2["Agent Reproduction Policy"]
X3["Agent Reproduction Mechanisms"]
X3 --> EES0
X3 --> EES1
X3 --> EES2
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agents Space' class=internal-link>Agents Space</a>
<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"---->X3
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
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

subgraph X8["Agent Reproduction Wiring"]
direction TB
X1["Agent Reproduction Boundary Action"]
X2["Agent Reproduction Policy"]
subgraph X7["Agent Reproduction Mechanisms"]
direction TB
X3["Create Agents Mechanism"]
X3 --> EES1
X3 --> EES2
X4["Update Food Mechanism"]
X4 --> EES0
X5[Domain]

direction LR
direction TB
X5 --"<a href='Agents Space' class=internal-link>Agents Space</a>"--> X3
X5 --"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"--> X4
end
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agents Space' class=internal-link>Agents Space</a>
<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"---->X7
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class X4 internal-link;
class X6 internal-link;
class EE0 internal-link;
class EE1 internal-link;
class EE2 internal-link;

```

## Description

Block Type: Stack Block
Wiring for agents hunting prey
## Components
1. [[Agent Reproduction Boundary Action]]
2. [[Agent Reproduction Policy]]
3. [[Agent Reproduction Mechanisms]]

## All Blocks
1. [[Agent Reproduction Boundary Action]]
2. [[Agent Reproduction Policy]]
3. [[Create Agents Mechanism]]
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
4. [[Terminating Space]]

## Metrics Used
1. [[Is Neighbor Metric]]
2. [[Neighboring Valid Tiles Metric]]
3. [[Open Locations Stateful Metric]]
4. [[Predator Stateful Metric]]
5. [[Prey Stateful Metric]]

## Parameters Used
1. [[Reproduction Food Needed]]
2. [[Reproduction Food Threshold]]
3. [[Reproduction Probability]]

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Food|Food]]
2. [[Global]].[[Global State-Agents|Agents]]
3. [[Site]].[[Site State-Agent|Agent]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Agent.py#L116](../../../../src/Wiring/Agent.py#L116)

