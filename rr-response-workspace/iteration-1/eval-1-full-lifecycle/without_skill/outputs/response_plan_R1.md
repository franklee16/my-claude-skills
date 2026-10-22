# Response Plan — JFQA R&R: "Retail Attention and the Cross-Section of Stock Returns" (MS# 26-10442)

**Date:** 2026-10-21
**Prepared from:** `referee_report_R1.txt`, `editor_letter.txt`, `changelog.md`
**Companion file:** `response_letter_R1_draft.md`

---

## 1. Decision reading

- R&R with one referee. The editor states the acceptance condition explicitly: **new supportive evidence that ATTN has stand-alone predictive content beyond the liquidity-provision channel (Comment 1)**, and warns that "cosmetic changes will not be sufficient." Everything in the revision is secondary to this.
- Deadline: six months from the editor's letter. Target a complete package in ~3 months to leave room for an internal red-team pass (see §6).
- Binding constraint: per the changelog, the Comment 1 analysis is **not run** (Bloomberg data obtained, measure construction underway) and Comment 2 has **not started**. The letter therefore cites only completed items with real numbers (Comments 3, 4, 5) and carries clearly marked placeholders everywhere else. **Do not submit until the placeholder count is zero.**

## 2. Triage

| # | Threat | Type | Status | Move (protocol) | Letter treatment |
|---|--------|------|--------|-----------------|------------------|
| 1 | MAJOR — the acceptance condition | "your variable proxies for my variable" | In progress (data only) | Grant-the-Threat, staged (4.1) | Longest response; staged tests; placeholders |
| 1a | Low — permissive ("I leave this to the authors") | Robustness demand | In progress | Comply, and monetize (feeds 1 and 3) | Short |
| 2 | MAJOR — cascades to Table 3 and the portfolio section | "your result contradicts Published Paper X" | Not started | Replication Grid (4.3) | Medium; grid design + placeholders |
| 3 | MAJOR — "what bothers me most," but actually the paper's best asset | "if your mechanism were real, X should happen" + magnitude attack | **Done** (Table IA.2) | Referee-conjecture promotion (4.11) + own-the-smallness (4.6) | Longest completed response; real numbers |
| 4 | MINOR | Typo | **Done** | Full concede | One sentence |
| 5 | MINOR | Missing citations | **Done** | Full concede | Two sentences + pointers |

**Key triage insight.** Comment 3's "contradiction" is a gift. The referee's own mechanism logic — retail cannot move prices where institutions dominate — *predicts* exactly the moderation in Table 5. His conjecture supplies the moderation test the paper should have run; formalizing it (Table IA.2, already done) converts his sharpest objection into the paper's mechanism evidence. The soft spot: the interaction t-stat is −1.05 (insignificant). Disclose it in the same breath as the point estimates — he will find it — and buy power via the 2024 sample extension and a continuous-IO specification.

**Reading-pass notes.**
- *Acceptance condition* (Pass 1): Comment 1, per both the editor and the referee. The summary-of-changes block is ordered to mirror it.
- *Permissive language* (Pass 3): 1a is explicitly optional; we comply anyway because the extension adds power to the C1 comparison and the C3 interaction — one work product, three debts.
- *Cascade risk* (Pass 5): if C1 is lost, the paper is lost; if C2 is lost, Table 3 and the portfolio section are at risk. Both get protocols, not one-shot answers.

## 3. Comment-by-comment strategy

### Comment 1 — liquidity-provision channel (acceptance condition)

Grant the threat conditionally, then run it to ground in stages (the [P4] flows-defense anatomy):

1. **Premise first:** replicate Wang (2021) liquidity-provision predictability in our own sample and report its strength honestly, even if modest, before defending ATTN.
2. **Horse race:** enter the LP measure as a control in the baseline Fama-MacBeth regressions; repeat the Table 3 portfolio sorts as conditional double sorts on the LP measure.
3. **Orthogonalization:** residualize ATTN against the LP measure; re-run baseline tests on the residual.
4. **Propagation:** if ATTN survives, propagate the LP control through the paper's other tables.

