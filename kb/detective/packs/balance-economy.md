# balance-economy

## money trails and debt
- [mechanism] Log each transaction and the starting count of a game currency or inventory so suspicious changes are detectable and spending can be rebuilt and checked against the current balance. When: A game tracks player purchases, payments or currency spending. Why: Recorded outflows can be verified rather than recalled from memory.
- [mechanism] Track each NPC's income, debts and visible spending; luxury purchases or a residence without matching income prompt players to question the source and check claims against observed deposits. When: When designing NPC wealth for a mystery system. Why: A visible mismatch between income and spending creates a lead the player can pursue.
- [mechanism] A spent casing found outside a window links the shooting to the area beyond it.
- [mechanism] A fixed income drawn on by several claimants, each taking a set amount, can be nearly exhausted by a few claims. When: Several beneficiaries each draw a fixed sum from one source. Why: Each claim subtracts from a limited total.
- [mechanism] A loan with a fixed monthly percentage and interest deducted up front means the borrower receives less than the principal, giving a checkable calculation. When: A lending system uses a set rate per period and prepaid interest.
- [mechanism] Cleared, fenced land was taxed at a much higher rate than unimproved wild land, so tax rates reward improvement.
- [rule] Log NPC fees, seizures, withdrawals and transfers in an economy ledger so players can infer which character or party paid or gained, leaving intent to inference. When: designing NPC economies with hidden transfers. Why: Visible money flows let players deduce motives. (x2)
- [rule] Trace cash found in a hidden stash back through the records to a payer or recipient. When: Designing a discovery that links to financial records. Why: Tracing connects physical finds to the people involved.
- [rule] Offer a small payment to buy a plain factual answer from someone with no stake in protecting the subject. When: a reluctant source may know a checkable fact.
- [rule] Tie an NPC's debts or secret routine to a faction or economy system so the player can uncover motive through shops, lenders or servants. When: designing a suspect's background. Why: it links motive to observable game systems.
- [rule] Model an NPC's debt and need as a visible motive for their bargaining. When: Designing NPC negotiation with financial stakes. Why: Visible need makes bargaining behavior understandable and predictable.
- [heuristic] Credit a deduction more when the player kept several readings open until a second clue selected one. When: rewarding player reasoning. Why: holding alternatives open shows the reasoning was tested.
- [heuristic] Little cash on hand suggests the missing person did not prepare a trip. When: when judging whether an absence was planned. Why: a planned trip needs funds.
- [heuristic] A price or rent far below local norms, especially where many others were refused, is an anomaly that deserves explanation. Why: Unusual deals often have a hidden cause.
- [pitfall] An assistant credited with others' ideas may repeat them without understanding them.
- [pitfall] The person who bought an item and the person who carried it to the scene may be different people, so a buyer's name is not proof of use.
- [pitfall] The place where a payment was cashed is not necessarily where it was drawn, so each location must be checked separately. Why: Transaction location and cashing location can differ.
- [pitfall] Public accounts can distort the sequence of deductions and assign credit to the wrong party, so expect this after a solution is announced.
- [pitfall] Spreading a limited light supply across a search area, or spending it on the wrong spot, exhausts it quickly and leaves the search unfinished. When: when light sources are finite. Why: Each light covers only a small area and burns out.
- [pitfall] A falling assessment can hide a transfer of wealth rather than a loss of wealth.
- [fact] Creditors usually wait until a debt falls due, and blackmailers usually apply pressure where social shame is greatest; early or misplaced pressure is a lead.
- [fact] Prisoners may be made to pay their own keep, adding a financial cost to being accused.

## theft and blackmail
- [model] Model investigation constraints as resource limits: search time, the duration of legal holds, and a finite number of guards. When: a game requires the player to investigate under limited resources.
- [mechanism] Blackmail on a damaging secret keeps extracting resources, since each payment reveals new assets; a visible deadline such as a repossession visit forces the player to act. When: A victim has a strong reason to stay silent and the cost of silence grows; when designing blackmail or debt quests with time pressure. Why: Fear of exposure makes payment seem cheaper than reporting; a visible timer converts gradual pressure into a decision the player must make. (x2)
- [mechanism] Accused people are charged fees for maintenance, transport, clerks, reprieves, discharge and execution; where cash is scarce these fall on livestock and crops, ruining families while owners are absent. Why: Little cash forces payment in goods.
- [mechanism] Raising search effort for a larger reward increases time and cost without improving insight, so search cost can be modelled as a resource separate from search method.
- [mechanism] If a stolen item's value falls once its secret becomes public, holders face pressure to sell early, while holders expecting a rise may wait. When: the item's worth depends on secrecy or timing. Why: waiting either loses value or gains it, depending on how the value changes.
- [mechanism] Stolen money can be traced only if identifying details such as serial numbers were recorded at the transaction; without them recovery becomes nearly hopeless. Why: identifiers link a loss to a specific physical item.
- [mechanism] Seizing an arrested person's goods gives accusers a material motive to press charges, and can ruin families even after acquittal.
- [mechanism] Stolen items that cannot be broken down or converted into currency need a willing buyer. Without a buyer market, theft yields no value and the goods stay idle. When: When stolen goods are unique or hard to liquidate. Why: Conversion routes determine whether theft pays.
- [mechanism] If stolen items sell only in certain markets, players must track where loot can go, turning fencing into a routing problem with a discoverable path. When: In games with fencing or black-market systems. Why: Restricted outlets give players reasons to follow sales.
- [mechanism] A public reward, offer or appraisal raises an object's perceived worth and the number of people who know of it, making it a more attractive target. When: When a valuable item is publicly valued. Why: Publicity increases temptation and awareness.
- [rule] Keep investigation savings in a bank and calculate spending closely, since funds limit how long a hidden party can last.
- [rule] Treat a cash total that comes up short by a fixed amount as a clue the player can count and trace.
- [rule] Route hidden economy transactions through brokers so players must follow intermediaries to reach a single NPC. When: Designing a concealed market or trading chain. Why: Forces the player to trace the chain step by step.
- [rule] For consumables, treat theft of part of a stock differently from theft of the whole stock, using quantity thresholds. When: when designing a stockpile that can be partially stolen. Why: partial and total losses have different consequences.
- [rule] A game's suspect logic can use untouched valuables to rule out robbery as a motive, which is a strong test separating robbery from personal motives. When: when designing motive logic for a crime in a game. Why: Untouched valuables contradict a theft motive.
- [heuristic] Give each stolen-item report a precise inventory so the player can check it against items found in a suspect's room. When: Designing theft investigations in a game. Why: Precise inventories let the player verify claims against physical evidence.
- [procedure] 1) Track the victim's remaining resources as a state variable. 2) Scale each new demand to what remains. 3) Stop escalating when resources are exhausted. When: Implementing an extortion mechanic in a game. Why: Demands tied to remaining resources keep pressure meaningful without becoming impossible.
- [tradeoff] Destroying a container costs the container but can reveal its contents; it suits cases where the container's loss is acceptable. When: Deciding whether a player may break a container to find an item. Why: Destruction guarantees discovery at the cost of the container itself.
- [tradeoff] Bribery can be a mechanic whose cost is weighed against how reliable the purchased information proves to be. When: Designing a paid-information mechanic. Why: Players balance the price of information against its expected accuracy.

