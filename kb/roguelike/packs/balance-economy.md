# balance-economy

## ability resource economy
- [model] A battery is a charge pool: each use costs charge and the pool regenerates over time, which can be per ability or shared, and can have a recharge delay.
- [model] A power plant divides a fixed output below total demand among abilities, with some abilities needing a minimum threshold; the last allocation holds until changed and the plant is never exhausted.
- [mechanism] Wands hold limited rechargeable charges, while rods draw on the user's energy or slowly absorb it from the environment, so they are usable once per period.
- [mechanism] Recoverable resources act as negative feedback that stops chains of strong abilities from running out of control.
- [mechanism] Battery resources produce bursts of activity followed by recovery, with risk during the recharge.
- [mechanism] A cheap timed buff can behave like a power plant when its effect permanently reduces the maximum resource, as with all-day spells.
- [mechanism] A charge is one blow whose multiplier rises with weapon weight, reaching x12 for the heaviest weapon, while heaviest weapons' normal blows are capped at x4. When: comparing heavy weapons for charge attacks. Why: Single heavy charge blows outweigh the normal blow multipliers of heavy weapons.
- [mechanism] Raising an ability resource's maximum capacity over time gives players a sense of progression, but if challenge does not rise at the same pace, the game becomes easier. When: A game offers no skill-based progression and capacity grows per turn or across the game. Why: Capacity gains supply power that the difficulty curve does not match, so effective difficulty falls.
- [rule] Make scarce resources limited per run, with an optional unlimited alternative available. When: Designing run-based resource systems. Why: Scarcity creates decisions, and the optional alternative keeps casual play open.
- [rule] Set starting player resources such as hit points well below what completion requires, so players learn early that they must improve. When: Tuning the starting state of a game with reset mechanisms. Why: Low starting resources warn players of danger before a premature loss.
- [heuristic] Charging is effectively compulsory for light weapons, since their extra normal blows can beat the charge bonus when not charging. When: choosing whether to charge with light weapons. Why: Multiple light blows per round can outdamage one charge hit unless charging is used.
- [heuristic] Keep the spell form of a healing effect when its mana cost creates a trade-off, even if the item form is removed. When: When one healing effect exists as both an item and a spell. Why: Mana cost keeps the spell worth choosing over the item.
- [procedure] Stop grinding for abilities by giving each progression tier its own acquisition resource, capping abilities learned per tier, and making old currency worthless in new regions. Why: An uncapped ability-buying resource lets players grind low-risk areas for abilities instead of gaining skill.
- [metric] Maximum charge divided by cost gives the number of uses in a row, and the regeneration rate sets the time between uses. When: battery resource design.
- [tradeoff] Higher-tier spells cost more mana and have a higher chance of failing to cast, trading raw power against reliability.
- [tradeoff] Tiers can trade time against another resource, such as efficiency.
- [tradeoff] Capping a summoner's maximum mana prevents repeated cast-and-rest abuse but needs extra data structures and removes a resource spellcasters depend on. When: Player summoning can be spammed by casting, resting and casting again. Why: A mana cap is costly to implement and penalises spellcasters, so a timer may be the better limit.
- [pitfall] Unlimited resets or unlimited inventory let players save resources indefinitely, which slows progress. When: Players can keep unused consumables or resets with no cap. Why: Hoarded resources are never spent, so the game stalls.
- [fact] Increasing mana availability and separating mana gain from spells learned made a caster start easier in a variant game. When: easing a caster's early game. Why: More early resources and decoupled progression reduce the early difficulty spike.

