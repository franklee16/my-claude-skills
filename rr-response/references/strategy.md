<!-- SOURCE: C:\Users\frank\Dropbox\Frank-OS\Input\R&R Sample\response_strategy_guide.md @ 2026-10-21 md5=dd7c6d6cd5d6d7ed21e09ee49f372fbe -->

# Referee-Response Strategy Guide — Weikai Li

## 0. How to Use This Guide

This guide distills the **decision logic** behind Weikai Li's referee responses — how he triages comments, chooses a response move, stages evidence, manages concessions, and handles threats to the paper's contribution. It is the companion to [`response_letter_style_guide.md`](response_letter_style_guide.md), which distills the **execution layer** (voice, phrasing, letter skeleton, formatting). The two are used in sequence:

1. **At decision time** (before writing): consult this guide — classify the comment (§2), pick the move (§3), select the protocol for tough comments (§4), plan evidence and placement (§5–§7).
2. **At drafting time**: consult the style guide — skeleton (§2), phrase banks (§5–§6), formatting conventions (§8).

Every move in this guide has its execution phrasing in the style guide; nothing here replaces it. The Comment-Handling Taxonomy (style guide §4) is the shared vocabulary: this guide explains **when and why** each bucket is chosen.

**Evidence conventions.** Every quote is verbatim from the text-converted sources in `agent_tasks/response_strategy_distillation_202610202043/sources/` (legacy-encoding normalizations noted in the per-pair analyses). Strategic-motive attributions are reconstructions from the per-pair inference ledgers and are marked "(inferred)" where load-bearing. Letters speak as team "we"; the strategy is attributed to the author teams, not to Li individually (explicit in the P6 analysis).

**Source pairs and outcome weighting:**

- [P1] *Security Analysts and Capital Market Anomalies* (JFE) — successful; R&R granted despite a "not publishable" referee verdict.
- [P2], [P3] *Is Carbon Risk Priced…* (JFQA) — successful; **same paper, two referees**; shared templates weight them as ~1.5 independent sources (style-guide convention).
- [P4] *Short Selling ETFs* (RAPS) — successful.
- [P5] *Gender Effects of COVID* (RAST) — successful.
- [P6] *Inside Broker* (JFE) — successful; also an R&R granted against a "not publishable" verdict.
- [P7] *Financial Intermediaries and Comovement in Market Efficiency* (ETF comovement, RFS) — **outcome not stated in the files** (R&R in hand after a disposed appeal); strategies treated as corroborating, not as proof.
- [P8] *Naïve Earnings Growth Extrapolation* (JFQA) — **FAILED**; the round-1 response is judged line-by-line by the referee's round-2 verdict. This is the contrast case for §9.

---

## 1. Strategy Doctrine (Ten Governing Rules)

The spine of the method, in priority order. Each rule carries its evidence base.

**Rule 1 — Triage by threat, not by volume.** Effort allocation tracks the threat a comment poses to the headline result, identification, or contribution — not comment length, politeness, or position. The amplitude dial, observed in [P1], [P4], [P5], [P6]: identification/contribution threats get structural over-compliance; robustness demands get full literal compliance; presentation notes get one-sentence exact compliance. In [P5], the two MAJOR placebo comments absorbed nearly all new analysis while the title request got a one-line grant. (inferred from all six successful pairs; universal).

**Rule 2 — Answer threats with tests, not arguments.** Every MAJOR threat in the successful set is answered with new evidence executed honestly, including unfavorable sub-results. Arguments lose; tables win. The substitution threat in [P4] was met with a five-stage empirical defense, not a paragraph of assertion; the prior-literature conflict in [P2]/[P3] was met with a full replication grid.

**Rule 3 — Concede claims, preserve assets.** When attacked, interpretive and causal claims are surrendered instantly; tests, tables, and data are kept or upgraded. Across [P6]'s 19 comments there was not one pure-disagree move and nothing empirical was deleted: the RegFD causal claim was withdrawn ("We no longer make any such claim") while the underlying tests were preserved in the Internet Appendix as insurance; the 20% magnitude claim was traded for the robust-spec magnitude. The claim/test split is the workhorse of non-concession.

**Rule 4 — Non-concession never travels as disagreement.** The vehicles, exhaustively: "However" + new evidence; "While/Although" + hedge; reframing (measurement-driven, complementary, conditional); feasibility substitution; ambiguity rewrites; arbitration to the editor; escape hatches. See style guide §6 for the phrasings. In [P7], ~450 lines of responses contain no frontal disagreement; every resistance travels as a citation (MacKinnon on clustering), an alternative remedy (LeMM rename), or an arbitration offer.

**Rule 5 — Every declined item ships with an escape hatch.** "We would be pleased to… if you prefer" [P3] (three instances); "we would be happy to remove them entirely or restore them to the main text, depending on the editorial team's preference" [P7] — identical in both referee letters, near-identical in the editor letter. The hatch shifts the final call to the referee/editor at zero cost if declined, so inaction cannot later be read as defiance. Contrast: the phrase "if you prefer" appears **zero times** in the failed letter [P8] (verified by search) — every refusal there left the referee no graceful path.

