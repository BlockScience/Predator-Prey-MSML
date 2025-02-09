## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EES0(["Age"])
EES0 --- EE0
EES1(["Food"])
EES1 --- EE0
end

subgraph X4["Increase Agent Age Wiring"]
direction TB
X1["Increase Age Control Action"]
X2["Increase Agent Age Policy"]
X3["Age & Food Mechanisms"]
X3 --"State Update"--> EES0
X3 --"State Update"--> EES1
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>
<a href='Agent Age Delta Space' class=internal-link>Agent Age Delta Space</a>"---->X3
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
X3 --"State Update"--> EES1
X4["Increase Agent Age Mechanism"]
X4 --"State Update"--> EES0
X5[Domain]

direction LR
direction TB
X5 --"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"--> X3
X5 --"<a href='Agent Age Delta Space' class=internal-link>Agent Age Delta Space</a>"--> X4
end
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>
<a href='Agent Age Delta Space' class=internal-link>Agent Age Delta Space</a>"---->X7
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class X4 internal-link;
class X6 internal-link;
class EE0 internal-link;

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

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Agent.py#L33](../../../../src/Wiring/Agent.py#L33)

