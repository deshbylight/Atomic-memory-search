# G01: Camera eye height, field of view axis and joint action rules

[Parent group](Foundations.md) | [Knowledge hub](README.md)

General knowledge; design applications are untested. A game's own approved decisions prevail.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G01.06 Design constraints | [K01-24](#k01-24); [K01-25](#k01-25); [K01-26](#k01-26) |

## K01-24

**Eye height changes the implied body and scale.** Camera eye height changes perceived body size and the apparent scale of nearby geometry.

- Kind: general guidance. Focus: camera and embodiment.
- Apply: Compare eye offsets in one blockout while holding geometry and movement speed fixed.
- Limit: This supplies neither a universal height nor an approved camera change.
- Check: Repeat doorway approaches and nearby obstacle views at recorded eye heights.
- Requires [K06-07](SpatialDesign.md#k06-07): The view must relate to actual movement metrics.
- Supports [K14-03](Audiovisual.md#k14-03): An embodied viewpoint changes the information a frame reveals.

## K01-25

**Field-of-view comparisons need an axis and aspect ratio.** Horizontal, vertical and diagonal angles describe different fields of view; changing visible extent can change apparent peripheral motion.

- Kind: general guidance. Focus: camera and embodiment.
- Apply: Record angle axis and aspect ratio before comparing cameras at fixed physical speed.
- Limit: No universal preferred angle follows from this relationship.
- Check: Compare actual views with axis, aspect ratio, eye height and speed declared.
- Requires [K01-24](EmbodiedPlay.md#k01-24): Hold eye height consistent during the comparison.
- Constrains [K10-03](VisualLanguage.md#k10-03): Composition depends on the chosen view extent.

## K01-26

**Joint actions need an aggregation rule.** A joint action can resolve through one participant rather than separate attempts; group composition can therefore change the result.

- Kind: general guidance. Focus: solo and group compatibility.
- Apply: Declare contributors, the resolving capability and what happens with one participant.
- Limit: Using the weakest participant is one possible rule, not proof of solo compatibility.
- Check: Run the same obstacle alone and with the intended group; expose any simultaneous requirement.
- Requires [K05-01](CooperativePlay.md#k05-01): Contribution rules need a defined interdependence.
- Constrains [K06-20](EncounterComposition.md#k06-20): An opportunity to contribute does not establish solo sufficiency.

## Worked dependency

[K01-24](EmbodiedPlay.md#k01-24) -> [K06-07](SpatialDesign.md#k06-07) -> [K03-03](ActionsAndCombat.md#k03-03)

Condition: A first-person obstacle supports movement and retreat.
Rejecting probe: Hold geometry fixed, record the eye height and movement metrics, then traverse the intended approach and retreat.

## Project reading adapter

Use | with the approved camera target and | for view-dependent threat placement. Read | for contribution opportunities and split/rejoin cases. Joint resolution adds a solo/group comparison; it does not replace spatial cooperation tests. Applications remain untested.
