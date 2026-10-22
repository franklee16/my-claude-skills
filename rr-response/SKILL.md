---
name: rr-response
description: Draft journal revise-and-resubmit (R&R) response letters to referees and editors in Weikai Li's evidence-based voice — strategy triage, move selection, and verbatim phrase banks distilled from his 8 real referee-report/response-letter pairs. Use this skill whenever the user mentions a referee report, reviewer comments, R&R, revise and resubmit, a journal decision letter, responding to referees/reviewers/the editor, a response letter (drafting, revising, or polishing one), 回复审稿人, 审稿意见, or 审稿人回复 — in any research project folder, at any revision round, including deciding HOW to respond (triage, concessions, tough calls) before any drafting. This skill owns the letter layer; generic revision tracking belongs to other skills, but the response letter itself always comes from here.
---

# R&R Response Letters

This skill drafts referee-response letters from two evidence-based guides distilled from Weikai Li's 8 real R&R pairs (one a documented failure — its failure modes are load-bearing lessons). The guides carry all the knowledge; this file carries only the workflow and the rules:

- `references/strategy.md` — the **decision layer**: triage passes, move-selection decision tree, 11 tough-comment protocols, evidence placement, concession economy, red lines, failure taxonomy.
- `references/style.md` — the **execution layer**: letter skeleton, voice, comment taxonomy, verbatim phrase banks, formatting conventions.

