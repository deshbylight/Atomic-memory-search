# level-design

## level layout and structure
- [model] Progression can be gated by the map itself: locks opened by the player's current abilities, with reusable keys, instead of scripted quest triggers. When: Designing progression for a traversal-heavy game. Why: Ability-gated locks are more robust than scripts and allow out-of-order exploration.
- [model] Levels exist for eight reasons: resource limits, design workflow, visual unity, narrative, skill escalation, player memory, reset and pacing, plus theming and reward. When: when justifying a level structure. Why: each reason supports a different design goal.
- [mechanism] Corridors limit which tiles count as flank or rear, so room and corridor layout determines how facing rules play out. Why: Geometry constrains the attack directions that can occur.
- [mechanism] Sound markers point toward unseen areas, so their direction depends on the room layout. Why: Walls and rooms determine where noise originates relative to the player.
- [rule] A key opens one exit; each additional exit on a level costs one sacrificed item, and only one key can be carried at a time. When: levels with multiple exits.
- [rule] Level design should support learning rules, suspension of disbelief, and single-use content cool enough to justify being used once.
- [heuristic] Keep levels small enough to avoid boredom, but well connected between rooms. When: Designing roguelike levels. Why: Players tire of large empty levels yet dislike poorly linked ones.
- [heuristic] Dense levels with vaults, unusual monster groups, secret rooms and dungeon features keep play varied. When: Filling a roguelike level with content. Why: Varied features reduce repetition across the dungeon.
- [heuristic] Keep general areas to roam between pitfalls, where the player gains experience and has fun.
- [heuristic] Place a compelling obstacle between the player and a known destination to create a pull. When: Placing goals and blockers in a generated level.
- [heuristic] Judge a space by its topology, meaning its choke points, cover and objectives, rather than by its visual architecture, since players think in these terms. When: Evaluating or generating a layout for play. Why: Players navigate by tactical features, so structure matters more than appearance.
- [heuristic] Design goals such as mood, tempo, story, difficulty ramp and payoff justify level splits better than loading limits alone, which are not the sole reason for levels. When: when deciding whether to split a game into levels. Why: loading explains levels less well than design goals.
- [tradeoff] Corridors that allow only one or two attackers suit cautious play, while open rooms enable crowd tactics; room shape therefore shapes how crowd combat works. When: Designing levels for melee crowd combat. Why: Attacker count per position is set by geometry, so open layouts let many enemies reach the player.
- [pitfall] A single obvious path through a level removes choice and reduces the sense of discovery. When: Designing linear levels with one intended route. Why: Players follow the route without deciding anything, so puzzles lose their purpose.
- [pitfall] Relying on scale and visual effects in place of interesting structure weakens level design. When: Designing large levels with strong visuals. Why: Spectacle does not give the player meaningful choices or challenges.
- [fact] Worlds are usually quantized to a grid or cube, though hex grids have also been tried.
- [fact] Open worlds with minimal gating are better received than hub-and-spoke designs that unlock content through quests, forming a continuum.
- [fact] A level is a discrete area interrupted by a map load or a period without play. When: when defining levels in a game's structure.

## terrain and trap effects
- [model] A safe town or death area needs a distant, low-danger zone from which the player re-enters the dungeon. When: Generating the respawn zone of a dungeon game. Why: The re-entry point must be separated from danger to be a fair restart.
- [mechanism] Teleport, switching places and knockback depend on open tiles and room or corridor shape, so blocked tiles or layout change whether and how the effect plays out. When: A critical moves or swaps the target. Why: Blocked tiles change whether the effect can happen; movement effects interact with walls and open space.
- [rule] Distinguish disarmable traps from fixed trap regions in the display before adding overlapping regions. When: Designing how ranged trap areas are shown to the player. Why: Traps can be disarmed while regions cannot, so the player needs to tell them apart.
- [rule] Keep grids holding objects or features free of hidden hazards, so that an object on a grid reliably signals safe ground to the player. When: Placing ranged traps whose target regions may cover object-holding grids. Why: Players learn that objects mark safe floor, and a hazard under an object breaks that expectation.
- [rule] Design traps to produce the conditions that allow avoidance, such as a light trap that darkens the room, so players learn how to avoid them. When: Creating traps that should be learnable by the player. Why: Players can only learn avoidance when the trap reveals the state that counters it.
- [heuristic] Use a small set of terrain effects that fit the game's theme; stacking many effects overloads play. When: Designing terrain for a roguelike. Why: Too many effects are hard to learn and understand.
- [pitfall] Exotic terrain effects may confuse players if they are not explained. When: Adding unusual terrain behavior. Why: Players cannot predict an effect they do not understand.
- [pitfall] One-way movement can trap the player in a section that needs powers they do not yet have. When: Ability-gated maps allow one-way passages. Why: The player cannot leave without the missing powers, so progress stops.
- [pitfall] Procedurally generated open terrain exposes movement problems, such as tree roots blocking motion, that hand-smoothed levels hide. When: Generating open terrain procedurally for a shooter. Why: Hand-smoothed levels conceal movement faults that appear with irregular generated geometry.
- [pitfall] Relying on attractive terrain while neglecting topology and content is a common trap, since a good layout alone does not make a good game. When: Building a level or world around scenery. Why: Looks do not supply the tactical structure or the content that drive play.
- [fact] Roguelike terrain can affect movement, characters, items, combat, light, and other systems, including time-based change, encounter tables, hidden traps, summoning, and spellcasting.
- [fact] Movement terrain effects include slowing, speeding, blocking, preventing exit, randomizing movement, teleporting, changing level, adding fatigue, and changing stealth.
- [fact] Character terrain effects include damage, status changes, granting experience, draining stats, changing hunger or thirst rates, class or race bonuses, and religious influences.
- [fact] Item terrain effects include destroying, enchanting, cursing or blessing, damaging, preserving, or polymorphing items.
- [fact] Combat terrain effects include changing evasion, blocking, hindering or aiding missiles, destroying missiles, causing slips, and changing elemental attacks.
- [fact] Light terrain effects include blocking, distorting, making translucent, transparent or tinted, and self-illuminating light.
- [fact] Terrain triggers can be automatic, optional, a saving throw or skill roll, or vary by species, movement mode, items, statuses or skills.