## experience and leveling
- [mechanism] A steep power curve makes endgame characters far stronger than starters, while a shallow curve keeps them close in strength to the starting character.
- [mechanism] Experience thresholds set how fast a run's power rises, shaping how deep a player should go for a given strength. When: Designing how quickly characters grow across a run. Why: Thresholds control the pace at which players gain strength.
- [mechanism] Grind occurs when small gains at low difficulty add up to large improvements; it is a major problem with currency and can affect achievements requiring many small actions.
- [behavior] Grinding is separated from exploitation when exploitable resources are limited and permadeath keeps a non-zero risk during the grind. When: Designing reward loops where players can repeat safe actions. Why: Limited resources stop infinite farming, and permadeath keeps even repeated play carrying real risk.
- [rule] Level-wide monster interactions must be balanced and tested, because they can break a level. When: Adding monster-to-monster effects.
- [rule] Abilities introduced early must stay relevant later, or their difficulty level becomes mismatched.
- [rule] Review any change to a capacity ramp's slope carefully, because it shifts how fast the game's difficulty changes relative to player power. When: Adjusting how quickly ability capacity increases. Why: Capacity and challenge are coupled, so altering one slope alters overall difficulty.
- [heuristic] When skill checks remain, compare them directly with character level rather than with level multiplied by class progression.
- [heuristic] Buy armour class early against repeated paralysing enemies instead of running around corners, since early defence avoids repeated paralysis. When: When early enemies repeatedly paralyse the player in a roguelike. Why: Defence reduces how often the lock triggers.
- [procedure] 1) Set the starting gap between level 1 and 2 to 100 points. 2) For each next level, set the gap to the previous gap times one plus the factor raised to the level number. 3) Sum gaps to get total experience per level. When: Tuning a level progression curve. Why: A factor below one flattens later gaps, so each level costs less extra growth.
- [metric] The default experience factor is 0.95, and it controls how quickly the level curve flattens. When: Tuning experience progression. Why: A smaller factor flattens the curve faster.
- [tradeoff] Spellcasters are weak early but can outgrow melee classes when played well, rewarding mastery; if they start too weak and grow too slowly, players get frustrated early. Why: Delayed payoff rewards investment, but early weakness without visible progress drives players away.
- [tradeoff] Grinding can outpace the difficulty curve and flatten the skill requirement; making one of the two increases explicitly time-dependent stops long grinding from defeating the curve. When: Resource or capacity growth is available through repetitive play. Why: Time-independent gains let players accumulate progress without meeting the rising challenge.
- [pitfall] Assuming abilities or skills are equally useful is a fallacy: transferable points make players favour the strongest, so weigh one point's value against another's. When: designing skill systems with multiple skills. Why: A well-designed game usually makes one ability more useful at any moment; unequal skill costs make equal point spending produce unequal value.
- [pitfall] Grinding early wastes time that could be spent at the best reward-to-risk point later in the run. When: Planning how long players should farm before pushing deeper. Why: Early farming yields little compared with later high-reward encounters.
- [pitfall] Late-game difficulty spikes, unfair timing demands and re-fights of earlier bosses drive players away.
- [pitfall] Trivial early challenges can make a game feel pointless, causing players to lose interest quickly.