**Rule 6 — Amplify exactly where the referee touches the contribution; comply minimally elsewhere.** [P1]: a four-table t-stat question was answered with 12 tables re-estimated paper-wide plus a letter-only alternative; "A couple of sentences on possible reasons would be enough" got a new formal-test table; a typo comment got a copyeditor. [P5]: 1,000 permutation repetitions against a suggested 20–30, delivered as a figure. [P6]: two linked suggestions became the revision's organizing framework section (comment 2.1) plus three new main-text tables (comment 2.2.1). The trigger for amplification is threat to the contribution or identification, or a cheap conversion of defense into offense — never politeness.

**Rule 7 — The referee's conjecture is free identification.** When a referee proposes a mechanism or test, adopt it as the paper's own, run it, and return the result as confirmation of *their* conjecture: "The underlying channel we have in mind for the return patterns is in line with your conjecture" [P1]; "This result supports your conjecture that the existence of skilled analysts who exploit anomalies might mitigate (but not fully eliminate) mispricing" [P1]; "We also develop your idea that if the LMM widens its quotes, APs that execute against those quotes face higher trading costs" [P7], formalized as Hypothesis 3 and tested twice. Having proposed the channel, the referee must either accept the confirming evidence or attack his own conjecture (inferred). Credit can be made bilateral — in manuscript footnotes: "We acknowledge your help in footnote 10" [P6].

**Rule 8 — Placement is part of the argument.** Where evidence lives is a strategic decision with a consistent hierarchy (§5.1): contribution-adding evidence → main text; audit/repair/diagnostic evidence → letter-only R-tables; referee-conjecture tests → letter, with only needed conclusions promoted (to a footnote if necessary); contested-but-valuable identification → Internet/Online Appendix with a main-text address so the editor can promote or kill it without restructuring [P7]. Concessions land in footnotes [P1].

**Rule 9 — Cut only what you cannot defend, and cut with an evidentiary admission.** The successful cut: "we do not have causal evidence suggesting that ETF ownership reduces mispricing for underlying stocks. For these reasons, we have removed the corresponding part (Section 5 and Table 11 of the original paper) entirely from the revised manuscript" [P4]. The admission does the justifying. Never cut the referee's *requested evidence* to escape a reconciliation demand — that converts a results question into a trust question and is the single most documented failure move in [P8] (§9).

**Rule 10 — Write for the editor as much as for the referee.** The summary-of-major-changes block is the editor's accept-case in miniature, ordered to mirror the referee's stated acceptance condition ([P1]: items 1–4 answer the comments the referee said success "crucially depends" on). Verification-cost engineering throughout: mirror tables duplicating in-paper exhibits into the letter, verbatim pastes of revised text, page pins, migration lists, quantified page counts — so compliance can be verified without opening the manuscript and is credited rather than audited (inferred, [P6], [P7]).

---

## 2. Reading the Report: Triage (Before Writing Anything)

Six reading passes, distilled from the successful pairs. Do these before drafting any response.

**Pass 1 — Find the acceptance condition.** Referees state (or leak) what decision-relevant bar the revision must clear. [P1]'s referee: "the success of your revision crucially depends on your new supportive evidence (esp. those for my comments # 1 to 3)." [P7]'s R9: "a simple identification strategy that I see as a necessary condition for publication." [P8]'s round 1 was a "benefit of the doubt" R&R (per the referee's round-2 recap), with contribution insight as the implicit condition (inferred). The acceptance condition dictates where the structural budget goes and should order the summary block.

