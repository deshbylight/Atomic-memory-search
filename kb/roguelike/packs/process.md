# process

## game balance and testing
- [behavior] Most players who download a game never post feedback, so counting visible contributors gives a lower bound on the audience. When: Interpreting community feedback. Why: Silent players are invisible in forum activity.
- [rule] Publish balance numbers, since players will work them out anyway.
- [rule] Collect feedback through several channels, including blogs, forums, email, Usenet and traffic tools, and welcome bug reports even when they will not be fixed. When: Running a community-tested release. Why: Bug reports and both positive and constructive feedback help development continue.
- [rule] Test a game for locks even when only interrupts exist, because interrupts can create locks without any timed effect. When: validating a game's status or interrupt system. Why: Interrupts can chain into an unbreakable state that timed-effect analysis would miss.
- [heuristic] Untested design advice or proposed mechanics, such as horror advice from someone who has not played the genre or guessed combat values, should be validated through playtesting. When: Evaluating design advice or adopting untested mechanics without evidence. Why: Untested recommendations may not produce the intended player response, and designers cannot know in advance whether guessed values and rules are sufficient.
- [heuristic] Judge balance and feel by intuition built from playing many deep games and designing constantly, not in occasional bursts. When: Developing design skill or making balance decisions. Why: Constant design and play build the judgment needed to predict how a game will feel.
- [heuristic] Mostly ignore forum claims that an ability is too powerful; respect top players' feedback but verify it with other evidence.
- [heuristic] Use an automated player for stress testing, since it finds bugs such as object-stacking corruption without generating thousands of items by hand.
- [procedure] Run user testing to find out which player choices are interesting before deciding what to automate.
- [procedure] Change one variable at a time, as in a controlled experiment, so the effect of each value is visible.
- [procedure] 1) Make the rules playable, even as a paper or board prototype. 2) Play it and observe outcomes. 3) Check for gross exploits, degenerate strategies and lack of depth before committing. When: Before committing to a design; paper or board prototypes need no programmers. Why: Descriptions of rules can miss exploits and dead-end strategies that only appear in play.
- [pitfall] Automated players reliably find crashes and infinite loops but miss anomalies like water running uphill, which can reach real players when testing relies only on automation. When: Relying only on automated testing. Why: Bots miss semantic errors that players spot.

## open source contribution
- [rule] Have trusted helpers handle bug triage and spokesperson roles; they need not understand the code to give support.
- [heuristic] Tight limits on time, place or scope make finishing possible and focus effort; competitions and prototypes apply them, valuing limited work over starting new work. When: Choosing a prototype or jam format; planning small game projects. Why: Restrictions remove open-ended decisions and push effort toward completion.
- [heuristic] Use move records and replays when verification or learning matters; skip heavy save protection for games played only alone. When: Deciding how much save protection to build. Why: Protection cost is only justified when others depend on the results.
- [heuristic] Contribute to a related project you do not own, such as a community wiki, to stay engaged between your own work sessions.
- [procedure] 1) Install Java, Eclipse with a Subclipse plug-in, and MinGW with make. 2) Check out the development repository. 3) Build the default target. 4) Copy the executable up one folder. Repeat update, build and copy for each new version. When: building development source on Windows.
- [metric] The ratio of downloaders to forum contributors is estimated at 10:1 to 50:1, which gives a rough playtest signal. When: Estimating the active tester base from download and forum data. Why: Only a small share of downloaders post feedback, so contributions understate the audience.
- [pitfall] Informal build instructions can have error-prone steps, so expect to troubleshoot them.
- [pitfall] Refactoring discards hard-won lessons and exposes hidden assumptions, so new bugs may appear that players notice before old ones. When: Rewriting working but tangled systems. Why: Old code encodes fixes whose reasons are no longer written down.
- [fact] Offering saves can annoy both purists who want permadeath and players who want easy saving. When: Adding save or resurrection options to a roguelike. Why: Each audience expects a different level of difficulty.
- [fact] The development source setup downloads more than 100 MB, so it needs a broadband connection.
- [fact] Open source can improve a game through community fixes, ports to more platforms, and maintenance that continues after the original designer stops.

## roguelike project development
- [rule] Give developers a complete design specification that describes each mechanic and includes art assets, so they can focus on implementation and tuning. When: Handing a prototype to developers. Why: Complete specifications remove design and asset work, leaving implementation and tuning.
- [rule] Work on what currently interests you rather than on fixed targets.
- [rule] Test an idea's feasibility by explaining it in writing, rather than only talking it through.
- [heuristic] Solve design problems by writing code; sub-optimal code is acceptable because the user interface matters most.
- [heuristic] Study games that have lasted for decades, using a thorough survey of how they are played, before relying on personal play experience alone. When: learning game design from established examples. Why: Long-lived games have proven features, and a comprehensive survey gives an overview without years of play.
- [pitfall] Judging a rule set by description alone can miss exploits and dead-end strategies that appear only in actual play.
- [pitfall] Launching with too many options, such as nine factions at once, is a mistake; grow the options gradually instead. When: when adding class or faction options to a game.
- [fact] Roguelike features such as invisibility, polymorph-self, persistent levels, and monsters moving between levels look simple but prove difficult to code and balance. When: Estimating scope before committing to a roguelike feature. Why: These features touch many systems at once.
- [fact] Large refactor patches are hard to land unless one developer works alone on the branch, and such refactors often take longer than expected. When: Planning a large refactor on a shared codebase. Why: Parallel changes on a shared branch create merge conflicts and delay.
- [fact] Roguelike projects often run for many years, with some lasting more than a decade.
- [fact] Some long projects stop before reaching a sanctioned version 1.0.

## developer wellbeing and workload
- [rule] Plan natural absences into long development cycles, since they are normal and help prevent burnout.
- [rule] Exercise away from the keyboard while keeping a way to capture ideas nearby.
- [rule] Do not dwell on failures; learn your personal work rhythms instead.
- [heuristic] Learn the game's play before editing its data, so you can see how each change affects play. When: Starting a mod or balance edit. Why: Knowing normal play makes the effects of edits visible.
- [pitfall] Coding while tired raises bugs per line sharply, so avoid it. When: when fatigued.
- [pitfall] Watching generated output can consume all the time that procedural generation was meant to save. When: when reviewing many generated outputs by hand.
- [fact] Support work such as balancing, polishing, adding content, testing, documenting, and planning is also hard in roguelike development. When: Budgeting time for a roguelike project. Why: These tasks are often underestimated compared with coding.
- [fact] A design can stay in beta for over a year before a different design ships, so long betas can end in a replacement.
- [fact] Prevention delays burnout but does not stop it, so recovery habits are also needed.