## inheritance, stakes, and timing
- [mechanism] When a single event order decides who benefits, small timing differences cause large outcome changes, making timing the contested stake and inviting interested parties to shade testimony. When: Legacies are conditional on survivorship order, or a single event order decides who benefits. Why: A threshold rule concentrates large stakes on a small timing gap, turning a small timing question into a contested, high-value point.
- [mechanism] When a recurring timed effect escalates, intervals shorten and required doses rise; designers can show this as a visible countdown so urgency stays legible. When: when a timed effect or cover depends on repeated doses, or when designing escalating pressure on a player. Why: Escalating frequency and dose demand increases pressure, and a visible, accelerating timer makes urgency legible.
- [mechanism] When parents transfer farms to children while keeping income, the parents' assessments fall as the children's rise.
- [rule] Give each party in a shared enterprise a stake value, so the game can show who gains most from a loss, not just who lost most.
- [heuristic] Set a deadline for a squeeze so the victim's remaining resources are drained before they can meet escalating demands. When: Designing a pressure or extortion quest with a time limit. Why: A fixed window forces the victim to commit everything before escape is possible.
- [heuristic] Do not assume an opposing contest is settled by one decisive move; in an evenly matched contest, control often stays uncertain for a long time. When: when a plan assumes a quick, decisive victory. Why: evenly matched sides can stay balanced, so control is not won in a single stroke.
- [heuristic] Attach a reward or permission to a timed condition, so the player's action before or after a threshold changes which NPC benefits or which door unlocks. When: Designing timed outcomes in a game economy. Why: Threshold rules let players reason about outcomes without the designer naming a culprit.
- [metric] Track the count of unique instances: total produced minus held equals sold, and sold minus logged sales equals untracked sales. When: Designing limited-run or unique items in a game economy. Why: The running count shows how many instances are unaccounted for.
- [metric] Estimated effect durations can differ from actual outcomes, so calculated timings should be treated as approximate and checked against observed recovery. When: Predicting how long a dose or status effect lasts. Why: Calculations often miss real variation in recovery.
- [pitfall] Dependence on a consumable supply makes recurring effects fragile: a low or impure batch can cause failure, and a timeline ignoring this hidden cause misleads. When: when a character or cover relies on a recurring consumable, or when explaining the failure of a recurring effect. Why: Supply quality and quantity become a single point of failure, and blaming the effect itself hides the real cause in the supply chain.
- [pitfall] Independence of events can fail when a system has memory, so test that assumption before applying independent-event reasoning. When: applying chance reasoning to a game system. Why: systems with memory make earlier results affect later ones.
- [fact] For independent events such as dice throws, past outcomes do not change the chance of a future outcome. When: predicting the next result of a random event. Why: each independent trial has the same chance regardless of history.

## game progression and exits
- [rule] Gate an exit behind a payment so release has a clear mechanical cost and ends the branch.

## npc behavior and loyalty
- [mechanism] A reputation or loyalty system that rewards NPCs with gold or favors can change their dialogue and later answers, revealing hidden influence to a player who notices the change. When: Designing NPC loyalty or reputation systems that affect dialogue. Why: Rewards shift an NPC's incentives, so their statements change in observable ways.

## player psychology and belief
- [behavior] Players who lose heavily at a chance-based game tend to attribute losses to bad luck and believe a betting system can win, unless the mechanism is shown to be controlled. When: A chance-based game with a house edge is played for money. Why: Belief in luck and systems keeps players from suspecting the outcome is manipulated.

## probability and randomness
- [fact] Each independent random trial has the same chance regardless of earlier results, so a number that came up repeatedly is no more or less likely next time.