**Pass 2 — Code every comment** by threat level (MINOR / MODERATE / MAJOR) and type (identification-threat / robustness-demand / mechanism-question / contribution-positioning / data-limitation / interpretation-disagreement / framing-tone / presentation). MAJOR = threatens the headline result, identification, contribution, or data validity. This coding (not the referee's ordering) determines response amplitude; the referee's own ordering is preserved in the *letter's structure* only.

**Pass 3 — Read permissive language as a cost signal.** "It is up to the authors to make this decision though" and "If not, feel free to ignore" [P3]; "This is a minor point and will not impact my decision in any way" [P7]. Permissive language licenses optimization: refuse the free item with a precedent citation plus a hatch (table order, refused via Fama–French 1992 convention [P3]); accept the costly item but park it (the FM-dynamics figure produced letter-only, cross-referenced to an existing subperiod panel so the weakening premium reads as confirmation, not news [P3]) (inferred).

**Pass 4 — Read enthusiasm as the amplification invitation list.** "There are some kernels of interesting findings scattered throughout the manuscript that merit additional investigation" [P4] — both kernels were then converted into validation tests (hedge-fund ownership table; SUE earnings-news measure) that doubled as mechanism evidence for the main defense. "particularly compelling" [P5] became borrowable authority: the Du (2023) verdict in the intro is stated more causally than an unlicensed claim would permit (inferred). "This was really an excellent suggestion" attaches to exactly the comments that generated new identification architecture [P6].

**Pass 5 — Map cascade risk.** Which comments, if conceded, poison other results? [P4]'s substitution threat ("your variable is my published variable") would cascade to every downstream result — hence the five-stage defense. [P1]'s hump-shape comment threatened the contribution claim itself. Comments that cascade get protocols (§4), not one-shot answers.

**Pass 6 — Inventory what the referee values that the paper can deliver.** The referee's stated priorities that overlap the paper's strengths are the raw material for concede-and-amplify moves and for cross-comment arbitrage (§8).

---

## 3. Move Selection: The Decision Tree

Work through the questions in order for each coded comment. Moves use the style guide §4 taxonomy names.

```
Q1. Is this the acceptance condition or a MAJOR threat (Pass 1/2)?
    YES → Allocate structural budget. Choose a protocol from §4 by sub-type:
           - "Your variable proxies for my variable"          → 4.1 Grant-the-Threat
           - "This pattern undermines your story"             → 4.2 Forensic Artifact-Hunt
           - "Your result contradicts Published Paper X"      → 4.3 Replication Grid
           - "Your dependent variable is the wrong estimand"  → 4.4 Grant-the-Principle
           - "The referee's factual premise is wrong"         → 4.5 Agree-Then-Correct
           - "Your effects are too small"                     → 4.6 Own-the-Smallness
           - "This claim is indefensible"                     → 4.7 Claim-Withdrawal
           - "Your magnitude/quantification is inflated"      → 4.6 then 4.10
           - "If your mechanism were real, your result
              should not exist" (logical trap)                → magnitudes first, then
                                                                adopt-and-test (4.11, [P1] C8)
           - "Run this calculation" (may come out adverse)    → run exactly as specified,
                                                                land the shortfall as a
                                                                decomposition (4.4, [P2])
    NO  → Q2.

Q2. Is the ask mechanically cheap (typo, citation, wording, clarity)?
    YES → full-concede+act instantly, one-paragraph response, precise pointer.
          Optionally convert into an effort signal ("hired a copyeditor" [P1]).
          → done.
    NO  → Q3.

Q3. Is the ask feasible with data in hand?
    INFEASIBLE → 4.9 Feasibility Substitution: nearest feasible neighbor + stated
                 reasons + conclusion hedged to the substitution + escape hatch [P2].
    FEASIBLE   → Q4.

Q4. What is the cost-to-threat ratio?
    CHEAP relative to threat  → exceed the ask (oversupply to foreclose round 2):
                                more repetitions, more tables, more subgroup splits
                                [P1], [P5], [P6].
    COSTLY but protects a headline apparatus → full literal compliance at maximal
                                scope, one flat survival sentence [P6].
    COSTLY and discretionary  → comply in the cheaper placement the referee's own
                                language licenses; park per §5 [P3].
                                → done.

Q5. Does the referee's demand conflict with the paper's design, another
    referee, or prior literature?
    Referee factually wrong          → 4.5 Agree-Then-Correct.
    Referee's prior vs. paper's result → 4.8 Ambiguity rewrite, or premise-first
                                         testing under 5.1. Never frontal.
    Referee vs. referee              → redesign to satisfy both + cite the favorable
                                       referee in the strict one's letter + identical
                                       arbitration sentence in all letters [P7].
    Referee vs. prior literature     → 4.3 Replication Grid / reconciliation framing.
                                        → done.

Q6. Is a claim in the paper indefensible under the referee's framework?
    YES → 4.7 Claim-Withdrawal (keep the test if it has insurance value) or
           4.10 Concede-and-Cut (delete with the evidentiary admission stated).
    NO  → pushback-with-evidence (Rule 2), carried by Rule 4 vehicles.

HARD GATES (any answer routes to escalation, §8):
  - Would this response require saying the referee is wrong?  → escalate to user.
  - Would it cut evidence the referee asked to see reconciled? → forbidden.
  - Does it decline an incorporation the referee marked essential?  → re-plan;
    at minimum ship with escape hatch + layered reasons.
  - Does it leave a direct question unanswered?               → forbidden.
```

---

## 4. The Tough-Comment Playbook

Eleven protocols, each with trigger, ordered sequence, and specimen. Phrasings cross-reference the style guide phrase banks.

**Protocol index (trigger → protocol):**

| The referee essentially says… | Protocol |
|---|---|
| "Your variable may proxy for my variable" | 4.1 Grant-the-Threat |
| "This pattern in your tables undermines your story" | 4.2 Forensic Artifact-Hunt |
| "Your result contradicts Published Paper X" | 4.3 Replication Grid |
| "Your dependent variable / core measure is the wrong one" | 4.4 Grant-the-Principle |
| Factual premise wrong (sign/direction) | 4.5 Agree-Then-Correct |
| "Own it: your effects are small" | 4.6 Own-the-Smallness |
| Indefensible claim, test worth keeping | 4.7 Claim-Withdrawal |
| Prior contradicts an existing result; no test can help | 4.8 Ambiguity |
| Requested fix is data-infeasible | 4.9 Feasibility Substitution |
| Section cannot survive the referee's framework | 4.10 Concede-and-Cut |
| Referee proposes a channel / "necessary condition" | 4.11 Conjecture Promotion |
| "If your mechanism were real, your result should not exist" | 4.11 + magnitudes ([P1] C8) |
| "Run this calculation" (may come out adverse) | 4.4 run-and-reframe ([P2]) |

### 4.1 Grant-the-Threat Protocol
**Trigger:** "Your variable/result is really just [mechanism the referee owns]."
**Sequence** ([P4], the flows-proxy threat — the archetype):
1. **Concede the logic, not the facts** — a conditional that grants the framework while committing to nothing: "If both are true, then it indeed poses an empirical threat to the stand-alone return predictability of our ETF-based short ratio measure."
2. **Build the data the test requires** — "To evaluate this possibility, we obtain month-end ETF shares outstanding from Bloomberg," with a provenance footnote that pre-empts data-quality counterattack.
3. **Test the referee's PREMISE first, in your own sample** — replicate the effect he cited before defending your result; report it honestly even when modest: "The statistical significance is modest with a t-stat of 2.28." Owning the modest replication licenses the subsequent "premise is weaker than claimed" inference (inferred).
4. **Test the proxy claim directly**, where the referee's own institutional logic favors you — the null cross-sectional relation (t = −0.09) is explained using the referee's own AP-covering-end-of-day lecture, turned into the reason the proxy story fails at the monthly horizon.
5. **Run a fair outcome test** (double sort giving the rival measure every chance), then **propagate controls everywhere**, then add a **mechanism discriminator** (your measure predicts fundamentals; the rival does not) — converting the threat into new evidence for the paper.
**What is never conceded:** the headline result. The concession stays hypothetical; the magnitude attack is never answered head-on — attenuation is disclosed plainly (−0.8868 → −0.657) and argued via t-stat stability, exploiting the referee's own pre-commitment that attenuation "is actually a benefit" (inferred).
**Placement:** premise/proxy/extension tests in letter-only R-tables; only the needed conclusion promoted, at footnote altitude.

### 4.2 Forensic Artifact-Hunt
**Trigger:** "This pattern in your table undermines your story" (an empirical irregularity threatening the contribution).
**Sequence** ([P1], the hump-shape):
1. Signal sunk effort before any result: "We have spent considerable amount of time to investigate what caused the hump-shaped relation, because it is very crucial to our contribution to the literature."
2. Run the referee's own requested test first (the "Middle" column) — the pattern does not appear in portfolio sorts.
3. Diagnose the discrepancy between methods; identify the one structural suspect (controls → missing observations).
4. Prove the diagnosis by construction: restrict to the missing-control subsample and show the pattern lives exactly there (letter Table R3).
5. Fix the specification; report the residual honestly — "2 to 3 cases with a moderate hump-shaped relation."
6. Cover the residual with an economic story (footnote).
7. Count exceptions formally ("only the Distress anomaly shows…") — audit-proofing that makes every "no clear hump" claim falsifiable rather than rhetorical (inferred).
**What is never conceded:** the headline contrast. The referee's evidence against the result is recast as a sample-selection artifact of the *previous* specification — defense disguised as self-investigation (inferred).
**Placement:** forensic tables letter-only; the published record starts from the fixed specification.

### 4.3 Replication Grid & Measurement Reframing
**Trigger:** "Your result contradicts Published Paper X" — the reconciliation demand.
**Sequence** ([P2]/[P3], Bolton–Kacperczyk):
1. Grant every named action immediately and verifiably (promote the table; promote the footnote to a section).
2. Reduce the disagreement to exactly two named specification axes, stated neutrally: "There are two key differences between our empirical specifications and theirs."
3. Replicate the prior paper panel-by-panel in its exact specification.
4. Run the full grid (both markets × both timings × all measures).
5. Convert the referee's adverse prior ("intensity versus level does not make much a difference") into a demonstrated fact — the skewness of raw CEI shown with kernel densities, never stated as a rebuttal.
6. Land a hedged synthesis on your terms: "Overall, the above comparison suggests that the difference between our paper and Bolton and Kacperczyk (2021) is mainly caused by whether one uses the level of carbon emissions or carbon intensity as the measure of carbon risk."
7. Optionally, one footnote catching the prior paper's evidentiary gap without criticizing: "their paper never report the corresponding portfolio sorting results using CEI."
**Cross-referee note:** one replication work product served both referees with local tailoring; the stricter referee's main-text demand set the placement.

### 4.4 Grant-the-Principle, Keep-the-Estimand
**Trigger:** "Your left-hand-side variable (or core measure) is conceptually the wrong one."
**Sequence** ([P3], realized vs. expected bond returns):
1. Concede the principle: "We agree that for the bond market, the standard procedure of using realized returns might distort the true expected return."
2. Build the referee's alternative — implemented via a feasible construction (a silent substitution: the equity-anchored Merton route rather than the referee's rating/migration sketch).
3. Re-run both formats (sorts and Fama–MacBeth) on the alternatives.
4. Report that the result **strengthens**: alphas of −0.20% (t = −3.18) and −0.40% (t = −4.20) vs. the realized-return baseline.
5. Frame the whole thing as "two additional robustness checks" — the conceptual point is absorbed as a robustness axis; the headline estimand survives.
6. Park in the Online Appendix citing the shortening mandate, plus the escape hatch: "We would be pleased to move it to the main paper if you prefer."
**Variant ([P2], divestment):** when the requested split is infeasible, substitute the nearest feasible neighbor (investor *types* for investor *activity*) and downgrade the conclusion by exactly one hedge: "less likely to be fully explained."

