# Strategy Recommendation — R1-C2: Reconcile with Zhang (2022) or Remove the Portfolio-Sorting Section?

**Decision requested by:** Frank (author). **Prepared:** 2026-10-21.
**Skill gates:** Phase 0 sync check passed (both guide masters match their SOURCE headers). Phase 1 triage passes run below. Phase 2 plan-gate (Frank redlines the plan before drafting) — auto-passed for this test; the recommendation stands or falls with Frank's read of the reasoning.
**Basis:** `rr-response` skill; strategy guide §2, §3, §4.3, §4.7, §4.8, §4.9, §4.10, §5, §7.2, §8, §9; style guide §4, §6.5–§6.6.

---

## The call

**Reconcile, using the §4.3 Replication Grid. Do not remove the section. Reconciliation is mandatory work either way — run the grid before deciding anything about the section's fate.** Confidence: HIGH. This is the most directly attested case in the corpus: the grid is the exact move that carried [P2]/[P3] (carbon risk, JFQA) through the same comment shape, and deletion of a section the referee asked to have reconciled is the single most documented failure move in [P8] (JFQA, rejected round 2).

Frank's belief — "Zhang's result doesn't apply to our sample" — is admissible as a *hypothesis* and inadmissible as a *letter sentence*. Asserted without evidence, it is frontal disagreement with the referee's stated premise ("essentially the same stock universe, using the same CRSP/Compustat filters"), which trips the DISAGREE escalation gate. Demonstrated by a replication grid, it is the answer. Arguments lose; tables win (strategy Rule 2). The grid converts your belief into a named specification axis with a coefficient and a t-stat.

---

## Triage basis (Phase 1 passes)

- **Pass 1 — acceptance condition.** The General Assessment names Comment 1 as the main concern and Comments 2 and 3 as items "the authors need to explain." C2 is decision-relevant, not optional. C2's own demand: "Please reconcile your Table 3 with Zhang (2022), or remove the portfolio-sorting section."
- **Pass 2 — coding.** MAJOR × contribution-positioning (prior-literature conflict). It attacks the *sign* of a core exhibit and the paper's headline interpretation (attention-driven overpricing).
- **Pass 3 — permissive language.** The "or remove" clause is grammatically permissive and strategically loaded. It signals how much the referee cares about the reconciliation, and it functions as a trap: deletion without reconciliation is what [P8] did, and the referee there read it as evasion in round 2. A free-looking option offered by a referee who has just said "two papers cannot both be right about the sign" is not free.
- **Pass 5 — cascade.** HIGH. Portfolio sorts are load-bearing across this revision: the completed C3 response (Table IA.2: low-IO spread 0.44%/month, t = 2.62; high-IO 0.09%, t = 0.71) is a portfolio-sort product; C3 also quotes the 31 bps full-sample spread; the C1 stand-alone-predictability defense now in progress will run through the same machinery. Removing the sorting section guts a Completed response and undermines the C1 defense. It also fails on its own terms: the sign problem survives deletion — any remaining regression with a negative ATTN coefficient still contradicts Zhang's positive relation, now with no explanation on record.
- **Pass 6 — referee's values.** Engagement with the literature (C5 complained the draft engaged neither paper — already fixed, see changelog) and empirical honesty. Both point the same way: show the confrontation with Zhang, don't dodge it.

**Decision tree:** Q1 YES (MAJOR) → sub-type "Your result contradicts Published Paper X" → §4.3 Replication Grid. Q5's "Referee vs. prior literature" branch says the same: grid / reconciliation framing, never frontal.

**Hard gates:** the grid path requires no statement that the referee is wrong. Removal trips the "cut evidence the referee asked to see reconciled" gate — forbidden (red line 3).

---

## Why removal fails (four independent grounds)

