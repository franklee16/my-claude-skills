#!/usr/bin/env python3
"""Extract structured referee comments into a verbatim-confirmed inventory.

Input: referee report as .pdf, .docx, .txt, or .md
Output: comments_extracted.md with stable IDs (R1-C3), original numbering labels,
and nesting preserved verbatim. The letter's italic comment blocks are later copied
FROM this artifact, never re-extracted.

Usage:
    python extract_comments.py referee_report.pdf --output comments_extracted.md
    python extract_comments.py report.docx --output comments_extracted.md

PDF via pymupdf (preferred) with pdfplumber fallback; DOCX via python-docx.
Scanned/image PDFs produce garbage here — run the smart-ocr skill first.
"""
import re
import sys
import io
import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        try:
            import fitz  # pymupdf
            with fitz.open(path) as doc:
                return "\n".join(page.get_text() for page in doc)
        except ImportError:
            pass
        try:
            import pdfplumber
            with pdfplumber.open(path) as pdf:
                return "\n".join((page.extract_text() or "") for page in pdf.pages)
        except ImportError:
            sys.exit("Neither pymupdf nor pdfplumber installed — cannot read PDF. "
                     "pip install pymupdf")
    if suffix == ".docx":
        try:
            import docx
        except ImportError:
            sys.exit("python-docx not installed — cannot read DOCX. pip install python-docx")
        d = docx.Document(path)
        return "\n".join(p.text for p in d.paragraphs)
    return path.read_text(encoding="utf-8", errors="replace")


REVIEWER_HEADER = re.compile(
    r"^\s*(?:report\s+(?:from|for)|comments\s+(?:from|to|for)|response\s+to)?\s*"
    r"(referee|reviewer|report)\s*[-#]?\s*(\d+)\s*[:.)]?\s*$",
    re.IGNORECASE | re.MULTILINE)

# Sub-headers that group comments within one report (kept as context labels).
SUBHEADER = re.compile(
    r"^\s*(general\s+(?:assessment|comments?)|major\s+(?:concerns?|comments?)|"
    r"minor\s+(?:concerns?|comments?|points?|issues?)|specific\s+comments?|"
    r"summary\s+(?:of\s+)?(?:assessment|comments?))\s*[:.]?\s*$",
    re.IGNORECASE)

# Comment openers, most specific first: "2.2.1", "1a.", "3)", "1.", "-"/"*"/"•"
NESTED_NUM = re.compile(r"^\s*(\d+(?:\.\d+)+[a-z]?)[.)]?\s+")
SUBLETTER_NUM = re.compile(r"^\s*(\d+\s*[a-z])[.)]\s+")
PLAIN_NUM = re.compile(r"^\s*(\d+)[.)]\s+")
BULLET = re.compile(r"^\s*[-*•]\s+")


def split_referee_sections(text: str):
    """Yield (label, section_text). If no explicit headers, treat whole text as Referee 1."""
    matches = list(REVIEWER_HEADER.finditer(text))
    if not matches:
        yield "Referee 1", text
        return
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        label = f"{'Referee' if m.group(1).lower().startswith(('referee','report')) else 'Reviewer'} {m.group(2)}"
        yield label, text[start:end]


def split_comments(section_text: str):
    """Yield (number_label_or_None, comment_text) preserving order and nesting verbatim."""
    lines = section_text.splitlines()
    items = []  # (label, [lines])
    for line in lines:
        if not line.strip():
            if items:
                items[-1][1].append("")
            continue
        sub = SUBHEADER.match(line)
        if sub and not (PLAIN_NUM.match(line) or BULLET.match(line)):
            # Attach subheader as its own pseudo-comment so grouping survives verbatim.
            items.append((None, [f"[{sub.group(1).strip()}]", ""]))
            continue
        m = NESTED_NUM.match(line) or SUBLETTER_NUM.match(line) or PLAIN_NUM.match(line)
        if m:
            items.append((m.group(1).replace(" ", ""), [line.strip()]))
        elif BULLET.match(line):
            items.append((None, [line.strip()]))
        else:
            if items and items[-1][1] and not items[-1][1][-1] == "":
                items[-1][1].append(line.strip())
            elif items:
                items[-1][1].append(line.strip())
            elif line.strip():
                # Preamble before first numbered item — keep as context pseudo-comment.
                items.append((None, [line.strip()]))
    # Merge continuation-only fragments (< 50 chars) upward is skipped: verbatim wins over tidiness.
    for label, ls in items:
        body = "\n".join(ls).strip()
        if body:
            yield label, body


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    # Accept both `--output <path>` (as SKILL.md documents) and a bare positional path.
    out = Path("comments_extracted.md")
    positional = []
    i = 0
    while i < len(args):
        if args[i] == "--output" and i + 1 < len(args):
            out = Path(args[i + 1]); i += 2
        else:
            positional.append(args[i]); i += 1
    if not positional:
        sys.exit("Error: input file required.")
    src = Path(positional[0])

    text = extract_text(src)
    today = datetime.date.today().isoformat()
    lines = [
        "# Extracted Referee Comments",
        "",
        f"Source: `{src.name}` — extracted {today} by `extract_comments.py`",
        "",
        "<!-- VERBATIM GATE: confirm every comment below against the source document before",
        "     triage. The letter's italic blocks must be copied from this file, never",
        "     re-extracted. Extraction can mangle two-column PDFs, ligatures, and nesting. -->",
        "",
    ]
    total = 0
    for label, section in split_referee_sections(text):
        try:
            rnum = int(re.search(r"\d+", label).group(0))
        except AttributeError:
            rnum = 1
        lines += [f"## {label}", ""]
        n = 0
        for clabel, body in split_comments(section):
            n += 1
            total += 1
            tag = f" [original numbering: {clabel}]" if clabel else ""
            lines += [f"### R{rnum}-C{n}{tag}", "", body, ""]
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {total} comments for review to {out}")
    print("NEXT: show the inventory to the user for verbatim confirmation (Phase 0 gate).")


if __name__ == "__main__":
    main()
