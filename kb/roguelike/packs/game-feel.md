# game-feel

## combat design
- [definition] A charge is a single step followed by a bump in the same or an adjacent direction, which grants a first strike. When: melee characters approach an adjacent monster. Why: The step and bump combine into one heavier, first-striking attack.
- [pitfall] Even at full health after a healing item, a character can die next turn if incoming damage exceeds the maximum hit points. When: Maximum health is low relative to possible incoming damage. Why: Healing restores health but cannot prevent damage larger than the maximum.
- [fact] Plain ASCII conveys gore poorly, because most gore effect is visual.
- [fact] In first-person views attack shapes are hard to read, so weapon behaviour usually matters more than shape. When: first-person view. Why: players cannot easily judge the damaged volume from the camera angle.

## 3d spatial design
- [pitfall] Camera edge cases such as vegetation, cliff edges and uphill targeting can leave the player unable to see what they are doing.
- [fact] Moving a tactical game into 3D adds large design overhead, mainly in cameras and unit selection, which a top-down or 2D view avoids.

## player resources and mood
- [mechanism] Environment can affect mood: a blizzard reducing visibility can hide attacks, and a warm inn can restore incapacitated companions.
- [mechanism] A fixed number of inventory slots, each holding one item type, turns inventory choice into a budget where each slot works as one usable ability. When: A game limits carried items to a fixed slot count. Why: Each slot is scarce, so carrying one item type means giving up another ability.
