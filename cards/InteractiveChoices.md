# G09: Open tasks, alternative solutions and input synonyms

[Parent group](Narrative.md) | [Knowledge hub](README.md)

General knowledge; design applications are untested. A game's own approved decisions prevail.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G09.04 Plot and dramatic form | [K09-20](#k09-20) |
| G09.05 Interactive narrative | [K09-19](#k09-19); [K09-20](#k09-20); [K09-21](#k09-21); [K09-22](#k09-22) |
| G09.06 Quests and objectives | [K09-19](#k09-19); [K09-20](#k09-20); [K09-21](#k09-21); [K09-22](#k09-22) |

## K09-19

**Open tasks let a stuck player change the order.** Several independently available tasks let a player leave one unsolved problem and attempt another.

- Kind: general guidance. Focus: agency; Branching, bottlenecks and recombination; Choice visibility and meaningful alternatives; Nonlinear discovery and gating; task structure.
- Apply: Mark which objectives remain available when progress on one task stops.
- Limit: Freedom of order does not itself produce different outcomes.
- Check: Stop at one unsolved task and find another currently actionable objective.
- Requires [K09-03](Narrative.md#k09-03): Availability depends on prerequisites, not the number of listed tasks.
- Constrains [K01-02](Foundations.md#k01-02): Order choices and outcome changes need separate state descriptions.

## K09-20

**An endgame can narrow the remaining problem space.** A concluding phase can reduce relevant places and objects, helping players recognize that completion is near.

- Kind: general guidance. Focus: resolution and aftermath; Branching, bottlenecks and recombination; task structure.
- Apply: Identify what remains relevant after the transition and why.
- Limit: A final boss, timer or arbitrary removal of earlier choices is unnecessary.
- Check: Compare available tasks before and after the transition; explain each restriction.
- Requires [K06-10](SpatialDesign.md#k06-10): A narrowed map must still preserve the remaining mission dependencies.
- Supports [K09-05](Narrative.md#k09-05): A prepared transition can connect earlier progress to a causal conclusion.

## K09-21

**Alternative solutions differ from collecting prerequisites.** Several means can each satisfy one goal; this differs from requiring all listed items or actions together.

- Kind: general guidance. Focus: agency; Quest goals, prerequisites and consequences; Choice visibility and meaningful alternatives; alternative approaches.
- Apply: Label each proposed approach as sufficient alone or necessary in combination.
- Limit: Different methods need not create different endings.
- Check: Complete the goal by each claimed alternative without silently borrowing another method.
- Requires [K01-02](Foundations.md#k01-02): Each sufficient method needs an explicit enabling state and result.
- Supports [K03-08](ActionsAndCombat.md#k03-08): Relevant properties can suggest more than one workable approach.

## K09-22

**Input synonyms and different actions need separate treatment.** Different wording can express one intended operation, while verbs such as push and pull can describe materially different actions.

- Kind: general guidance. Focus: Puzzle-story integration and fairness; alternative approaches.
- Apply: Group equivalent expressions; preserve distinctions that change the attempted operation.
- Limit: Accepting synonyms does not require every verb to succeed.
- Check: Compare two phrasings of one action and two genuinely different operations.
- Requires [K03-02](ActionsAndCombat.md#k03-02): Vocabulary handling must preserve the reasoning the puzzle asks for.
- Supports [K09-23](PuzzleRecovery.md#k09-23): An understood but unsuccessful operation needs a response distinct from unrecognized wording.

## Worked dependency

[K09-20](InteractiveChoices.md#k09-20) -> [K06-10](SpatialDesign.md#k06-10) -> [K01-02](Foundations.md#k01-02)

Condition: A final phase closes earlier locations while several methods remain possible.
Rejecting probe: Reject a spatial restriction that removes a still-required mission action or silently equates every method with one outcome.
