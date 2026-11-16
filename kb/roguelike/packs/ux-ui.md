# ux-ui

## information density and feedback
- [rule] Show only the next age's technologies that current inventions unlock, since standard tech tree screens fail when inventions have many messy cross-links. When: the dependency graph has many cross-links that make a standard tree unreadable. Why: Cross-links make standard tree screens hard to read.
- [rule] Show by default only what changes the next decision, and keep full detail one command away. Why: Excess information slows play, while hidden information forces lookups.
- [rule] Present complex game information visually so players can understand it at a glance, since visual representation is a critical part of play. When: Designing information displays. Why: Players must read state quickly during play.
- [rule] Present at most seven options at once.
- [rule] Use a GUI toolkit that fits the game framework rather than building a custom GUI from scratch. When: Building menus and interface screens. Why: Custom GUIs without a toolkit tend to give unclear feedback.
- [rule] Provide search by tags and multiple filters, not only by author, so players can find generated content. When: when a large library of generated or user content is browsable. Why: Without filters, players cannot select useful items from large volumes.
- [heuristic] Designers must decide how much extra information the interface shows the player, since information shapes what decisions are possible. When: When designing the interface for procedurally generated or unpredictable levels. Why: Information matters most when maps are generated or enemies move unpredictably.
- [heuristic] Show a stack header with the total count and best identified item, and list sub-groups when the slot is selected. When: A slot holds several variants of one item type. Why: The header gives a quick read, while sub-groups show detail on demand.
- [metric] The number of status effects a player can use is limited by how clearly they can perceive each one, through border colours, icon size and screen space. When: designing how many status effects to show on screen. Why: Players can only track as many distinct effects as the display makes distinguishable.
- [pitfall] Showing only the current elevation hides lower levels, making combat and line of sight hard to judge. When: Displaying a multi-level map in a limited-color ASCII game. Why: Players lose the spatial context needed to judge threats and sight lines.
- [pitfall] A vi-key 'y' or 'n' can be pressed by accident at a prompt, so require uppercase answers. Why: Single lowercase letters are easy to hit by mistake.
- [pitfall] A camera that is partly free and partly locked is confusing, especially when control is taken away and the camera snaps back.
- [pitfall] Large sweeping camera pans add latency to every navigation step between map areas.
- [pitfall] A game can look polished and still fail in its first minutes when controls and screens are unclear. When: Reviewing the opening minutes of any game. Why: New players quit before reaching the core loop.
- [pitfall] Numerous hidden stacking exceptions, from identification state, inscriptions and special containers, make inventory behaviour hard for players to predict. When: Inventory stacking depends on many attributes and special cases. Why: Each extra exception adds a hidden condition the player must learn.
- [pitfall] Positional play is hard to read in a roguelike because the interface has no equivalent of a fighting game's stance graphics. When: when designing position-based combat for text or grid roguelikes. Why: players cannot see their stance or the trigger state.
- [pitfall] Incorrect information shown in the user interface is often worse than incorrect information found in the game world. When: when designing interface feedback. Why: players trust the interface to be accurate.

