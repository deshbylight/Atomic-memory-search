# G06 — Level design and spatial experience: visible destinations and traversable routes

[Knowledge hub](README.md) · [Cross-domain chains](Connections.md) · [Continuation: Learning sequences, nonlinear pacing and navigation signals](SpatialLearning.md) | [Continuation: Roster matrices and usable opportunities for supported approaches](EncounterComposition.md) | [Continuation: Current occupation, inhabitant responses and unclaimed rewards](SpatialOccupation.md) | [Continuation: Rest conditions, service adjacency and activity districts](RecoveryAndServices.md)

General principles below are distinct from their proposed application; the applications are untested.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G06.01 Experience and pacing | [K06-01](#k06-01); [K06-06](#k06-06); [K06-11](#k06-11); [K06-15](SpatialLearning.md#k06-15); [K06-16](SpatialLearning.md#k06-16) |
| G06.02 Topology and circulation | [K06-02](#k06-02); [K06-05](#k06-05); [K06-06](#k06-06); [K06-11](#k06-11); [K06-12](#k06-12); [K06-13](#k06-13) |
| G06.03 Navigation and discovery | [K06-02](#k06-02); [K06-05](#k06-05); [K06-08](#k06-08); [K06-12](#k06-12); [K06-14](#k06-14); [K06-17](SpatialLearning.md#k06-17); [K06-18](SpatialLearning.md#k06-18); [K06-27](RecoveryAndServices.md#k06-27) |
| G06.04 Metrics and blockout | [K06-01](#k06-01); [K06-07](#k06-07) |
| G06.05 Encounter space | [K06-03](#k06-03); [K06-08](#k06-08); [K06-11](#k06-11); [K06-13](#k06-13); [K06-17](SpatialLearning.md#k06-17); [K06-19](EncounterComposition.md#k06-19); [K06-20](EncounterComposition.md#k06-20); [K06-25](RecoveryAndServices.md#k06-25) |
| G06.06 Space and fiction | [K06-03](#k06-03); [K06-12](#k06-12); [K06-21](SpatialOccupation.md#k06-21); [K06-22](SpatialOccupation.md#k06-22); [K06-23](SpatialOccupation.md#k06-23); [K06-24](SpatialOccupation.md#k06-24); [K06-26](RecoveryAndServices.md#k06-26) |
| G06.07 Hubs and repeated spaces | [K06-04](#k06-04); [K06-06](#k06-06); [K06-22](SpatialOccupation.md#k06-22); [K06-25](RecoveryAndServices.md#k06-25); [K06-26](RecoveryAndServices.md#k06-26); [K06-27](RecoveryAndServices.md#k06-27) |
| G06.08 Procedural experience | [K06-04](#k06-04); [K06-09](#k06-09); [K06-10](#k06-10) |

## K06-01

**A drawing is an experience hypothesis.** A layout organizes a proposed experience; its navigability and timing require a blockout and playtest rather than visual inspection alone.

- Kind: general guidance. Focus: experience goals; blockout iteration.
- Apply: Pair each pacing beat with an intended action and build the cheapest playable space that can test it at player scale.
- Limit: A pleasing plan or a successful traversal by its author does not verify player experience.
- Check: Observe approach time, hesitation and decisions in a blockout before committing art production.
- Supports [K16-02](ResearchAndProduction.md#k16-02): The cheapest prototype should test the largest uncertain dependency.

## K06-02

**Topology and recognition solve different problems.** Circulation, vertical links and the critical path describe connections; a usable connection still requires the player to recognize where it leads.

- Kind: general guidance. Focus: loops and shortcuts; landmarks.
- Apply: Draw a route graph separately from landmark and sightline placement; test a return route as well as the outward path.
- Limit: Extra loops can reduce retracing but can also create ambiguity; a recognizable landmark does not repair a disconnected graph.
- Check: Trace destination reachability, then ask a new player to choose the correct exit from each decision point.
- Requires [K02-01](PlayerExperience.md#k02-01): Players need distinctive cues to retrieve the route they previously learned.
- Supports [K15-04](InteractionAndAccess.md#k15-04): When participants separate, recognizable destinations need a way to communicate shared intent and state.
- Supports [K06-14](SpatialDesign.md#k06-14): Remembered relationships between recognizable places can support return navigation.

## K06-03

**Encounter geometry is a functional story.** A room typology and its circulation organize possible activity; visible geometry can explain occupation while shaping access and exposure.

- Kind: general guidance. Focus: position and cover; original function.
- Apply: Give an encounter a former use, a current use and a movement consequence; place obstructions where those uses explain them.
- Limit: Historical plausibility does not guarantee good combat; verify reach, visibility and escape using the game's actual metrics.
- Check: Explain why each major obstruction exists and which player or enemy action it changes.
- Requires [K11-01](BuiltWorld.md#k11-01): Occupation and service routes give the room a programme beyond its combat label.
- Supports [K06-12](SpatialDesign.md#k06-12): A place's activities and users can explain the roles of its connecting spaces.

## K06-04

**Repeated spaces need state-aware tests.** A structure that works once may behave differently when revisited; dependency bottlenecks and changed access can reshape the next route.

- Kind: general guidance. Focus: meaningful change on return; seed-specific evaluation.
- Apply: Test generated or reused spaces in initial, occupied, altered and return states; choose representatives by structural differences.
- Limit: This is a design test strategy, not proof of generation correctness or permission to reset the approved persistent world.
- Check: Compare a return visit after a door change, resource removal and group separation.
- Requires [K01-04](Foundations.md#k01-04): The approved persistence contract determines which changes survive a return.
- Constrains [K03-04](ActionsAndCombat.md#k03-04): When recovery revisits altered spaces, its route and participation cost must use the retained state.

## K06-05

**Sightlines and traversal are different connections.** Seeing a destination does not imply a route to it; route direction and traversal cost are independent attributes.

- Kind: general guidance. Focus: critical and optional paths; branching; sightlines; concealment and reveal.
- Apply: Overlay visibility and movement relationships rather than treating every visual connection as a passage.
- Limit: This abstraction does not establish runtime line-of-sight or navigation.
- Check: Trace the route to a visible goal and identify where knowledge of the route is obtained.
- Requires [K01-07](Foundations.md#k01-07): Network edges need direction and a stated meaning.

## K06-06

**A loop changes the cost of returning.** A connecting route can shorten retracing while an irreversible shortcut changes the set of reachable return states.

- Kind: general guidance. Focus: repeat traversal; loops and shortcuts; gates and return routes; player loops.
- Apply: Compare first approach, return traversal and reverse access separately.
- Limit: Extra connections can weaken deliberate commitment or orientation.
- Check: Trace both visits and verify what the shortcut preserves, bypasses and makes unreachable.
- Requires [K01-04](Foundations.md#k01-04): Return routes operate in the retained world state.

## K06-07

**Metrics depend on the action toolkit.** Combat space depends on movement, attack reach, resource availability and camera conditions.

- Kind: general guidance. Focus: player dimensions; movement clearance; combat distances; scale and proportions; blockout iteration.
- Apply: Block out clearance, reach and sightlines using representative actions before surface detail.
- Limit: A scale drawing cannot establish how the implemented controller handles the space.
- Check: Check movement, response and retreat in the same blockout rather than separately idealized diagrams.
- Requires [K03-03](ActionsAndCombat.md#k03-03): Position changes what the encounter permits.

## K06-08

**A room presents information in layers.** An initial description can establish essential orientation while inspection reveals optional detail.

- Kind: general guidance. Focus: entry and survey; orientation cues.
- Apply: Separate immediate threats, exits and distinguishing features from deeper evidence.
- Limit: Withholding a prerequisite cue as optional detail can make the intended decision unfair.
- Check: Explain the first available choice using only information exposed on entry.
- Supports [K03-08](ActionsAndCombat.md#k03-08): Inspection should deepen an inference after orientation is established.

## K06-09

**A good sample does not establish a good generator.** Expressive range describes which measurable combinations a generator produces and how frequently; selected attractive outputs conceal bias.

- Kind: general guidance. Focus: variation with identity; seed-specific evaluation.
- Apply: Compare a representative sample along experience-relevant dimensions.
- Limit: Metric diversity is not proof of enjoyable play and depends on the dimensions chosen.
- Check: Include rejected outputs and identify dense, absent and rare regions of the sample.
- Requires [K16-01](ResearchAndProduction.md#k16-01): Generator quality needs an observation matched to the claim.
- Supports [K01-09](Foundations.md#k01-09): Observed output changes help evaluate whether author controls are useful.

## K06-10

**Mission dependencies and spatial adjacency are separate graphs.** A mission graph orders required actions; a spatial graph connects places. Mapping between them must preserve action dependencies without assuming a room's geometry.

- Kind: general guidance. Focus: mission and spatial graphs; room roles; adjacency and transition.
- Apply: Label actions and prerequisites before assigning them to rooms and transitions.
- Limit: A valid mission ordering does not establish movement clearance, readable gates or suitable encounter space.
- Check: Trace the intended and bypass routes in the spatial graph against the mission prerequisites.
- Requires [K01-02](Foundations.md#k01-02): Action prerequisites must be explicit before embedding them in space.
- Requires [K06-07](SpatialDesign.md#k06-07): Geometric realization still needs action-specific metrics.
- Supports [K09-03](Narrative.md#k09-03): Spatial mapping can expose a narrative prerequisite bypass or bottleneck.

## K06-11

**Verticality needs an activity purpose.** Stairs, ramps and changes in height alter speed, turning and exposure; additional vertical variation is not inherently better.

- Kind: general guidance. Focus: beats and contrast; vertical connections; position and cover.
- Apply: Name the activity changed by each raised route, drop or landing.
- Limit: An inefficient route can deliberately support observation or tension; smoothness is not the only goal.
- Check: Traverse the blockout with the actual movement toolkit and compare intended versus observed behavior.
- Requires [K06-01](SpatialDesign.md#k06-01): A layout's proposed movement must be tested in a blockout.
- Requires [K06-07](SpatialDesign.md#k06-07): Height changes are meaningful relative to available actions.

## K06-12

**Circulation hierarchy carries expectations about use.** Primary, secondary, public and private circulation describe different uses of connecting space. Apparent passage size can suggest importance, but recognizable function can change that reading.

- Kind: general guidance. Focus: critical and optional paths; orientation cues; original function; inhabitant logistics.
- Apply: Relate doors, corridors and stairs to the people and destinations they serve; compare that fictional use with the player's usable route.
- Limit: A wide opening is not automatically the main route; a vehicle door and a pedestrian door can imply different access despite their size.
- Check: At a junction, state where each passage appears to lead and verify its actual users, access and destination.
- Requires [K11-10](BuiltWorld.md#k11-10): Circulation must account for the users and loads expected to pass through it.
- Supports [K06-02](SpatialDesign.md#k06-02): Recognizing a route's role complements its actual connectivity.

## K06-13

**Lanes and rotations organize shared movement.** A lane is a prominent movement route; connecting lanes lets participants change approach or flank a blocked route. Rotation is movement between those routes.

- Kind: general guidance. Focus: branching; position and cover; cooperative routes.
- Apply: Compare how teammates change approach, regroup or respond to a blocked lane, including the connections between routes.
- Limit: Lane count alone does not establish balance; alternate routes need a distinct practical role and may increase coordination demands.
- Check: Block one main approach and trace the remaining options, including what teammates must know to rotate together.
- Requires [K01-10](Foundations.md#k01-10): Local connections and travel between routes must be evaluated separately.
- Requires [K05-02](CooperativePlay.md#k05-02): When rotation needs shared coordination, communication bottlenecks affect the usable alternatives.

## K06-14

**Mental maps need relationships as well as landmarks.** A mental representation of space can include paths, boundaries, districts, junctions and landmarks; recognizing a landmark does not alone specify one's position or a route.

- Kind: general guidance. Focus: landmarks; orientation cues; maps and spatial memory.
- Apply: Evaluate whether a player can relate recognizable places across a return journey, including when the current goal changes.
- Limit: A mental map is a conceptual representation, not necessarily a geometrically accurate survey; different navigation strategies can succeed.
- Check: After exploration, ask for a route between two known places and a sketch of the relevant junctions; compare relationships with actual access.
- Requires [K06-02](SpatialDesign.md#k06-02): Recognizable places and usable connections contribute different information.
- Requires [K02-01](PlayerExperience.md#k02-01): Landmark cues must remain distinctive enough to support later retrieval.
