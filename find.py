#!/usr/bin/env python3
"""Search the game-development knowledge atoms (kb/*/atoms.jsonl): BM25, Python standard library only.

Usage:
    python find.py "what happens to an economy without sinks"           (8-40 atoms, sized by relevance)
    python find.py --domain balance-economy "positive feedback loop"
    python find.py --top 10 "guide the player without signs"            (fixed count)
    python find.py "что будет с экономикой без стоков"                  (Russian query, English atoms)
    python find.py --game roguelike "pacing between fights"             (ranked for one kind of game)
    python find.py --cards "retained changes between visits"            (concept cards in cards/)
    python find.py --worlds "a city that hides from what it fears"      (world records in worlds/)

A short atom shares few words with a question, so AtomIndex also scores it by its topic and, strongest, by
its best group (all atoms sharing a group id). A Russian query is mapped to English index
terms through kb/*/lexicon_ru.json; results stay English.

--game <name|path> applies a game profile (kb/profiles/<name>.json) to the atom ranking: each atom's fit record
(kb/<set>/fit.jsonl) says which genres, cameras, player counts and structures it is about, and atoms made for
other kinds of games sink (see fit_multiplier). Result lines show the fit tag of every atom.
"""
import json
import argparse, math, re, sys
from collections import Counter
from pathlib import Path

STOP = set("a an the of to in and or for on with is are be it this that how do i my can what why when which does by as at from into vs".split())
K1, B = 1.2, 0.75
TOPIC_W = 0.5  # weight of the atom's topic score
SEC_W = 1.0  # weight of the best group score
SEC_TAKE = 12  # atoms of the best-matching group placed first in the result
CUT_REL, CUT_MIN, CUT_MAX = 0.75, 8, 40  # default result: the best group's head, then every atom scoring >=
# CUT_REL x the best score, CUT_MIN-CUT_MAX atoms, so a narrow question gets a short answer and a broad one a long one
KB = Path(__file__).resolve().parent / "kb"
CARDS = Path(__file__).resolve().parent / "cards"
WORLDS = Path(__file__).resolve().parent / "worlds"
PAGE_TOP = 8  # default number of card or world-record hits
FIT_FLOOR = 0.25  # score multiplier of an atom that fits nothing in the profile (it sinks, it is not deleted)
FIT_UNIVERSAL = 2 / 3  # fit of a statement that holds across genres: below a genre-core match (1.0), above weak ones
AXIS_MISS = 0.4  # fit factor per axis (camera, players, structure) the atom depends on and the profile excludes
HEAD_MIN_MULT = 0.5  # with a profile, best-group atoms below this multiplier do not take the leading slots
FIT_AXES = {"genres": {"action", "rpg", "crawler", "roguelike", "platformer", "shooter", "strategy", "puzzle", "horror",
                       "adventure", "sim", "mmo", "casual", "sports", "tabletop"},
            "cam": {"fp", "tp", "topdown", "side2d", "text"}, "pl": {"solo", "coop", "pvp", "massive"},
            "st": {"run", "persistent", "levels", "match", "story"}}


def tok(text):
    out = []
    for w in re.findall(r"[a-z0-9]+", text.lower()):
        if w in STOP:
            continue
        for suf in ("ing", "ies", "es", "ed", "s"):
            if len(w) > 4 and w.endswith(suf):
                w = w[: -len(suf)]
                break
        out.append(w)
    return out


# Russian queries: each Cyrillic word is stemmed and replaced by the English index terms the lexicon maps it to
# (kb/*/lexicon_ru.json). Documents stay English; only the query changes.
RU_STOP = set("и в во на не ни с со к ко по о об от до из за для при без над под про у а но или ли же бы то это этот эта эти "
              "как что чтобы где когда почему зачем какой какая какие каких который которая которые чем кто чей "
              "мне меня мой моя мои я ты вы мы он она они его ее их свой своя свои есть быть был была были "
              "так также тоже уже еще очень можно нужно надо ли если будет будут буду бывает нет них ним ней "
              "может могут мог могли например каков какова каковы каково которое которого которой которому которым "
              "которых".split())
_RU = {}


def ru_stem(word):
    if "stem" not in _RU:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from vendor.snowball import RussianStemmer
        _RU["stem"] = RussianStemmer().stemWord
    return _RU["stem"](word.replace("ё", "е"))


def ru_lexicon():
    if "lex" not in _RU:
        files = sorted(KB.glob("*/lexicon_ru.json"))
        if not files:
            raise FileNotFoundError(f"Russian query, but no lexicon in {KB}/*/lexicon_ru.json")
        lex = {}
        for f in files:
            for s, terms in json.loads(f.read_text(encoding="utf-8")).items():
                lex.setdefault(s, set()).update(terms)
        _RU["lex"] = lex
    return _RU["lex"]


