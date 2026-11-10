# G03 — Player actions, combat and systemic mechanics

[Knowledge hub](README.md) · [Cross-domain chains](Connections.md) | [Continuation: Cover and encounter commitment](EncounterTactics.md) | [Continuation: Force, travel and contact in tool interactions](ToolMechanics.md)

General principles below are distinct from their proposed application; the applications are untested. For objects moving with water currents, inspect [relative motion](#k03-10) before assigning resistance.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G03.01 Movement and embodiment | [K03-01](#k03-01); [K03-11](#k03-11); [K03-12](#k03-12); [K03-13](#k03-13) |
| G03.02 Interaction and affordances | [K03-02](#k03-02); [K03-11](#k03-11); [K03-14](#k03-14); [K03-15](#k03-15); [K03-20](ToolMechanics.md#k03-20); [K03-21](ToolMechanics.md#k03-21); [K03-22](ToolMechanics.md#k03-22); [K03-23](ToolMechanics.md#k03-23) |
| G03.03 Combat | [K03-03](#k03-03); [K03-05](#k03-05); [K03-06](#k03-06); [K03-12](#k03-12); [K03-16](EncounterTactics.md#k03-16); [K03-17](EncounterTactics.md#k03-17); [K03-18](EncounterTactics.md#k03-18); [K03-19](EncounterTactics.md#k03-19) |
| G03.04 Stealth and evasion | [K03-03](#k03-03); [K03-07](#k03-07); [K03-12](#k03-12); [K03-16](EncounterTactics.md#k03-16) |
| G03.05 Puzzles and investigation | [K03-02](#k03-02); [K03-08](#k03-08); [K03-09](#k03-09); [K03-15](#k03-15) |
| G03.06 Environmental systems | [K03-01](#k03-01); [K03-07](#k03-07); [K03-10](#k03-10); [K03-13](#k03-13); [K03-22](ToolMechanics.md#k03-22) |
| G03.07 Objects and equipment | [K03-04](#k03-04); [K03-06](#k03-06); [K03-09](#k03-09); [K03-14](#k03-14); [K03-20](ToolMechanics.md#k03-20); [K03-21](ToolMechanics.md#k03-21); [K03-23](ToolMechanics.md#k03-23) |
| G03.08 Failure and recovery | [K03-04](#k03-04); [K03-09](#k03-09) |

## K03-01

**Motion follows accumulated forces.** Acceleration depends on net force and mass; zero net force means unchanged velocity, not an automatic stop.

- Kind: general guidance. Focus: locomotion; physics interactions.
- Apply: Describe movement through acceleration, braking and contact rather than only maximum speed; apply the same logic to affected props.
- Limit: A game can simplify physics, but exceptions need a legible and consistent response; this is no engine parameter prescription.
- Check: Compare starting, stopping, turning and external pushes in a simple movement sketch.
- Supports [K13-03](CharactersAndMotion.md#k13-03): Readable anticipation and recovery depend on how movement starts and stops.
- Supports [K03-10](ActionsAndCombat.md#k03-10): Resistance is one force whose effect depends on the medium and motion.
- Supports [K03-13](ActionsAndCombat.md#k03-13): A movement model can combine multiple influences before applying the resulting acceleration.

## K03-02

**Puzzles should test an inference, not vocabulary.** A solvable puzzle must expose enough evidence for its intended operation; refusing reasonable equivalent actions can turn inference into input guessing.

- Kind: general guidance. Focus: interaction consistency; clues and deduction.
- Apply: Write an intended reasoning path plus plausible failed actions and their feedback before adding locks or unique tools.
- Limit: Historical puzzle preferences do not prove that all players dislike a particular puzzle type.
- Check: Can the player infer the operation from visible evidence, and does a sensible failure teach something?
- Requires [K09-03](Narrative.md#k09-03): Puzzle prerequisites must be available before an irreversible dependency blocks progress.
- Requires [K03-08](ActionsAndCombat.md#k03-08): An inference needs observable properties that inspection can reveal.

## K03-03

**Position changes the encounter.** Opposition can change through position, visibility, retreat and morale rather than only through damage or health totals.

- Kind: general guidance. Focus: range and positioning; hiding and escape.
- Apply: Design an encounter with an approach, a readable commitment and a viable disengagement condition; compare direct and evasive choices.
- Limit: These are candidate encounter properties, not a specification of defensive actions, stealth rules or enemy morale.
- Check: Trace the encounter from two starting positions and identify which choices actually change.
- Requires [K06-03](SpatialDesign.md#k06-03): Approach and retreat depend on sightlines, reach and escape space.

## K03-04

**Recovery costs can occupy other capabilities.** Recovery can consume time, exposure or carrying capacity; these produce different tradeoffs from a simple currency deduction.

- Kind: general guidance. Focus: equipment tradeoffs; cooperative rescue.
- Apply: Evaluate a recovery proposal against the activities it displaces and the distance to the next meaningful choice.
- Limit: The game's own death and loot rules prevail; this principle does not by itself call for equipment loss, timed corpse removal or hunger.
- Check: Trace failure to useful participation and count forced repetition and lost cooperative activity.
- Constrains [K04-01](EconomyAndProgression.md#k04-01): A cost changes progression by displacing resources or opportunities.
- Requires [K04-04](EconomyAndProgression.md#k04-04): A recurring recovery cost needs repeated-use observation to separate decisions from handling work.

## K03-05

**Telegraphs must expose a usable response.** A timed defensive action depends on detecting an attack cue before the response opportunity closes.

- Kind: general guidance. Focus: attack and defense; timing and commitment; enemy intent; hit feedback and recovery.
- Apply: Specify cue, commitment, consequence and recovery as separate moments.
- Limit: A readable still pose does not establish a usable timing window.
- Check: Check whether the intended response remains possible from representative camera views.
- Requires [K13-04](CharactersAndMotion.md#k13-04): Motion must reveal the decision window before impact.

## K03-06

**Weapons occupy situational roles.** Range, rate, resource demand and handling distinguish weapons across situations.

- Kind: general guidance. Focus: tools and weapons; range and positioning.
- Apply: Compare tools against near, distant, crowded and resource-poor encounters.
- Limit: A numerical upgrade can erase niches without creating a new decision.
- Check: Find a situation where each proposed tool is preferable and one where it is costly.
- Requires [K04-03](EconomyAndProgression.md#k04-03): Balance comparisons need stated conditions.

## K03-07

**Detection rules need observable evidence.** A player can reason about danger when exposure and consequences are communicated before commitment.

- Kind: design inference. Focus: visibility and exposure; search and suspicion; fair detection; consequence readability.
- Apply: Separate an observer's possible perception from what the player knows about that perception.
- Limit: This is a design inference about fairness; it establishes no particular stealth model.
- Check: Explain a detection using cues available before the action.
- Requires [K02-01](PlayerExperience.md#k02-01): Threat cues must remain distinctive enough to retrieve.

## K03-08

**Inspection should support incremental inference.** Examination can reveal properties relevant to different approaches without directly announcing a solution.

- Kind: general guidance. Focus: rule discovery; spatial puzzles; physical puzzles.
- Apply: Give observable material, spatial and behavioral clues at increasing inspection depth.
- Limit: Hiding every relevant property behind trial and error prevents informed inference.
- Check: Show how a player could reject one approach and justify another from available evidence.
- Supports [K03-02](ActionsAndCombat.md#k03-02): Puzzle interaction should test reasoning rather than a hidden vocabulary.
- Supports [K03-15](ActionsAndCombat.md#k03-15): Deeper inspection can be compared with its time cost when events continue during searching.

## K03-09

**Consuming prerequisites can make later objectives unreachable.** Consuming or losing a required object can make a later objective unreachable; other irreversible changes can remove needed states.

- Kind: general guidance. Focus: multiple solutions and dead ends; softlocks and safeguards; inventory decisions.
- Apply: Trace consumed, abandoned and transformed prerequisites through alternate action orders.
- Limit: This does not by itself justify replacing a game's established death or inventory rules.
- Check: Find a continuation after each permitted early loss, or explicitly reject the action in the design.
- Requires [K09-03](Narrative.md#k09-03): Softlocks are exposed by the dependency graph.

## K03-10

**Drag depends on motion relative to the medium.** In a quadratic drag model, resistance opposes velocity relative to the fluid and its magnitude grows with the square of that relative speed. An object carried by a current can move quickly through the world while having little motion relative to the water.

- Kind: general guidance. Focus: material reactions; physics interactions; system combinations.
- Apply: Compare how drag slows an object in stationary water with its response in a flowing current.
- Limit: Quadratic drag is a model with regime assumptions; it is not every fluid's universal response.
- Check: Compare an object moving with the current against one moving equally fast against it.
- Requires [K03-01](ActionsAndCombat.md#k03-01): Drag contributes to net force rather than directly specifying position.
- Requires [K16-11](ResearchAndProduction.md#k16-11): A discrete update can introduce behavior absent from the force model.

## K03-11

**Seeking and arriving need different speed goals.** Steering toward a target at full desired speed can overshoot; arrival reduces desired speed near the destination.

- Kind: general guidance. Focus: locomotion; movement feedback; reach and timing.
- Apply: Specify both approach behavior and the intended stopping condition for a movement concept.
- Limit: This simple steering model does not guarantee obstacle avoidance or feasible body motion.
- Check: Approach from different speeds and distances; inspect overshoot and time to settle.
- Requires [K01-03](Foundations.md#k01-03): Steering and locomotion must remain distinguishable.
- Requires [K13-11](CharactersAndMotion.md#k13-11): Turning response is a separate constraint from desired speed.
- Supports [K03-12](ActionsAndCombat.md#k03-12): Pursuit adds target-position prediction to the separate problem of approach speed.

## K03-12

**Pursuit aims ahead of a moving target.** Pursuit can steer toward a target's future position extrapolated from its current velocity instead of continually aiming at its present location.

- Kind: general guidance. Focus: locomotion; range and positioning; hiding and escape.
- Apply: Distinguish following behind a moving target from attempting an interception; state what motion the pursuer can observe and predict.
- Limit: A velocity-based prediction can fail when the target turns or accelerates; it does not establish a traversable route or guaranteed interception.
- Check: Compare straight motion with abrupt target turns and inspect where the pursuer aims before evaluating contact or attack timing.
- Requires [K03-11](ActionsAndCombat.md#k03-11): The desired target position and the desired approach speed are separate choices.
- Requires [K06-05](SpatialDesign.md#k06-05): A predicted point still needs a traversable connection rather than visibility alone.

## K03-13

**Weighted steering combines competing movement goals.** A steering model can combine separately calculated influences, such as seeking a target and separating from neighbors, with weights controlling their relative contribution.

- Kind: general guidance. Focus: locomotion; physics interactions; system combinations.
- Apply: When crowded agents seek one destination, inspect how attraction and spacing compete rather than assuming that both intentions are fully satisfied.
- Limit: A weighted sum can weaken or cancel an influence; it is not a guarantee of collision-free movement or biological accuracy.
- Check: Compare isolated influences with their combination near a crowded target and record loss of progress, spacing or directional stability.
- Requires [K03-01](ActionsAndCombat.md#k03-01): The combined influences must agree with the model's accumulated forces.
- Supports [K01-08](Foundations.md#k01-08): Local movement interactions can produce different group patterns from different starting arrangements.

## K03-14

**Consumable depletion can count transitions instead of time.** A depletion model can spend a use each time a light is lit or restarted, while continuous burning spends no further uses. This differs from depletion by elapsed time.

- Kind: design inference. Focus: consumables; action feedback.
- Apply: For a consumable concept, state the event that reduces its remaining uses and how that change is communicated.
- Limit: Design inference: a use counter is one possible model; it does not establish a timer, approved resource rule or optimal depletion rate.
- Check: Compare uninterrupted use with repeated stopping and restarting; explain exactly which events spend a use and what the participant can observe.
- Requires [K01-06](Foundations.md#k01-06): The depletion event needs an observable counterpart consistent with its actual trigger.
- Supports [K03-09](ActionsAndCombat.md#k03-09): Limited remaining uses can affect whether an item-dependent objective remains reachable.

## K03-15

**An exhaustive search can trade uncertainty for exposure time.** An exploration procedure can make a thorough search reveal relevant hidden features while consuming time during which other events remain possible.

- Kind: design inference. Focus: clues and deduction; reach and timing.
- Apply: Define the searched object or area, the evidence a completed search provides and the opportunity displaced by spending that time.
- Limit: Design inference: this tradeoff exists only if the model advances consequential time; repeating a button press is not evidence of a meaningful search decision.
- Check: Compare searching now, searching later and moving on; identify the uncertainty reduced and the events or opportunities that can change meanwhile.
- Requires [K03-08](ActionsAndCombat.md#k03-08): The information revealed must support an inference about the examined place or object.
- Supports [K04-05](EconomyAndProgression.md#k04-05): Time spent searching can displace another useful action or opportunity.