1. **It is the documented failure move.** [P8] deleted the section its referee asked to have reconciled, with a length/value rationale; the round-2 verdict quoted it back as "leaving the revised draft presenting a less-than-complete picture" (strategy §9, Failure 3). The successful counterpart is categorical: "Reconciliations are answered with decomposition, never deletion." Red line 3 and Rule 9 say the same. Cutting the referee's requested evidence converts a results question into a trust question.
2. **Cascade.** See Pass 5 — C3's completed answer and C1's planned defense both sit on portfolio sorts. You would be dismantling your own revision to dodge one comment.
3. **Editor optics.** The referee has framed the issue as "two papers cannot both be right about the sign." If the section vanishes, the editor's natural reading is that your sign did not survive contact with Zhang. Removal concedes the contradiction implicitly while the paper's thesis stays exposed everywhere else.
4. **§4.10 does not apply.** Concede-and-Cut is for a section whose claim *you* cannot defend, cut with the evidentiary admission stated ("we do not have causal evidence suggesting that…"). You believe Table 3 is correct. Cutting a result you believe correct, to avoid running a grid, appears in no successful letter; its nearest relative is the [P8] cut with a length rationale.

---

## The reconcile path — §4.3 sequence adapted to this comment

Status check: changelog marks C2 "Not Started." The letter may claim only Completed changes, so the grid is the gating work item for this comment's entire response.

