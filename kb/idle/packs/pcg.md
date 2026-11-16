# pcg

## dungeon design
- [model] A dungeon data definition holds: ID, name, description, icon, required combat level, recommended food, ordered enemy IDs, boss ID, reward entries, and estimated duration in minutes. When: Authoring static dungeon data. Why: These fields together describe everything the game needs to run and display a dungeon.
- [mechanism] Storage, upkeep and defense constraints are layout pressures that a dungeon generator's output must satisfy. When: when generating dungeon layouts for dungeon-building idle games.
- [rule] Store clear status and clear counts in save data, not in the static dungeon definition. When: Persisting dungeon progress. Why: Keeping per-save state out of the definition keeps the definition reusable across saves.
- [rule] Refuse dungeon entry when the player's combat level is too low or when they hold fewer than 5 food items. When: Validating dungeon entry. Why: Entry checks prevent starting a run the player cannot survive.
- [rule] Advance game systems each frame using accumulated delta time rather than a timer node, which makes offline simulation simpler to run. When: Designing a game loop that must also support offline progress. Why: A shared tick path lets the same logic run live and offline.
- [heuristic] Dungeon enemy sequences can end with a boss, with food and equipment fixed for the run unless upgraded. When: Structuring generated dungeon runs. Why: A boss ending with fixed loadout gives a clear endpoint to each run.
- [procedure] 1) Record the clear and increment the clear count. 2) Roll each reward entry against its chance. 3) Add each rolled quantity to the player. 4) Emit a clear event. When: A player completes a dungeon. Why: Ordered handling ensures rewards and progress are recorded consistently.
- [pitfall] Mastery bonus tiers described as ranges must be resolved by the integer-level checks in code, since boundary values decide which bonus applies. When: Implementing tiered mastery bonuses. Why: Range wording is ambiguous at exact thresholds.

## procedural content generation
- [heuristic] A chain of spawn or production tiers, where each tier feeds the one below, can model layered resource flow in a dungeon economy. When: Designing dungeon resource systems. Why: Layered feeding mirrors stacked production.
- [heuristic] Tying each stage to a specific unlocked area lets generated floors gate deeper zones. When: Generating layered dungeon content. Why: Gating deeper zones behind earlier clears gives generated content a progression structure.
- [heuristic] Apply the faucet-and-sink check to any reward a generator produces, such as loot or currency per room, to confirm it has a sink. When: Generating rewards procedurally. Why: Generated rewards without a sink accumulate uselessly, just like hand-placed currency.
- [heuristic] In generated dungeons, dungeon clears can be standard achievements and enemies defeated can be incremental achievements. When: Adding achievements to procedurally generated content. Why: Mapping existing events to achievement types reuses the same tracking.

## encounter sequencing
- [heuristic] A fixed pacing template (easy, repeat, new mechanic, combined, then boss) can order procedurally generated encounters per room layout, teaching each mechanic before combining them. When: Generating dungeon encounters procedurally. Why: A fixed sequence with a boss ending gives a predictable structure to fill with generated content; the pattern teaches each mechanic before combining them, then ends on a boss.
