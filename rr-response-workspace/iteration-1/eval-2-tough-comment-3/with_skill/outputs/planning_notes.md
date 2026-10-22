# Planning Notes — Response to Referee 1, Comment 3 (Institutional Ownership + Economic Magnitude)

Eval run: `eval-2-tough-comment-3` (with skill), 2026-10-21. Scope: comment 3 only.

## Skill-compliance trail

| Step | Status |
|---|---|
| Phase 1 full read of `references/strategy.md` | Done before coding any comment |
| Phase 3 full read of `references/style.md` | Done before writing letter text |
| Sync check (masters vs SOURCE headers) | PASS — strategy md5 `dd7c6d6c…` and style md5 `7bd5be7d…` both match the Dropbox masters |
| Phase 0 extraction | `extract_comments.py` run on `referee_report_R1.txt` → `comments_extracted.md` (10 items; R1-C7 = original numbering 3). Script note: its output path is a **positional** arg (argv[2]); passing `--output <path>` writes a literal `--output` file (cleaned up and re-run). SKILL.md documents the flag form — minor doc/script mismatch worth fixing upstream. |
| Verbatim gate | Auto-passed for this test (inputs pre-confirmed). Comment block in the letter copied verbatim from `comments_extracted.md` R1-C7; audit verbatim-diff similarity ≥ 0.98. |
| Phase 2 plan approval gate | Auto-passed for this test; plan row below follows the recommended move (no runner-up conflict to resolve). |
| Phase 4 critics | Skipped per test instructions; mechanical audit run instead. |

## Phase 1 — Triage

**Acceptance condition (Pass 1).** General Assessment: main concern = Comment 1 (measure validity); Comment 2 = internal tension; Comment 3 = "a subsample result that the authors need to explain," and in the comment itself "Here is what bothers me most… Please answer directly." So C3's bar is a *direct answer* plus a magnitude justification — directness is the demanded currency, not volume.

**Coding (Pass 2).** R1-C7 = **MAJOR × mechanism-question + magnitude/interpretation challenge**. Two sub-demands:
- 3a — logical trap: "If your mechanism were real, the predictability should disappear in the high-IO subsample — that is exactly what happens. Doesn't this contradict your story?"
- 3b — "31 bps is tiny; turnover wouldn't cover transaction costs. Justify the economic magnitude."

**Pass 3 (permissive language).** None — the opposite ("Please answer directly"). No licensed optimization.

**Pass 4 (enthusiasm).** "The data are unusual and interesting." More useful: the referee *supplies the channel* ("retail investors cannot move prices in stocks dominated by institutions") — free identification under Rule 7; his own logic interprets Table 5 for us.

**Pass 5 (cascade).** C3's IO heterogeneity is differential evidence relevant to C1 (attention vs. liquidity-provision): attention effects should live where retail dominates. C1's analysis is In Progress — **the letter claims nothing on this link** (see Pending).

**Pass 6 (values we can deliver).** Direct answers; his necessary condition formalized as a test; magnitude benchmarks. All three are Completed in the changelog.

**§7.2 arbitrage scan.** The Table IA.2 construction pays C3 fully and can later serve C1's response — noted for the C1 letter, not claimed here.

## Move selection (strategy §3 + protocol index)

- Q1: MAJOR → yes. Sub-type "If your mechanism were real, this result should [not] exist" → **Conjecture Promotion (§4.11) + magnitudes / Own-the-Smallness (§4.6)**.
- Hard gates: no output requires saying the referee is wrong (his reading is *confirmed*; his logic is adopted as the interpretation) → **no DISAGREE escalation**. Nothing cut; nothing run-then-refused; both direct questions get sentences.