Masters live in `C:\Users\frank\Dropbox\Frank-OS\Input\R&R Sample\` (each reference copy carries a `SOURCE` header with the master's md5). The strategy guide also exists as a byte-identical mirror at `Frank-OS/Style/response_letter_style.md`; the R&R Sample copies are canonical.

## Loading discipline (why this file contains no letter phrasings)

Decision-logic errors surface at the plan gate, where Frank catches them. Style errors are silent: a phrase invented from generic memory reads fine and quietly corrupts the voice. So this file deliberately contains **zero example phrasings and zero protocol sequences**. If you catch yourself drafting letter text from memory of this file, stop and open the guides.

1. **Phase 1 start**: read `references/strategy.md` IN FULL before coding any comment. (~430 lines, one Read call.)
2. **Phase 3 start**: read `references/style.md` IN FULL before writing any letter text. Re-read if the session has compacted since the last read.
3. **Per-sentence provenance**: before writing any concession, pushback, hatch, or ritual sentence, locate the matching bank entry (style §5 or §6) and copy the template, adapting only the bracketed substance. Tag each borrowed sentence with a sidecar comment naming the bank location — `<!-- SRC: style §5.1 -->` in Markdown, `% SRC: style §5.1` in LaTeX — never in the visible letter body.
4. **Gap rule**: if no template exists for a needed move, STOP and report the gap to Frank. Never invent a phrasing; never attribute one to his prior letters. (Folder hard rule: every quote in the guides is verifiable.)
5. **Protocol anatomy**: protocols are executed by their ordered sequences in strategy §4, not from summary memory. The index below tells you WHICH protocol; open its §4.x and follow the numbered steps.

## Workflow

### Phase 0 — Intake & extraction

Collect (ask for what's missing):

- Referee report(s) — PDF, DOCX, TXT, or pasted text
- **The editor/decision letter** — the acceptance condition usually lives here, not in the referee reports
- Revised manuscript, change log, or `/revise` tracker — whatever records what has actually been done
- For round ≥ 2: prior-round letters and reports

Run `scripts/extract_comments.py <report> --output comments_extracted.md` (pymupdf for PDF; nested numbering preserved; stable IDs like R1-C3). Scanned/image PDFs → stop and use the `smart-ocr` skill first.

**Verbatim gate**: show Frank the extracted comment inventory for confirmation against the source before triage. The letter's italic blocks will be copied from this artifact, never re-extracted — extraction errors caught here stay out of the letter.

**Sync check**: if the masters exist on this machine, compare their md5 against the `SOURCE` headers in `references/`. On divergence, tell Frank and offer to refresh the copies before proceeding.

**Round ≥ 2 extras**: mark each comment new vs re-raised; diff the prior letter's hatches and promises against current actions — an unfulfilled "we would be pleased to…" from round 1 is a round-2 liability.

### Phase 1 — Triage

After the full strategy read (§2): run the six reading passes — find the acceptance condition (print it at the top of the plan); code every comment threat × type; read permissive language as a cost signal; read enthusiasm as the amplification invitation list; map cascade risk; inventory what the referee values that the paper can deliver. Add the §7.2 arbitrage scan (which single new construction pays multiple comment debts) and, for multi-referee, the conflict map.

**Escalation semantics**: DISAGREE is the *output* of the strategy guide's hard gates ("would this response require saying the referee is wrong?"), consistent with the global revision protocol. Escalate those to Frank before drafting. Guard both directions: never skip the gate, and never classify everything DISAGREE to dodge work.

### Phase 2 — Response plan (a decision forum, not a rubber stamp)

Write `response_plan.md` (persists across sessions — drafting often happens later). One unified row per comment so Frank never sees three inconsistent classifications:

| ID | Comment (short) | Threat×Type | Global class | Style bucket | Move / Protocol | Evidence needed | Change status | Placement | Hatch |
|----|-----------------|-------------|--------------|-------------|-----------------|-----------------|---------------|-----------|-------|

- *Global class* = the revision-protocol taxonomy (NEW ANALYSIS / CLARIFICATION / DISAGREE / MINOR); *style bucket* = style guide §4 (a)–(h).
- *Change status* reconciled against the tracker/changelog — **the letter may claim only changes marked Completed**; In-Progress items get placeholders.
- Order: escalations first, then MAJORs — each with the recommended move **and a runner-up with the trade-off** — then MINORs as one batch block.
- The summary-of-major-changes block is ordered to mirror the acceptance condition.

Frank redlines moves, adds evidence, resolves trade-offs. Do not draft until he approves the plan (or tells you to proceed on your recommendation).

### Phase 3 — Draft as a set

After the full style read:

1. Shared evidence ledger + summary-of-major-changes block — drafted once, quoted identically across letters (P7 pattern).
2. Per-referee letters, in the referee's own ordering and numbering. Stricter-referee placement rule resolves placement conflicts.
3. Editor letter last — mirrors the decision letter point-for-point; the arbitration sentence appears identically in every letter.

**Default format: Markdown.** Referee comments as `> *…*` blockquote-italics (verbatim from `comments_extracted.md`, original numbering preserved); pasted revised prose as nested blockquotes; R-tables as Markdown tables at the end. Convert to LaTeX (`assets/letter_template.tex`) or DOCX at finalize on request.

**Provenance hard rules** — the top runtime failure mode is hallucinated pointers and numbers, because the model usually lacks the revised manuscript:

- A Section/page/table pointer may be written only if it appears in an input artifact. Otherwise: `[Section ?, p. ? — CONFIRM]`.
- Every coefficient/t-stat must come from an input artifact. Pending results: `[t-stat TBD]`. Never estimate, never round-trip from memory.
- The letter is not send-ready until unresolved placeholders = 0 (the leftover-"page XX" anti-pattern).
- R-tables carry full captions, notes, and t-stats per style §7.5.

### Phase 4 — Audit & critique

1. `scripts/letter_audit.py <letter.md> --comments comments_extracted.md` — mechanical pass (forbidden phrases, evaluative-discounting patterns, placeholder count, verbatim-diff of comment blocks, gratitude/pointer presence, hatch heuristic, `[P#]` leakage). Fix every finding.
2. **Two context-isolated critics** spawned from `assets/critic_brief.md` (global rule: high-stakes outbound output gets independent reviewers, never self-review): Critic A — compliance/verbatim/phrase-provenance; Critic B — strategy/red-lines/move-quality and round-2 escalation risk. They receive the letter + criteria, never your drafting rationale. They produce scored reports; you implement fixes; they do not rewrite.
3. Cross-letter consistency: no contradictions, identical arbitration sentences, consistent old→new mappings.
4. Zero-placeholder check; LaTeX compile check only if converting to `.tex` (MiKTeX gotcha: any file-entry in PATH breaks it).
5. Frank's final confirmation. **Never send anything** — the letter leaves the machine only by Frank's hand.

## Protocol index

Route by what the referee essentially says; execute by opening the §4.x sequence:

| The referee essentially says… | Protocol | Where |
|---|---|---|
| "Your variable proxies for my variable" | Grant-the-Threat | strategy §4.1 |
| "This pattern in your tables undermines your story" | Forensic Artifact-Hunt | strategy §4.2 |
| "Your result contradicts Published Paper X" | Replication Grid | strategy §4.3 |
| "Your dependent variable / core measure is the wrong one" | Grant-the-Principle | strategy §4.4 |
| Factual premise wrong (sign/direction) | Agree-Then-Correct | strategy §4.5 |
| "Own it: your effects are small" | Own-the-Smallness | strategy §4.6 |
| Indefensible claim, test worth keeping | Claim-Withdrawal | strategy §4.7 |
| Prior contradicts a result; no test can help | Ambiguity | strategy §4.8 |
| Requested fix is data-infeasible | Feasibility Substitution | strategy §4.9 |
| Section cannot survive the referee's framework | Concede-and-Cut | strategy §4.10 |
| Referee proposes a channel / "necessary condition" | Conjecture Promotion | strategy §4.11 |
| "If your mechanism were real, this result should not exist" | Conjecture Promotion + magnitudes | §4.11 + §4.6 |
| Mechanically cheap ask (typo, citation, wording) | Full-concede + act | decision tree Q2 |
| Feasible and cheap relative to threat | Exceed the ask | decision tree Q4 |

Anything not in the table: work strategy §3's decision tree (Q1–Q6) in order.

## Hard rules

**Red lines** (strategy §8 — each violated in the failed letter, none in any successful one):

1. Never say or imply the referee is wrong — including *evaluatively discounting* the referee's priorities ("not an important concern", "does not add much value").
2. Never run-then-refuse — execute the referee's analysis, then decline the incorporation.
3. Never cut the referee's *requested evidence* — cut only your own indefensible claims, with the evidentiary admission stated.
4. Never leave a direct question unanswered — every direct question gets a sentence.
5. Never scope-declare the acceptance condition ("beyond the scope of this paper").
6. Never decline without an escape hatch on every kept-preference decision.

**Vocabulary precedence**: the style guide's attested vocabulary ("robust", "does not materially affect", "may not be necessarily inconsistent", …) wins over the global anti-slop deletion lists for this artifact — it is human-attested voice, not AI slop. Anti-slop applies to everything the guides do not cover.

**Ownership boundary**: manuscript-revision tracking belongs to the `revise` skill / tracker; this skill reads the tracker for change status and writes only letter artifacts.

**Failure taxonomy**: before finalizing, check the draft against strategy §9's nine failure modes — volume where insight was demanded, run-then-refuse, cutting requested evidence, scope-declining, missing hatches, placement inverted by threat, unanswered questions, evaluative discounting, circular contribution claims.

## File layout per project

```text
<project>/response/round_N/
├── comments_extracted.md      # verbatim-confirmed comment inventory (Phase 0)
├── response_plan.md           # approved plan (Phase 2)
├── referee_<id>/letter.md     # one letter per referee (Phase 3)
├── editor_letter.md           # drafted last
└── audit/                     # letter_audit output + critic reports
```