### 4.5 Agree-Then-Correct
**Trigger:** The referee's factual premise is wrong (sign, direction, magnitude attribution).
**Sequence** ([P5], the placebo direction the referee misread):
1. Concede both true criticisms first, by name (magnitude; near-significant p-value).
2. Correct the fact with minimal machinery — a sign comparison across two existing tables, with italics on the operative words: "we do note that the direction of the coefficient is *not* consistent with the results in the main analysis."
3. **Make the correction pay a dividend immediately** — the "wrong"-signed placebo implies the main effect "may *underestimate*" the crisis impact, so the referee is invited to accept being wrong while gaining a stronger paper.
4. Hedge the residual mechanism question explicitly; offload interpretation to literature.
**Rule:** the correction is sandwiched in concessions and never framed as disagreement. In the observed instance, two concessions preceded the correction.

### 4.6 Own-the-Smallness (Magnitude Rebuild)
**Trigger:** "Your effects are small / your quantification conceals this."
**Sequence** ([P7], after "The authors should just own the fact that the observed effects are relatively small, and not try to conceal them behind unrealistic assumptions about trading behavior"):
1. **Unconditional removal of whatever the referee named** — both banned calculations deleted, no defense offered.
2. Concede smallness in print, inside the manuscript: "We acknowledge that this baseline effect is modest in absolute terms."
3. Rebuild significance on an anchor the referee did not ban: distributional benchmarking (2.786 bps = 12.2% of the mean deviation), a dollar figure on *traded volume* rather than the banned market-cap base ($40M/day), with a self-inserted caveat paragraph on the measure's subjectivity.
4. Let the amplification result carry the headline: 6.985 bps in COVID ≈ 2.2× baseline.
**Logic:** the smallness concession is a credibility purchase that protects the amplification numbers actually carrying the contribution (inferred).