## crowd control and disables
- [definition] Juggling restricts an ability by a non-time criterion, such as the number of instances already in play or a regeneration condition that is not time based. When: Limiting repeated use of an ability.
- [mechanism] Higher-level characters or strong monsters may attack several times per round. Why: Extra attacks scale damage output with power.
- [mechanism] Stun applies a slight penalty that grows incrementally until the character is knocked out, reaching the same end result as paralysis.
- [mechanism] Abilities that move, disable or interrupt an opponent can be chained so the target never recovers, and batteries or power plants cannot stop this, because charge regenerates during recovery time. When: Designing abilities that disable opponents. Why: Regenerating resources refill during the recovery time, so resource limits alone do not prevent chaining.
- [mechanism] Limiting the number of projectiles in play lets players reach closer targets sooner than distant ones, because a hit frees a slot for the next shot. When: A projectile count is capped in play. Why: Projectiles return to the pool on hit, so close targets are reached faster.
- [mechanism] Explicit timers, such as a food counter or a chasing ghost, push players onward instead of letting them linger. When: Designing runs where players might stall to farm or explore. Why: A pressing countdown makes waiting costly, so players keep moving.
- [mechanism] A summoner waits a short cooldown before summoning again, while summoned creatures face a longer cooldown before they may summon. When: Summoners and their summons can create other summons. Why: Staggered timers stop summon chains from building up faster than the player can respond.
- [rule] Add warning states such as slow before paralysis, and a cooldown before sleep takes hold, so the player can react before a total loss. When: designing disabling effects.
- [rule] Give opponents a counter to each disabling ability; if that is too hard, put a cooldown on the ability or on a combination that would form a trap. When: Designing disable or interrupt abilities. Why: Counters preserve player agency; cooldowns are the fallback when counters are hard to design.
- [rule] Cure effects should each target a clearly distinct status, such as paralysis, confusion, cuts, stun or poison, so that every cure answers a different need. When: When designing status cures for a roguelike. Why: Distinct cures avoid overlap and keep each one useful.
- [rule] Every trap or lock should cause damage or advance progress, otherwise play becomes an inescapable loop. Why: Locks that neither hurt nor progress leave the player stuck.
- [rule] When a player-controlled summon dies, charge the player a debt equal to the monster's power level, paid from mana first and then from hit points. When: Player summons die and the design needs a real penalty for losing them. Why: Making the loss cost a resource gives players a reason to protect their minions.
- [metric] The time to achieve a status lock should be roughly equal to the time needed to kill the target. When: balancing a status-lock strategy against damage. Why: Matched times make both routes comparably viable.
- [tradeoff] Juggling is less intuitive than a cooldown, so use it only when a time-based limit would cause problems, such as allowing an extra action mid-air. When: Choosing a repeat-use limit. Why: Players must manage a non-obvious limit, which costs clarity.
- [tradeoff] A common cooldown across attacks prevents switching between them, but it may break suspension of disbelief.
- [pitfall] A disabling effect that also lets the attacker escape dominates play against worthwhile targets unless it is weakened.

## damage formulas and notation
- [mechanism] When each higher spell tier has a steeper damage-per-level slope than the one below, total damage per round approximates exponential growth as the player levels.
- [mechanism] Random damage between 1 and a percentage of player health creates a richer risk curve than fixed damage. When: Designing damage ranges. Why: Random rolls spread the chance of death across several hits.
- [rule] Tune numbers and drop tables through data edits; deeper logic needs code, since data files are not a full scripting language. When: Modding a data-driven game. Why: Data files hold values, not behaviour, so logic changes require code.
- [heuristic] Balancing the attack and defense rating formulas is the hardest part of simple combat; start simple and expand gradually. Why: Unscaled ratings produce unintended hit rates.
- [procedure] Hit chance can be always hit, a random value below ATK over max ATK, ATK greater than DEF with optional randomness, or a random value below ATK over (ATK plus DEF). When: Choosing a hit model using only ATK and DEF. Why: Each option produces different balance outcomes.
- [procedure] Damage can be constant 1 HP, equal to ATK (optionally randomized), ATK minus DEF, ATK divided by DEF, the attacker's HP, or an outright kill when the margin exceeds defender HP. When: Choosing a damage model using only ATK, DEF and HP. Why: Each option produces different balance outcomes.
- [metric] Spell damage can be a constant plus a scalar times caster level, or dice form XdY plus Z, where XdY means X dice with Y sides. Why: Scaling with caster level lets one spell definition grow in power; dice notation expresses variable damage compactly.
- [metric] In one example, attack rating equals strength divided by 4 plus class and level modifier plus equipment bonus; defense rating equals dexterity times 4 plus class and level modifier plus equipment bonus. Why: Concrete formulas show how stats map to ratings, though they need scaling.
- [metric] Damage per second (DPS) is average damage over a long period, and similar threats should have similar DPS. When: balancing attacks assuming infinite range, perfect accuracy and instant hits.
- [metric] Two close-range rocket or grenade hits kill the player class, and a critical rocket does 270 damage while a critical grenade does 280 to 300. Why: Reference values for judging survivability thresholds.
- [pitfall] Listed spell damage can far understate real damage when shapes hit many targets; poison touch can double damage over time, and an area aura can multiply damage when surrounded.
- [pitfall] Pure ATK-over-DEF damage can let a 3/3 character beat 5/1 or 1/5 opponents, so balance must be checked. When: Using ratio-based damage. Why: Ratios produce counterintuitive matchups.
- [pitfall] The relative strength of attack shapes is often only revealed by extensive playtesting and statistical analysis.
- [pitfall] Combining damage sources, such as direct hits and damage over time, or grouping damage by class instead of weapon, hides causes and produces misleading rankings.
- [pitfall] Stacking resistances before deciding what damage numbers mean produces results that cannot be sensibly interpreted. When: designing damage and resistance values. Why: The stacking formula depends on whether damage scales as a fraction of a threshold or as a raw quantity.
- [fact] A fixed-damage attack kills with 0% or 100% chance, which gives a dull risk curve.

