# player-psychology

## combat tactics and resources
- [model] Player failure has distinct types: failure to learn, failure to engage, failure to play by the rules, failure to win, failure of choice, failure to finish, failure to honour outcomes, failure to be consistent, and failure to have a sequel. When: Diagnosing why players drop off or break the rules. Why: Each type has a different cause and fix, so naming them locates the actual problem.
- [definition] Yomi is predicting the opponent's next move; it becomes the core skill in one-on-one games and adds difficulty when other players are involved. When: designing one-on-one or multiplayer competitive games. Why: When players react to each other directly, guessing opponent choices decides outcomes; players must predict what others will do.
- [definition] A clicklet is an unavoidable on-screen click with no real choice, giving a reward and consuming only attention; better seen as operant conditioning than a mechanic, since skipping changes nothing.
- [definition] Failure in games is mainly pedagogical: it shows the player that their approach is wrong or their skill is short. A true failure state occurs only when the player stops learning and quits. When: Evaluating whether a failure helps or harms engagement. Why: Failure that teaches keeps players engaged, while failure that teaches nothing drives them away.
- [behavior] Magic lets players choose attacks that fit the situation, making it the main alternative to melee-focused play. Why: Spell choice gives tactical options that melee lacks.
- [behavior] Players can judge combat approaches because defeating opponents is an obvious goal, but conversations often lack a clear goal. When: designing social encounters. Why: Without a clear goal, players cannot judge which approach is best.
- [behavior] Abilities that are underused or unclear are often forgotten, since players struggle to remember more than about seven options.
- [behavior] Players solve a creature's resistance as a puzzle once per creature type, cycling through attacks until the correct element is found. When: Creatures have hidden elemental resistances. Why: Without information, players test attacks one by one.
- [behavior] Some players rule out legal actions themselves, saying they feel they are cheating, which limits their play without any rule being broken. When: Players who avoid legal options. Why: Self-imposed limits come from perceived fairness, not from the rules.
- [behavior] Some players reload repeatedly to explore every result until they get the one they prefer, which fails to honour outcomes. When: Games with save-and-reload and random results. Why: Players want control over outcomes, so reloading becomes a way to avoid accepting results.
- [behavior] Players feel escalating amazement when each puzzle raises the complexity of the previous one, which holds attention through the sequence. When: A puzzle sequence increases complexity step by step. Why: Each step builds on the last, making the player's sense of challenge grow.
- [behavior] Players of games with fixed rules derive the underlying rules by repeated experiments, treating play as a form of scientific testing. When: A game gives fixed, consistent rules and the player tests them through action. Why: Players form hypotheses from observed outcomes and revise them when results contradict expectations.
- [heuristic] Warn the player when ammunition runs low, around 50 or 100 rounds, to build a sense of paranoia. When: Gun-based games. Why: Warning builds tension about running out.
- [procedure] 1) Record how much gore pools on each tile. 2) Describe it in messages across levels, from knee-deep to slowed by thick blood. When: Gore-themed roguelikes with floor state.
- [tradeoff] A power plant gives more control than a battery but adds management overhead the player must handle.
- [pitfall] A bad event can upset the player enough to quit, so recovery from setbacks must be possible.
- [fact] A viable choice is competitive at high level play, while a valid choice is one players can easily confirm was worth picking. Validity matters at every skill level.

## player engagement and onboarding
- [model] A roguelike can make mood matter by tying emotional events to changeable attributes, scaled by how much the lost or gained thing was valued.
- [mechanism] Placing unrelated elements side by side, like a dart trap, a bone pile and a serpent, invites the player to build a story from them.
- [behavior] Players tend not to look upward, so features placed overhead may go unnoticed. When: designing 3D spaces with vertical features.
- [behavior] Players quit games when they stop receiving new tools or new ways to use them, or when difficulty spikes, boss fights repeat, or timing demands feel unfair. When: In long games and roguelikes with progression. Why: Repetition and unfair spikes make the experience feel stale or punishing.
- [behavior] Players who use experience rewards often justify them by acting out training in the fiction, suggesting in-game rewards serve role-play better. When: Players of experience-based role-play systems. Why: Players seek fictional justification for mechanical rewards they already depend on.
- [behavior] On a first visit, players cannot tell whether a layout reflects designer intent or an intentionless generating process. When: first encounter with a generated space.
- [behavior] Habits learned early in a roguelike dungeon are reinforced by the interface and become hard to unlearn later. When: Players learn strategies in the early game of a roguelike with feedback that rewards those habits. Why: Interface feedback such as counters and level-ups reinforces early choices, so they persist after they stop being optimal.
- [rule] Treat the player's time and attention as the most valuable resource in design decisions.
- [heuristic] Some realism, such as needing to eat, poison and bleeding, adds depth, but too much pulls focus to nitpicks.
- [heuristic] Harder classes should not be offered first to new players, yet they are needed to teach advanced strategy. When: introducing classes to new players. Why: Hard classes overwhelm novices but reward experienced players with advanced strategy.
- [metric] A reviewer estimated that about a third of players might quit after a failed opening involving a trapped character. When: Judging the impact of a broken game start. Why: Opening frustration drives early abandonment.
- [fact] Player emotion matters more than character emotion, which serves only as a medium for it.

## reward and randomness
- [definition] Replayability is the ability of a game to be played many times without becoming boring.
- [mechanism] Reward and punishment feedback loops can drive strong, compulsive engagement, as gambling shows, and the same conditioning can also build useful skills. When: Designing feedback systems that reward repeated actions. Why: Operant-style conditioning links player actions to outcomes, strengthening the behaviour.
- [behavior] Without an endgame, repeated actions such as repeated building or repeated viewing have no meaning. When: A game has no defined goal or conclusion. Why: Actions gain meaning only relative to a goal.
- [behavior] Players may only notice the pattern in a procedurally built level after many runs, so recurring small beats can be learned gradually. When: In games built from small repeated platforming or encounter beats. Why: Patterns are subtle and emerge only across many varied runs.
- [behavior] Experienced roguelike designers tolerate random damage, which critics often see as the core objection to hit point combat. Why: Familiarity with randomness reduces the perceived cost of unpredictable damage.
- [behavior] Fully predictable generated output is too dull to be interesting, while pure random noise offers nothing to learn.
- [behavior] When stat gains have one obviously best option, players face no real choice; a meaningful choice appears only where each option has a distinct use. When: players pick among stat boosts. Why: A single dominant option removes the decision and makes the item trivial to choose.
- [heuristic] Automate routine, uninteresting choices with clear safe conditions, such as eating while travelling or recasting safe buffs, but not decisions that make the game interesting. When: repetitive choices with clear safe conditions. Why: automation that replaces meaningful decisions can make the game play itself.
- [tradeoff] Repetition should teach rules or be automated; once learned, repeat only to serve more complex rules, yet grinding pleases when it adds feel, even after its logic is understood. When: Designing repetitive or grind-heavy mechanics. Why: Repetition can be satisfying in itself, so mechanical play is not always a failure.
- [pitfall] Randomised risk and reward, or random rewards for repetitive activity, can drift toward Skinner-box behaviour and addictive loops. When: Designing random rewards, loot drops or reward randomness for repeated play. Why: Variable, unpredictable reinforcement encourages compulsive repetition beyond what the player intends.