**Flags to resolve before building anything:**
- **Data window check (first-principles catch):** the Bloomberg pull covers 2020–2024 only, and the original sample ends December 2022. If the original sample *starts* before 2020, the horse race cannot run on the full sample with this data. Preferred fix: extend the Bloomberg pull to the full sample start. Fallback: run the LP test on the overlapping subsample with explicit disclosure — but note this visibly weakens the answer to the editor's acceptance condition, so the data extension is strongly preferred.
- **Spec fidelity:** read Wang (2021) Table 2 in the actual paper; do not implement the referee's paraphrase. Same for Zhang (2022) under Comment 2.
- **Exit conditions:** if ATTN survives with the LP control, promote the conclusion to the main text (new subsection in Section 4) and report the grid in Table R1 to the response. **If ATTN is subsumed, stop and escalate to Frank before any letter language is finalized** — the "not subsumed" concluding sentence must not exist until the numbers do.

### Comment 1a — sample extension (permissive; comply anyway)

Extend through December 2024 (data pulled, cleaning underway). Monetized three ways: new attention episodes (its stated purpose), power for the C1 LP comparison, and power for the C3 interaction. Retain original-sample results in the Internet Appendix for continuity.

### Comment 2 — reconciliation with Zhang (2022)

- The referee offers an ultimatum: reconcile, or remove the portfolio-sorting section. **Removing the section is the documented failure move** (it cuts exactly the evidence the referee asked to see reconciled, converting a results question into a trust question). The strategy is reconciliation by replication grid; removal is not offered and not mentioned in the letter.
- Grid axes: (1) Zhang's measure and full specification in our sample; (2) Zhang's measure with our filters/horizon; (3) ATTN with Zhang's filters/horizon; (4) equal- vs value-weighted portfolios for both measures. Commit in the letter to reporting the full grid whatever it shows.
- Read Zhang's actual construction from the paper before locking the grid.
- **If the grid cannot reconcile the signs, escalate to Frank** — that is a DISAGREE-class decision (push back diplomatically vs. restructure the portfolio section), not a call to make unilaterally.

### Comment 3 — IO moderation + magnitude (both answerable now)

(a) *Moderation.* Agree he reads Table 5 correctly; apologize once for the original draft leaving the implication implicit; state plainly that the pattern is what the mechanism predicts (attention moves prices through retail order flow; institutional dominance absorbs it); credit his comment as supplying the test. Report Table IA.2 numbers exactly as in the changelog: baseline ATTN 0.032 (t = 3.05); ATTN × High-IO −0.011 (t = −1.05); low-IO spread 0.44%/month (t = 2.62); high-IO spread 0.09%/month (t = 0.71); new paragraph at the end of Section 4.3, page 21. Disclose the insignificant interaction immediately — a credibility purchase that protects the subsample contrast.
   - Planned upgrades (fill placeholders when run): continuous-IO interaction instead of the tercile indicator; interaction re-estimated on the extended sample.
(b) *Magnitude.* Own the smallness ("We acknowledge that this baseline effect is modest in absolute terms"); concede directly that the spread does not cover round-trip transaction costs; then reframe: the paper's object is mispricing, not an implementable strategy, and the transaction-cost arithmetic is part of the mechanism — the spread persists precisely because it is too small, after costs, to be arbitraged away. The referee's own calculation explains why the mispricing survives.
   - Benchmarks (computed from changelog figures; MAD of monthly returns = 6.8%): 0.31%/month ≈ 4.6% of MAD; Table 3's ~0.40%/month ≈ 5.9%; low-IO 0.44%/month ≈ 6.5%. Simple annualized: ≈ 3.7% and ≈ 5.3% per year.
   - **Manuscript work needed:** a magnitude/benchmarking paragraph (Section 4.3 or 4.4) does not yet exist in the changelog; it must be drafted before the letter's pointer is real. Pair with a tone-down pass on abstract/introduction magnitude language.

### Comments 4 and 5 — done