## buffs and power balance
- [model] Run progress can be plotted as accumulated power P against rising risk R over time. Exploitation occurs when P exceeds R; evasion occurs when R exceeds P. When: Roguelike-style runs where threat rises with depth. Why: Comparing power to risk tells the player when to fight for rewards and when to avoid danger.
- [mechanism] A stat used in more combined formulas dominates outcomes; if hit and damage both use ATK, ATK dominates. When: Combining stats in hit and damage formulas. Why: Repeated use multiplies a stat's influence.
- [mechanism] Arbitrary build penalties such as slower skill growth, weapon restrictions, heavy armour limits or required spell components frustrate players later in the game, so temporary buffs or modifiers can offset them. When: a restrictive class or respec system is designed. Why: Offsets keep restrictive builds enjoyable without removing their constraints.
- [mechanism] Unlimited ability choice lets players exploit an opponent's weakness, which makes weaknesses less meaningful; restricting choice to balanced loadouts keeps weaknesses meaningful. When: designing a build or ability loadout system. Why: Free choice lets players always pick the counter, so weaknesses stop mattering.
- [rule] Replace repeated buff recasting with a permanent buff that carries a meaningful cost, such as reduced maximum mana, to turn a chore into a decision.
- [rule] Improve the unfavoured option rather than nerfing the favoured one.
- [heuristic] A critical bonus to attack or defense should last only the next turn to avoid stacking problems. When: Granting temporary combat bonuses from criticals. Why: Longer bonuses stack in unwanted ways.
- [heuristic] Asymmetric rock-paper-scissors with unequal payoffs can create a meaningful prediction game. When: designing one-on-one choice mechanics. Why: Unequal payoffs make each option's outcome differ, so the opponent's expected move matters.
- [heuristic] Balancing effort should prioritise making each option's usefulness noticeable, since validity matters more to design than competitive strength alone. When: when deciding where to spend balancing effort, especially for casual or mixed-skill players. Why: players judge choices by evidence of worth, which competitive numbers do not show.
- [procedure] 1) Pick the strongest option as the benchmark. 2) Raise the weaker options toward it. 3) Stop before they overshoot the benchmark. When: tuning a set of competing choices.
- [tradeoff] Adding a variable such as DEX lets heavier gear trade hit chance against damage or defense. When: Designing gear differences. Why: An extra stat creates a meaningful choice between accuracy and power.
- [tradeoff] Casters trade melee effectiveness, movement effectiveness and hit points for a larger set of choices, so each turn carries more risk. When: comparing caster and warrior designs. Why: A wide option set is paid for with fragility, so one wrong choice can end the run.
- [tradeoff] Raising size above strength slows the character, so size and strength must be balanced against each other. When: A character's size stat is raised above its strength stat. Why: Size gains in hit points and charge damage come at the cost of agility.
- [pitfall] Overpowered buffs and build modifiers unbalance builds, letting one class outperform another in an unintended role; they need careful balancing. When: tuning temporary buffs or build modifiers. Why: Excess power breaks intended trade-offs; a modifier fixing one weakness may make the build better than its intended counterpart.
- [pitfall] A high-level character fighting low-level enemies takes no risk, which removes the fun; danger, not raw numbers, should stay constant.

