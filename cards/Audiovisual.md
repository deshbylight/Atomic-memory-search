# G14 — Sound, music, effects and cinematic presentation

[Knowledge hub](README.md) · [Cross-domain chains](Connections.md)

General principles below are distinct from their proposed application; the applications are untested.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G14.01 Sound foundations | [K14-01](#k14-01); [K14-05](#k14-05); [K14-06](#k14-06); [K14-15](#k14-15) |
| G14.02 Soundscape | [K14-01](#k14-01); [K14-06](#k14-06); [K14-13](#k14-13) |
| G14.03 Gameplay audio | [K14-02](#k14-02); [K14-11](#k14-11) |
| G14.04 Music and voice | [K14-02](#k14-02); [K14-07](#k14-07); [K14-08](#k14-08) |
| G14.05 Camera and cinematography | [K14-03](#k14-03); [K14-09](#k14-09); [K14-10](#k14-10); [K14-14](#k14-14) |
| G14.06 Visual effects | [K14-04](#k14-04); [K14-12](#k14-12) |
| G14.07 Audiovisual coordination | [K14-04](#k14-04); [K14-13](#k14-13); [K14-14](#k14-14); [K14-15](#k14-15) |
| G14.08 Production and validation | [K14-04](#k14-04); [K14-11](#k14-11) |

## K14-01

**Sound propagation describes the space.** Propagation time grows with path length; reflection and scattering depend on surface geometry relative to wavelength.

- Kind: general guidance. Focus: Propagation and attenuation; spatial storytelling.
- Apply: Describe nearby, distant and reflected sound separately when proposing an underground soundscape; connect audible changes to space.
- Limit: A simplified acoustic model may be appropriate; this establishes no audio engine behaviour or measured room response.
- Check: Compare the proposed cue in an open room, behind an obstruction and near a reflective boundary.
- Requires [K11-03](BuiltWorld.md#k11-03): The shape and openings of an underground space constrain a plausible acoustic description.
- Supports [K14-06](Audiovisual.md#k14-06): An enclosed space can distinguish early reflections from its later reverberant tail.

## K14-02

**Critical audio needs an information role.** A signal competes with other information, and a single sensory distinction can fail for some users or playback conditions.

- Kind: design inference. Focus: threat cues; Ducking, voice priority and mix interaction.
- Apply: Assign each critical sound a meaning and priority; coordinate music and voice so they do not hide that meaning, and provide another cue channel.
- Limit: This is a design inference, not a claim that a specific mix or adaptive music system has been tested.
- Check: Can the player identify the essential event with music present and again with sound disabled?
- Requires [K15-03](InteractionAndAccess.md#k15-03): Essential information should survive loss of one cue channel.
- Requires [K14-15](Audiovisual.md#k14-15): When cue audibility depends on nearby spectral energy, compare it within the competing mix.

## K14-03

**Camera framing changes what can be decided.** Framing controls which spatial relations and movements remain visible; pictorial balance alone does not guarantee actionable information.

- Kind: design inference. Focus: point of view.
- Apply: Judge a camera proposal against threat visibility, interaction reach and orientation during movement, using the game's own camera constraints.
- Limit: Cinematic framing is not automatically suitable for continuous player control; embodied comfort remains unverified.
- Check: Trace approach, interaction and retreat with the proposed framing and identify any hidden required cue.
- Requires [K10-03](VisualLanguage.md#k10-03): Visual hierarchy and scale must be evaluated from the playable viewpoint.

## K14-04

**Effects should agree about the event.** Concurrent visual and auditory elements can reinforce a common interpretation or compete for attention and hide other cues.

- Kind: design inference. Focus: anticipation and impact; effect readability; contextual review.
- Apply: Tie effect onset, direction and decay to the state change they communicate; evaluate the combined result under group activity.
- Limit: A standalone effect preview does not validate combat readability, comfort, runtime performance or replication.
- Check: Show the event in a crowded encounter and check whether observers still identify its cause, target and end.
- Requires [K13-04](CharactersAndMotion.md#k13-04): Effects must preserve the action cue and response window rather than overwrite them.
- Requires [K15-03](InteractionAndAccess.md#k15-03): A critical encounter event should retain its essential meaning when one cue channel is unavailable.
- Requires [K02-12](PlayerExperience.md#k02-12): Critical event cues need an attention check during competing activity.
- Supports [K14-12](Audiovisual.md#k14-12): Source activity and surviving particles can communicate different event phases.

## K14-05

**Distance reduces pressure differently from intensity.** For ideal spherical spreading from a point source, pressure amplitude falls approximately with inverse distance and intensity with inverse distance squared.

- Kind: general guidance. Focus: loudness; space and distance; Amplitude, loudness and dynamic range; Propagation and attenuation.
- Apply: Distinguish propagation delay, level loss and the surrounding acoustic response.
- Limit: Rooms, extended sources, occlusion and near-field behavior depart from this ideal model.
- Check: State the model's conditions before using a distance rule to justify an audio concept.
- Supports [K14-01](Audiovisual.md#k14-01): Distance presentation needs both path timing and spatial response.

## K14-06

**Early reflections and late reverberation have different structure.** Sparse early echoes can be distinguished from the dense later reverberant tail.

- Kind: general guidance. Focus: Early reflections and reverberation decay; Room geometry, materials and acoustics; spatial storytelling.
- Apply: Describe initial spatial reflections and sustained decay separately when comparing enclosed spaces.
- Limit: A single decay time does not capture every perceptual or frequency-dependent property.
- Check: Compare an impulse-like event in both spaces and identify which part of the response differs.
- Requires [K11-03](BuiltWorld.md#k11-03): Acoustic claims must be consistent with the space's geometry and openings.

## K14-07

**Beat grouping differs from beat subdivision.** Meter groups beats while simple or compound division describes subdivisions of the beat; tempo is another variable.

- Kind: general guidance. Focus: harmony and rhythm; Rhythm, metre and tempo.
- Apply: Specify pulse, grouping and subdivision separately before comparing musical variants.
- Limit: These categories describe particular musical traditions and do not assign universal emotional meanings.
- Check: Describe two passages with equal tempo but different grouping or subdivision.
- Constrains [K14-02](Audiovisual.md#k14-02): Musical structure must preserve the information role of critical cues.

## K14-08

**Motif variation can preserve rhythm and contour.** A recurring musical idea can retain characteristic rhythm or contour while its exact notes vary.

- Kind: general guidance. Focus: motifs; Melody, motif and thematic variation; Character, regional and narrative-state coherence; Persistent motifs across gameplay states.
- Apply: Identify what remains recognizable across variants and what changes with context.
- Limit: Recognizable structure does not establish a listener's intended narrative association.
- Check: Compare original and variant without their labels and ask what relationship is heard.
- Requires [K02-01](PlayerExperience.md#k02-01): Repeated identity depends on distinctive retrievable cues.

## K14-09

**Screen direction needs spatial context.** Cutting across an established action axis can reverse apparent positions and eyelines; a new orienting view can establish a changed relation.

- Kind: general guidance. Focus: continuity; Screen direction and spatial continuity; Eyelines and axis of action.
- Apply: Record the established relation before comparing shot changes.
- Limit: Continuous player-controlled movement does not follow every convention of edited film.
- Check: Trace a subject's direction and partner position across the transition.
- Requires [K14-03](Audiovisual.md#k14-03): Camera choices must preserve information needed for orientation.

## K14-10

**Cross-cutting can imply a relation between separate actions.** Alternating between lines of action invites the viewer to connect their timing, stakes or meaning.

- Kind: general guidance. Focus: Montage, rhythm and ellipsis; Reveal timing and withheld information.
- Apply: State which relation the alternation should imply and what establishes it.
- Limit: Juxtaposition does not by itself prove that events are simultaneous or causally linked.
- Check: Ask what temporal or causal relation a viewer infers without explanatory labels.
- Requires [K09-05](Narrative.md#k09-05): An implied narrative relationship should agree with the actual causal structure.
- Supports [K14-14](Audiovisual.md#k14-14): Audio overlap can influence the relationship inferred between alternating images.

## K14-11

**Captions include meaningful nonspeech information.** Synchronized text can convey relevant speech and meaningful nonspeech events when audio is unavailable.

- Kind: general guidance. Focus: Subtitles, captions and speaker identity; Visual alternatives for essential sound; threat cues.
- Apply: Include the event information needed to interpret an audiovisual sequence.
- Limit: A transcript alone does not preserve the timing of a time-critical cue.
- Check: With audio disabled, check whether the essential event and its timing remain understandable.
- Supports [K15-03](InteractionAndAccess.md#k15-03): Essential meaning should survive loss of a sensory channel.

## K14-12

**Stopping emission differs from ending every particle.** An emitter can stop creating particles while particles already created continue through their remaining lifetimes.

- Kind: general guidance. Focus: Anticipation, active phase and decay; Particle emission, lifetime and variation; Scale, time and camera-distance consistency.
- Apply: Specify the source's active interval separately from the visible aftermath.
- Limit: Particle lifetime need not equal opacity duration or source duration; attachment and cleanup policies can alter the result.
- Check: Stop emission mid-effect and inspect which parts persist and when the final visible element ends.
- Requires [K14-04](Audiovisual.md#k14-04): Remaining elements must still communicate the same event phase.
- Supports [K03-01](ActionsAndCombat.md#k03-01): Surviving particles can continue moving under their accumulated forces.

## K14-13

**A sound's story-world status differs from visibility.** Diegetic sound belongs to the represented world; nondiegetic sound addresses the audience outside that world. A world source can be outside the image frame.

- Kind: general guidance. Focus: Ambience, room tone and off-screen events; Diegetic and non-diegetic information; World consistency and supernatural exceptions.
- Apply: An unseen footstep still has a world source, while an audience-only score need not be heard by characters. Specify the source, visibility and intended listeners.
- Limit: Subjective or deliberately ambiguous sound needs a stated interpretation; being off-screen alone does not make a sound nondiegetic.
- Check: For each cue, state its source and intended listeners, then check character reactions against that account.
- Supports [K09-09](Narrative.md#k09-09): Sound can give the audience access beyond a character's viewpoint.
- Requires [K15-09](InteractionAndAccess.md#k15-09): If a world sound supports a decision, its alternative must be available at the useful moment.

## K14-14

**Sound can cross an image cut.** A sound bridge overlaps a visual transition: incoming audio can precede its image, or outgoing audio can continue after the picture changes.

- Kind: general guidance. Focus: Scene-change consistency; Sound continuity and audiovisual counterpoint; Emotional pacing and controlled silence; Persistent aftermath and transitions.
- Apply: Use the overlap to carry attention, prepare a new place or retain the previous action's emotional effect.
- Limit: Audio continuity alone does not prove that the two images share a place or time.
- Check: Draw separate picture and sound timelines; identify what the overlap leads the audience to infer and test that inference.
- Requires [K14-13](Audiovisual.md#k14-13): The source and story-world status of the overlapping sound must remain interpretable.
- Supports [K09-12](Narrative.md#k09-12): Audio and image can disclose an event at different moments.

## K14-15

**A nearby stronger spectral component can mask a weaker one.** A small spectral peak near a much stronger peak can become inaudible through auditory masking; presence in the signal does not guarantee perceptibility.

- Kind: design inference. Focus: masking; Temporal and frequency masking; priority and mixing; Priority during simultaneous events.
- Apply: Compare a critical cue alone and within the intended mix, then vary competing energy near its important frequencies.
- Limit: Design inference: this is frequency masking; it specifies no universal threshold and does not establish temporal masking, listener hearing or loudness safety.
- Check: Keep the critical cue unchanged and compare recognition with the competing sound present and absent.
- Constrains [K14-02](Audiovisual.md#k14-02): Assigning a cue priority does not ensure its defining components remain audible in the mix.
- Supports [K15-03](InteractionAndAccess.md#k15-03): Another information channel can preserve essential meaning when the auditory distinction is masked.
