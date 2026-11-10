# G10 — Atmospheric depth, light scattering and edges

[Parent group](VisualLanguage.md) · [Knowledge hub](README.md)

General knowledge; all design applications below are untested. A game's own approved decisions prevail.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G10.04 Light and material appearance | [K10-16](#k10-16); [K10-17](#k10-17); [K10-18](#k10-18); [K10-19](#k10-19); [K10-20](#k10-20) |
| G10.05 Perspective and scale | [K10-16](#k10-16); [K10-17](#k10-17) |

## K10-16

**Atmospheric perspective depends on the viewing conditions.** Distance can change observed color and value through the intervening atmosphere; the strength of that change varies with atmospheric conditions.

- Kind: general guidance. Focus: atmosphere; Atmospheric depth and exposure; depth cues; Atmospheric perspective.
- Apply: Compare foreground, middle distance and background in the intended clear or hazy condition before choosing their value and color separation.
- Limit: Distance does not require one fixed blue tint or contrast reduction; clear conditions can leave subtle differences.
- Check: Hold geometry and viewpoint fixed and compare the proposed depth readings under clear and hazy lighting studies.
- Requires [K10-03](VisualLanguage.md#k10-03): A depth comparison needs a stated viewpoint and viewing distance.
- Supports [K12-01](EnvironmentArt.md#k12-01): Atmospheric separation can preserve or weaken the planned environmental mass hierarchy.

## K10-17

**An edge can disappear where adjacent colors and values agree.** Contour visibility can vary around one object: neighboring color and value may merge along one segment and separate along another.

- Kind: general guidance. Focus: Contrast allocation and dynamic range; camera-dependent readability.
- Apply: Design lost and found edges deliberately, retaining contrast where recognition or an action boundary depends on it.
- Limit: A silhouette test isolates shape but does not prove that the boundary remains visible against its final background.
- Check: Place the same object against its intended backgrounds; mark where its outline vanishes and test the required recognition there.
- Constrains [K10-07](VisualLanguage.md#k10-07): Recognition of an isolated filled silhouette does not establish contrast against neighboring scene colors.
- Supports [K10-01](VisualLanguage.md#k10-01): Selective boundary contrast can strengthen a chosen first reading without outlining every object equally.

## K10-18

**Atmosphere is a relation across a picture, not uniform blur.** An atmospheric impression can depend on coherent color and value relationships rather than indiscriminate haziness or vague contours.

- Kind: general guidance. Focus: atmosphere; Atmospheric depth and exposure.
- Apply: Compare a study that adjusts relationships between depth planes with one that merely blurs the whole image.
- Limit: Blur may represent a particular condition, but its presence alone does not establish convincing depth or breathable space.
- Check: At matched size, check whether near and distant masses separate while essential foreground boundaries remain legible.
- Requires [K10-16](VisualDepth.md#k10-16): The intended atmospheric condition determines which depth relationships should change.
- Supports [K10-17](VisualDepth.md#k10-17): Locally varied boundary contrast allows atmospheric integration without uniformly softening every edge.

## K10-19

**Absorption removes light while scattering redirects it.** Absorption reduces light along a path; scattering redirects it, removing some from a direction and potentially adding light from other directions.

- Kind: general guidance. Focus: atmosphere; exposure and visibility.
- Apply: Distinguish a dark absorbing veil from a lit scattering haze before using one fog treatment for both.
- Limit: Scattering does not create light; a bright shaft needs illumination and a path that scatters some of it toward the observer.
- Check: Trace source, medium and observer for a proposed shaft; compare its lit and unlit appearance and reject unexplained brightness.
- Supports [K10-16](VisualDepth.md#k10-16): The kind of intervening medium helps explain changes in atmospheric depth.
- Requires [K10-13](VisualLanguage.md#k10-13): The position and direction of illumination constrain where scattered light can become visible.

## K10-20

**Optical thickness accumulates along a path through a medium.** Extinction accumulated along a path is optical thickness. Beam transmittance measures the surviving fraction after absorption and scattering out of a path; consecutive segment transmittances multiply.

- Kind: general guidance. Focus: exposure and visibility; Atmospheric depth and exposure.
- Apply: Compare a short path across haze with a longer path through the same medium before assigning equal visibility to equally dense regions.
- Limit: Beam transmittance excludes emitted light and scattering into the path. Density at one point alone does not determine the final image.
- Check: Sketch the full viewing path and compare short and long segments while holding medium properties fixed; account separately for added light.
- Requires [K10-19](VisualDepth.md#k10-19): Attenuating an original beam and adding scattered light are different contributions.
- Supports [K10-16](VisualDepth.md#k10-16): Longer paths through an intervening medium can change depth relationships even when local density is unchanged.

## Worked visibility dependency

[K10-20](#k10-20) -> [K10-19](#k10-19) -> [K10-16](#k10-16): separate loss along the viewing path from added scattered light before changing atmospheric depth. Useful when a long fog-filled passage and a short crossing have been assigned the same visibility.