## critical hits and bursts
- [mechanism] In roguelikes, hit points set a hard survival margin, so recognising lethal danger matters more than knowing the rules: a character survives damage up to its hit point total and no further. When: Character survival is determined by a numeric hit point pool against incoming damage. Why: A small difference in damage relative to hit points decides life or death, so threat assessment dominates play.
- [rule] When multiple slays, brands or elemental bonuses affect one attack, apply only the highest multiplier instead of summing them. When: Computing damage from multiple slays, brands or elemental damage bonuses on one attack against a monster type. Why: Summing would make multi-brand weapons far stronger than multi-slay weapons, since resisting one element would not stop the extra damage; stacking would let a weapon dominate.
- [rule] An outright-kill damage option needs randomization, or evenly matched enemies never hurt each other. When: Using a kill-outright damage rule. Why: Deterministic kills in equal matchups stall combat.
- [rule] Balance each added critical effect, since a second critical can easily become too strong. When: Adding critical hit effects. Why: Stacked effects can outpace base combat.
- [rule] At full player health no single attack should kill; each lower health level should raise the chance of elimination.
- [rule] High-burst attacks with DPS equal to others should carry a risk, such as recovery time, short range or reduced movement while attacking.
- [heuristic] Limit criticals per attack to two, since chained critical effects can become far too strong. When: A critical can trigger another critical. Why: Uncapped chains can overpower combat.
- [procedure] 1) Compute a power level for each monster by summing its vulnerabilities. 2) Precompute values for artifacts and ego items. 3) Limit magic items to one special ability so brands are balanced against each other. When: when balancing weapon brands and special abilities. Why: prevents one brand from overshadowing the rest.
- [metric] If maximum damage equals player health divided by x (x above 1), the player cannot die before turn x; on turn x, death chance is one hundredth raised to the power x. When: Maximum damage is set as a fraction of player health. Why: The hit count needed to deplete health sets the earliest possible death turn.
- [tradeoff] Taking only the highest multiplier across items removes the reward for specialising in one element, while combining multipliers across items requires balancing around the highest multiplier times the number of slots that can contribute. When: Deciding whether damage multipliers from different equipment items should combine. Why: Non-stacking removes specialisation incentives, while stacking needs slot counts to cap its power.
- [pitfall] A random chance of being left for dead feels arbitrary when the odds are hidden, and heavy money losses turn recovery into a grind.
- [pitfall] In hit-point games, a high-burst attack can remove an enemy before it responds, so DPS alone does not balance it.
- [pitfall] If the top tier also has the highest DPS, the next tier must be much weaker to keep effective DPS balanced.
- [pitfall] When one element beats others, such as acid beating fire and cold, or fire beating slay undead, that brand overshadows the rest and makes weapon choice trivial. When: when designing elemental vulnerabilities across weapons and monsters. Why: one dominant option removes the reason to pick others.

