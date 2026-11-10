# Agent instructions: AtomKB

AtomKB is a read-only knowledge base of game-development atoms (`kb/all/`, 20,777 short English
statements in 842 topics). Use it to answer design, balance, AI, level, narrative, audio, UX and
programming questions at the lowest token cost: search, then answer from the few atoms returned.

## Answer a question

1. Search: `python find.py "<question>"` (from another folder: `python "<path>/find.py" "<question>"`).
   The query may be English or Russian; the results are English. Output: one atom per line, best first,
   8-40 lines sized by relevance (`--top N` for a fixed count):
   `score  domain/topic (xN)  [type] text When: ... Why: ...`
2. When the domain is clear, add `--domain <domain>`: `core-design`, `process`, `player-psychology`,
   `balance-economy`, `level-design`, `narrative`, `audio`, `game-feel`, `game-ai`, `pcg`, `programming`,
   `algorithms`, `ux-ui`.
3. When the user's game is known, rank for it: `--game <profile>` (`kb/profiles/`: `roguelike`,
   `arena-shooter`, `rts`, `mobile-puzzle`, `coop-dungeon-crawler`, `idle-incremental`, or a path to the project's own profile
   JSON in the same format). Each line shows `[fit: ...]`; `[off-profile: ...]` atoms were made for other
   kinds of games: use them only with that caveat.
4. One search per question. If the result misses the point, at most two more searches with the words a
   design text would use ("money sink", not "too much gold"). A Russian word the lexicon lacks is named on
   stderr and ignored: rephrase it or use the English term.
5. Answer from the returned atoms, in the user's language, and name the topics used (`domain/topic`).
   `(xN)` means the atom was confirmed N times independently; prefer those when atoms disagree. If nothing
   relevant comes back, say the knowledge base does not cover it instead of filling the gap from memory as
   if it came from the knowledge base.
6. Need a whole topic? Read only its section of `kb/all/packs/<domain>.md`: find the line `## <topic>`
   (the topic name from the result) and read up to the next `## ` heading (median 440 words, largest
   about 5,200).
7. Concept questions (a principle with its application, limit, check and links to related principles):
   `python find.py --cards "<question>"`; follow a card's `Requires` / `Supports` / `Constrains` edges
   only when their reason applies.
8. Worldbuilding (a fictional world's layers, laws, how it is shown): `python find.py --worlds "<question>"`,
   then open only the matching record in `worlds/` if more is needed.

## Do not

- Read `kb/all/atoms.jsonl`, `kb/all/fit.jsonl`, `kb/all/lexicon_ru.json` or a whole pack: each pack is 17k-100k words.
- Edit anything in `kb/` or `cards/`: the atoms and packs are generated and maintained upstream.
- Copy AtomKB files into another project. Connect a project with `python connect.py <project-dir>`
  (it only appends a marked block to that project's `AGENTS.md` / `CLAUDE.md`, see `README.md`).
- Present an atom as a quotation: atoms are short statements, cite them by `domain/topic`.