1. **Cheap gives already banked** (grid step 1). Wang (2021) and Zhang (2022) are now cited in the Introduction (p. 3, fn. 5) and Section 2.1 (p. 8) — comment 5, Completed. The manuscript now has the hooks the reconciliation discussion will hang on.
2. **Pin the axes.** Reduce the disagreement to named specification axes, stated neutrally ("There are two key differences between our empirical specifications and theirs" is the [P2] template). Candidate axes, to be pinned against Zhang's actual specification — [INFERRED] from the fixture, not verified against Zhang's paper:
   - attention measure construction (our app-opening ATTN vs. Zhang's measure);
   - sample period (ours ends 2022; a 2022 JFE paper draws on earlier data — regime shift is a live axis);
   - horizon / holding period (short-horizon continuation vs. longer-horizon reversal is the classic both-right resolution of opposite signs);
   - universe and filters — the referee said "*essentially* the same stock universe" and "the same CRSP/Compustat filters you describe in Section 2"; the grid tests exactly what "essentially" hides;
   - portfolio construction / weighting.
   Frank's "doesn't apply to our sample" most plausibly lives in the measure or period axis; the grid locates it.
3. **Premise first** (§5.2 staging; §4.1 step 3). Replicate Zhang panel-by-panel in his exact specification on our sample, before defending anything of ours. Report the replication honestly whatever it shows. If Zhang's result is modest or fails to appear in our sample, owning that demonstration licenses the "the premise is weaker than asserted" inference — shown, never claimed. If it replicates cleanly, you have learned something you needed to know before the referee teaches it to you in round 2.
4. **Run the full grid.** Both measures × horizons × sample periods (× universe variants as pinned). Include the Wang (2021) liquidity-provision return measure, once built, as a control — see arbitrage below.
5. **Land the hedged synthesis** on our terms: "Overall, the above comparison suggests that the difference between our paper and Zhang (2022) is mainly caused by [axis]" ([P2]/[P3] closer; style §6.5 "another important difference," §6.6 complementary positioning). This sentence *is* the direct answer to "two papers cannot both be right about the sign" (red line 4: every direct challenge gets a sentence): they can both be right if their estimands differ on a named axis — the grid names it.
6. **Optional footnote** on any evidentiary gap in Zhang, without criticizing ([P2] pattern: noting the prior paper never reported the corresponding sort).

**Placement (§5.1).** Grid tables → letter-only R-tables and/or Internet Appendix with a main-text address. The synthesis discussion must land in the manuscript — Section 2.1 (where Zhang is now cited) and/or the Table 3 discussion. Hard placement rule (i): never park the only exhibit that answers an incorporation demand in the letter alone; [P2]/[P3] promoted the reconciliation discussion to the main text under exactly this demand shape.

---

## Contingencies — decided by the grid, not before it

| Grid outcome | Move |
|---|---|
| Zhang's sign fails to appear in our sample under his spec | Strongest case: the demonstration replaces the assertion; synthesis lands on the period/measure axis; section stays |
| Both signs hold on different axes (e.g., horizon) | Both-right synthesis; add reconciliation discussion to §2.1/Table 3; possibly two-sided discussion rewrite (§4.8 flavor) where interpretation is genuinely ambiguous |
| Zhang replicates and our Table 3 weakens under his spec | Not removal-by-evasion: §4.7 Claim-Withdrawal (withdraw the overpricing interpretation, keep tests as insurance) or §4.10 cut *with the evidentiary admission stated*. Escalate to Frank with the actual numbers — this is a content decision, and it is only honest after the grid, never instead of it |
| Zhang's measure infeasible to construct | §4.9 Feasibility Substitution: nearest feasible neighbor + stated reasons + hedge + escape hatch. Nothing in the fixtures suggests this — the referee's own sameness claim implies the data are in hand |

One self-check Frank should run before the grid: "Zhang doesn't apply" — is that belief or hope? The grid is the same action in both worlds. If you are right, it is your evidence; if you are wrong, you need to know before the referee's round 2 tells you.

---

## Cross-comment arbitrage and sequencing (§7.2)

- The **Wang (2021) liquidity-provision measure** under construction for C1 (In Progress) enters the Zhang grid as a control: if Zhang's positive relation is attenuated by liquidity-provision returns, one construction pays C1 and C2 debts simultaneously. [INFERRED], MED — depends on whether liquidity-provision returns plausibly load on Zhang's sort; decide when the measure exists.
- The **sample extension to 2024** (C1a, data pulled) strengthens the grid's period axis — run the grid on both endings.
- **Sequencing:** finish the Wang measure → replicate Zhang in exact spec → run the grid → return to this table for the placement/contingency call. Only then does anything about C2 become claimable in the letter.

---

## Escalation-gate check

- The recommended path requires no "referee is wrong" statement anywhere — the grid speaks. No DISAGREE escalation.
- The one DISAGREE trigger on this comment is asserting non-applicability without the grid. Do not let that sentence into any draft.
- If, seeing grid results, Frank still wants the section removed despite Table 3 surviving, that is a §4.10 judgment call requiring an evidentiary admission that would be false if the result holds — escalate rather than draft.

---

## Phase 2 plan row (unified format)

| ID | Comment (short) | Threat×Type | Global class | Style bucket | Move / Protocol | Evidence needed | Change status | Placement | Hatch |
|----|-----------------|-------------|--------------|-------------|-----------------|-----------------|---------------|-----------|-------|
| R1-C2 | Table 3 sign contradicts Zhang (2022); reconcile or remove sorting section | MAJOR × contribution-positioning (prior-lit conflict) | NEW ANALYSIS | (c) Concede the question, reframe via new evidence; pushback via (f) vehicles inside | §4.3 Replication Grid (steps 1–6 above) | Zhang replication in exact spec on our sample; full grid over measure/period/horizon/universe; Wang liquidity-provision measure as control (shared with C1) | Not Started (changelog) — grid gates all claims | Grid → letter R-tables + IA with main-text address; synthesis → §2.1 and Table 3 discussion | Contingent: if grid kills Table 3 → §4.7/§4.10 with evidentiary admission; escalate to Frank with numbers |

**Next actions, in order:** (1) pull Zhang (2022) and pin its exact specification — measure, sample period, horizons, filters, weighting; (2) finish the Wang measure (C1 dependency); (3) run the Zhang replication, then the grid; (4) reconvene on the contingency table with numbers in hand; (5) only then draft the C2 response — opening per style §4(c), closer per the "Overall, the above comparison suggests…" template.