Key strategic reading: the referee's stated logic *predicts* the Table 5 pattern, so 3a is answered by adopting his conjecture, formalizing it (Table IA.2), and conceding only the presentation debt (the old draft left the heterogeneity implicit). The mechanism survives and is strengthened. For 3b, concede the full-sample smallness in print-level language, then rebuild on two anchors the referee did not ban: (i) mechanism-consistent subsample concentration (0.44% vs 0.09%), (ii) distributional benchmark vs the sample's 6.8% mean absolute monthly return deviation (the [P7]-pattern anchor the changelog's MAD figure exists to serve).

Placement: Table IA.2 in the Internet Appendix + main-text discussion (new paragraph, end of Section 4.3, p. 21) = the §5.1 "contested-but-valuable, IA with main-text address" pattern; no incorporation demand exists for main-text placement.

## Phase 2 — Plan row

| ID | Comment (short) | Threat×Type | Global class | Style bucket | Move / Protocol | Evidence needed | Change status | Placement | Hatch |
|----|-----------------|-------------|--------------|-------------|-----------------|-----------------|---------------|-----------|-------|
| R1-C7 ("3") | High-IO subsample "contradicts story" + 31 bps tiny vs transaction costs | MAJOR × mechanism-question + magnitude | NEW ANALYSIS (completed) + CLARIFICATION | (d) concede-mechanism-and-run-with-it, then (f) pushback-with-evidence; magnitude via (c) | §4.11 Conjecture Promotion + §4.6 Own-the-Smallness; direct answer to "Doesn't this contradict your story?" | Table IA.2: interaction + subsample spreads + MAD benchmark (all in changelog) | Completed (Table IA.2; new ¶ end of Section 4.3, p. 21) | IA table + main-text address | "pleased to add net-of-cost returns analysis if you prefer" |

## Evidence ledger

From changelog (Completed) — the only numbers the letter may carry:

- Table IA.2 (Internet Appendix): ATTN × High-IO indicator, top-tercile IO, Thomson Reuters 13F.
- Baseline ATTN coefficient (full sample): 0.032 (t = 3.05).
- ATTN × High-IO interaction: −0.011 (t = −1.05, insignificant) — disclosed in the letter as imprecise (credibility purchase, §5.2).
- Low-IO subsample long-short spread: 0.44%/month (t = 2.62); high-IO: 0.09%/month (t = 0.71).
- Mean absolute deviation of monthly returns: 6.8%.
- New paragraph: end of Section 4.3, page 21.

From referee report: full-sample spread 31 bps/month (his Table 5 reading — confirmed, not disputed).

[COMPUTED] (arithmetic on artifact numbers, both stated in the letter):
- 0.44/6.8 ≈ 6.5% — the low-IO spread as a share of the mean absolute monthly deviation.
- 0.44/0.31 ≈ 1.4 — low-IO spread relative to the full-sample spread.

Not claimed anywhere (no artifact basis): turnover, transaction-cost estimates, any comment-1 (liquidity-provision) or comment-2 (Zhang) results, any manuscript footnote crediting the referee.

## Red-line / failure-taxonomy check on the draft

1. Never say/imply referee wrong — his Table 5 reading is confirmed verbatim ("you are reading Table 5 correctly"); his logic is credited ("which is the logic of your comment"; "in line with your conjecture"). PASS
2. Run-then-refuse — the test is incorporated (IA table + main-text discussion + pointers). PASS
3. Cut requested evidence — added, not cut. PASS
4. Direct questions — "Doesn't this contradict your story?" answered in the response's second sentence; "justify the economic magnitude" answered with two benchmarks; the transaction-cost sub-point engaged at principle level + hatch offer. PASS
5. Scope-declaration — none (claims framed positively as "the object our analysis is designed to measure"; nothing declined). PASS
6. Hatch — "We would be pleased to add an analysis of net-of-cost returns to the paper if you prefer." PASS
- No volume-for-insight substitution: two tight evidence paragraphs; every coefficient carries its t-stat; every magnitude carries a benchmark.

## Phase 4 — Mechanical audit (critics skipped per test instructions)

`letter_audit.py … --comments comments_extracted.md` → **0 FAIL, 0 REVIEW-needed** (forbidden phrases, evaluative discounting, scope-declaration, placeholders, [P#] leakage, verbatim diff ≥ 0.98, gratitude opener, pointer, escape-hatch heuristic all PASS).

## Pending before this block is send-ready

1. Insert the verbatim paste of the new Section 4.3 paragraph (p. 21) after the evidence paragraph — [P4]/[P6] proof-of-completion pattern; the paragraph text is not in the changelog artifact, so the letter currently points without pasting (pointers alone are licensed; the paste is the upgrade).
2. Frank to confirm the letter's characterization "we left this heterogeneity implicit in Table 5" matches how the previous draft actually read.
3. Decide whether to mirror Table IA.2 into the letter as an R-table "for the ease of your reference" (needs full table layout — std errors, N — from the manuscript; not in artifacts).
4. If the referee's round-2 follows on transaction costs, the offered net-of-cost analysis becomes a promise — schedule it before sending if Frank prefers to include it now instead.
5. Cross-letter consistency (not applicable yet): when comments 1 and 2 letters are drafted, cite the IA.2 heterogeneity as differential evidence for the attention interpretation only if the C1 analysis supports it by then.
