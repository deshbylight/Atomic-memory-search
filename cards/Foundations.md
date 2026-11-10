# G01 — Game design foundations and systems

[Knowledge hub](README.md) · [Cross-domain chains](Connections.md) | [Continuation: Established solutions, resolution stakes, chance branches and risk preferences](DecisionRisk.md) | [Continuation: Player fantasy, core activities and integrated prototypes](GameplayScope.md) | [Continuation: Activity clocks, retained project milestones and cycle reset scope](SessionCycles.md) | [Continuation: Camera eye height, field of view axis and joint action rules](EmbodiedPlay.md)

General principles below are distinct from their proposed application; the applications are untested.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G01.01 Identity and intended experience | [K01-01](#k01-01); [K01-05](#k01-05); [K01-18](GameplayScope.md#k01-18); [K01-20](GameplayScope.md#k01-20) |
| G01.02 Formal game structure | [K01-02](#k01-02); [K01-05](#k01-05); [K01-06](#k01-06); [K01-12](#k01-12); [K01-13](#k01-13); [K01-15](DecisionRisk.md#k01-15); [K01-16](DecisionRisk.md#k01-16) |
| G01.03 System relationships | [K01-03](#k01-03); [K01-06](#k01-06); [K01-07](#k01-07); [K01-08](#k01-08); [K01-10](#k01-10); [K01-11](#k01-11); [K01-15](DecisionRisk.md#k01-15); [K01-19](GameplayScope.md#k01-19) |
| G01.04 Agency and uncertainty | [K01-02](#k01-02); [K01-07](#k01-07); [K01-08](#k01-08); [K01-12](#k01-12); [K01-13](#k01-13); [K01-14](DecisionRisk.md#k01-14); [K01-16](DecisionRisk.md#k01-16); [K01-17](DecisionRisk.md#k01-17) |
| G01.05 Time and persistence | [K01-04](#k01-04); [K01-21](SessionCycles.md#k01-21); [K01-22](SessionCycles.md#k01-22); [K01-23](SessionCycles.md#k01-23) |
| G01.06 Design constraints | [K01-01](#k01-01); [K01-05](#k01-05); [K01-09](#k01-09); [K01-19](GameplayScope.md#k01-19); [K01-20](GameplayScope.md#k01-20); [K01-24](EmbodiedPlay.md#k01-24); [K01-25](EmbodiedPlay.md#k01-25); [K01-26](EmbodiedPlay.md#k01-26) |

## K01-01

**Experience goals decide exclusions.** A layout has meaning relative to the experience it should produce; detail without an interaction can consume space without adding a decision.

- Kind: general guidance. Focus: experience pillars; scope and exclusions.
- Apply: State one player experience and one observable choice before selecting a visual motif; cut elements that serve neither.
- Limit: An evocative image alone does not establish a playable experience or a chosen direction.
- Check: Describe what the player notices, chooses and changes in one encounter.
- Requires [K16-01](ResearchAndProduction.md#k16-01): An experience claim needs an observable research question.
- Requires [K01-05](Foundations.md#k01-05): A distinctive promise needs stated dimensions of permitted variation.

## K01-02

**Consequences require a state model.** An interactive dependency graph distinguishes available actions, prerequisites and outcomes; circular prerequisites can make a goal unreachable.

- Kind: general guidance. Focus: game states; meaningful alternatives.
- Apply: Sketch states and information available before a choice; include refusal and an alternative route.
- Limit: Extra branches do not create agency if they converge without a perceivable consequence.
- Check: Trace a successful path and a refused path without assuming knowledge revealed only afterwards.
- Supports [K09-03](Narrative.md#k09-03): Narrative alternatives depend on reachable states and prerequisites.
- Supports [K01-12](Foundations.md#k01-12): A reachable play is one path; a strategy also specifies choices after other histories.

## K01-03

**Separate decisions from locomotion.** An autonomous actor can be described as action selection, steering and locomotion; local perception and interactions can produce group patterns.

- Kind: general guidance. Focus: emergence; cross-system consequences.
- Apply: For a world concept specify what inhabitants need, notice and choose before naming animations or individual jobs.
- Limit: A plausible rule set does not guarantee the desired group behaviour or a runtime implementation.
- Check: Walk through two inhabitants pursuing incompatible needs in the same space.
- Constrains [K13-01](CharactersAndMotion.md#k13-01): A chosen action must remain feasible for the body that executes it.

## K01-04

**Time contracts change return play.** A world that retains changes makes a return visit depend on previous actions; a reset world removes that dependency.

- Kind: general guidance. Focus: world memory; simulation time.
- Apply: Decide the world's lifecycle explicitly; distinguish elapsed active time, a paused closed world and explicit destruction.
- Limit: Recovery or seasonal examples from other games do not by themselves justify a reset or offline catch-up.
- Check: Trace exit, death, unload and return; none implicitly recreates the dungeon.
- Constrains [K06-04](SpatialDesign.md#k06-04): Repeated spaces must account for retained changes rather than assume a pristine visit.

## K01-05

**Rule vocabularies bound possible novelty.** A representation admits some combinations and excludes others; unconstrained combinations mostly produce invalid candidates.

- Kind: general guidance. Focus: genre conventions; distinctive promise; rules and exceptions; procedural variability; authoring cost.
- Apply: List fixed rules, variable dimensions and forbidden combinations before comparing concepts.
- Limit: A larger possibility space does not establish useful novelty.
- Check: Construct two distinct valid variants and one rejected combination.
- Requires [K01-01](Foundations.md#k01-01): Variation needs an experience goal that decides what to preserve.

## K01-06

**State transitions need observable counterparts.** A formal rule becomes usable when its prerequisites and state changes have a perceivable representation.

- Kind: general guidance. Focus: goals and subgoals; information structure; win loss and continuation; mechanics dynamics and experience.
- Apply: Pair every goal transition with what the player can observe before and after acting.
- Limit: A visible animation can still misrepresent the actual rule.
- Check: Describe how a player distinguishes blocked, available, completed and failed states.
- Requires [K01-02](Foundations.md#k01-02): Observable transitions must agree with the underlying state model.
- Supports [K01-13](Foundations.md#k01-13): Observable evidence determines which decision situations a participant can distinguish.
- Supports [K03-14](ActionsAndCombat.md#k03-14): A consumable counter needs a cue that matches the event spending its next use.

## K01-07

**Network direction changes reachability.** A directed connection permits asymmetric access; an undirected connection permits travel both ways. Edge costs can differ from physical distance.

- Kind: general guidance. Focus: resource and state networks; constraints and opportunity; reversibility and commitment.
- Apply: Distinguish travel, information and resource edges, including one-way commitments.
- Limit: A connected sketch does not prove every required destination is reachable in the allowed direction.
- Check: Trace the return path after each irreversible transition.
- Supports [K06-02](SpatialDesign.md#k06-02): Route topology must represent direction as well as recognition.
- Supports [K01-10](Foundations.md#k01-10): Defined connections allow local clustering and overall journey length to be compared separately.

## K01-08

**Emergence depends on initial conditions and update rules.** Identical local rules can yield stable, oscillating or spreading patterns from different starting arrangements.

- Kind: general guidance. Focus: feedback loops; emergence; predictability and surprise.
- Apply: Evaluate interactions over several steps and starting states before promising a dynamic outcome.
- Limit: A cellular model demonstrates possibility, not the behavior of a biological or gameplay system.
- Check: Find a starting condition that contradicts the proposed outcome.
- Constrains [K01-03](Foundations.md#k01-03): Local actor rules require observation of their collective consequences.
- Supports [K01-11](Foundations.md#k01-11): A local attachment rule can reinforce differences in connection counts during network growth.

## K01-09

**Authoring control differs from parameter count.** A generator offers useful control when an author can steer intended output properties predictably; additional parameters alone do not establish that control.

- Kind: general guidance. Focus: procedural variability; authoring cost.
- Apply: State the intended change, then identify a control that produces it without unrelated changes.
- Limit: A controllable generator can still produce an unsuitable experience.
- Check: Ask an unfamiliar author to obtain a specified variation; record failed adjustments and collateral changes.
- Requires [K01-05](Foundations.md#k01-05): The representation must admit the intended variation.
- Requires [K06-09](SpatialDesign.md#k06-09): Output sampling can reveal whether a control actually changes the intended property.

## K01-10

**Local clustering differs from journey length.** Clustering describes connections among a node's neighbors; shortest-path length describes separation between nodes. A network can combine dense local connections with short journeys between distant regions.

- Kind: general guidance. Focus: resource and state networks.
- Apply: Compare local neighborhoods and overall travel separately when adding a shortcut or connecting groups.
- Limit: Hop count ignores unequal travel costs, and disconnected or directed networks need an explicit reachability convention.
- Check: Keep local neighborhoods similar while changing cross-region links; compare both local clustering and reachable journey lengths.
- Requires [K01-07](Foundations.md#k01-07): Direction and edge costs determine which journeys the comparison represents.
- Supports [K06-13](SpatialDesign.md#k06-13): Different lane connections can change travel between routes without changing each route's local layout.

## K01-11

**Existing connections can attract further connections.** In a growing network with preferential attachment, popular nodes attract more new connections because attachment is more likely for nodes with higher existing degree. This creates a reinforcing growth mechanism.

- Kind: general guidance. Focus: feedback loops; emergence; resource and state networks.
- Apply: When established connections increase future exposure or opportunity, compare the resulting concentration with growth that does not favor existing degree.
- Limit: This is one model of network growth, not proof that every hub formed this way or that popularity measures quality.
- Check: Hold growth size comparable, change the attachment rule, and compare how concentrated the connections become.
- Requires [K01-10](Foundations.md#k01-10): Similar journey lengths can conceal different distributions of local connections.
- Requires [K16-01](ResearchAndProduction.md#k16-01): A proposed growth explanation needs an observation that distinguishes it from competing mechanisms.

## K01-12

**A strategy includes choices outside the observed play.** A strategy specifies a choice at every decision situation assigned to a player, including situations the eventual play does not reach. One recorded sequence describes only one play.

- Kind: general guidance. Focus: game states; information structure; meaningful alternatives.
- Apply: When evaluating a proposed solution, record the response if another player chooses an unexpected branch; one successful sequence does not provide those answers.
- Limit: A complete contingent plan is a formal model, not evidence that a human can remember it or that it guarantees success.
- Check: Change an earlier branch and identify the next prescribed choice; flag any situation for which the supposed strategy provides no answer.
- Requires [K01-02](Foundations.md#k01-02): The alternative decision situations must exist in the state model.
- Requires [K01-13](Foundations.md#k01-13): A contingent choice must respect what its player can distinguish at that moment.

## K01-13

**Hidden histories limit contingent choices.** An information set groups decision situations that a player cannot distinguish. A pure strategy must prescribe the same action across those indistinguishable situations rather than consult the hidden history.

- Kind: general guidance. Focus: information structure; constraints and opportunity.
- Apply: Compare the designer's complete state diagram with the evidence available to each participant before acting.
- Limit: This statement concerns pure strategies under explicit observation and memory assumptions; identical-looking screens need not imply identical remembered information.
- Check: Change an unseen earlier event while keeping the participant's information unchanged; check whether the proposed plan improperly changes its action.
- Requires [K01-06](Foundations.md#k01-06): The distinction between hidden state and observable transitions must be explicit.
- Supports [K05-03](CooperativePlay.md#k05-03): Separated participants can have different information sets because their discoveries differ.