## pushables and obstacle puzzles
- [mechanism] Area spell reach depends on the map, so how far an effect extends across rooms and walls depends on layout. Why: Walls and rooms cut area shapes.
- [mechanism] A push promises something more impressive than what has been seen, while a pull promises the shown thing will be as good as it seems.
- [behavior] When players can reshape terrain and attach to what they build, dead-end corridors become useful corridors or landmarks. When: Games let players modify topology and build structures. Why: Player investment in built structures turns otherwise useless spaces into meaningful places.
- [rule] Obstacles should admit several solutions, and risky options should offer rewards the player can decline. When: Designing obstacles and optional risks. Why: Multiple solutions keep choices meaningful and voluntary.
- [rule] A platform part that must stay attached to a chain can have stricter terrain requirements than the rest of the platform.
- [heuristic] Clear target identification helps players make tactical decisions. When: designing encounters with many similar-looking actors. Why: Players must be able to tell threats apart to act on them.
- [heuristic] If a puzzle can be solved once understood with no trial and error, it may be too easy to learn from; require planning and experimentation. When: Checking whether a puzzle rewards thinking. Why: Puzzles solved trivially after understanding give no lasting challenge.
- [procedure] 1) Bumping an impassable terrain feature pushes it into an adjacent empty floor grid. 2) The player steps into the vacated grid. 3) Try the push direction first, then alternate clockwise and counter-clockwise through neighbouring grids.
- [tradeoff] Simple node-and-edge maps are honest but weak, so push dominates; non-trivial maps let pull narrative do more work. When: Choosing map complexity for a game's progression. Why: Simple maps leave no puzzle between the player and the destination, while complex maps invite exploration.
- [pitfall] Players may button-mash past an obstacle without learning the underlying skill.
- [pitfall] Pushing terrain into a dead end can trap the player, so a recovery method such as a pull command or a push-down action with a random direction is needed.

## doors and ability gating
- [definition] The door need not be literal; a river, lake, boulder, guardian or end-of-level boss can serve as the obstacle.
- [mechanism] In a randomly generated layout, a lock-and-key key hunt becomes a fetch quest with no clear destination, unlike hand-designed levels where locations are fixed. When: Gated lock-and-key progression is applied to random layouts. Why: Without designed locations, the player has no defined target for the key.
- [mechanism] Levels guarantee a minimum skill level and a maximum challenge, while open worlds allow instant-death zones that break escalation. When: when deciding between level-based and open-world structure. Why: bounded areas control how hard the player's next challenge can be.
- [rule] Gate areas with the player's current powers, such as breaking a lock with a specific weapon, so keys can be reused and locks broken without blocking progress. When: Designing progression gates in a metroidvania-style map. Why: Reusable keys and breakable locks keep progress possible even when the player skips sections.
- [heuristic] To avoid a repetitive treadmill, introduce new behaviours such as ranged attacks or new movement one at a time, then in combination. When: When difficulty alone feels repetitive.
- [procedure] 1) Place an obstacle that blocks progress until the player masters an ability. 2) Make it look insurmountable at first. 3) Include hints pointing to the needed ability. 4) Reuse that ability in later skill, timing or interrelated puzzles. When: An important ability's use or interface is not obvious.
- [tradeoff] Introducing abilities in later levels or harder difficulties splits the game into sub-games of rising complexity, but may not suit fast action genres such as RTS or FPS. Why: Intense action can be disrupted by tutorial-style gating.
- [pitfall] If an obstacle gives no clear way to learn the ability, the player may never understand it and quit in frustration.

## saves, memory, and pacing
- [definition] Narrative velocity is what keeps a player moving through a game; a push is the designer pointing toward an unknown next goal, and a pull is a known destination that is compelling enough for the player to set their own goal.
- [mechanism] Levels limit the number of options a player must remember, reducing memory load. When: when designing area size and complexity. Why: smaller areas present fewer things to track.
- [mechanism] Levels give every player the same starting footing and natural save points. When: when designing progression and saving. Why: clear boundaries provide consistent resets and save moments.
- [heuristic] Pushes rely on novelty and pulls rely on repetition, so good design balances introducing new tools with paying off each one.
- [pitfall] Save points placed far from danger force players to repeat the same route after each load, which becomes boring. When: Placing save points in a dungeon or world layout. Why: Repeated traversal of the same route after each reload wears down player patience.
- [pitfall] Heavy scripting and unclear guidance make players doubt whether a journey is worthwhile; scripted set pieces with one solution shrink the feeling of open exploration.

## monsters and atmosphere
- [heuristic] Use scenery such as old mansions, sewers, factories, and malls for gore settings; hellish places should make the environment itself dangerous. When: Gore-themed level design.
- [heuristic] Because distance falloff limits monster influence to nearby actors, dense monster spacing in a generator will change how groups interact. When: Generating levels with many monsters. Why: Nearby-only influence means clustering alters the overall motive balance.
- [heuristic] Placing monsters in themed rooms such as kennels, throne rooms and temples adds more flavour than unseen monster interactions.