def ru_terms(word):
    """English index terms of one Russian word. Snowball stems one lemma inconsistently across its forms
    (память -> памя, памяти -> памят), so a stem missing from the lexicon takes the nearest lexicon stems that
    extend or shorten it by at most 2 letters, and a compound (геймдизайнер) the union of two known stems."""
    lex, s = ru_lexicon(), ru_stem(word)
    if s in lex:
        return lex[s]
    if len(s) >= 4:
        for d in (1, 2):
            near = [k for k in (s[:-d],) if len(k) >= 4 and k in lex]
            near += [k for k in lex if len(k) == len(s) + d and k.startswith(s)]
            if near:
                return set().union(*(lex[k] for k in near))
        for i in range(4, len(s) - 3):
            if s[:i] in lex and s[i:] in lex:
                return lex[s[:i]] | lex[s[i:]]
    return set()


def repair_mojibake(text):
    """Undo UTF-8 text that reached argv decoded as cp1251 ('что' -> 'С‡С‚Рѕ'), as a Windows shell layer running
    under the ANSI code page delivers it. Real Cyrillic encoded as cp1251 is not valid UTF-8, so it never changes;
    ASCII is identical either way."""
    try:
        fixed = text.encode("cp1251").decode("utf-8")
    except UnicodeError:
        return text
    if fixed != text:
        print(f"query repaired from cp1251-decoded UTF-8: {fixed}", file=sys.stderr)
    return fixed


def query_terms(query, unknown=None):
    """Index term groups of a query: an English word is a group of one term (tok), a Russian word the group of
    its English translations (stem + lexicon). BM25 treats a group as one synonym term (summed tf, df of the
    union), so a word with many translations weighs like one word. Russian words the lexicon does not know are
    appended to `unknown` (when given) and match nothing, like an unknown English word."""
    q = query.lower()
    groups = [(t,) for t in tok(q)]
    for w in re.findall(r"[а-яё]+", q):
        if len(w) < 2 or w in RU_STOP:
            continue
        mapped = ru_terms(w)
        if mapped:
            groups.append(tuple(sorted(mapped)))
        elif unknown is not None:
            unknown.append(w)
    return list(dict.fromkeys(groups))  # unique groups, first-seen order


def bm25_scores(query, docs):
    """BM25 of every doc. A query term group (query_terms) scores as one term: tf summed over its terms, df the
    number of docs holding any of them; a one-term group is plain BM25."""
    if not docs:
        return []
    n = len(docs); avg = sum(d["len"] for d in docs) / n
    groups = query_terms(query)
    tfs = [[sum(d["tf"].get(t, 0) for t in g) for g in groups] for d in docs]
    df = [sum(1 for row in tfs if row[k]) for k in range(len(groups))]
    idf = [math.log(1 + (n - x + 0.5) / (x + 0.5)) for x in df]
    out = []
    for d, row in zip(docs, tfs):
        norm = K1 * (1 - B + B * d["len"] / avg)
        out.append(sum(idf[k] * f * (K1 + 1) / (f + norm) for k, f in enumerate(row) if f))
    return out


def atom_line(a):
    s = f"[{a['type']}] {a['text']}"
    if a["when"]:
        s += f" When: {a['when']}"
    if a["why"]:
        s += f" Why: {a['why']}"
    return s


def _norm_max(xs):
    m = max(xs, default=0) or 1
    return [x / m for x in xs]


