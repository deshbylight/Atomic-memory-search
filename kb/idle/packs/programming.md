# programming

## shop and purchases
- [model] Each shop item defines an ID, the granted item, a display name, a gold cost, a quantity per purchase, a purchase cap where 0 means unlimited, a restock time where 0 means always available, and an optional skill level requirement. When: Building a data-driven shop. Why: A complete item record lets one service handle every shop entry.
- [rule] Refresh the shop panel when items are added or removed and when a purchase completes. When: Shop inventory or purchase state changes. Why: Stale rows would show wrong costs or stock.
- [heuristic] Track total owned and purchased counts separately so the system can distinguish player-built features from automation-produced ones. When: Designing dungeon systems with automated and built features. Why: Mixing the two counts hides which features the player chose.
- [procedure] 1) Confirm the item exists. 2) Confirm gold covers the total cost. 3) Confirm the purchase cap is not exceeded. 4) Confirm any level requirement is met. 5) On success remove gold, grant the item, record the purchase count and emit a purchase-completed event. When: Processing a shop purchase. Why: Checks before granting prevent invalid or unaffordable transactions.
- [procedure] 1) When a purchase cap applies, reduce the requested quantity to the remaining allowed purchases. 2) Complete the purchase with the reduced quantity. When: A bulk purchase exceeds the remaining cap. Why: Trimming the quantity avoids rejecting a partly valid order.

## browser game size constraints
- [heuristic] A strict byte budget forces every feature to earn its place, producing tighter and more focused games.
- [metric] Small browser idle games can ship at 4 to 30 KB with no framework, a size at which they load before the player's attention wanders.
- [tradeoff] Vanilla JavaScript with no framework, engine or dependencies keeps idle browser games very small, which matters because load time strongly affects whether players stay. When: when building browser games where load time decides retention. Why: a multi-hundred-kilobyte game shows a loading bar and loses attention.

## level calculation
- [procedure] If the language lacks a log function for an arbitrary base, divide the natural or common log of the inner expression by the natural or common log of the growth rate. When: Computing max affordable count in a language without arbitrary-base logarithms. Why: Change-of-base identity gives the same result.
- [procedure] 1) Build the XP table once on first use. 2) Every lookup calls the build step first. 3) Read values from the cached array. When: Serving level-XP lookups from a precomputed table. Why: Avoids recalculating the curve on each lookup.
- [pitfall] Level-from-XP lookups that search downward from the top level must handle the highest level boundary explicitly. When: Converting total XP to level.

## achievement tracking
- [procedure] 1) Listen to game events such as level-up, enemy defeat, dungeon clear, craft completed, and mastery level-up. 2) Update the relevant stat from every such event, since missed event coverage leaves progress unrecorded. When: Implementing or checking achievement progress tracking against game events. Why: Tracking from every relevant event prevents missed progress; gaps in event coverage leave some progress unrecorded.

## clear progress storage
- [rule] Record dungeon clears in a separate progress table so the static dungeon definition stays reusable across saves. When: Storing dungeon clear progress. Why: Separating progress from definitions keeps definitions reusable.

## continuous generator output
- [pitfall] Treating generator output as continuous can cause confusion when a generator is created within the same tick; handle the partial production explicitly. When: Implementing generators that produce in discrete time steps. Why: Continuous assumptions break on newly created units.

## data-driven skill content
- [rule] Define skills, actions and loot as data resources so new actions can be added without changing skill code. When: Building content for a skill system. Why: Keeps content changes out of code paths.

## threshold trigger
- [rule] Trigger a boss special attack only when HP crosses the threshold from above, using a flag so it fires once. When: Implementing a one-time boss event at an HP threshold. Why: Checking the crossing direction and a flag prevents repeated firing.

## xp multiplier application
- [procedure] 1) Multiply the XP amount by the XP multiplier inside the skill's XP-adding method. 2) Store the result as the new XP value. When: Applying a prestige or upgrade XP multiplier. Why: Applying it at one central point ensures every XP gain is boosted.