### 4.7 Claim-Withdrawal / Test-Preservation
**Trigger:** A causal or interpretive claim is indefensible, but the underlying test has value.
**Sequence** ([P6], RegFD):
1. Agree instantly, no defense of the old claim.
2. Take a third path the referee did not offer — relocate rather than fix or drop.
3. Justify retention with exactly one narrow, non-causal point: the tests show survival in the recent period, contra the literature expecting analyst effects to die post-RegFD — insurance for the next round, not sentiment (inferred).
4. Withdraw the claim in writing: "However, we do agree with you that any claim suggesting that these effects are related to RegFD is not appropriate. We no longer make any such claim."
5. Paste the revised passage so the referee can verify the claim is gone.
**The split:** the *claim* dies; the *test* is parked. Refusing to cut is carried as "We considered dropping these tests altogether, but believe that they are somewhat helpful in making one point…" — a grant-with-reasons, not a refusal.

### 4.8 Ambiguity Joint-Authorship
**Trigger:** The referee's economic prior contradicts an existing result, and no new test can help.
**Sequence** ([P6], stocks-covered):
1. Agree — to the *ambiguity*, not to the referee's prediction: "We agree with you and have changed our discussion of this test to reflect the ambiguity in what we should expect to see."
2. Rewrite the discussion two-sided; give the referee's logic the literal last word in the pasted text.
3. Change no table; run no test.
**Logic:** converts a prediction the data contradict into an open question — neither wrong nor right, unresolved — while the result and the paper's primary mechanisms survive as the other half.

### 4.9 Feasibility Substitution
**Trigger:** The requested fix is data-infeasible.
**Sequence** ([P4], creation/redemption baskets):
1. Validate the mechanics ("Indeed, the creation/redemption baskets need not fully replicate the holdings").
2. Import an external bound on the problem's size (Todorov 2021: 85–95% basket coverage for equity ETFs).
3. Admit the gap without hedging: "Since we do not have data on ETFs' creation/redemption basket lists, we cannot precisely determine an ETF's exposure to a particular stock at a moment in time."
4. Offer the conditional argument for why the proxy still works ("As long as…"); state the hopeful assumption rather than disguise it.
5. Deliver exactly the requested disclosure, quoted verbatim from the revised text.
**Silent-substitution variant ([P5], magnitudes):** when the referee's example is a trap ("for instance by estimating the monetary value of the difference in forecast accuracy between male and female analysts") and a stronger substitute exists (coefficient-ratio benchmark: 55.5% of the Forecast Age coefficient; 49 vs. 86 days), supply the substitute, insert it at two locations, and stay silent on the skipped instance — no refusal on the record. Use only where the referee's "for instance" marks the instance optional.

