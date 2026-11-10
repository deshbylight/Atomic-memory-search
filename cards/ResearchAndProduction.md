# G16 — Research, concept methods, evaluation and production

[Knowledge hub](README.md) · [Cross-domain chains](Connections.md) · [Continuation: Playtest facilitation, comprehension and debrief questions](PlaytestPractice.md)

General principles below are distinct from their proposed application; the applications are untested.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G16.01 Research framing | [K16-01](#k16-01); [K16-05](#k16-05); [K16-06](#k16-06); [K16-11](#k16-11); [K16-12](#k16-12); [K16-13](#k16-13); [K16-15](#k16-15) |
| G16.02 Concept generation | [K16-02](#k16-02) |
| G16.03 Design reasoning | [K16-01](#k16-01); [K16-10](#k16-10) |
| G16.04 Prototyping | [K16-02](#k16-02); [K16-09](#k16-09); [K16-10](#k16-10); [K16-11](#k16-11); [K16-12](#k16-12); [K16-15](#k16-15); [K16-16](PlaytestPractice.md#k16-16); [K16-17](PlaytestPractice.md#k16-17) |
| G16.05 Evaluation | [K16-03](#k16-03); [K16-05](#k16-05); [K16-06](#k16-06); [K16-09](#k16-09); [K16-10](#k16-10); [K16-11](#k16-11); [K16-12](#k16-12); [K16-13](#k16-13); [K16-14](#k16-14); [K16-15](#k16-15); [K16-16](PlaytestPractice.md#k16-16); [K16-17](PlaytestPractice.md#k16-17) |
| G16.06 Production planning | [K16-04](#k16-04); [K16-07](#k16-07); [K16-08](#k16-08); [K16-14](#k16-14) |
| G16.07 Knowledge maintenance | [K16-04](#k16-04) |
| G16.08 Ethics and sustainability | [K16-03](#k16-03) |

## K16-01

**A claim needs an observation that could reject it.** A study needs a question, an operational measure and a design that can distinguish the proposed explanation from competing explanations.

- Kind: general guidance. Focus: assumptions; causal explanations.
- Apply: Turn a concept claim into an expected player action and a visible failure condition; name what evidence would change the choice.
- Limit: A measurable proxy is not automatically the intended experience, and a preference is not a runtime fact.
- Check: If all possible outcomes would be called success, rewrite the question before making the prototype.
- Supports [K01-01](Foundations.md#k01-01): Experience goals become useful when a failed player observation can revise the concept.
- Requires [K16-05](ResearchAndProduction.md#k16-05): The observation must measure the intended construct as well as be repeatable.
- Supports [K16-11](ResearchAndProduction.md#k16-11): Time-step refinement can reject an apparent physical effect in a simulation.

## K16-02

**Compare alternatives around an uncertain dependency.** A cheap layout or sample interaction can reveal a structural problem before expensive detail makes revision harder.

- Kind: general guidance. Focus: divergent alternatives; prototype scope.
- Apply: Generate alternatives that change a causal assumption, then prototype the one whose failure would invalidate the largest amount of work.
- Limit: Cosmetic variants do not test a mechanical assumption; a successful paper walkthrough does not verify timing or feel.
- Check: State which uncertainty the prototype settles and what can be discarded without production rework.
- Requires [K06-01](SpatialDesign.md#k06-01): Spatial experience claims need a playable blockout at representative metrics.
- Requires [K16-15](ResearchAndProduction.md#k16-15): A prototype comparison intended to isolate a cause must account for systematic condition differences.

## K16-03

**Order and participant selection limit conclusions.** Random assignment and random sampling answer different concerns; repeated conditions can introduce learning, fatigue and carryover effects.

- Kind: general guidance. Focus: comparison and iteration; player welfare.
- Apply: Record sample, task and order; counterbalance reversible conditions where appropriate, and report confounds and participant burden.
- Limit: Counterbalancing cannot undo every lasting learning effect, and a small test does not establish population prevalence.
- Check: Can the observed preference be explained by order, familiarity or a task difference rather than the design change?
- Constrains [K02-04](PlayerExperience.md#k02-04): Player and group differences determine which conclusions the evaluation can support.
- Supports [K16-12](ResearchAndProduction.md#k16-12): Separating assignment from sampling exposes the limits of volunteer recruitment.

## K16-04

**Preserve uncertainty alongside reusable knowledge.** A general principle, a design deduction and an observed result in a game have different evidential status; storing them together without that distinction hides uncertainty.

- Kind: design inference. Focus: quality gates; coverage gaps.
- Apply: Keep principle, application, limitation and test separate; reuse stable identifiers and review links when an approved decision changes.
- Limit: A populated subgroup is not proof that every discovery topic was extracted, and route tests cannot prove that an agent will always follow instructions.
- Check: Can a reader distinguish studied guidance, an untested application, an open topic and an approved constraint of the game?
- Supports [K16-01](ResearchAndProduction.md#k16-01): Explicit evidence boundaries keep the next concept claim testable.

## K16-05

**Reliable measurements can still miss the intended construct.** Consistency of measurement differs from validity: a repeatable score can measure the wrong property.

- Kind: general guidance. Focus: Constructs, operational definitions and measurement quality; Performance, experience and accessibility measures.
- Apply: Explain why a metric represents the claimed experience rather than merely being easy to count.
- Limit: A stable completion time does not establish comprehension, enjoyment or accessibility.
- Check: Name an alternate explanation that produces the same metric without the intended experience.
- Constrains [K16-01](ResearchAndProduction.md#k16-01): An operational measure needs evidence that it addresses the claim.
- Supports [K16-14](ResearchAndProduction.md#k16-14): Construct validity and practical magnitude address distinct limits of a measured result.

## K16-06

**Observers need shared criteria.** Inter-rater reliability concerns whether different observers make consistent judgments of the same behavior.

- Kind: general guidance. Focus: Think-aloud, behavioral observation and qualitative coding; Failure classification, contradictory findings and negative results; evidence strength.
- Apply: Define categories and compare independent judgments before combining observations.
- Limit: Agreement does not prove the categories capture the intended experience.
- Check: Have two observers classify the same ambiguous event and inspect the disagreement.
- Requires [K16-05](ResearchAndProduction.md#k16-05): Consistent observation must still measure the intended construct.

## K16-07

**Decomposition does not establish a schedule.** A work breakdown identifies deliverables and activities; their sequence and dependencies require a separate scheduling analysis.

- Kind: general guidance. Focus: content inventories; dependencies; Scope, work breakdown, dependencies and schedules.
- Apply: Break concept delivery into inspectable outputs, then connect prerequisites.
- Limit: A complete-looking tree can still omit integration, review and revision work.
- Check: Identify what cannot begin until another output is available.
- Requires [K01-07](Foundations.md#k01-07): Dependency direction changes which sequence is possible.

## K16-08

**Scope needs acceptance conditions and boundaries.** A scope statement describes the work and deliverables whose completion can be evaluated.

- Kind: general guidance. Focus: scope; quality gates; Traceability from goals to concept to evaluation; Iteration priorities and stop criteria.
- Apply: Tie each concept output to a goal, exclusion and acceptance question.
- Limit: More detail does not establish completeness if the boundary keeps changing.
- Check: Find a plausible requested addition and decide whether it is inside the stated scope.
- Requires [K01-01](Foundations.md#k01-01): Experience goals determine justified inclusions and exclusions.

## K16-09

**Generator diversity and player experience are separate claims.** Output statistics describe a generator's range; a claim about experienced engagement requires observing players interacting with its content.

- Kind: general guidance. Focus: system simulations; Observable behavior versus reported preference; Performance, experience and accessibility measures.
- Apply: Pair structural sampling with participant observation only when both claims are being made.
- Limit: A diverse heatmap cannot establish that players notice or value the differences.
- Check: Check whether the proposed evidence actually includes the people whose experience is claimed.
- Requires [K06-09](SpatialDesign.md#k06-09): Representative sampling is needed before generalizing about output range.

## K16-10

**A distribution model needs a fit check.** An analytic distribution is a simplifying model of finite observations; different models can describe different portions of the data differently.

- Kind: general guidance. Focus: system simulations; Sampling error, uncertainty and statistical inference; contradictions.
- Apply: Compare observed cumulative outcomes and tails with the model used for a concept's forecast.
- Limit: A visually plausible central fit does not guarantee accurate rare-event predictions.
- Check: Inspect the range where the design would fail rather than only the most common outcomes.
- Requires [K04-07](EconomyAndProgression.md#k04-07): Outcome spread and tails matter alongside averages.

## K16-11

**A numerical step can invent a physical reversal.** A large discrete update can make a resisting force overshoot zero velocity and reverse an object even when the continuous model only slows it.

- Kind: general guidance. Focus: system simulations; Causality, confounds and alternative explanations; Failure classification, contradictory findings and negative results.
- Apply: Separate a simulation artifact from the intended material behavior before drawing a design conclusion.
- Limit: This check concerns drag alone in a stationary medium; other forces or moving fluid can change velocity direction legitimately.
- Check: Reduce the time step and isolate drag; reject a claimed bounce that disappears under refinement.
- Requires [K03-10](ActionsAndCombat.md#k03-10): The intended force direction must be stated relative to the medium.
- Supports [K16-01](ResearchAndProduction.md#k16-01): A rejecting observation can distinguish a model claim from its numerical artifact.

## K16-12

**Recruiting volunteers bounds audience claims.** Convenience and self-selected samples can differ systematically from the population of interest; missing or nonresponding participants can bias a result.

- Kind: general guidance. Focus: Sampling, recruitment and representativeness; Interviews, surveys and field observation; playtests.
- Apply: State the target audience, recruitment channel and who could not or chose not to participate before generalizing a concept test.
- Limit: A larger sample from the same restricted channel does not by itself remove selection bias.
- Check: Compare the recruitment frame with the intended audience and identify an excluded group whose experience could change the conclusion.
- Constrains [K16-03](ResearchAndProduction.md#k16-03): Random assignment among volunteers does not make them a random audience sample.
- Supports [K15-03](InteractionAndAccess.md#k15-03): Testing only participants with typical vision can miss barriers in essential visual signals.

## K16-13

**Stratification protects planned subgroup comparisons.** Stratified random sampling divides the target population into defined groups and samples within each; smaller groups can be deliberately sampled more heavily for their own comparisons.

- Kind: general guidance. Focus: Sampling, recruitment and representativeness; playtests.
- Apply: Plan subgroup questions before recruitment and distinguish audience-proportion sampling from deliberate oversampling.
- Limit: Stratification does not repair an incomplete recruitment frame; oversampled subgroup proportions are not automatically audience proportions.
- Check: Check that each planned comparison has relevant observations and explain how subgroup results relate to any overall claim.
- Requires [K16-12](ResearchAndProduction.md#k16-12): Subgroup coverage is meaningful only relative to the stated audience and recruitment limits.
- Requires [K16-05](ResearchAndProduction.md#k16-05): The chosen group comparison must measure the intended experience.

## K16-14

**Statistical significance does not measure usefulness.** Statistical significance depends on effect strength and sample size; a small effect can be significant without being practically useful.

- Kind: general guidance. Focus: hypotheses; Effect size, comparison, confounds and replication; cost and risk.
- Apply: Compare the observed improvement with an explicit design goal and statistical uncertainty. Even a statistically clear improvement may offer too little player benefit to justify its production cost or continuing maintenance.
- Limit: A nonsignificant result is not proof of no effect; practical value depends on context rather than a universal cutoff.
- Check: Report the size and uncertainty of the change, then explain what player-relevant decision that magnitude would justify.
- Requires [K16-05](ResearchAndProduction.md#k16-05): A precisely measured change is useful only if the metric addresses the intended construct.
- Supports [K04-05](EconomyAndProgression.md#k04-05): Practical adoption can be compared with the alternative use of the same resources.

## K16-15

**A confound varies systematically with the tested condition.** Uncontrolled variation can add noise; a factor that differs systematically across test conditions can instead provide an alternative explanation for their outcome difference.

- Kind: general guidance. Focus: Causality, confounds and alternative explanations; Experimental, observational and mixed-method studies; Effect size, comparison, confounds and replication.
- Apply: When comparing a design change, record differences in tasks, instructions, facilitation and participants rather than attributing every outcome difference to that change.
- Limit: Not every varying factor is a confound. Controlling conditions can narrow generalization, and merely listing a confound does not remove its effect.
- Check: Identify a plausible alternative cause that changes with the tested condition; redesign the comparison or bound the causal claim.
- Requires [K16-03](ResearchAndProduction.md#k16-03): Participant selection and condition order can create systematic differences that a comparison must account for.
- Constrains [K16-01](ResearchAndProduction.md#k16-01): An outcome difference alone cannot reject alternative causal explanations when the conditions are confounded.
