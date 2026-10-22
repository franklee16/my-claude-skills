#!/usr/bin/env python3
"""Mechanical audit of an R&R response letter (Markdown primary; basic checks on .tex).

Checks (severity in brackets):
  forbidden phrases [FAIL]      — direct-negation family, style §6 forbidden list
  evaluative discounting [FAIL] — "not an important concern" family, strategy §8/§9
  scope-declaration [REVIEW]    — "beyond the scope" (intent needs human/critic judgment)
  placeholders [FAIL in --send-mode] — [CONFIRM] [TBD] "page XX" TODO FIXME
  [P#] tag leakage [FAIL]       — source-pair tags must not appear in the letter
  verbatim comment diff [REVIEW]— blockquote-italic comment blocks vs comments_extracted.md
  gratitude opener [REVIEW]     — per response block
  pointer presence [REVIEW]     — per response block (Section/Table/footnote/page/...)
  escape-hatch heuristic [REVIEW] — decline-looking blocks without a hatch phrase

Exit code 1 if any FAIL-severity check trips (or placeholders in --send-mode).
Full detail as JSON via --json <path>.

Usage:
    python letter_audit.py letter.md --comments comments_extracted.md
    python letter_audit.py letter.md --send-mode
"""
import io
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

FORBIDDEN = [
    r"respectfully\s+disagree",
    r"with\s+all\s+due\s+respect",
    r"\byou\s+are\s+wrong\b",
    r"\b(the\s+)?referee\s+is\s+mistaken\b",
    r"\bthe\s+reviewer\s+is\s+(wrong|mistaken)\b",
]
DISCOUNT = [
    r"not\s+(?:be\s+)?an?\s+important\s+concern",
    r"does\s+not\s+add\s+much\s+value",
    r"not\s+(?:particularly\s+)?important\s+for\s+our\s+(?:story|paper)",
    r"less\s+relevant\s+for\s+our\s+(?:story|paper)",
]
SCOPE = [r"beyond\s+the\s+scope", r"outside\s+the\s+scope\s+of\s+(?:this|our)\s+paper"]
PLACEHOLDER = [
    r"\[[^\]]*(?:CONFIRM|TBD)[^\]]*\]",
    r"\bpage\s+XX\b", r"\bp\.?\s*XX\b",
    r"\bTODO\b", r"\bFIXME\b",
    r"\[Section\s*\?", r"\[Table\s*\?",
]
PTAG = re.compile(r"\[\s*P\d(?:\s*/\s*P\d)?\s*\]")
GRATITUDE = re.compile(
    r"thank\s+you|we\s+thank|we\s+are\s+(?:sincerely\s+)?grateful|we\s+(?:very\s+much\s+)?appreciate|"
    r"your\s+comments\s+are\s+much\s+appreciated|excellent\s+suggestion|really\s+good\s+comment", re.I)
POINTER = re.compile(
    r"\bSection\b|\bTable\b|\bFigure\b|\bfootnote\b|\bFootnote\b|\bAppendix\b|"
    r"\bpage\s+\d|\bpp\.\s*\d|\bp\.\s*\d|\bEqn\b|\bEquation\b|\bcolumn\s*\(", re.I)
HATCH = re.compile(
    r"if\s+you\s+prefer|we\s+would\s+be\s+(?:pleased|happy)|we\s+are\s+happy\s+to|"
    r"depending\s+on\s+the\s+(?:editorial|editor)'s|at\s+your\s+(?:discretion|preference)|"
    r"should\s+you\s+prefer", re.I)
