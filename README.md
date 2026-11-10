# AtomKB - game-development knowledge atoms

`kb/all/` holds 20,777 **knowledge atoms** in 842 topics and 13 domains: short, self-contained rules,
pitfalls, definitions, models, procedures, metrics and tradeoffs about game development. `(xN)` in the
results marks an atom confirmed N times independently.

## Quick start

Requires Python 3.8 or newer, no packages to install.

```
git clone <repository-url> AtomKB
cd AtomKB
python find.py "what happens to an economy without sinks"
python find.py "что будет с экономикой без стоков"
python find.py --domain level-design --top 10 "guide the player without signs"
python find.py --game roguelike "pacing between fights"
python find.py --cards "retained changes between visits"
python find.py --worlds "a city that hides from what it fears"
```

Output: one atom per line, best first: `score  domain/topic (xN)  [type] text When: ... Why: ...`.
A narrow question gets about 8-15 atoms, a broad one up to 40; `--top N` returns a fixed count.

Domains: `core-design`, `process`, `player-psychology`, `balance-economy`, `level-design`, `narrative`,
`audio`, `game-feel`, `game-ai`, `pcg`, `programming`, `algorithms`, `ux-ui`.

## Connect to a project

```
python <path-to-AtomKB>/connect.py <project-dir>            # add the block
python <path-to-AtomKB>/connect.py <project-dir> --dry-run  # only show what it would do
```

`connect.py` gives the project's coding agent (anything that reads `AGENTS.md`, and Claude Code through
`CLAUDE.md`) a short block with the search command and the path to this folder's `AGENTS.md`, which holds
the working rules. It never replaces a project's files or text:

- an existing `AGENTS.md` / `CLAUDE.md` gets the block appended at its end, line endings kept;
- the block sits between `<!-- AtomKB:begin -->` and `<!-- AtomKB:end -->`; a rerun (for example after
  AtomKB moved) rewrites only the text between these markers, so it never duplicates;
- a `CLAUDE.md` that already imports `@AGENTS.md` is left as is;
- a project with neither file gets a new `AGENTS.md` with the block and a `CLAUDE.md` with `@AGENTS.md`;
- a file that is not UTF-8 is skipped with a message: paste the block by hand.

To disconnect, delete the lines from `<!-- AtomKB:begin -->` to `<!-- AtomKB:end -->`. AtomKB files are
never copied into the project; the project only points here.

Without an agent, the packs can be read directly: `kb/all/packs/<domain>.md` (one `##` per topic, one
line per atom), with `kb/all/packs/index.md` as the table of contents.

## Atom format

`kb/all/atoms.jsonl`, one JSON object per line:

| Field | Meaning |
|---|---|
| `id` | stable id (`k` + hash) |
| `domain`, `topic` | one of the 13 domains; topic name inside it |
| `type` | `rule`, `heuristic`, `pitfall`, `behavior`, `mechanism`, `definition`, `model`, `procedure`, `metric`, `tradeoff` or `fact` |
| `text` | the statement, up to 30 words (procedures up to 60) |
| `when`, `why` | when it applies and why it holds; may be empty |
| `support` | how many times it was confirmed independently (`(xN)` in the results) |
| `group` | ids of the groups it belongs to: atoms that belong together share a group id |

## Fit to a game

`kb/all/fit.jsonl` records, for every atom (same `id`), which kinds of game it is about:

| Field | Meaning |
|---|---|
| `u` | 1 = holds across most genres (general design, psychology, process, programming, math) |
| `g` | genre weights 1-3 (3 = core to that genre, 2 = fits it well, 1 = usable with adaptation): `action`, `rpg`, `crawler`, `roguelike`, `platformer`, `shooter`, `strategy`, `puzzle`, `horror`, `adventure`, `sim`, `mmo`, `casual`, `idle` (incremental), `sports`, `tabletop` |
| `cam` | camera it depends on: `fp`, `tp`, `topdown`, `side2d`, `text` |
| `pl` | players: `solo`, `coop`, `pvp`, `massive` |
| `st` | structure: `run`, `persistent`, `levels`, `match`, `story` |

Every result line shows this as `[fit: ...]`. `--game <name>` ranks the atoms for one kind of game: a profile
in `kb/profiles/<name>.json` (examples: `roguelike`, `arena-shooter`, `rts`, `mobile-puzzle`,
`coop-dungeon-crawler`, `idle-incremental`) gives genre weights and the cameras, player counts and structures of that game.
An atom's score is multiplied by its fit (genre weight x profile weight, a universal atom at least 2/3,
times 0.4 per axis it depends on that the profile excludes, never below 0.25), so advice for other kinds of
games sinks instead of vanishing; it is shown as `[off-profile: ...]`. For your own game copy a profile,
edit the weights and pass its path: `--game path/to/mygame.json`.

## How search works

`find.py` is BM25 over the atoms, Python standard library only, no embeddings and no network. An atom
is scored by its own words, its topic and, strongest, by its best group (all atoms sharing a group id),
so a short atom inherits the context its siblings give. The best group's atoms come first; the rest of
the result is every atom scoring at least 0.75 of the best score, 8-40 atoms.

A Russian query is mapped word by word to English index terms: Snowball stem (`vendor/snowball/`) ->
`kb/all/lexicon_ru.json`. Each Russian word counts as one term however many translations it has, and the
results stay English. A word the lexicon lacks is named on stderr and ignored.

Measured on our question sets (share of expected facts found in the result, judged by a model): English
0.85, Russian 0.81; one search takes about 0.7 s.

## World records

`worlds/` holds 13 records of fictional worlds, each from one public-domain book read in whole: layers,
rules with their exact form, interactions, how the world is shown, and what the text leaves unresolved,
every row marked `high` (stated) or `medium` (inferred) confidence. They are reference material for
worldbuilding, not atoms. `python find.py --worlds "<question>"` returns the best-matching table rows and
paragraphs (8 by default), each with its record and section; `worlds/README.md` has one summary line per
record (about 10 KB each).

## Concept cards

`cards/` holds 358 concept cards in 16 groups (game design foundations, player psychology, actions and
combat, economy, cooperative play, spatial design, physical world and ecology, societies, narrative,
visual language, built world, environment art, characters and motion, sound and cinematics, UX, research
and production). Each card states one principle and separates it from its untested application: `Kind`,
`Apply`, `Limit` (where it stops holding), `Check` (how to reject it) and typed edges to other cards
(`Requires`, `Supports`, `Constrains`) with the reason for each; `cards/Connections.md` walks chains across
groups. `python find.py --cards "<question>"` returns whole cards (8 by default); `cards/README.md` is
the group table. Coverage is partial: the cards come from selected topics, not complete volumes.

## License

Code (`*.py`) is released under the MIT license, see `LICENSE`. The atoms in `kb/`, the cards in `cards/` and the records in `worlds/` are offered for
study and reference under the same terms, to the extent the contributors of this repository hold rights
in them. `vendor/snowball/` is the unmodified Snowball Russian stemmer (Python port), under its own
BSD-3-Clause license in `vendor/snowball/LICENSE`.