class AtomIndex:
    """Ranks atoms by their own structure only, BM25 throughout, no embeddings:

    score = (atom BM25 + TOPIC_W * topic BM25) / (1 + TOPIC_W) + SEC_W * best group BM25

    each normalized to the best hit. A group is every atom sharing one id in its "group" field (atoms that
    belong together), so an atom inherits the context its siblings give. The best group's top SEC_TAKE
    atoms lead the result (top-k by score alone let atoms of similar groups push half of it out), the rest
    follows by score.
    """

    def __init__(self, atoms):
        self.atoms = atoms
        self.docs = [{"tf": Counter(t), "len": len(t)} for t in (tok(atom_line(a) + " " + a["topic"]) for a in atoms)]
        keys = sorted({(a["domain"], a["topic"]) for a in atoms})
        kidx = {k: i for i, k in enumerate(keys)}
        self.topic_of = [kidx[(a["domain"], a["topic"])] for a in atoms]
        secs = sorted({s for a in atoms for s in a["group"]})
        sidx = {s: i for i, s in enumerate(secs)}
        self.secs_of = [[sidx[s] for s in a["group"]] for a in atoms]
        self.topics = self._groups([[t] for t in self.topic_of], len(keys))
        self.sections = self._groups(self.secs_of, len(secs))
        self.members = [[] for _ in secs]
        for i, g in enumerate(self.secs_of):
            for j in g:
                self.members[j].append(i)

    def _groups(self, member_of, n):
        tf = [Counter() for _ in range(n)]
        for d, gs in zip(self.docs, member_of):
            for g in gs:
                tf[g].update(d["tf"])
        return [{"tf": c, "len": sum(c.values())} for c in tf]

    def rank(self, query, top=None, rel=CUT_REL, mult=None):
        """Return [(score, atom index)], best first, atoms with no matching word left out. top=None sizes the
        result by relevance: atoms scoring >= rel x the best score, clamped to [CUT_MIN, CUT_MAX].
        mult: per-atom game-fit multipliers (fit_multiplier). They scale the scores; the leading group is the one
        whose relevance times its atoms' mean fit is highest, and only its atoms fitting at HEAD_MIN_MULT or more lead."""
        s_a = _norm_max(bm25_scores(query, self.docs))
        s_t = _norm_max(bm25_scores(query, self.topics))
        s_s = _norm_max(bm25_scores(query, self.sections))
        sc = [(s_a[i] + TOPIC_W * s_t[self.topic_of[i]]) / (1 + TOPIC_W) + SEC_W * max((s_s[j] for j in g), default=0)
              for i, g in enumerate(self.secs_of)]
        if mult is not None:
            sc = [x * m for x, m in zip(sc, mult)]
            s_s = [s * sum(mult[i] for i in mem) / len(mem) if mem else 0 for s, mem in zip(s_s, self.members)]
        order = sorted(range(len(sc)), key=lambda i: -sc[i])
        best = max(range(len(s_s)), key=s_s.__getitem__, default=None)
        head = []
        if best is not None and s_s[best] > 0:  # the best group's own atoms first
            lead = [i for i in self.members[best] if mult is None or mult[i] >= HEAD_MIN_MULT]
            head = sorted(lead, key=lambda i: -sc[i])[:SEC_TAKE]
            taken = set(head)
            order = head + [i for i in order if i not in taken]
        if top is None:  # the whole head (cutting it loses the group's context), then the rest above rel x peak
            peak = max(sc, default=0)
            rest = sum(1 for i in order[len(head):] if peak > 0 and sc[i] >= rel * peak)
            top = min(CUT_MAX, max(CUT_MIN, len(head) + rest))
        return [(sc[i], i) for i in order[:top] if sc[i] > 0]


def load_profile(game):
    p = Path(game) if game.endswith(".json") else KB / "profiles" / f"{game}.json"
    if not p.exists():
        sys.exit(f"no game profile {p} (profiles: {', '.join(x.stem for x in (KB / 'profiles').glob('*.json'))})")
    prof = json.loads(p.read_text(encoding="utf-8"))
    for axis, allowed in FIT_AXES.items():  # a misspelt value would silently fit nothing
        bad = set(prof.get(axis) or ()) - allowed
        if bad:
            sys.exit(f"{p}: unknown {axis} values {sorted(bad)}; allowed: {sorted(allowed)}")
    if not prof.get("genres"):
        sys.exit(f"{p}: profile needs genres")
    return prof


def load_fit():
    return {o["id"]: o for f in sorted(KB.glob("*/fit.jsonl")) for o in map(json.loads, f.open(encoding="utf-8"))}


def fit_multiplier(fit, prof):
    """Score multiplier in [FIT_FLOOR, 1]. Genre fit = best product of atom weight and profile weight (both 0-3) / 9;
    a universal atom fits at least FIT_UNIVERSAL; each context axis the atom depends on with no value in common with
    the profile multiplies the fit by AXIS_MISS."""
    g = max((w * prof["genres"].get(k, 0) for k, w in fit["g"].items()), default=0) / 9
    f = max(FIT_UNIVERSAL, g) if fit["u"] else g
    for axis in ("cam", "pl", "st"):
        if fit[axis] and prof.get(axis) and not set(fit[axis]) & set(prof[axis]):
            f *= AXIS_MISS
    return FIT_FLOOR + (1 - FIT_FLOOR) * f


def fit_tag(fit, prof=None):
    if fit is None:
        return ""
    g = ", ".join(f"{k} {w}" for k, w in sorted(fit["g"].items(), key=lambda kv: -kv[1]))
    ctx = " ".join(fit["cam"] + fit["pl"] + fit["st"])
    body = "; ".join(x for x in (("universal" if fit["u"] else ""), g, ctx) if x)
    if prof is not None and fit_multiplier(fit, prof) < HEAD_MIN_MULT:
        return f"[off-profile: {body}] "
    return f"[fit: {body}] "


