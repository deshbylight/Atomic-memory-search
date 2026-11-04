#!/usr/bin/env python3
"""Connect AtomKB to a project: add a short AtomKB block to the project's agent instruction files.

Usage: python connect.py <project-dir> [--dry-run]

Never replaces a project's own text. The block is appended to the project's AGENTS.md and CLAUDE.md that
already exist; a later run changes only the text between the block's own markers (for example after AtomKB
was moved). With neither file present it creates AGENTS.md with the block and CLAUDE.md importing it. A
CLAUDE.md that already imports AGENTS.md (a line "@AGENTS.md") gets no second copy. A file that is not
UTF-8 or has a broken block is left untouched. To disconnect, delete the lines from
"<!-- AtomKB:begin -->" to "<!-- AtomKB:end -->".
"""
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BEGIN, END = "<!-- AtomKB:begin -->", "<!-- AtomKB:end -->"


def block(nl):
    r = ROOT.as_posix()
    return nl.join([
        BEGIN,
        "## Game-development knowledge (AtomKB)",
        "",
        "For game design, balance, AI, level, narrative, audio, UX or game-programming questions run",
        f'`python "{r}/find.py" "<question>"` (English or Russian query; English results, 8-40 atoms) and',
        f"answer from the returned atoms, naming their topics. Rules: `{r}/AGENTS.md`. Never read files in",
        f"`{r}/kb/` whole.",
        END])


def plan_for(project):
    agents, claude = project / "AGENTS.md", project / "CLAUDE.md"
    if not agents.exists() and not claude.exists():
        return [(agents, "create", block("\n") + "\n"), (claude, "create", "@AGENTS.md\n")]
    plan = []
    for f in (agents, claude):
        if not f.exists():
            continue
        try:
            text = f.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            plan.append((f, "skip: not UTF-8, add the block by hand (README)", None)); continue
        if f is claude and agents.exists() and re.search(r"^@AGENTS\.md\s*$", text, re.M):
            plan.append((f, "skip: imports AGENTS.md", None)); continue
        nl = "\r\n" if "\r\n" in text else "\n"
        i = text.find(BEGIN); j = text.find(END, i + 1) if i >= 0 else -1
        if i >= 0 and j >= 0:
            new = text[:i] + block(nl) + text[j + len(END):]
            plan.append((f, "update block", new) if new != text else (f, "unchanged", None))
        elif BEGIN in text or END in text:
            plan.append((f, "skip: broken AtomKB block (one marker), fix it by hand", None))
        else:
            lead = "" if not text else (nl if text.endswith("\n") else nl + nl)
            plan.append((f, "append block", lead + block(nl) + nl))
    if agents.exists() and not claude.exists():
        plan.append((claude, "note: Claude Code reads CLAUDE.md; add a line @AGENTS.md there if you use it", None))
    return plan


def main():
    ap = argparse.ArgumentParser(description="Add the AtomKB block to a project's AGENTS.md / CLAUDE.md.")
    ap.add_argument("project"); ap.add_argument("--dry-run", action="store_true", help="show the plan, write nothing")
    a = ap.parse_args()
    project = Path(a.project).resolve()
    if not project.is_dir():
        sys.exit(f"not a folder: {project}")
    if project == ROOT:
        sys.exit("this is the AtomKB folder itself; give the project folder")
    for f, action, data in plan_for(project):
        print(f"{action}: {f}")
        if a.dry_run or data is None:
            continue
        if action == "create":
            with f.open("x", encoding="utf-8", newline="") as out:  # "x": fails instead of overwriting
                out.write(data)
        elif action == "append block":
            with f.open("a", encoding="utf-8", newline="") as out:  # existing bytes are never rewritten
                out.write(data)
        else:  # update block: only the text between the markers differs
            f.write_bytes(data.encode("utf-8"))


if __name__ == "__main__":
    main()
