# programming

## physical simulation rules
- [mechanism] Buoyancy depends on weight versus displaced water; added weight sinks a submerged object, removing it lets it float; decay gas, body fat, bone size and water temperature alter surfacing.
- [mechanism] Include real ground shape in a physical test: slopes or banks can roll or deflect a falling object so it ends far from its first contact point. When: testing a claimed fall from height, or an object falls across a curved slope or embankment. Why: intermediate motion and the slope change the direction of travel.
- [mechanism] Impact type shapes the fragment pattern: a drop yields a few large pieces, while crushing grinds material into many small grains. Why: the energy and contact type determine how material separates.
- [mechanism] A trajectory system that records where a thrown item lands lets players reconstruct an event from what remains in the scene.
- [mechanism] Physics-driven props respond to forces, so a staged display can collapse or shift on contact, revealing whether it was disturbed.
- [mechanism] A recording instrument with a damper that stops motion after each shock can register the next shock cleanly, whereas undamped instruments keep vibrating and blur the record. When: Detecting small vibrations from movement. Why: Residual oscillation from one shock masks the next.
- [mechanism] A flash-lit camera capture can reveal a fine wire or trigger that dim ordinary light hides from view. When: A decisive moment involves a mechanism too fine to see in normal lighting. Why: Flash exposure freezes an instant with light the eye does not get.
- [mechanism] A freshly washed surface fixes a timeline: footprints on it show whether anyone walked there since the washing. When: A surface was cleaned or wetted at a known time. Why: Any print made after the wetting records a later passage.
- [mechanism] Tides and currents can carry objects and bodies from one place and strand them in eddies at another. When: A body or object lies far from its origin. Why: Moving water transports material and drops it where flow slows.
- [rule] Derive damage and wear from material properties, so a damaged item shows which force caused it.
- [rule] Rule out deflection before trusting a straight trajectory: a steep impact angle and high velocity keep a projectile on a straight path.
- [rule] Trace a ray from a recorded hit point back along the shot's path to narrow a sniper's probable location.
- [rule] A game can split evidence processing into roles, where a lab tool gives a range or a match rather than a single answer. When: designing forensic tools in a game. Why: Probabilistic results keep players reasoning rather than receiving a final answer.
- [heuristic] Treat a rough physical test as a filter that rules some explanations out, not as proof that a specific explanation is true. When: a cheap experiment is used on a complex event. Why: a simple model cannot capture every factor.
- [procedure] 1) Replace the moving object with a simple stand-in 2) Launch it at a set force 3) Note where its path ends relative to the scene 4) Repeat several trials. When: a physical event must be tested against a scene. Why: a stand-in gives cheap evidence about plausibility.
- [fact] A snag usually splits fabric into two rents at right angles that meet where the object entered. When: when modelling how fabric tears from a point impact.
- [fact] A piece with two free edges can be torn off by one force, while a piece with one edge or a hemmed edge is much harder to remove.
- [fact] Light containers may float rather than sink, so water is a poor disposal method for small boxes. When: Choosing a disposal method for an object. Why: Buoyancy can bring an object back into view.

## item and object state
- [mechanism] A sealed item's state flag, or an object's position, can record that it was opened, letting the player test whether it was tampered with. Why: flags record handling as game state.
- [rule] Track each object's location and change history, including moves by NPCs or the player, so visible shade or wear differences and disturbed evidence can be traced to recorded moves. When: Objects can be moved during play or change off-screen, or when implementing interactions that can affect clues. Why: A recorded history explains visible state changes; recorded changes let players detect what happened before they arrived; a change log shows whether a scene has been altered. (x2)
- [rule] Record which items should exist in a scene and which were removed, so a missing item is detectable and checkable as a clue. When: A puzzle depends on items removed from a scene or designing item tracking for a scene. Why: Comparing expected and actual state exposes the gap; tracked removals make the missing item checkable.
- [rule] Track wet or muddy clothing as a state flag on each NPC, so it can disprove a claimed alibi when the check is made.
- [rule] Store item wear with a timestamp so the game can distinguish fresh damage from old damage. Why: Clues that depend on recency need the game to know when the damage happened.
- [rule] Store a bleed state and a time-of-wound flag on a corpse, so a blow applied after death reads as a staged injury. When: Building a corpse-inspection system. Why: Recorded timing lets the game distinguish pre-death and post-death injuries.
- [rule] Give bodies and objects state tags such as fragmentation pattern, residue, decay level and submersion position so players can deduce origin and handling. When: Designing physical remains or objects that players should interpret. Why: Structured state tags make physical evidence readable and consistent.
- [heuristic] Track which character holds which document as game state, since access to a copy can open or close a route. When: Designing quests where documents gate progress.
- [heuristic] Give vehicles, lamps or torches a fuel or charge count that falls with use, so players can work out how long each was active.
- [heuristic] Store item wear, condition and location values so an object's use and handling can be read from its record. When: When designing inventory or loot data. Why: Recorded history lets the player infer how an object was used.

## investigation state tracking
- [rule] Record a last-seen state for each NPC, and let a staged sighting in another location create or remove suspicion. When: Implementing NPC tracking and suspicion systems. Why: Lets the game respond to false or misleading information in a consistent way.
- [rule] Track the player's current theory as game state, and when a new clue contradicts it, prompt re-evaluation instead of silently keeping the old theory. When: When a game lets players hold explicit suspicions about events. Why: Explicit tracking makes contradictions visible so the player can revise their beliefs.

## clue source tracking
- [rule] Track the source of each clue so the game can tell whether a conclusion rests on independent evidence or one shared inference. When: When a game system evaluates whether an accusation is supported. Why: Shared origins can make a conclusion appear better supported than it is.

## verdict state handling
- [rule] Let a formal verdict fire on sworn-style testimony and revise it only when new evidence is introduced. When: Implementing legal or verdict systems in games. Why: Matches the logic of record-based decisions and keeps state changes intentional.