## shop design and stock
- [model] Shops serve five functions: give money a purpose, let low-level players earn cash, supply essentials, allow enchantment upgrades, and offer a larger spend for a useful item. When: Designing or evaluating a shop system in a roguelike economy. Why: Diagnosing each function separately shows which parts of a shop system to keep.
- [mechanism] When shops appear randomly throughout the dungeon, deciding whether to spend all gold becomes tactical, since a better shop may lie deeper.
- [mechanism] Buying an identified item reveals its type, and cheap or cursed items are likely to be bought, which reveals hazards almost for free.
- [mechanism] Buying an unidentified item reveals only its base type, so the item may be excellent, mundane or worthless.
- [mechanism] Inventory and equipment limits prompt players to leave, sell and restock. When: when designing carry limits in a roguelike. Why: full inventories force trips to shops.
- [mechanism] Buying out a shop's stock triggers regeneration, and periodic refresh removes and adds items and may replace the shopkeeper. When: Designing shop inventories that change over time. Why: Refresh keeps stock varied, but essential consumables can run out until the next restock.
- [mechanism] A shopkeeper's purse drops when it buys from the player and rises when it sells, so offers shrink as the purse falls and a large purse can lead the shopkeeper to retire. When: Shops both buy and sell player items with a limited purse. Why: The purse acts as a visible profit meter that constrains how much the shop will pay.
- [mechanism] Making high-level shop stock rotate and depend mainly on Charisma reduces Charisma's direct effect on prices. When: Designing shop stock quality for a character with a Charisma stat. Why: Tying item level to a stat that rotates stock diffuses the price advantage of high Charisma.
- [rule] An infrequently chosen option can have situational strengths, but such advantages must be rare to justify its low pick rate.
- [heuristic] Keep shops whose role is supplying essential consumables, and drop shops whose only function is absorbing money. When: Deciding whether a shop belongs in the economy. Why: Consumables give shops a gameplay purpose beyond sinking currency.
- [heuristic] Make shop items about 80% as powerful as dungeon finds, chosen according to the player's current equipment. When: Tuning items sold in shops against dungeon loot. Why: Shop items that are nearly as strong as dungeon finds keep shopping worthwhile without replacing exploration.
- [tradeoff] Town-only shops return the player to town to assess loot, identify items and upgrade gear, creating stages between dungeon trips.
- [pitfall] An item that costs as much as a clearly better item is effectively useless, though low-value steps can sometimes be needed to reach higher peaks. When: Pricing items or upgrade paths. Why: Players will never choose an item that is dominated by a better one at the same cost.
- [fact] Shops can be menu-based or physically placed in the world, and shops spread through the dungeon appear randomly.

## resistance and vulnerability
- [definition] Resistance reduces damage by type, either as an explicit value per element or as an indirect matchup; a vulnerability is like fewer hit points plus implicit resistance to every other attack. When: Defining how creatures respond to elemental damage. Why: Vulnerabilities change effective survivability more than the stated hit points suggest.
- [mechanism] Taking damage during a sleep effect wakes the target, so the effect can be avoided entirely.
- [mechanism] Summing several random values, as in rolling several dice, produces a bell curve that teaches players how damage accumulates over hits. When: Designing damage rolls. Why: Summed rolls concentrate outcomes around the mean, making accumulation intuitive.
- [mechanism] Crediting burning enemies toward critical chance as soon as they are set on fire rewards the skill of applying fire, but may overstate payoff in sparse situations. Why: Crediting damage before it is dealt is a shortcut.
- [mechanism] Innate explosive resistance lets a player at high health survive one critical explosive hit that would otherwise be near-certain death.
- [mechanism] Multiplicative stacking of resistances yields lower total reduction than additive stacking, because each new resistance applies only to the damage still getting through. When: two or more resistances of the same damage type apply to one target. Why: Each resistance multiplies the unresisted fraction, so returns diminish as more are added.
- [mechanism] When casters can learn monster resistances too easily, they can counter nearly any threat, so they rarely need to flee. When: players can identify monster weaknesses and resistances freely. Why: Easy information removes the situations where the player must avoid a fight they cannot counter.
- [rule] Give enemies the same damage model as players so players can recognise the underlying behaviour. When: Designing combat damage for players and enemies. Why: Shared models let players learn the rules once.
- [rule] Balance creatures as if always hit at their weakest point, or remove vulnerabilities entirely. When: Setting creature stats with elemental weaknesses. Why: Players will exploit weaknesses, so average-case balance misjudges difficulty.
- [heuristic] Blocking suits archers, while dodging suits spellcasters. When: choosing a defensive stance for a character class. Why: Archers benefit from standing still, while casters benefit from moving to avoid area damage.
- [procedure] 1) Decide what damage numbers mean. 2) Choose additive or multiplicative stacking to match that meaning. 3) Compute combined resistance from the chosen model. When: designing how multiple resistances combine. Why: Whether a damage number represents a fraction of a threshold or a raw amount determines which stacking model makes sense.
- [metric] Under geometric progression, resistance at level n equals n divided by (n plus one): level 1 gives 50 percent, level 2 about 66 percent, level 3 75 percent. When: resistance grows with level and stacks multiplicatively. Why: Each level gives a large early benefit that tapers, while later levels still add value.
- [pitfall] Some monster effects are severe or hard to implement, such as time warp, condemn and digestion, and need careful tuning. Why: Severe effects can dominate play or break systems.