**Observed deviation — the silent drop.** In [P4], one peripheral request (transaction-cost measures of synthetic shorting) received no response at all — neither grant, refusal, nor hatch; it is the only unaddressed demand across the eight pairs (inferred rationale from the P4 analysis: the revision's empirical budget was consumed by the denominator rework and the flows defense, and a partial transaction-cost analysis would have opened a new attack surface). The doctrine does not license silence for any comment the referee marks essential or decision-relevant; at most it is survivable for peripheral asks, and it remains a deviation, not a recommended move.

### 4.10 Concede-and-Cut (Done Right)
**Trigger:** A section's claim cannot survive the referee's framework — and keeping it contradicts the story the revision is building.
**Sequence** ([P4], Section 5/Table 11, where only "tone down" was asked):
1. Agree explicitly with the concern.
2. Reframe at the literature level ("mixed empirical findings"), backed by the surplus citations banked elsewhere.
3. State the evidentiary admission as the operative reason: "our evidence regarding the mitigating effect of ETF ownership on mispricing is based on simple portfolio sorting, and we do not have causal evidence suggesting that ETF ownership reduces mispricing."
4. Delete, with table numbers named.
5. Disclose at point-to-point altitude, not in the headline change summary (inferred) — the summary stays framed as robustness wins.
**Why over-comply ([P1] variant):** a weak section deleted outright (compressed to a footnote) frees table numbers and space for the mechanism evidence the referee demanded most; the referee's own discount of the section does the justifying.
**Contrast:** [P8]'s cut removed the *referee's requested evidence* with a length rationale — see §9, Failure 3.

### 4.11 Referee-Conjecture Promotion (concede-mechanism-and-run-with-it, amplified)
**Trigger:** The referee proposes a channel, test, or "necessary condition."
**Sequence** ([P7] R9-7; [P1] C3; [P6] 2.2.1):
1. Signal exact compliance first: "We now indeed provide the results following your comment."
2. Implement in escalating granularity (decomposition → per-class panels → pairwise transmission), with the referee's own words as scaffolding.
3. Disclose the one failing cell immediately, with an economic reason, not a burial: "Currency is the only exception (0.830, t = 0.96), potentially reflecting the smaller and less persistent deviations in this more liquid segment."
4. Attach pre-trend nulls to every event-style estimate.
5. Reuse the construction to pay other comment debts (§8).
**In [P6]** the analogous move converted one comment into the revision's core: descriptive measurement (9.68% of firms use one broker for all insiders; 41.1% of job-changers keep their broker) plus three orthogonal new tables, each killing a different version of the firm-link confound — triangulation instead of hedges.

---

## 5. Evidence Architecture

### 5.1 The Placement Hierarchy

| Tier | What goes there | Rule | Specimens |
|---|---|---|---|
| Main text | Evidence that adds a claimed contribution; identification-critical results; referee-validated promotions | Promote with a stated justification ("Because this key result provides the underlying channel…") | [P1] new Table 6 + Section 4.4; [P6] Tables 6–8; [P2] old A.10 → Table 8 |
| Online/Internet Appendix | Referee-licensed parking; mechanism robustness; contested identification kept promotable | Always with a main-text pointer or address; cite the licensing comment as justification | [P3] A.2–A.5 "Following your suggestions to shorten the paper"; [P7] IA.3/IA.4 with §4.5 bridge |
| Letter-only R-tables | Tests of the referee's conjecture; forensic/repair/diagnostic evidence; replication audits | Promote only the conclusions the paper needs, at minimum altitude (a footnote suffices) | [P1] R1–R8; [P4] R.1–R.4; [P3] Figure R.1 |
| Footnotes | Concessions at the margin; alternative-specification documentation; residual anomalies | Anything that concedes ground is footnote-sized in the paper | [P1] fns 12, 15, 17, 25; [P4] fn 26 |
| Unreported | Tests that cannot meet the paper's FE standard | State the methodological reason in a footnote, "for the sake of completeness" | [P6] All-Star test, fn 14 |

**Two hard placement rules.** (i) Never park the *only* exhibit that answers a referee's incorporation demand — [P8] parked exactly the two tables (residual reframe; contemporaneous surprise) the referee escalated into round-2 complaints, while promoting the supporting cast. (ii) Contested identification evidence parked in the IA keeps a main-text address so the editor can promote or kill it without restructuring the paper [P7].

### 5.2 Staging Rules

- **Premise first.** Test the referee's premise before defending your result ([P4] stage 3); conclusions are stated only after the threat has been run to ground.
- **Column-by-column walks** for every new table, with attenuation disclosed and t-stat stability as the operative statistic ([P4]: −0.8868 → −0.761 → −0.657 with t ≈ −2.5 throughout).
- **Benchmark every magnitude** against the paper's own moments ([P1]: 2.95% net-buy difference vs. Table 1's mean 1.47%, SD 5.63%), literature numbers, or unconditional baselines ([P6]: 16.6% vs. 14.6% base rate).
- **Count exceptions** rather than asserting "no problem" ([P1]: "only the Distress anomaly"; "only two cases").
- **Attach pre-window nulls** to event-style estimates ([P7]: pre-event windows "statistically indistinguishable from zero").
- **Disclose unfavorable sub-results in the main text** — insignificant F-tests [P5], the VW null [P4], the t = 1.90 interaction [P7] — as credibility purchases that protect the favorable claims and pre-empt selective-inference attacks (inferred).

### 5.3 Oversupply to Foreclose

When a test defends the identification, supply it beyond what was asked: 1,000 repetitions vs. 20–30 suggested, as a figure with the actual coefficient marked in the tail [P5]; 12 tables re-estimated where 4 were questioned [P1]; an unprompted sample extension to 2024 that also hardens the COVID analysis [P7]. The design is chosen so no second-round demand for "more" is available (inferred).

### 5.4 Verification-Cost Engineering

Mirror tables duplicating in-paper exhibits into the letter "for the ease of your reference" [P6]; verbatim pastes of every revised passage; page pins throughout; explicit old-paper→OA migration lists ("We have also moved Section 3.1.1, Section 5.2.4, Section 5.2.5, Figure 2, Table 9, and Table 10 of the old paper to the Online Appendix" [P3]); quantified page counts (61→45 [P3]; footnotes ~46→~20 [P7]). Making the referee's re-review fast and trust-free raises the probability compliance is credited rather than audited (inferred).

---

## 6. The Concession Economy

**Cheap gives first.** Open the compliance ledger with near-zero-cost items granted instantly and visibly — the title adopted verbatim [P5], typos plus a copyeditor [P1], citations in multiple named locations [P4] — so every contested item later reads against a background of demonstrated cooperativeness.

**Apology rationing.** Exactly one apology per provable, objective error, spent fully: "We apologize for the careless" [P1] — on the one confirmed statistical mistake. In [P6], all five apologies attach to objective defects (sloppy magnitude, imprecise labels, poor writing, italics, delay); none to judgment calls, where the register switches to "We agree…" + action. Conceding the one provable error fully purchases the credibility that funds qualified resistance everywhere else (inferred).

**Effort signals on the make-or-break items.** "We have spent considerable amount of time…" [P1]; the apology-for-delay reframed as effort: "We first apologize for the delay in getting back to you. In part, however, this reflects how seriously we have taken your report" [P6]; enumerated effort metrics (200 simulations; 1,985 events on 51 dates [P7]).

