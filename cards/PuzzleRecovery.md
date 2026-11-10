# G09: Failure feedback, changed actions and recovery windows

[Parent group](Narrative.md) | [Knowledge hub](README.md)

General knowledge; design applications are untested. A game's own approved decisions prevail.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G09.05 Interactive narrative | [K09-23](#k09-23); [K09-24](#k09-24); [K09-25](#k09-25); [K09-26](#k09-26) |
| G09.06 Quests and objectives | [K09-23](#k09-23); [K09-25](#k09-25); [K09-26](#k09-26) |

## K09-23

**A reasonable failed attempt deserves a specific response.** A plausible unsuccessful action can receive a response that recognizes the intended attempt and its obstacle.

- Kind: general guidance. Focus: reactivity; Puzzle-story integration and fairness; failure and continuation.
- Apply: Write responses for likely wrong approaches alongside the intended solution.
- Limit: Acknowledging an attempt need not reveal the complete solution.
- Check: Distinguish an unrecognized instruction from an understood action that cannot work here.
- Supports [K03-08](ActionsAndCombat.md#k03-08): A response can reveal a relevant property for the next inference.
- Supports [K03-02](ActionsAndCombat.md#k03-02): Specific failure feedback reduces guessing at accepted vocabulary.

## K09-24

**Major events must change the actions that remain possible.** A consequential event can invalidate earlier actions or entity roles; later interactions must respect the changed situation.

- Kind: general guidance. Focus: reactivity; persistent consequences; World-state reactivity and persistent consequences.
- Apply: After a departure or death, inspect interactions that previously required that participant.
- Limit: Revised descriptions alone do not establish consistent action availability.
- Check: Attempt an old interaction after the event and compare it with the stated consequence.
- Requires [K01-02](Foundations.md#k01-02): Consequences must alter the relevant action prerequisites or outcomes.
- Supports [K09-08](Narrative.md#k09-08): State-sensitive wording should agree with the interactions still available.

## K09-25

**Continued play can hide an already unreachable ending.** Losing a necessary resource or leaving it beyond an irreversible boundary can make completion impossible while ordinary play continues.

- Kind: general guidance. Focus: Quest goals, prerequisites and consequences; Failure states and recovery; failure and continuation.
- Apply: Check future goals after plausible consumption, abandonment or one-way travel.
- Limit: One failed attempt does not establish that the whole run is unwinnable.
- Check: Trace a remaining completion path after each irreversible loss of a prerequisite.
- Requires [K09-03](Narrative.md#k09-03): Future dependencies reveal whether the lost resource was indispensable.
- Requires [K09-24](PuzzleRecovery.md#k09-24): Reachability must be checked against the changed action set.

## K09-26

**A warning needs a usable recovery window.** An immediate warning after an irreversible mistake permits correction only if an available recovery action can still reverse that mistake.

- Kind: general guidance. Focus: Failure states and recovery; failure and continuation.
- Apply: Place warnings before commitment or identify the actual remaining recovery opportunity.
- Limit: General undo examples do not by themselves justify changing a game's persistence or death rules.
- Check: Follow the warning at its actual time and demonstrate the available corrective action.
- Requires [K03-07](ActionsAndCombat.md#k03-07): A preventive warning must provide useful evidence before commitment.
- Requires [K01-04](Foundations.md#k01-04): Any proposed recovery must respect the approved persistence contract.

## Worked dependency

[K09-26](PuzzleRecovery.md#k09-26) -> [K03-07](ActionsAndCombat.md#k03-07) -> [K02-01](PlayerExperience.md#k02-01)

Condition: An action would consume a resource needed for a later objective.
Rejecting probe: Locate the useful cue before commitment, or demonstrate an allowed recovery action while it remains available.
