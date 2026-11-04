#!/usr/bin/env python3
"""Search the game-development knowledge atoms (kb/*/atoms.jsonl): BM25, Python standard library only.

Usage:
    python find.py "what happens to an economy without sinks"           (8-40 atoms, sized by relevance)
    python find.py --domain balance-economy "positive feedback loop"
    python find.py --top 10 "guide the player without signs"            (fixed count)
    python find.py "что будет с экономикой без стоков"                  (Russian query, English atoms)

A short atom shares few words with a question, so AtomIndex also scores it by its topic and, strongest, by
its best group (all atoms sharing a group id). A Russian query is mapped to English index
terms through kb/*/lexicon_ru.json; results stay English.
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

    def rank(self, query, top=None, rel=CUT_REL):
        """Return [(score, atom index)], best first, atoms with no matching word left out. top=None sizes the
        result by relevance: atoms scoring >= rel x the best score, clamped to [CUT_MIN, CUT_MAX]."""
        s_a = _norm_max(bm25_scores(query, self.docs))
        s_t = _norm_max(bm25_scores(query, self.topics))
        s_s = _norm_max(bm25_scores(query, self.sections))
        sc = [(s_a[i] + TOPIC_W * s_t[self.topic_of[i]]) / (1 + TOPIC_W) + SEC_W * max((s_s[j] for j in g), default=0)
              for i, g in enumerate(self.secs_of)]
        order = sorted(range(len(sc)), key=lambda i: -sc[i])
        best = max(range(len(s_s)), key=s_s.__getitem__, default=None)
        head = []
        if best is not None and s_s[best] > 0:  # the best group's own atoms first
            head = sorted(self.members[best], key=lambda i: -sc[i])[:SEC_TAKE]
            taken = set(head)
            order = head + [i for i in order if i not in taken]
        if top is None:  # the whole head (cutting it loses the group's context), then the rest above rel x peak
            peak = max(sc, default=0)
            rest = sum(1 for i in order[len(head):] if peak > 0 and sc[i] >= rel * peak)
            top = min(CUT_MAX, max(CUT_MIN, len(head) + rest))
        return [(sc[i], i) for i in order[:top] if sc[i] > 0]


def search_atoms(query, domain, top=None):
    atoms = [json.loads(l) for f in sorted(KB.glob("*/atoms.jsonl")) for l in f.open(encoding="utf-8")]
    atoms = [a for a in atoms if not domain or a["domain"] == domain]
    if not atoms:
        return []
    idx = AtomIndex(atoms)
    return [(s, atoms[i]) for s, i in idx.rank(query, top)]


def main():
    ap = argparse.ArgumentParser(description="Search the knowledge atoms; English or Russian query, English results.")
    ap.add_argument("query")
    ap.add_argument("--top", type=int, help="fixed number of atoms (default: 8-40, sized by relevance)")
    ap.add_argument("--domain", help="one domain, e.g. balance-economy")
    a = ap.parse_args()
    if a.top is not None and a.top < 1:
        ap.error("--top must be at least 1")
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")  # stderr names Russian words
    unknown = []
    query_terms(a.query, unknown)
    if unknown:
        print(f"not in the Russian lexicon, ignored: {' '.join(unknown)}", file=sys.stderr)
    hits = search_atoms(a.query, a.domain, a.top)
    if not hits:
        print(f"no matching atoms (domain={a.domain or 'any'}; atom files: kb/*/atoms.jsonl)", file=sys.stderr)
    for s, at in hits:
        agree = f" (x{at['support']})" if at["support"] > 1 else ""
        print(f"{s:5.2f}  {at['domain']}/{at['topic']}{agree}  {atom_line(at)}")


if __name__ == "__main__":
    main()