**Credit as endowment.** Bilateral attribution — acknowledging the referee inside the manuscript's footnotes on the paper's *strongest new evidence* [P6] — makes the referee a co-owner of the revision he must then either accept or reject along with his own contribution (inferred).

**Honesty as inventory.** Unfavorable sub-results are disclosed in the main text, not parked, precisely where they protect load-bearing claims (§5.2). The failed letter [P8] also disclosed its tables — but then refused the incorporations they supported; disclosure without compliance is not credibility, it is evidence for the prosecution (§9, Failure 2).

**Conversion rule.** Every concession is monetized — converted into robustness (the old measure "relegated as a robust measure" [P4]), mechanism evidence ([P1]'s deleted section freed the Table 6 slot for the demand-channel result), or goodwill. A concession that buys nothing is a wasted asset (inferred).

---

## 7. Portfolio Management (Sequencing, Cross-Comment, Cross-Referee)

### 7.1 The Summary Block as Accept-Case

The summary of major changes is ordered to mirror the acceptance condition ([P1]: items 1–4 answer comments 1–3) and framed as adoptions, not defenses. In [P7], one threefold contribution paragraph is quoted verbatim in all three letters — a single controlled contribution narrative for every reader, editor included.

### 7.2 Cross-Comment Arbitrage: One Work Product, Many Debts

- [P7]'s cross-asset LMM Deviation construction pays five debts at once (two referees' identification attacks, the publication-condition prescription, the contribution attack, and the all-tables control demand) — which is why it is developed in escalating granularity rather than as one table.
- [P6]'s new framework section monetizes four comments simultaneously and becomes the container hosting three other fixes; its descriptive stats become another table's identifying variation.
- [P1]'s cut section recycles its table number into the mechanism evidence.
- Surplus citations banked under one comment become the "literature is mixed" justification for a cut under another ([P4]).

Scan the coded comment list for demands that one new construction can satisfy jointly before building anything.

### 7.3 Cross-Referee Management

- **Stricter-referee rule.** When referees differ on placement, satisfy the stricter demand ([P2]/[P3]: main-text promotion even though the other referee authorized response-only).
- **Build once, tailor locally.** Shared analyses deployed to both referees with identical table numbers and only local framing ([P2]/[P3] B&K grid).
- **Consistency maintenance.** Identical opening/closing paragraphs; no response contradicts the other letter; every cross-version reference carries the old-to-new mapping.
- **Leverage the favorable referee.** Cite the other referee's positive view inside the strict referee's letter ([P7]: retention of the switching tests is justified "based on the other referee's view that the test could be expanded").
- **Disclose conflicts, offer arbitration, identically.** "The omnibus referee recommended removing this analysis from the paper, while the de-novo referee asked that its limitations be acknowledged. We have tried to seek common ground…" followed by the arbitration sentence repeated verbatim in both referee letters and near-identically in the editor letter — zero switching cost for the editor, making the authors' preferred outcome the path of least resistance (inferred).
- **Expansion vs. contraction.** When one referee adds material and another demands shortening, resolve by net accounting: migration list + quantified page count, with the shortening referee's mandate cited as the stated justification for parking ([P3]).

### 7.4 The Editor Letter

Mirror the decision letter's structure point-for-point; quote the contribution paragraph; disclose referee conflicts rather than hiding them; fold in appeal results at the editor's instruction ([P7]); keep one quiet methodological resistance carried by citation with a verification fallback. Post-appeal or post-conflict, the editor's goodwill is the binding constraint — engineer the package so the editor can verify and defend an accept without reading the manuscript (inferred).

---

## 8. Red Lines and Escalation

**Never (universal in the successful set, violated in the failed case):**