## selling and currency
- [mechanism] Allowing selling encourages players to haul loot, and offered prices are usually half the original value or less.
- [mechanism] Currency lets accumulated points transfer between any abilities, whereas item and achievement systems acquire each ability separately and non-interchangeably.
- [behavior] Expert players in some roguelikes value early gold above experience, because gold buys survival tools that make later progress possible. When: Early game resources can be spent on equipment or consumables that improve survival. Why: Survival tools compound into later progress, so early currency can matter more than raw advancement.
- [rule] Disallowing selling, with merchants refusing to buy anything, is easier to balance than allowing it.
- [rule] Scale the effect of a lost companion by its value to the player, so one that helped or is emotionally attached costs more when lost. When: Companion loss in a roguelike. Why: Attachment makes the loss matter.
- [heuristic] Death penalties that take easily regained resources such as money or experience are preferred over penalties on equipment that took effort to earn. When: Choosing what a death penalty removes. Why: Equipment penalties feel harsh because they are costly to replace.
- [tradeoff] Currency suits multiplayer games where a real economy forms, while single-player games can only simulate an economy; item or achievement acquisition better encourages trying unusual abilities. When: choosing how players acquire abilities. Why: Currency tends to encourage grinding.
- [pitfall] Enchantment alone rarely wins fights, so it works best combined with other schools.
- [pitfall] Items grind when the choice system does not limit how many of an item a player can acquire, and ammunition can unbalance a game the same way.
- [pitfall] Money stops mattering once late-game items are available, after which stock availability becomes the real limit on progress. When: Players progress far enough that they can buy the best items they need. Why: Once gold no longer limits purchases, currency loses its purpose as a progression gate.
- [pitfall] Making money useful again after it has become plentiful can unbalance the game. When: An economy where currency had stopped mattering is revived. Why: Renewed purchasing power on a large surplus of currency accelerates progress beyond intended pacing.
- [fact] Enchantment is the largest money sink in a roguelike economy but tends to break game balance. Why: Large spending on power upgrades inflates strength faster than balance can absorb.

## ammo and fuel supply
- [mechanism] Light sources must be refuelled after a set number of turns, while magical light sources last indefinitely.
- [mechanism] Limited fuel makes the player value a weapon more. When: Weapons that need fuel. Why: Scarcity raises the perceived worth of the weapon.
- [mechanism] A post-apocalyptic scarcity setting justifies rare guns and ammunition that runs out, making melee strong. When: Post-apocalyptic or low-supply settings. Why: No factories remain to supply ammunition.
- [mechanism] When levels are inexhaustible, players can regenerate levels until one has a wanted item or monster nearby. When: when levels are regenerated on demand. Why: cheap regeneration turns levels into a searchable resource.
- [mechanism] Limited fuel forces players to fetch refills from a common point, which pulls them away from the action and can turn repeated trips into tedium. When: Batteries or power plants run out and must be refuelled from a map location. Why: Refuel points are fixed, so each refill requires travel that interrupts combat.
- [rule] Keep consumables meaningful by making them scarce enough that holding them for a dangerous moment matters, since using them too freely leaves nothing when needed.
- [procedure] 1) Place refuel points on the map. 2) Let defeated enemies drop fuel. 3) Make fuel more likely to appear near enemies that were just killed, reducing repeated trips to the refuel point. When: Designing finite resources that players must restore in the world. Why: Drops close to combat shorten fetch trips while keeping resources finite and in-world.
- [tradeoff] Raising a weapon's damage while halving its ammo capacity, and doubling the effective ammo cost of each use, turns use into a real decision.
- [tradeoff] Requiring players to leave a safe position to refuel limits exploitation of map positions, but forces movement that exposes them to risk. When: Deciding whether refuelling can happen from anywhere. Why: Refuel trips counter camping but add travel and exposure.

