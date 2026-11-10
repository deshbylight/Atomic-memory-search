# G13: Equipment inertia, contact cooling and insulating layers

[Parent group](CharactersAndMotion.md) | [Knowledge hub](README.md)

General knowledge; design applications are untested. A game's own approved decisions prevail.

## Tree placement

| Subgroup | Relevant cards |
|---|---|
| G13.04 Costume and equipment | [K13-32](#k13-32); [K13-33](#k13-33); [K13-34](#k13-34); [K13-35](#k13-35) |

## K13-32

**Rotational inertia depends on where the mass sits.** For a chosen rotation axis, mass farther from that axis contributes more rotational inertia; equal total mass can therefore require different torque for the same angular acceleration.

- Kind: general guidance. Focus: Grip, reach and leverage; Mass, inertia and centre of gravity.
- Apply: Compare a tool with mass near the grip against one with the same mass concentrated near its far end.
- Limit: The result depends on the axis and motion; static balance alone does not determine handling.
- Check: Keep total mass and applied torque fixed, redistribute the mass and compare the change in turning response.
- Requires [K03-20](ToolMechanics.md#k03-20): The torque comparison needs a stated force arm and rotation axis.
- Supports [K13-09](CharactersAndMotion.md#k13-09): Handling differences should appear in the progression between poses.

## K13-33

**Equal temperature can produce different contact cooling.** Two surfaces at the same temperature can draw heat from skin at different rates; conductive heat transfer depends on material, geometry and the temperature difference.

- Kind: general guidance. Focus: materials; climate and use; Climate, activity and protection.
- Apply: Distinguish an exposed metal fitting from an insulating grip or skin-contact layer.
- Limit: A cold sensation is not a direct thermometer reading; contact area and duration also matter.
- Check: Hold surface temperature constant and compare the proposed contact materials and areas.
- Requires [K13-20](CreatureSenses.md#k13-20): The proposed thermal cue still needs a stimulus at the receiving surface.
- Supports [K12-15](EnvironmentArt.md#k12-15): A thermally different contact layer can be distinct from the visible outer facing.

## K13-34

**Insulating bulk depends on retained air and thickness.** Fibrous insulation can hold small air pockets with low thermal conduction; thickness and restricted air movement help limit heat transfer.

- Kind: general guidance. Focus: materials; climate and use; Climate, activity and protection.
- Apply: Explain the air-holding volume beneath a cold-climate outfit rather than only adding a fur texture.
- Limit: Insulation reduces heat transfer rather than generating heat; compression, moisture and openings need separate assessment.
- Check: Flatten the proposed insulating layer and reconsider the claimed protection without assuming its performance is unchanged.
- Requires [K13-07](CharactersAndMotion.md#k13-07): The cut and supports must provide room for the proposed insulating volume.
- Constrains [K13-29](CreatureDefense.md#k13-29): Insulation changes how body size and surroundings translate into heat loss.

## K13-35

**Cold airflow can defeat a still-air explanation.** Moving cold air can carry heat away faster than still cold air; insulation works differently when air can circulate through or around its protected layer.

- Kind: general guidance. Focus: climate and use; Climate, activity and protection.
- Apply: Inspect the openings, overlaps and exposed edges of an outfit in a windy setting.
- Limit: Wind cooling does not mean the air temperature itself has fallen; hot conditions and evaporation need their own heat balance.
- Check: Keep air temperature fixed, add airflow and identify which protected air pockets remain sheltered.
- Requires [K13-34](WornEquipment.md#k13-34): The protected layer must retain the air its insulation explanation depends on.
- Supports [K07-21](WeatherAndWater.md#k07-21): The same airflow can also promote evaporative cooling when moisture is available.

## Worked dependency

[K13-35](WornEquipment.md#k13-35) -> [K13-34](WornEquipment.md#k13-34) -> [K13-29](CreatureDefense.md#k13-29)

Condition: A small warm-bodied traveler wears a bulky outfit in cold wind.
Rejecting probe: Trace air retention and layer openings before claiming the same protection in still and moving air.