1. **Never say the referee is wrong** — and never *evaluatively discount* the referee's priorities ([P8]: "may not be an important concern for our story"; the deleted section "does not add much value"). The failed letter never used a forbidden phrase either; telling the referee his observation is *unimportant* fails the rule in spirit while passing it in letter.
2. **Never run-then-refuse.** Executing the referee's analysis and then declining the incorporation proves him right with your own table ([P8] Table R7, quoted back: "a serious omitted variables problem").
3. **Never cut the referee's requested evidence.** Cut your own indefensible claims (with the admission stated); never delete the analysis he asked to see reconciled ([P8]: "rather than providing a more convincing response, the revised draft removed the long term return analysis altogether").
4. **Never leave a direct question unanswered.** [P8]'s "not irrational after all?" received no sentence and returned in round 2 as the welfare attack on the thesis.
5. **Never scope-declare the acceptance condition.** "This is beyond the scope of our current paper" — aimed at the referee's most-repeated question — declared the paper's acceptance condition out of scope ([P8]).
6. **Never decline without an escape hatch.** "If you prefer" / "we would be pleased to" on every kept-preference decision; zero occurrences in the failed letter. (The one observed deviation in the corpus — [P4]'s unaddressed transaction-cost request — is documented in §4.9; silence is not licensed for any comment the referee marks essential or decision-relevant.)

**Escalation.** If a comment appears to require outright disagreement (a "pure disagree" move — never observed in any successful letter), escalate to the author before drafting, per the revision protocol's DISAGREE rule. Likewise escalate fundamental trade-offs the framework cannot resolve (e.g., an infeasible acceptance condition).

---

## 9. The Failure Taxonomy ([P8] Contrast Case)

What the failed response did differently, dimension by dimension, with the successful counterpart. The failure was **not** incivility and **not** under-effort — the gratitude register matched the playbook and the robustness volume (8 tables, ~20 adapted variables) exceeded it. The failure was systematic protection of the headline framing at exactly the three points conversion required.

| # | Failure mode (documented) | Successful counterpart |
|---|---|---|
| 1 | **Volume where insight was demanded.** Robustness batteries delivered where the referee asked for economic reasoning: "I find the responses either mechanical, incomplete, or lacking sufficient new economic insight." | Thesis questions get thesis answers: reframing with *new evidence* ([P2]/P3 grid), economic stories covering residuals ([P1] fn 17), magnitude decomposition with prepared landing ([P2] two-channel reframe). |
| 2 | **Run-then-refuse.** Both contested analyses executed, both incorporations declined ("we decide to continue to use Ytd-EG"; "we decide to not include it as a control"); the referee quoted the authors' own coefficients back at them. | Either comply fully (maximal scope, flat survival sentence [P6]) or decline-with-hatch ([P3] ×3). Never execute the incriminating table and then withhold it from the main text. |
| 3 | **Cut the requested evidence.** The monthly section the referee asked to have reconciled was deleted ("too long… does not add much value") — read as evasion: "leaving the revised draft presenting a less-than-complete picture." | Cut only indefensible own-claims, with the evidentiary admission stated ([P4]). Reconciliations are answered with decomposition, never deletion. |
| 4 | **Scope-declared the acceptance condition.** "Beyond the scope of our current paper" on the contribution question. | The contribution question is always answered — reframed via measurement axes ([P2]/P3), new facts ([P7] cross-asset + GS-exit), or prioritized contribution statements installed in the intro. |
| 5 | **No escape hatches.** "If you prefer": zero occurrences. | Mandatory hatch on every decline (Rule 5). |
| 6 | **Placement inverted by threat.** The two exhibits that answered the referee (residual reframe R6; surprise control R7) parked in the IA; supporting robustness promoted; R8 — the one table that could win the reconciliation — never spent on the argument it could win. | Placement tracks the acceptance condition: the evidence that answers the referee's core demand goes where he demanded it (stricter-referee rule, §7.3). |
| 7 | **Unanswered direct questions.** The rationality/welfare question never addressed; the PEAD answer implicitly conceded profitability (inferred). | Every direct question gets a sentence; concessions that open new flanks are closed in the same response ([P5] dividend move). |
| 8 | **Evaluative discounting.** "May not be an important concern for our story." | The referee's priorities are never ranked below the authors' in print; disagreement travels as evidence, reframing, or deference. |
| 9 | **Circular contribution claims.** "distinct from the alternative mechanisms… highlighting the incremental contribution" — assertion where evidence was owed. | Contribution claims are backed by new facts or demonstrated measurement differences, then installed as quotable statements repeated across letters ([P7]). |

The closest [P8] came to the playbook: comment 6 — conceding the premise, explaining the design, and benchmarking to the prior paper's identical choice — has the grant-the-premise-then-neutralize anatomy (style guide §6.7; a §4.5/§4.9 hybrid here). Even so, the round-2 verdict still lists comment 6 among the unresolved inconsistencies ("see comments 2, 6, 7, and 8 of the prior report"), so the move mitigated without converting. The craft vocabulary transferred; the strategic choices did not.

---

## 10. Pre-Send Checklist

**Triage**
- [ ] Acceptance condition identified and ordered first in the summary block?
- [ ] Every comment coded (threat × type); amplitude allocated by threat?
- [ ] Permissive language read as cost signals; enthusiasm read as the amplification list?
- [ ] Cascade risks identified and given protocols?

**Moves**
- [ ] Zero frontal disagreements; zero evaluative discounting of the referee's priorities?
- [ ] Zero run-then-refuse combinations?
- [ ] Zero cuts of referee-requested evidence?
- [ ] Every direct question answered with a sentence?
- [ ] Every decline carries an escape hatch?
- [ ] Every apology attached to an objective error only; one per error?
- [ ] Every concession monetized (robustness / mechanism / goodwill)?

**Evidence**
- [ ] New tests execute the referee's design where he specified one; oversupplied where identification is at stake?
- [ ] Premise tested before own result; column walks; benchmarks on every magnitude; exceptions counted; pre-trends attached?
- [ ] Unfavorable sub-results disclosed in the main text where they protect load-bearing claims?
- [ ] Placement follows §5.1; nothing the referee demanded sits only in the letter or IA against an incorporation demand?

**Portfolio**
- [ ] One-construction-many-debts scan done?
- [ ] Cross-referee conflicts resolved (stricter rule / redesign / identical arbitration sentence)?
- [ ] Editor can verify and defend an accept from the letter alone (mirrors, pastes, page pins, migration list, page count)?
- [ ] Migration list and old→new mappings complete?

**Escalation**
- [ ] Any comment requiring pure disagreement escalated to the author before drafting?

---

*End of guide. All quotes verbatim from `agent_tasks/response_strategy_distillation_202610202043/sources/` ([P1]–[P8]); per-pair decision analyses, comment inventories, and inference ledgers in `…/analyses/`. Claims about motive marked "(inferred)" are reconstructions from those ledgers, not statements in the letters. [P7]'s outcome is not documented in the files; [P8] is the failed contrast case.*
