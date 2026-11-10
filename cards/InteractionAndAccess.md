# G15 — UX, interfaces, onboarding and accessibility

[Knowledge hub](README.md) · [Cross-domain chains](Connections.md)

General principles below are distinct from their proposed application; the applications are untested.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G15.01 Interaction design | [K15-01](#k15-01); [K15-07](#k15-07); [K15-08](#k15-08); [K15-11](#k15-11); [K15-12](#k15-12); [K15-13](#k15-13) |
| G15.02 Information design | [K15-02](#k15-02); [K15-05](#k15-05); [K15-09](#k15-09); [K15-12](#k15-12) |
| G15.03 Controls and ergonomics | [K15-01](#k15-01); [K15-07](#k15-07); [K15-13](#k15-13) |
| G15.04 Onboarding | [K15-02](#k15-02); [K15-08](#k15-08); [K15-09](#k15-09); [K15-11](#k15-11) |
| G15.05 Accessibility | [K15-03](#k15-03); [K15-05](#k15-05); [K15-06](#k15-06); [K15-09](#k15-09); [K15-10](#k15-10); [K15-11](#k15-11); [K15-12](#k15-12); [K15-13](#k15-13) |
| G15.06 Embodied comfort | [K15-03](#k15-03); [K15-10](#k15-10) |
| G15.07 Cooperative UX | [K15-04](#k15-04) |
| G15.08 Validation and localisation | [K15-04](#k15-04); [K15-06](#k15-06); [K15-07](#k15-07); [K15-11](#k15-11); [K15-12](#k15-12) |

## K15-01

**Interaction should accept plausible intent.** When an interface rejects reasonable equivalent actions without explanation, users must discover the interface vocabulary before solving the actual task.

- Kind: general guidance. Focus: consistency; device differences.
- Apply: Specify visible action, input, result and failure feedback for each core interaction; account for alternate control schemes in the concept.
- Limit: This defines no widget implementation; actual player UI follows the game's own interface rules.
- Check: Give a player the goal without input instructions and observe whether the interface communicates the next available action.
- Supports [K03-02](ActionsAndCombat.md#k03-02): A puzzle or object should test reasoning about the world rather than hidden input conventions.

## K15-02

**Teach retrieval through information hierarchy.** Useful organization and distinctive cues support finding and recalling information; a prompt visible at every step can conceal dependence on that prompt.

- Kind: general guidance. Focus: hierarchy; practice.
- Apply: Introduce an action in context, let the player attempt it, then test later use without the same instruction.
- Limit: Less text is not automatically clearer, and successful recognition does not demonstrate recall.
- Check: Can the player explain the relevant state and perform the action after the instruction is removed?
- Requires [K02-03](PlayerExperience.md#k02-03): Onboarding completion should include independent retrieval and transfer.

## K15-03

**Redundant cues preserve essential meaning.** Foreground contrast and non-colour distinctions affect whether information remains readable; colour alone can exclude users who cannot distinguish it.

- Kind: general guidance. Focus: vision; motion sickness.
- Apply: Combine a critical colour cue with shape, position or text; assess movement and effects separately for comfort and sensory load.
- Limit: A static contrast check does not establish overall accessibility, readable motion or absence of discomfort.
- Check: Identify the essential event in grayscale and with one sensory channel unavailable; separately test representative movement.
- Constrains [K12-04](EnvironmentArt.md#k12-04): Dressing and lighting must preserve distinctions that essential cues depend on.
- Requires [K15-05](InteractionAndAccess.md#k15-05): An alternate cue must preserve the information purpose rather than merely add detail.

## K15-04

**Cooperative state must be legible to late readers.** Participants can have different information and control; identical-looking state does not prove that ownership or shared consequences are understood.

- Kind: design inference. Focus: group status; language expansion.
- Apply: Show who acts, who pays and who is affected; test a late participant and longer localized labels without relying on voice explanations.
- Limit: This defines acceptance questions, not approved party permissions, a localization implementation or an irreversible voting rule.
- Check: Can a late participant explain a pending group action, its owner and their own available response?
- Requires [K05-04](CooperativePlay.md#k05-04): The interaction must respect who bears a shared cost and who has authority over it.

## K15-05

**An alternative description should preserve purpose.** A functional image needs an alternative that conveys its purpose; decorative detail can create unnecessary description noise.

- Kind: general guidance. Focus: Icons, labels and spatial organization; vision; Low vision, color vision and nonvisual information.
- Apply: Identify the decision-relevant content of a symbol or diagram before describing it.
- Limit: Listing every visible detail can obscure the information the task requires.
- Check: Complete the task from the alternative description alone.
- Supports [K15-03](InteractionAndAccess.md#k15-03): Redundant presentation must preserve the same essential meaning.

## K15-06

**Visual information may be missing from narration.** Speech can refer to visible information without conveying it; an added description is useful when essential context is otherwise absent.

- Kind: general guidance. Focus: comprehension; vision; Low vision, color vision and nonvisual information.
- Apply: Check what remains understood when an instructional scene is heard without its image.
- Limit: Describing information already fully conveyed can add repetition without helping.
- Check: Identify every instruction that depends on a gesture, location or unlabeled visual.
- Requires [K15-05](InteractionAndAccess.md#k15-05): An alternative should preserve the purpose of the information being replaced.

## K15-07

**Keyboard navigation depends on predictable focus.** Keyboard interaction uses a predictable focus path and familiar distinctions between moving, selecting and leaving a control.

- Kind: general guidance. Focus: Input mapping, consistency and discoverability; input mapping; device differences; Contrast, keyboard and assistive-technology audits.
- Apply: Describe navigation, activation and cancellation as separate actions across input devices.
- Limit: Web keyboard conventions are a transferable interaction analogy, not a game widget specification.
- Check: Complete the task without pointing and identify where focus will move next.
- Supports [K15-01](InteractionAndAccess.md#k15-01): Interaction should communicate an actionable intent rather than demand hidden conventions.
- Supports [K15-11](InteractionAndAccess.md#k15-11): A focus path can expose explanations otherwise available only on hover.

## K15-08

**An interrupting dialog needs a return point.** A modal interaction redirects attention and focus until resolved; returning to the initiating context supports continuation.

- Kind: general guidance. Focus: error recovery; Action selection, mode errors and recovery; Feedback, safe failure and recoverable mistakes.
- Apply: Record the initiating task, required response and place to resume.
- Limit: Modal interruption is costly and should match the importance of the decision.
- Check: Dismiss or complete the interruption and check whether the original task can continue without reconstruction.
- Requires [K15-07](InteractionAndAccess.md#k15-07): Focus must have a predictable destination before and after interruption.

## K15-09

**A cue's availability differs from its timing.** Information supplied after a decision cannot support that earlier decision; synchronized alternatives preserve a different function from retrospective records.

- Kind: design inference. Focus: HUD, diegetic information and attention competition; Contextual instruction and just-in-time help; Cognitive access, readability and memory demands.
- Apply: Distinguish advance instruction, immediate state feedback and later review.
- Limit: This is a design inference, not a universal tutorial schedule.
- Check: Find the earliest moment each required fact is available during a task.
- Requires [K14-11](Audiovisual.md#k14-11): An audio alternative must arrive while its event information is useful.

## K15-10

**Visual movement can conflict with bodily motion cues.** Visual motion can disagree with vestibular cues and contribute to discomfort.

- Kind: general guidance. Focus: Vestibular comfort, camera motion and sensory overload; camera motion; motion sickness.
- Apply: Make camera motion an explicit variable when evaluating an embodied presentation.
- Limit: No single camera setting guarantees comfort for every person or display; a stationary screenshot cannot establish comfort.
- Check: Compare optional camera-motion conditions during representative movement and record discomfort and task performance separately.
- Constrains [K02-05](PlayerExperience.md#k02-05): Agreement between event cues does not eliminate conflict with bodily motion cues.
- Requires [K14-03](Audiovisual.md#k14-03): Comfort changes must also preserve information needed for decisions.

## K15-11

**Passive help needs access without taking focus.** A passive tooltip explains its trigger without becoming the focus destination; access through focus as well as hover makes the help available without a mouse.

- Kind: general guidance. Focus: Affordances, signifiers, feedback and system state; contextual teaching; progressive disclosure; motor access; assistive compatibility.
- Apply: Keep focus on the triggering control, provide a way to dismiss help, and use a different interaction pattern when the popup contains actions.
- Limit: This describes passive help; an interactive popup needs its own navigation and focus behavior.
- Check: Reach the explanation with keyboard navigation, dismiss it, and continue the original task without a focus detour.
- Requires [K15-07](InteractionAndAccess.md#k15-07): The trigger must be reachable through the focus path.
- Requires [K02-08](PlayerExperience.md#k02-08): When testing learning, prompted help must be distinguished from independent execution.

## K15-12

**Progress state and completion need distinguishable reports.** A visual progress bar alone does not expose its current value to someone who cannot see it; progress information and completion can be reported separately.

- Kind: design inference. Focus: feedback; Affordances, signifiers, feedback and system state; status and inventory; vision; Low vision, color vision and nonvisual information; assistive compatibility.
- Apply: For a loading bar, make current progress available through accessible information so someone who cannot see it can tell whether work is ongoing or complete, distinguishing completion from an intermediate update.
- Limit: Design inference: unknown progress needs an honest state description; arbitrary percentages do not become informative through announcement.
- Check: Without looking at the bar, determine whether work is ongoing or complete and obtain current progress when it is known.
- Requires [K15-09](InteractionAndAccess.md#k15-09): State reports must arrive while they can guide the next action.
- Supports [K14-11](Audiovisual.md#k14-11): Text can preserve meaningful information when an audio announcement is unavailable.

## K15-13

**A slider can offer both small steps and endpoints.** A slider selects a value within a range; keyboard operation can provide small increments, larger changes and movement to the range endpoints.

- Kind: general guidance. Focus: Pointing, aiming, selection and motor demands; Remapping, input alternatives and device differences; precision; motor access; Motor access, timing windows and fatigue.
- Apply: Expose the current value and meaningful step sizes so precise adjustment does not depend only on dragging a small thumb.
- Limit: Discrete steps must fit the quantity; reaching an endpoint is different from confirming or leaving the control.
- Check: Set a near-endpoint value and a precise interior value without dragging; verify the displayed value and focus after each action.
- Requires [K15-07](InteractionAndAccess.md#k15-07): Value adjustment depends on reaching and remaining on the intended control.
- Constrains [K15-11](InteractionAndAccess.md#k15-11): Any explanatory help must not steal the focus needed for adjustment.