def search_atoms(query, domain, top=None, prof=None):
    """[(score, atom, fit record or None)]. With a game profile, every atom needs a fit record."""
    atoms = [json.loads(l) for f in sorted(KB.glob("*/atoms.jsonl")) for l in f.open(encoding="utf-8")]
    atoms = [a for a in atoms if not domain or a["domain"] == domain]
    if not atoms:
        return []
    fits = load_fit()
    mult = None
    if prof:
        missing = sum(a["id"] not in fits for a in atoms)
        if missing:
            sys.exit(f"{missing} atoms have no fit record (kb/<set>/fit.jsonl)")
        mult = [fit_multiplier(fits[a["id"]], prof) for a in atoms]
    idx = AtomIndex(atoms)
    return [(s, atoms[i], fits.get(atoms[i]["id"])) for s, i in idx.rank(query, top, mult=mult)]


MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def card_units(root):
    """One unit per concept card (a `## K..` section): its claim, fields and edges, links reduced to their text."""
    units = []
    for p in sorted(root.glob("*.md")):
        title = p.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ").strip()
        for m in re.finditer(r"^## (K\d+-\d+)\n(.*?)(?=^## |\Z)", p.read_text(encoding="utf-8"), re.M | re.S):
            body = " ".join(l.strip() for l in MD_LINK.sub(r"\1", m.group(2)).splitlines() if l.strip())
            units.append({"label": f"cards/{p.name}#{m.group(1).lower()}", "head": title, "text": body})
    return units


def world_units(root):
    """One unit per table row or paragraph of a world record, labelled with the record and its section."""
    units = []
    for p in sorted(root.glob("*.md")):
        if p.name == "README.md":
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        title, section, para = lines[0].lstrip("# ").strip(), "", []

        def flush():
            if para:
                units.append({"label": f"worlds/{p.name} § {section}", "head": title, "text": " ".join(para)})
                para.clear()
        for i, l in enumerate(lines[1:], 1):
            s = l.strip()
            if s.startswith("## "):
                flush(); section = s[3:]
            elif s.startswith("|"):
                flush()
                nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
                if set(s) <= set("|-: ") or re.match(r"^\|[-: |]+\|$", nxt):  # separator or header row
                    continue
                units.append({"label": f"worlds/{p.name} § {section}", "head": title,
                              "text": " — ".join(c.strip() for c in s.strip("|").split("|") if c.strip())})
            elif not s:
                flush()
            elif section:
                para.append(MD_LINK.sub(r"\1", s))
        flush()
    return units


def search_pages(query, units, top):
    docs = [{"tf": Counter(t), "len": len(t)} for t in (tok(u["head"] + " " + u["text"]) for u in units)]
    sc = bm25_scores(query, docs)
    order = sorted((i for i in range(len(sc)) if sc[i] > 0), key=lambda i: -sc[i])
    return [(sc[i], units[i]) for i in order[:top]]


def main():
    ap = argparse.ArgumentParser(description="Search the knowledge atoms; English or Russian query, English results.")
    ap.add_argument("query")
    ap.add_argument("--top", type=int, help="fixed number of atoms (default: 8-40, sized by relevance)")
    ap.add_argument("--domain", help="one domain, e.g. balance-economy")
    ap.add_argument("--game", help="game profile name in kb/profiles/ (e.g. roguelike) or a profile .json path")
    where = ap.add_mutually_exclusive_group()
    where.add_argument("--cards", action="store_true", help="search the concept cards in cards/ instead of the atoms")
    where.add_argument("--worlds", action="store_true", help="search the world records in worlds/ instead of the atoms")
    a = ap.parse_args()
    if a.top is not None and a.top < 1:
        ap.error("--top must be at least 1")
    if (a.cards or a.worlds) and (a.domain or a.game):
        ap.error("--domain and --game apply to atoms, not to --cards or --worlds")
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")  # stderr names Russian words
    a.query = repair_mojibake(a.query)
    prof = load_profile(a.game) if a.game else None
    unknown = []
    query_terms(a.query, unknown)
    if unknown:
        print(f"not in the Russian lexicon, ignored: {' '.join(unknown)}", file=sys.stderr)
    if a.cards or a.worlds:
        root = CARDS if a.cards else WORLDS
        hits = search_pages(a.query, card_units(root) if a.cards else world_units(root), a.top or PAGE_TOP)
        if not hits:
            print(f"no matching entries in {root.name}/", file=sys.stderr)
        for s, u in hits:
            print(f"{s:5.2f}  {u['label']}  [{u['head']}]  {u['text']}")
        return
    hits = search_atoms(a.query, a.domain, a.top, prof)
    if not hits:
        print(f"no matching atoms (domain={a.domain or 'any'}; atom files: kb/*/atoms.jsonl)", file=sys.stderr)
    for s, at, fit in hits:
        agree = f" (x{at['support']})" if at["support"] > 1 else ""
        print(f"{s:5.2f}  {at['domain']}/{at['topic']}{agree}  {fit_tag(fit, prof)}{atom_line(at)}")


if __name__ == "__main__":
    main()