## enemy scaling and difficulty
- [mechanism] A half-cost move that builds movement debt, shown as fatigue, accumulates on rough terrain, when encumbered or when hasted, and forces the player to rest or faint. When: when designing a faster movement option with a cost. Why: the debt limits how often the cheap move can be used.
- [rule] Set an overland quest's difficulty to the highest difficulty among the regions crossed to reach its location. When: when a quest lies across several wilderness regions. Why: the player must survive the hardest region on the route.
- [heuristic] Start with three variables for simplicity and add more only when needed. When: Designing a first combat model. Why: Fewer variables are easier to balance and test.
- [pitfall] Raising player and enemy stats together cancels progression, and stronger items plus stronger monsters alone feel repetitive, like a treadmill; harder monsters are interesting only up to a point.
- [pitfall] Changing the speed setting alters every actor's timing, so balance must be rechecked after any change. When: Offering a customizable game speed in an energy-based system. Why: Timing changes affect how often every actor acts relative to the others.
- [pitfall] Raising enemy stats alone can make harder play feel cheap; let the difficulty curve carry challenge instead.
- [pitfall] Clamping speeds into coarse classes, so that nearby speeds look identical, prevents nuanced chases.
- [pitfall] Difficulty curves can attach to classes implicitly, even when designers do not intend it. When: designing class progression and tuning. Why: Class-specific strengths and weaknesses across stages can make some classes harder by accident.
- [pitfall] Changing a short window between an action and a delayed effect, such as backstab timing before a turret activates, can shift balance between opposing roles. When: A delayed effect follows an action by a rival role. Why: Adjusting the window changes how long the opponent is vulnerable or safe.

## healing and life potions
- [rule] Each healing item should provide a distinct kind of reset so that no potion supersedes another, and weak items overlapping stronger ones should be removed. When: When a game has many healing items that overlap in function. Why: Overlapping items make the weaker ones almost never used.
- [rule] Heal effects for high-hit-point characters should be percentage-based, so they scale with the character's large hit point pool. When: When designing heals for warrior-style characters with high hit points. Why: Flat heals become trivial relative to large pools.
- [rule] Do not let ordinary healing items raise maximum hit points when used at full health, since selling maximum health feels like bad balance. When: Designing common healing items. Why: Common items that grant permanent stat gains undermine progression.
- [tradeoff] Potions that fully heal or cure all statuses can supersede other potions, so keep only one such reset-everything item. Why: Multiple full resets make the other healing items pointless.
- [tradeoff] A life potion that rerolls maximum hit points and keeps the new value only if higher trades guaranteed recovery now for a gamble on permanently higher maximum health. When: A rare, powerful healing item is used at full health. Why: The reroll can only improve the maximum, so the player takes a risk that is always upside-only.
- [pitfall] Players can grind out healing reserves before a final fight, which undermines the challenge of the ending. When: Designing RPG healing and resource systems that persist to the final fight. Why: Resources accumulated outside the fight trivialise it.
- [fact] A potion heals three life and blocks monster, spell and water damage for three turns; a mushroom heals one life on pickup and is never carried.
- [fact] A wand fires in one direction through all targets until a wall or door and is then destroyed; a staff hits every adjacent monster and is then destroyed.

## attack tiering
- [mechanism] Tiering gives only the top tier top DPS; lower tiers have lower DPS, and their quality depends on the top tier's immediate damage.

## exclusive reward satisfaction
- [heuristic] Exclusive rewards, such as a hard-to-reach island or a late-game land, give greater satisfaction.

## license alone fails to stop re-hosting
- [pitfall] A license forbidding re-hosting did not by itself stop many sites from hosting the file anyway. When: Relying on license terms to control file distribution. Why: Sites may ignore license terms, so a restriction alone does not control where the file appears.

## procedural marginal cost
- [mechanism] Once generation rules exist, each new level costs little, whereas hand-designed levels may need rework when creature movement or player assumptions change.

## unresearched tech cost
- [mechanism] Skipping a technology costs little when weaker civilisations can supply it as a trade item, reducing the penalty for not researching it. When: Trade or diplomacy allows acquiring technologies from other civilisations. Why: Obtainable substitutes remove the scarcity that would otherwise make a skipped path matter.