## ability and command keys
- [rule] When letters run out, add modifiers, an extended command mode, or action menus; menus suit mobile and console play. Why: Limited keys need extra input layers.
- [rule] Map spells, abilities and attacks to macros or function keys, and use one ability key to pick from a list. Why: A single list-picking key avoids many dedicated keys.
- [rule] Queue spells in order so the player can select them before they are cast. When: Two-key targeting with spells.
- [rule] Provide an interaction command letting the player take equipment from allies, give them items, dismiss them, and cast self-only spells such as healing on them. When: allies can pick up items the player may want back. Why: Without it, anything an ally picks up is lost unless the ally dies.
- [rule] Do not start in darkness, and do not start with the player character unable to move unless during a cutscene. When: Designing the first minutes of a game. Why: Players who cannot see or act quickly lose patience and may quit.
- [rule] Every menu must be easy to exit. When: Designing any menu screen. Why: A menu that traps the player forces a restart or process kill.
- [rule] List basic movement, attack and light commands and keys at the start of the manual, not only remapping instructions. When: Writing documentation for a game with a complex command set. Why: Players cannot use commands they cannot discover.
- [rule] Do not rely on the numpad alone for movement; provide alternative bindings, since laptop players may lack a numpad. When: Choosing default keyboard controls. Why: Keys that some players cannot reach exclude them from core play.
- [heuristic] Assign action keys to mnemonic letters, such as q for quaff, w for wear or wield, and e for eat. Why: Mnemonics are easier to remember than arbitrary letters.
- [heuristic] Use one generic interact command, one equip command, and one use command, letting the inventory screen handle most item actions. Why: Fewer commands keep the interface small.
- [heuristic] Generalise the interaction command into a talk-to-monsters action, such as buying stolen gear back from thieves or asking a monster across a chasm for a rope.
- [procedure] 1) Press the target key to enter target mode, which gives each in-range target an id. 2) Press a target's id to fire the active weapon at it. When: Real-time roguelikes where ranged combat speed matters. Why: One key assigns ids and a second key fires, which speeds up ranged attacks.
- [tradeoff] Cycling through levels with a key is inconvenient compared with showing several levels at once. When: Choosing how players switch between elevations in a multi-level display. Why: Repeated key presses slow players down and hide relations between levels.
- [fact] Commonly preferred command keys include i for inventory, l for look, z for zap, and . for rest. Why: Familiar mappings reduce learning cost.

## movement input controls
- [model] Instead of an explicit jump command, a character is standing when above solid ground and falling otherwise. Standing allows movement in any direction; falling tends toward downward movement. When: when the game has height and gaps. Why: removes the jump command and airborne cell handling.
- [rule] During movement, show only status conditions, speed, and visible items or creatures; full attributes belong on a character screen. Why: Keeps the play view uncluttered.
- [heuristic] Use point-and-click movement with the screen centred on the player when a game is mouse-driven. When: Designing movement for a mouse-driven game. Why: Centred view keeps the player's position and target on screen.
- [procedure] 1) Offer both vi-keys and numpad for movement, since some laptop keyboards have no numpad. 2) Let both work at once, or let players configure keys in an external file. Why: Players differ in keyboard hardware and habits.
- [tradeoff] Vi-keys need no numpad and are traditional, but have a learning curve, a QWERTY bias and fewer free letters. Numpad is intuitive and leaves letters free, but some laptops lack it, overlaid NumLock can toggle, and hand movement slows real-time play. Why: Each movement scheme trades familiarity against access and speed.
- [pitfall] Expanding the number of movement directions makes controls harder to learn, and inconsistent gravity leaves players unsure whether their character is standing.
- [pitfall] Split ergonomic keyboards may separate the 'y' key from the other vi-keys. Why: Layout changes can break the vi-key cluster.
- [pitfall] Movement by rolling the mouse in a direction fails in windowed mode because the pointer leaves the window, forcing players to re-centre it constantly. When: Using mouse-pointer position as a movement input in windowed display. Why: The pointer reaches the window edge and stops reporting useful position.
- [pitfall] A modal half-cost movement mode demands too much bookkeeping, and a modifier key for it overloads the input scheme. When: when adding a faster movement mode to a roguelike. Why: players must track the mode or spend input on the modifier.
- [fact] Movement directions grow from 4 cardinal moves to 8 plus stay, and to 27 when vertical moves are included.
- [fact] Numpad keys 8, 2, 4, 6 move in the cardinal directions, 7, 9, 1, 3 move diagonally, and 5 stays in place.
- [fact] Vi-keys h, j, k, l move in the cardinal directions, y, u, b, n move diagonally, and period is often used to stay in place.

