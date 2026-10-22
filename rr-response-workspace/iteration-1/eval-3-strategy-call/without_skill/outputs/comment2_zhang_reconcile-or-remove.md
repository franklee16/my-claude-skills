# Strategy Call — Comment 2: Reconcile with Zhang (2022), or Remove the Portfolio-Sorting Section?

**Manuscript:** "Retail Attention and the Cross-Section of Stock Returns" (JFQA MS# 26-10442)
**Comment:** R1-2 — "Please reconcile your Table 3 with Zhang (2022), or remove the portfolio-sorting section from the paper."
**Inputs:** `referee_report_R1.txt`, `changelog.md` (status: Comment 2 not started; Comment 3/IO-split table completed; Comment 1 in progress)
**Date:** 2026-10-21

---

## 1. The Call

**Reconcile. Run the replication grid. Do not remove the section.**

Removal is a contingency gated on the grid's outcome, and the information that could justify it does not exist yet — the changelog records that no replication or grid has been run. Deciding now to remove means choosing the branch that forfeits the test.

Confidence: **HIGH** (≥80%) on the move itself — reconcile-first dominates removal in every branch of the decision tree (§4). **MED** (50–80%) that the reconciliation lands cleanly on a defensible axis — that is unknowable until Zhang's exact specification is read and the premise replication is run, which is itself the strongest reason to run it.

The cleanest statement of why: the decision tree's hard gate — *"Would it cut evidence the referee asked to see reconciled? → forbidden."* Removing the portfolio-sorting section to escape a reconciliation demand fails this gate outright. This is not an academic nicety; it is the single most documented failure move in the corpus ([P8], the failed JFQA response: the authors deleted the section the referee asked to have reconciled, and the round-2 verdict read it as evasion — "leaving the revised draft presenting a less-than-complete picture").

## 2. Pushback on the Working Hypothesis

The current position is "Zhang's result doesn't apply to our sample." Three problems with treating that as the answer:

1. **It is a hypothesis with zero evidence behind it.** The changelog says no replication or grid has been run. The referee, meanwhile, has asserted the opposite premise on the record: "essentially the same stock universe, using the same CRSP/Compustat filters you describe in Section 2." An unevidenced belief set against a documented premise, sent as prose, loses. Standing doctrine: arguments lose, tables win (Rule 2). The prior-literature conflict in the carbon-risk paper was met with a full replication grid, not a paragraph of assertion.
2. **Even if true, it cannot travel as an assertion.** The letter can never carry "Zhang's setting differs from ours" as a hand-wave. It can carry "the sign difference is attributable to [a named axis]" with a table behind it. Whether the belief is right is exactly what the grid tests.
3. **The binary frame — applies / doesn't apply — is the wrong question.** Sign contradictions between two published results are almost never resolved by one paper being wrong; they resolve on a specification axis: measure construction, weighting, horizon, sample composition. The referee's sentence "two papers using the same data cannot both be right about the sign" is rhetorically strong and analytically weak — both papers can be right under their own specifications. Bolton–Kacperczyk vs. the carbon-risk paper looked like the same situation and resolved on level-vs-intensity measurement. The operative question is: **along which axis does the sign flip?** Only the grid answers that.

One more observation that keeps the hypothesis alive without proving it: our ATTN measure is retail brokerage app openings — retail-side by construction. What Zhang (2022) uses as his attention measure is not stated in the report or changelog and must not be assumed; if his measure differs (search-volume tradition, news counts, anything else), the referee's "same universe" premise can be entirely true while the *measures* differ — which is precisely the resolution pattern the grid is built to surface. Unknown until Step 0 below; flagged, not assumed.

## 3. Triage

| Dimension | Coding |
|---|---|
| Threat level | MAJOR (threatens a main result and the paper's sign claim) |
| Type | Prior-literature contradiction → Protocol 4.3 (Replication Grid & Measurement Reframing) |
| Referee's own priority | Second-order: his general assessment names Comment 1 as the main concern and Comment 3 as "what bothers me most." Comment 2 gets a full grid, not the paper's structural budget (Rule 1) |
| Cascade risk | **Highest of the three comments.** Table 3's spread construction underpins the *completed* Comment 3 response (Table IA.2 subsample spreads); Comment 1's stand-alone-predictivity defense will presumably also run through sorts; Comment 5 compliance now cites Zhang in the Introduction and Section 2.1 |

## 4. Why Removal Fails — Branch Analysis

1. **It is the documented failure move.** Rule 9 / Red Line 3: never cut the referee's requested evidence to escape a reconciliation demand — it converts a results question into a trust question. The referee's "or remove" licenses removal, but the license does not change the signal. "Reconcile" is the primary ask; "remove" is the fallback for authors who cannot reconcile. Choosing the fallback without attempting the primary tells the referee and editor "we cannot reconcile," which they will read as "our sign is wrong." [INFERRED, from sentence ordering + [P8] precedent]
2. **The sign claim survives the deletion.** Table 3 is evidence for the story (attention-driven overpricing), and the same sign stays alive in the completed IA.2 results and wherever else the long-short spread appears. Delete the section and the contradiction stands unanswered — now with the appearance of concealment on top.
3. **Cascade.** Cutting the sorting section orphans IA.2 — the Comment 3 answer — and weakens the Comment 1 defense before it is built. One deletion damages three responses.
4. **Internal incoherence with completed compliance.** Per Comment 5, the revised draft now engages Zhang in the Introduction and Section 2.1. Deleting the section that engages Zhang's *evidence* while citing him in the literature review is a position the referee will notice.
5. **Editor optics (Rule 10).** The editor's one-line takeaway from a removal response: "the authors could not answer the sign contradiction." From a grid response: "the contradiction was apparent, not real." Only one is an accept signal.
6. **Worst-case due diligence.** Suppose the hypothesis is wrong and Zhang's specification, run on our data, robustly produces his sign. Then the headline result is fragile, and we need to know that *before* the letter goes out. Removal without running the test would be concealment of a risk we had every opportunity to check. Removal-now is dominated in every branch: even if we ultimately cut, the grid tells us how much to cut — the section, the overpricing interpretation, or the headline.

## 5. The Plan — Protocol 4.3, Staged

**Step 0 — Read Zhang (2022) exactly.** Extract: attention measure construction, sample period, universe filters, weighting, sort horizon, portfolio formation. Nothing about his design may be assumed anywhere in the response.

**Step 1 — Premise first (§5.2).** Replicate Zhang's result in his exact specification, on his measure and sample as closely as public data permits. Report it honestly whatever it shows, including modest significance. Owning the replication licenses everything that follows ([P4] stage-3 archetype: the premise is tested before our own result is defended).

**Step 2 — Walk the grid** from his specification to ours, one axis at a time. Candidate axes, ordered by the support our completed work already provides:

- **IO composition — the leading candidate.** IA.2 (completed) shows the spread lives in low-IO stocks (0.44%/month, t = 2.62) and is absent in high-IO stocks (0.09%/month, t = 0.71). Our result exists where retail investors dominate the register. If Zhang's sign concentrates in high-IO or cap-weighted segments, the contradiction decomposes into sample composition — and the decomposition doubles as mechanism evidence for Comment 3 (conversion rule, §6).
- **Weighting (VW vs. EW)** — interacts with IO composition; a cap-weighted sort on the full universe mechanically tilts toward the institutional segment.
- **Attention measure** — his vs. ours (app openings, retail-side by construction).
- **Sample period** — his endpoint vs. our December 2022; the 2023–24 extension from Comment 1a adds an out-of-sample cell when ready.
- **Sort horizon / portfolio count** — if his design differs.

**Step 3 — Land the synthesis, hedged, on our terms.** Pattern from the archetype: "Overall, the comparison suggests that the difference between our paper and Zhang (2022) is mainly attributable to [axis]." Both results stand under their own specifications. The referee's "cannot both be right" is superseded by the grid, never contradicted in prose (Red Line 1: no frontal disagreement).

**Step 4 — Placement (hard rule §5.1-i).** The reconciliation *conclusion* goes in the main text — a short "Relation to Zhang (2022)" passage in Section 4 or a footnote at Table 3. The full grid lives in the Internet Appendix with a main-text pointer; mirror tables go in the letter for verification-cost engineering. Nothing the referee demanded sits letter-only.

**Step 5 — If a cell comes out adverse** (his sign appears in some of our specifications), disclose it in the main text and land the shortfall as a decomposition, not a defeat ([P2] run-and-reframe). Unfavorable sub-results disclosed where they protect load-bearing claims are credibility purchases (§5.2).

**Cross-comment arbitrage (§7.2) — one grid, three debts:** Comment 2 (the reconciliation itself), Comment 3 (the IO split becomes the *economic interpretation* of the axis rather than a defense), Comment 1 (a liquidity-provision control column showing the sign structure follows IO, not volume — a preview of the stand-alone-predictivity defense). The 1a extension supplies the out-of-sample cell.

**Feasibility:** everything Steps 0–2 need exists now — ATTN through 2022, CRSP/Compustat in house, Zhang's published specification. Do not gate the grid on the 2023–24 extension; add that cell when the cleaning finishes.

## 6. Contingency — Decision Rule After the Grid

| Grid outcome | Move |
|---|---|
| **Favorable** — his sign does not replicate in our sample, or flips on a named axis | Full 4.3 landing; Table 3 stays. If his sign does not replicate even in his exact spec, report the replication honestly and let the premise weaken itself — the "referee is wrong" sentence never appears anywhere (4.5 discipline) |
| **Mixed** — the sign is conditional on an axis | Decompose and condition: our claim becomes the segment where retail dominance makes attention matter — which *is* the paper's mechanism, already evidenced by IA.2. This is the strongest outcome: the contradiction converts into heterogeneity evidence |
| **Adverse** — his sign robust in our sample, ours fragile | Escalate to the author team before drafting (§8: fundamental trade-off). The move is then Concede-and-Cut done properly: withdraw the overpricing interpretation with the evidentiary admission stated in the letter, cut what the admission requires (possibly the interpretation rather than the table), restructure the story, and decide with coauthors whether the contribution survives. That path costs weeks — but removal-now hides the same information and pays the same cost in round 2, with interest |

## 7. Internal Audit Before the Letter

- **40 vs. 31 bps.** Table 3 reports ~40 bps/month; the referee quotes a 31 bps/month full-sample spread in Comment 3, and IA.2 reports subsample spreads. Have the mapping ready (raw spread vs. adjusted alpha, EW vs. VW, sorted vs. regression-implied). If unexplained, the referee's "internal tension" remark gets free fuel.
- **Letter discipline.** The letter cites only Completed items with actual pointers (changelog rule). The grid must reach Completed before the letter references it. If the timeline slips, the letter ships later with the grid in it — deadline pressure is not a reason to take the dominated branch.

## 8. Red Lines for This Comment

- No "Zhang's result doesn't apply to our sample" as prose assertion — in the letter it may appear only as a demonstrated axis with a table behind it.
- No evaluative discounting of the contradiction ("not an important concern for our story" — [P8] Failure 8).
- No removal of the section while the reconciliation is unrun.
- The referee's direct demand gets a direct answer: reconcile, and here is the table.

---

**Bottom line:** the honest version of "Zhang doesn't apply to our sample" is a testable claim about a specification axis, and the paper already holds the most promising axis in IA.2. Run it. If it wins, Comment 2 converts from a threat into heterogeneity evidence. If it loses, we need to know before the referee tells us — and removal now would only postpone that conversation to a round 2 we would enter as the authors who deleted the contested table.
