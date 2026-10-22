# Audit Report — Draft Response Letter to Referee 1

JFQA MS# 26-10442, "Retail Attention and the Cross-Section of Stock Returns", round 1.
Audited artifact: `letter_referee_1.md` (draft of 2026-10-21). Raw output: `audit_output.txt`; JSON: `audit_findings.json`.

## Mechanical audit (`scripts/letter_audit.py`, non-send-mode)

Command: `python scripts/letter_audit.py letter_referee_1.md --comments comments_extracted.md --json audit_findings.json`

| Check | Result |
|---|---|
| Forbidden phrases (direct-negation family) | PASS |
| Evaluative discounting | PASS |
| Scope-declaration | PASS |
| Placeholders | REVIEW — 24 unresolved, **pending-by-design** (see below) |
| [P#] tag leakage | PASS |
| Verbatim comment diff vs `comments_extracted.md` | PASS — 6 of 6 comment blocks matched (similarity ≥ 0.98) |
| Gratitude opener per response block | PASS — 6 of 6 |
| Pointer per response block | PASS — 6 of 6 |
| Escape-hatch heuristic | PASS — no decline-without-hatch |

**0 FAIL.** The 24 placeholders are the letter's honest record of unfinished work: Comment 1 analysis (premise test, double sorts, discriminator — changelog: In Progress, nothing run), Comment 1a extension (cleaning in progress), Comment 2 replication grid (Not Started), the §4.3 revised-passage paste, the referee-credit footnote number, the tradability-treatment decision, and the Wang/Zhang full references. Per the skill's provenance rules these may only be resolved from actual artifacts; the letter becomes send-ready when the count reaches zero (`response_plan.md`, send-readiness checklist). A `--send-mode` run would fail on these by design.

## Failure-taxonomy verification (strategy §9, nine modes)

1. Volume where insight was demanded — N/A yet for C1/C2 (analyses pending); C3 answers with the mechanism table and benchmarks, not volume.
2. Run-then-refuse — none: C1/C2 commit to incorporation in the manuscript alongside the analysis.
3. Cut the requested evidence — none: Comment 2 takes the reconciliation path; the remove-option is neither taken nor evaluated in print.
4. Scope-declare the acceptance condition — none (audit PASS; no "beyond the scope" anywhere).
5. Missing hatches — the one kept-preference decision (Table IA.2 placement) carries "We would be pleased to move Table IA.2 to the main paper if you prefer."
6. Placement inverted by threat — C1 evidence committed to a new main-text subsection; IA.2 keeps a main-text address (§4.3, p. 21); mirror Table R1 duplicated into the letter.
7. Unanswered direct questions — Comment 3's two direct questions each open with a direct sentence (contradiction answer; magnitude justification).
8. Evaluative discounting — none (audit PASS).
9. Circular contribution claims — none; stand-alone-content claim is deferred to the pending C1 evidence rather than asserted.

## Provenance verification

- All six italic comment blocks byte-copied from `comments_extracted.md` (audit-verified ≥ 0.98, actual source texts identical).
- Every coefficient/t-stat in the letter traces to the changelog (0.032/3.05; −0.011/−1.05; 0.44%/2.62; 0.09%/0.71; 6.8% MAD) or is attributed to the referee (40 bps, 31 bps, Table 3/Table 5 readings). The single computed quantity is 0.44/6.8 ≈ 6.5%, arithmetic on artifact numbers, shown with its inputs.
- Every manuscript pointer (p. 12; p. 3 fn. 5; §2.1 p. 8; §4.3 p. 21; Table IA.2) appears in an input artifact; unknown locations use the prescribed `[Section ?, p. ? — CONFIRM]` form.
- Every bank-borrowed sentence carries an `<!-- SRC: … -->` sidecar; no bracketed source tags (leakage check PASS).

**Known near-gap, reported per the skill's gap rule:** the phrase-banks contain no template for the *direct answer to a yes/no question* ("Doesn't this contradict our story?"). The letter's answer sentence ("To answer your question directly: no, …") is a minimal functional construction required by the never-leave-a-direct-question-unanswered red line; the load-bearing claims around it ride on attested templates (style §6.3, §6.8, §5.7). Flagged for Frank rather than silently treated as bank-sourced.

## Phase 4 critics

Context-isolated critics A and B (compliance/verbatim; strategy/red-lines) were **skipped for this test run** per the harness instruction ("Phase 4 critic subagents are NOT needed"). The mechanical audit above ran as specified. Before this letter ships, critics A/B must score it and any fix cycle complete.

## Verdict

Draft passes the mechanical gate (0 FAIL) and the failure-taxonomy review. Not send-ready: 24 placeholders pending the C1/C1a/C2 analyses and the six open decisions in `response_plan.md`. Final confirmation is Frank's; nothing is sent by the assistant.
