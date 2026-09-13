# paper-to-social

A Claude Code skill for turning an academic paper into platform-native social media posts for public engagement. Produces LinkedIn, X/Twitter, 小红书, and Substack content — each calibrated to its platform's tone, length, and conventions.

Tuned for empirical social science (economics, finance, marketing, accounting, management, public policy).

## What it does

Reads an academic manuscript (`.docx`, `.tex`, `.pdf`, `.md`) and produces a `posts/` folder with one file per platform:

| Platform | File | Length | Voice |
|----------|------|--------|-------|
| **LinkedIn** | `posts/linkedin.md` | 200–400 words | Professional first-person research. Hook → numbered findings → causal note → practitioner takeaway. 3–5 hashtags. |
| **X / Twitter** | `posts/x.md` | Single tweet (~280 chars) or 4–5 tweet thread | Terse, contrarian. Single tweet = headline + causal beat + paper credit. Thread = hook → magnitude → heterogeneity → causality → bottom line. No hashtags. |
| **小红书** | `posts/xiaohongshu.md` | 400–600 字 Chinese | Professional academic Chinese (not lifestyle-influencer voice). Section dividers (📌), numbered findings (①②③), 6–8 hashtags. |
| **Substack** | `posts/substack.md` | 800–1,500 words (sweet spot ~1,100) | Long-form narrative essay. Walks reader through puzzle → data → finding → heterogeneity → causality → meaning. |

The skill also writes a `posts/README.md` index summarizing platforms, length, tone, co-author list, and any caveat the user should remember when posting.

## Quick Start

```
"Turn this paper into social posts for all four platforms."
"Write a LinkedIn post and a 小红书 post for my working paper."
"Turn this manuscript into an X thread."
```

The skill accepts:

- `.docx` — parsed via Python zipfile + XML (footnotes are in `word/footnotes.xml`, not `document.xml`)
- `.tex` — read directly
- `.pdf` — via `pymupdf` (`fitz`)
- `.md` — read directly

## The 6-Step Workflow

| Step | Action | Output |
|------|--------|--------|
| 1 | Read the paper and extract text | `paper_text.md` |
| 2 | Verify metadata — affiliations and publication status (do **not** skip) | Verified author affiliations + status label (working paper / under review / forthcoming / accepted / published) |
| 3 | Extract the six research-story elements (puzzle, data, headline, identification, heterogeneity, implication) | Internal extraction |
| 4 | Confirm which platforms to draft for | Platform list |
| 5 | Draft one post per platform using platform-specific conventions | One file per platform in `posts/` |
| 6 | Quality check + save | `posts/` folder + `posts/README.md` index |

## Why each platform gets its own voice

The single biggest failure mode is producing four versions of the same post in the same voice. Each audience reads with a different posture:

- **LinkedIn** readers scan for professional signal. They want the takeaway, evidence, and business implication, fast. Hashtags and structure help them triage.
- **X** readers are doomscrolling. You have one sentence to earn the next one. Terse, contrarian, no friction.
- **小红书** readers are in discovery mode, but academic-account followers expect substance, not lifestyle performance. The platform's visual-card structure still applies; the voice stays professional.
- **Substack** readers have opted into long-form. They want the story, reasoning, and meaning. They will read 1,200 words if you earn them.

## Anti-overclaim checklist (run before reporting done)

- [ ] Effect sizes match the paper exactly (no rounding up, no direction reversal)
- [ ] Author affiliations verified from paper footnotes, not memory or funding lines
- [ ] Publication status verified from cover letter / metadata / user statement — never inferred
- [ ] No causal language ("causes", "proves", "drives") unless the identification strategy supports it — otherwise use "plausibly causal", "associated with", or "correlated with"
- [ ] No AI-slop phrases (no "leverage", "robust", "delve", "navigate the complexities", "tapestry", "intricate", "pivotal", "crucial", "underscores", rule-of-three for emphasis, em-dash piles)
- [ ] SSRN / DOI / arXiv link included if the user provided one
- [ ] 小红书 post in professional-academic Chinese (no lifestyle-influencer markers like 姐妹们/家人们/巨/超/真的)
- [ ] X post has no hashtags (or at most one); LinkedIn has 3–5

## Metadata verification (the most common mistakes)

Two mistakes account for almost all of the embarrassing drafts. Verify both before posting:

**Author affiliations.** Extract from the title-page footnote. Do NOT infer from funding acknowledgments — a "financial support from X University" line is about a grant, not employment. If a prior draft sourced affiliations from memory or funding lines, treat it as a bug.

**Publication status.** Check the draft date, any cover letters in the same folder, and what the user has said. Map to the public-facing label:

| Evidence | Label |
|----------|-------|
| No journal involvement | "working paper" |
| Review/R&R underway | omit journal, or "under review" if user confirms |
| Editor signals acceptance path | "forthcoming at [Journal]" |
| Formal acceptance letter | "accepted at [Journal]" |
| Published online | "[Journal] (year)" |

When unsure, ask the user. Never infer "forthcoming" from R&R status alone unless cover-letter language supports it.

## File Structure

```
paper-to-social/
├── SKILL.md                              # Main skill definition (6-step workflow + per-platform conventions)
├── README.md                             # This file
└── references/
    └── example-posts.md                  # Four annotated real posts (one per platform) with design rationale
```

## Bundled Reference

`references/example-posts.md` contains four annotated real posts (one per platform) generated from a finance paper on ESG and consumer behavior. Read it when calibrating tone, length, or structural moves for a specific platform. Each annotation explains what makes the post match its platform's register.

## Installation

Copy or symlink the `paper-to-social/` directory into your Claude Code skills folder:

```bash
# Option 1: Copy directly
cp -r paper-to-social/ ~/.claude/skills/

# Option 2: Symlink (if managing skills from a central repo)
ln -s /path/to/paper-to-social ~/.claude/skills/paper-to-social
```

## Requirements

- **Claude Code** with skill support
- For `.docx` parsing (optional): Python 3.8+ with standard library only (zipfile + xml.etree)
- For `.pdf` parsing (optional): `pymupdf` (`pip install pymupdf`)
- A Markdown viewer / editor for the generated posts

## License

MIT
