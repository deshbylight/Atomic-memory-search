# G03: Force, travel and contact in tool interactions

[Parent group](ActionsAndCombat.md) | [Knowledge hub](README.md)

General knowledge; design applications are untested. A game's own approved decisions prevail.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G03.02 Interaction and affordances | [K03-20](#k03-20); [K03-21](#k03-21); [K03-22](#k03-22); [K03-23](#k03-23) |
| G03.06 Environmental systems | [K03-22](#k03-22) |
| G03.07 Objects and equipment | [K03-20](#k03-20); [K03-21](#k03-21); [K03-23](#k03-23) |

## K03-20

**Leverage depends on perpendicular force arms.** A lever balances torques about its pivot; the ratio of perpendicular input and output arms determines its ideal force advantage.

- Kind: general guidance. Focus: object manipulation; tools and weapons; equipment tradeoffs.
- Apply: Place the pivot, load contact and operator before enlarging a tool handle.
- Limit: A longer handle supplies no free energy and needs room to travel; an angled push changes its effective arm.
- Check: Keep the load fixed, move the grip and compare both required force and handle clearance.
- Requires [K13-01](CharactersAndMotion.md#k13-01): The intended operator must reach the input point and brace the tool.
- Supports [K03-06](ActionsAndCombat.md#k03-06): A force advantage with a clearance cost can distinguish tool roles.

## K03-21

**Pulley advantage depends on the supporting rope paths.** An ideal fixed pulley redirects tension without multiplying it; several rope segments supporting a moving load can reduce the input force, at the cost of pulling more rope.

- Kind: general guidance. Focus: object manipulation; tools and weapons; equipment tradeoffs.
- Apply: Trace each supporting segment and reserve space for the free end to travel.
- Limit: Friction, pulley weight and oblique segments change actual forces; counting visible wheels alone is insufficient.
- Check: Raise the load through one interval and account for the length taken up by every supporting segment.
- Requires [K03-01](ActionsAndCombat.md#k03-01): The supporting tensions must agree with the load and its acceleration.
- Supports [K13-19](MotionStudies.md#k13-19): A visible rope detail can communicate take-up that a uniform strand hides.

## K03-22

**Starting friction and sliding friction need separate treatment.** Static friction responds up to a limiting value before slipping; sliding friction acts during relative motion and can be lower for the same contact pair.

- Kind: general guidance. Focus: object manipulation; material reactions.
- Apply: Distinguish breaking a crate free from keeping it moving across the same surface.
- Limit: Simple friction coefficients approximate particular contacts; a rough appearance does not establish a universal force.
- Check: Compare starting and sustained motion while holding load and contact materials constant.
- Requires [K03-01](ActionsAndCombat.md#k03-01): Friction is part of the net force rather than an automatic stop rule.
- Supports [K03-08](ActionsAndCombat.md#k03-08): Inspectable contacts can explain why one manipulation works differently from another.

## K03-23

**A ramp exchanges lifting force for travel distance.** An ideal ramp spreads a given height gain over a longer path, reducing the required force along the slope without reducing the gravitational work.

- Kind: general guidance. Focus: object manipulation; equipment tradeoffs.
- Apply: Compare a freight ramp with a direct lift using the same load and destination height.
- Limit: Friction and handling add work; a longer path can conflict with the available footprint.
- Check: Trace the complete load journey and account for both height gained and contact resistance.
- Requires [K03-22](ToolMechanics.md#k03-22): Actual ramp effort depends on the friction along the contact path.
- Supports [K11-19](SettlementNetworks.md#k11-19): A freight route can trade a longer run for a different handling operation.

## Worked dependency

[K03-23](ToolMechanics.md#k03-23) -> [K03-22](ToolMechanics.md#k03-22) -> [K03-01](ActionsAndCombat.md#k03-01)

Condition: A bulky load must reach a higher workshop platform.
Rejecting probe: Trace the slope, load contacts and applied force; reject a ramp justified only by lower effort with no travel cost.