Cite exactly as logged: typo fixed on page 12; Wang (2021) and Zhang (2022) cited in the Introduction (page 3, footnote 5) and Section 2.1 (page 8).

## 4. Evidence architecture (placement)

| Evidence | Placement |
|----------|-----------|
| LP horse-race conclusion (C1) | **Main text** — the editor's condition demands main-text visibility; grid detail in Table R1 to the letter |
| Zhang reconciliation conclusion | Main text discussion (Section 2.1 and the portfolio section); grid in Table R2 to the letter and/or IA |
| Table IA.2 (IO moderation) | Currently IA. **Recommendation: promote to main text** — it is the mechanism test answering the referee's "bothers me most" comment, and parking the core answer in the appendix is the documented placement failure. Decision for Frank. |
| Magnitude concession + benchmarks | Main-text paragraph; concession sentence may also live in a footnote |
| Extended-sample tables | Main text; original-sample tables retained in IA |
| Referee acknowledgment footnote | Optional bilateral-credit move; decision for Frank |

## 5. Decision points for Frank (escalations)

1. LP-data coverage: extend the Bloomberg pull to the full sample start vs. overlap-subsample disclosure (§3, C1 flag).
2. Promote Table IA.2 to the main text? (Recommended: yes.)
3. Contingency if the LP control subsumes ATTN — strategy decision before letter finalization.
4. Contingency if the Zhang grid fails to reconcile the sign — push back vs. restructure; do not offer removal.
5. Tone-down pass scope (abstract/intro) tied to the magnitude concession.
6. Referee acknowledgment footnote yes/no.
7. Consistency check: the referee cites ~40 bps (Table 3 portfolio spread) and 31 bps (Comment 3) — confirm these are different exhibits and use each consistently in the letter's magnitude paragraph.
8. Complete full bibliographic entries for Wang (2021) and Zhang (2022) from the actual papers; the letter's References block carries placeholders.
9. Fill all table/section number pointers from the revised manuscript map (the letter avoids inventing table numbers).

## 6. Timeline (12 weeks, inside the 6-month window)

| Weeks | Work |
|-------|------|
| 1–2 | Read Wang (2021) and Zhang (2022); lock specifications; finish cleaning (extension + Bloomberg); resolve the data-window flag |
| 3–5 | LP measure construction; premise replication; Zhang exact-spec replication panel |
| 5–7 | Horse race + orthogonalization; Zhang grid rotation; continuous-IO interaction |
| 8–9 | Re-run everything on the extended sample; assemble tables; settle placements (§4) |
| 10–11 | Manuscript edits (Section 2.1 discussion, LP subsection, magnitude paragraph, IA updates, tone-down); resolve every letter placeholder |
| 12 | Adversarial internal review of the full package (fresh reviewer, near-final severity); submit |

## 7. Pre-send checklist for the letter

- [ ] Zero placeholders; every pending claim either has its real number and pointer or is cut
- [ ] Every number paired with its t-statistic; every magnitude paired with a benchmark
- [ ] Comments reproduced verbatim, in the referee's own order (1, 1a, 2, 3, 4, 5; major/minor buckets)
- [ ] Summary block ordered to mirror the acceptance condition (Comment 1 first)
- [ ] Both direct questions in Comment 3 answered with explicit sentences
- [ ] No forbidden phrasings ("we respectfully disagree," "with all due respect," any direct negation of the referee)
- [ ] Actions in present-perfect with precise pointers; interpretations hedged
- [ ] References block completed; closing ritual present
- [ ] Companion editor letter drafted (mirrors the decision letter; states how Comment 1 was answered) — separate to-do, not in scope here

## 8. Provenance of numbers in the letter draft

- All coefficients, spreads, t-stats, MAD (6.8%), and completed-item pointers: taken verbatim from `changelog.md` (completed items only).
- Benchmarks (4.6%, 5.9%, 6.5%, 3.7%, 5.3%): computed this session from changelog figures.
- Wang (2021) and Zhang (2022) are characterized only as the referee's report states them; nothing about either paper beyond that is asserted anywhere. Full citations and specification details to be filled from the actual papers before submission.