DECLINE = re.compile(
    r"we\s+(?:have\s+)?(?:chose|chosen|decided|decide)\s+not\s+to|we\s+do\s+not\s+(?:report|include|adopt|follow)|"
    r"we\s+prefer\s+to\s+keep|we\s+include\s+this\s+(?:table|figure)\s+to\s+the|we\s+keep\s+the|"
    r"we\s+retain\s+the", re.I)


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[*_`>#]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def parse_letter_blocks(letter: str):
    """Split into comment blocks (blockquote-italic) and response blocks (prose between)."""
    lines = letter.splitlines()
    blocks, current_comment, current_response = [], [], []
    in_comment = False
    for line in lines:
        stripped = line.strip()
        is_q = stripped.startswith(">")
        looks_comment = is_q and bool(re.match(r"^>\s*[*_]", stripped))
        if looks_comment:
            if current_response:
                blocks.append(("response", "\n".join(current_response)))
                current_response = []
            in_comment = True
            current_comment.append(stripped)
        elif is_q and in_comment:
            current_comment.append(stripped)  # continuation line of the comment block
        else:
            if in_comment and current_comment:
                blocks.append(("comment", "\n".join(current_comment)))
                current_comment, in_comment = [], False
            if stripped:
                current_response.append(stripped)
    if current_comment:
        blocks.append(("comment", "\n".join(current_comment)))
    if current_response:
        blocks.append(("response", "\n".join(current_response)))
    return blocks


def main():
    args = sys.argv[1:]
    send_mode = "--send-mode" in args
    comments_path = None
    json_path = None
    pos = []
    i = 0
    while i < len(args):
        if args[i] == "--comments" and i + 1 < len(args):
            comments_path = args[i + 1]; i += 2
        elif args[i] == "--json" and i + 1 < len(args):
            json_path = args[i + 1]; i += 2
        elif args[i] == "--send-mode":
            i += 1
        else:
            pos.append(args[i]); i += 1
    if not pos:
        sys.exit(__doc__)
    letter = Path(pos[0]).read_text(encoding="utf-8", errors="replace")

    findings = []  # {check, severity, status, detail}

    def add(check, severity, ok, detail=""):
        findings.append({"check": check, "severity": severity,
                         "status": "pass" if ok else "fail", "detail": detail})

    # 1. forbidden / discounting / scope
    for name, pats, sev in (("forbidden phrases", FORBIDDEN, "FAIL"),
                            ("evaluative discounting", DISCOUNT, "FAIL"),
                            ("scope-declaration", SCOPE, "REVIEW")):
        hits = [f"L{n+1}: …{line.strip()[:90]}…" for n, line in enumerate(letter.splitlines())
                for p in pats if re.search(p, line, re.I)]
        add(name, sev, not hits, "; ".join(hits) if hits else "")

    # 2. placeholders
    ph = [m.group(0) for p in PLACEHOLDER for m in re.finditer(p, letter)]
    add("placeholders", "FAIL" if send_mode else "REVIEW", not ph,
        f"{len(ph)} unresolved: {ph[:8]}" if ph else "")

    # 3. [P#] leakage
    pt = PTAG.findall(letter)
    add("[P#] tag leakage", "FAIL", not pt, str(pt[:8]) if pt else "")

    blocks = parse_letter_blocks(letter)
    comments = [b for t, b in blocks if t == "comment"]
    # Only prose that FOLLOWS a comment block is a per-comment response; the preamble
    # before the first comment is the opening framing, not a response block.
    responses, seen_comment = [], False
    for t, b in blocks:
        if t == "comment":
            seen_comment = True
        elif seen_comment:
            responses.append(b)

    # 4. verbatim diff vs comments_extracted.md
    if comments_path and Path(comments_path).exists() and pos[0].endswith(".md"):
        src = Path(comments_path).read_text(encoding="utf-8", errors="replace")
        src_items = [normalize(m) for m in
                     re.findall(r"###\s+R\d+-C\d+[^\n]*\n\n(.*?)(?=\n###\s+R\d+-C\d+|\Z)", src, re.S)
                     if not normalize(m).startswith("[")]
        mismatches = []
        for idx, c in enumerate(comments):
            cn = normalize(re.sub(r"^>\s*|\[\d+[\.\d]*[a-z]?\]", "", c))
            best = max((1 - _dist_ratio(cn, s) for s in src_items), default=0.0)
            if best < 0.98:
                mismatches.append(f"comment block {idx+1}: best similarity {best:.3f}")
        add("verbatim comment diff", "REVIEW", not mismatches,
            "; ".join(mismatches) if mismatches else f"{len(comments)} blocks matched (>=0.98)")
    else:
        add("verbatim comment diff", "REVIEW", True,
            "skipped (.tex letter or no comments_extracted.md provided)")

    # 5. per-response-block rituals
    no_grat = [i + 1 for i, r in enumerate(responses) if not GRATITUDE.search(r)]
    add("gratitude opener per response", "REVIEW", not no_grat,
        f"missing in response blocks {no_grat}" if no_grat else f"{len(responses)} blocks OK")
    no_ptr = [i + 1 for i, r in enumerate(responses) if not POINTER.search(r)]
    add("pointer per response", "REVIEW", not no_ptr,
        f"missing in response blocks {no_ptr}" if no_ptr else f"{len(responses)} blocks OK")
    no_hatch = [i + 1 for i, r in enumerate(responses)
                if DECLINE.search(r) and not HATCH.search(r)]
    add("escape-hatch heuristic", "REVIEW", not no_hatch,
        f"decline-without-hatch in response blocks {no_hatch}" if no_hatch
        else f"no unmatched declines among {len(responses)} blocks")

    hard = [f for f in findings if f["status"] == "fail" and f["severity"] == "FAIL"]
    soft = [f for f in findings if f["status"] == "fail" and f["severity"] == "REVIEW"]
    print(f"Letter: {pos[0]}  ({len(comments)} comment blocks, {len(responses)} response blocks)")
    for f in findings:
        mark = "PASS" if f["status"] == "pass" else ("FAIL" if f["severity"] == "FAIL" else "REVIEW")
        print(f"  [{mark:6}] {f['check']}" + (f" — {f['detail']}" if f["detail"] else ""))
    print(f"\n{len(hard)} FAIL, {len(soft)} REVIEW-needed")
    if json_path:
        Path(json_path).write_text(json.dumps(findings, indent=2), encoding="utf-8")
    sys.exit(1 if hard else 0)


def _dist_ratio(a: str, b: str) -> float:
    """Cheap similarity: 1 - levenshtein/maxlen (fine for short comment blocks)."""
    if a == b:
        return 0.0
    la, lb = len(a), len(b)
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        for j in range(1, lb + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))
        prev = cur
    return prev[lb] / max(la, lb)


if __name__ == "__main__":
    main()