## color and contrast signaling
- [behavior] Unseen sounds can be shown as a marker next to the player in the noise's direction, with color indicating distance or type. Why: Markers hint at unseen areas without revealing their contents.
- [rule] Make blocking walls, dangerous enemies and interesting items high contrast, and keep plain floor, blood and junk muted so they do not pull the eye. When: Coloring roguelike tiles. Why: Players notice high-contrast elements first, and a muted background lets important elements stand out.
- [rule] Never convey important information by red and green alone, since many players cannot tell those colors apart. When: Using color to encode meaning. Why: Color-blind players lose the information.
- [rule] During combat, show monster HP, player HP, MP, resistances, and attack results, using graphical feedback rather than messages. Why: Messages at the top of the screen slow play.
- [rule] Show visible feedback when a click registers, such as changing the clicked button or cursor, especially when processing is delayed. When: Designing menus or buttons that may take time to respond. Why: Without feedback, players cannot tell whether their click was received and repeat or abandon it.
- [rule] Show which element a creature takes damage from and which attacks have already been tested. When: Designing an interface for elemental combat. Why: Clear feedback turns trial and error into informed choice.
- [heuristic] Show status messages only when an attack is blocked or dodged, rather than on every move and stand, to avoid distraction. When: displaying combat defence feedback. Why: Constant messages on every action clutter the screen and distract players.
- [pitfall] Dark gray on dark brown is hard to tell apart. When: Choosing tile colors on dark backgrounds. Why: Low luminance difference hides details.
- [pitfall] Coding overlapping regions by colour alone fails quickly, because only about 28 colours are clearly distinguishable on a terminal display. When: Using one character per grid with a limited palette. Why: Many similar hues become hard to tell apart, so overlaps cannot be read reliably.
- [fact] Blue reads as cold and red as hot, and gradients can add depth.

## icons and glyph display
- [definition] An icon is any abstract symbol standing for an idea or action, including ASCII glyphs, tiles, item names, and command keys. Why: Defining the broad category lets every interface symbol be reviewed the same way.
- [definition] In a character display each glyph has its own meaning, such as period for floor, angle brackets for stairs, at-sign for the hero, and letters for monsters.
- [rule] Name items with words players already know, since familiar names work as icons while obscure names force lookup. Why: Recognition breaks when players must check meaning.
- [rule] Exaggerate key features so that icons differ clearly from one another. Why: Similar icons are confused at a glance.
- [heuristic] In a 16-colour ASCII game, display of multiple levels is the main problem; fix it before adding a third axis, using dimmed tiles, extra grey shades, shadows or a rotatable view. When: Planning how to show height in a text roguelike with a small palette. Why: Limited colours and single-layer display make elevation hard to read.
- [heuristic] Judge icons by three criteria in priority order: recognizability first, distinctness from other icons second, and consistency with the game's style third. Why: Recognition matters most; style cannot compensate for unclear meaning.
- [pitfall] Garbled speech can be hard to read, because certain letters and small words are easy to miss.
- [fact] Console roguelikes used a 16-color palette, encoded with four bits for red, green, blue and bright; modern tools support full 24-bit tile color.
- [fact] Graphical displays draw pixels directly and often use tiles instead of characters.
- [fact] Roguelikes present the world clearly without art assets by using characters to represent objects and creatures.

## inventory and food management
- [rule] Name items by their concrete effects, such as to-hit and carrying capacity bonuses, rather than by an abstract stat value. When: items grant bonuses to character attributes. Why: Direct effect values let players judge an item without translating through an abstract stat.
- [procedure] 1) Press the cycle button to move through carried items, briefly highlighting the selected one. 2) Press the use button to apply the selected item.
- [metric] Players may struggle to compare items with more than about 7 to 10 distinct numeric values. When: Designing item stat displays. Why: Human comparison of many numbers at once is limited.
- [tradeoff] Numeric values and bars show the clock to players, while status lines such as Hungry hide it and often surprise new players. When: Choosing how hunger is shown in the interface. Why: Visible numbers reveal time pressure; status words conceal it until a problem appears.
- [tradeoff] Cooldowns push players toward other abilities, which requires UI such as cooldown timers and fast access to alternatives. When: Adding cooldowns to abilities. Why: Players must see when abilities are unavailable and switch to alternatives quickly.
- [pitfall] Players may dislike micromanaging food and worrying about small wasted moves. When: Designing food and hunger for ongoing play. Why: Constant small food decisions feel tedious.
- [fact] Players can carry at most three items; to pick up a fourth, one carried item must first be used.
