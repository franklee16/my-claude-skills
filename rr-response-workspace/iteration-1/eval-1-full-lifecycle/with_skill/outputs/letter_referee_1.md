<!-- DRAFT STATUS — NOT SEND-READY (2026-10-21). Unresolved placeholders are pending-by-design:
     Comment 1 analysis (liquidity-provision premise test, double sorts, discriminator) not yet run;
     Comment 1a sample extension cleaning in progress; Comment 2 Zhang (2022) replication not started;
     Section 4.3 revised-paragraph paste, referee-credit footnote number, transaction-cost treatment,
     and full Wang/Zhang references unconfirmed. Ship only when all placeholders resolve to zero,
     per response_plan.md send-readiness checklist. Frank's final confirmation required; never send. -->

**Responses to the Report from Referee 1 on the Manuscript Titled "Retail Attention and the Cross-Section of Stock Returns" (JFQA MS# 26-10442, Revised)**

Dear Referee,

Thank you very much for all the helpful and insightful comments and suggestions on the earlier version of our manuscript. In this revision, we have made every effort to incorporate your suggestions and comments. The paper has clearly improved because of these changes. Below, we reproduce your comments point by point in *italics* and then give our responses.

<!-- SRC: style §5.1 (P1) — opening gratitude + improvement sentences; §8.1 (P1) — convention sentence; §2 (P6) — salutation -->

Before responding to the specific points in your report, we would like to summarize our major changes in the paper: <!-- SRC: style §2[4] (P1) — summary lead-in -->

1. **New evidence on the stand-alone predictive content of ATTN (Comment 1).** We have obtained daily bid-ask spreads and dollar volume from Bloomberg and are constructing the liquidity-provision return measure of Wang (2021), following the specification of his Table 2. We are testing whether ATTN retains predictive content beyond this measure, and will report the results in a new subsection of the revised manuscript [Section ?, p. ? — CONFIRM; results TBD].
2. **Institutional-ownership partition (Comment 3).** We have added a new table, Table IA.2 in the Internet Appendix, which interacts ATTN with a high-institutional-ownership indicator, and we discuss it in a new paragraph at the end of Section 4.3 (page 21). The long-short spread is 0.44% per month (t-stat. = 2.62) in the low-IO subsample and 0.09% per month (t-stat. = 0.71) in the high-IO subsample.
3. **Reconciliation with Zhang (2022) (Comment 2).** We are replicating Zhang (2022) in its exact specification on our stock universe, and will reconcile the sign difference along the specification dimensions that differ between the two analyses [results TBD].
4. **Sample extension to 2024 (Comment 1a).** The 2023–2024 data have been pulled and cleaning is in progress; we will re-estimate the main tables (including Table 3) on the extended sample [results TBD].
5. **References and typo (Comments 4 and 5).** Wang (2021) and Zhang (2022) are now cited in the Introduction (page 3, footnote 5) and in Section 2.1 (page 8); the typo on page 12 is corrected.

**Detailed Responses to the Referee's Comments** <!-- SRC: style §2[5] (P1) — bridge header -->

***Major Comments*** <!-- referee's own heading preserved -->

> *1. Throughout the paper, the "ATTN" measure is constructed from daily app openings per stock. But app openings rise when trading volume rises, and Wang (2021, JF) shows that returns to liquidity provision — rebalancing activity by market makers around high-volume days — generate substantial return predictability on its own. In other words, your measure may simply be picking up liquidity-provision returns rather than attention-driven mispricing. If both mechanisms are at work, your headline result does not establish that attention matters. Please provide evidence that ATTN has stand-alone predictive content beyond liquidity-provision returns.*

Thank you very much for pointing out this very important issue. <!-- SRC: style §5.1 (P1) --> We agree that app openings can rise with trading volume, and that the returns to liquidity provision documented in Wang (2021) generate return predictability on their own. If both are at work in our measure, it indeed poses an empirical threat to the stand-alone return predictability of ATTN. <!-- SRC: style §6.7 (P4) — grant-the-threat template -->

To evaluate this possibility, we obtain daily bid-ask spreads and dollar volume (2020–2024) from Bloomberg, and are constructing the liquidity-provision return measure of Wang (2021), following the specification of his Table 2. <!-- SRC: style §7.1 (P4) — "To evaluate this possibility, we obtain … from Bloomberg" -->

The analysis proceeds in three steps. First, we verify whether the liquidity-provision measure of Wang (2021) replicates in our own sample, so that the premise of the concern is established in our data before we evaluate ATTN against it [premise results TBD]. <!-- SRC: style §7.1 (P4) — "We first verify whether …"; strategy §5.2 — premise tested before own result --> Second and more importantly, we examine whether the predictive content of ATTN is subsumed by that of the liquidity-provision measure, using independent sorts and multivariate regressions in which both measures enter side by side [results TBD]. <!-- SRC: style §9.5 (P4) — "Second and more importantly, …" --> Third, we examine whether ATTN predicts outcomes associated with retail attention that volume-based measures do not [discriminator outcomes TBD]. <!-- SRC: style §8.2 (P2) — "First, … Second, … Finally, …" enumeration --> The results will be reported in a new subsection of the revised manuscript [Section ?, p. ? — CONFIRM], with supporting tables to this response [to be appended — analysis in progress]. <!-- SRC: style §7.5 (P1) — response-only exhibit convention -->

> *1a. On a related note, the sample ends in December 2022. The 2023-2024 period saw several attention episodes that would sharpen your tests. Extending the sample would help, though I leave this to the authors.*

Thank you for this suggestion. <!-- SRC: style §5.1 (P3) --> Following your suggestion, we are extending the sample through 2024; the data have been pulled and cleaning is in progress. <!-- SRC: style §5.2 (P1) — "Following your suggestion, we have …", tense adapted to actual status --> The extension covers the attention episodes you mention, and it also strengthens the tests for the liquidity-provision channel that we describe in our response to Comment 1. We will re-estimate the main tables (including Table 3) on the extended sample and report the estimates in the revised manuscript [results TBD].

> *2. Table 3 of the paper reports that high-ATTN portfolios UNDERPERFORM low-ATTN portfolios by roughly 40 bps per month, which the authors interpret as attention-driven overpricing. This directly contradicts Zhang (2022, JFE), who finds that retail attention is associated with HIGHER subsequent returns on essentially the same stock universe, using the same CRSP/Compustat filters you describe in Section 2. Two papers using the same data cannot both be right about the sign. Please reconcile your Table 3 with Zhang (2022), or remove the portfolio-sorting section from the paper.*

Thank you for raising these important issues. We agree with you that the opposite signs in our Table 3 and in Zhang (2022) must be reconciled. <!-- SRC: style §5.1 (P2) — gratitude + agreement templates -->

Following your suggestion to reconcile the two results, we are replicating Zhang (2022) in its exact specification on the stock universe and CRSP/Compustat filters described in Section 2 of our paper. <!-- SRC: style §5.2 (P1); strategy §4.3 (P2/P3) — replicate the prior paper in its exact specification --> We then re-estimate our portfolio sorts along the specification dimensions on which the two analyses differ [dimensions TBD after the replication]. The replication and the grid will be reported in tables to this response [to be appended — analysis in progress], and we will summarize the outcome in the discussion of Table 3 in the revised manuscript [Section ?, p. ? — CONFIRM]. Once the grid is complete, we expect to conclude in the form: "Overall, the above comparison suggests that the difference between our paper and Zhang (2022) is mainly caused by [TBD]." <!-- SRC: style §6.5 (P2/P3) — reconciliation closer template -->

> *3. Here is what bothers me most. The paper's story is that retail attention drives mispricing. But retail investors cannot move prices in stocks dominated by institutions. If your mechanism were real, the predictability should disappear in the high-institutional-ownership subsample — and unless I am misreading your Table 5, that is exactly what happens: the long-short spread is insignificant there. Doesn't this contradict your story? Relatedly, even in the full sample the spread of 31 bps per month is tiny — the annual turnover of this strategy would not cover its transaction costs. Please answer directly, and justify the economic magnitude of your findings.*

Thank you very much for providing the potential mechanism and empirical test. <!-- SRC: style §5.1 (P1) --> We agree that if retail attention drives mispricing, the predictability should be concentrated in stocks where retail investors' trading can move prices, and should disappear in the high-institutional-ownership subsample. <!-- SRC: style §4(d) (P2) — "We agree that … should be stronger when …" conjecture-agreement template -->

To answer your question directly: no, the pattern you identify in Table 5 does not contradict our story; it is the pattern our mechanism predicts, for the reason you give. <!-- functional direct answer (red line: every direct question gets a sentence); confirmation carried by the templates that follow --> The fact that the long-short spread is insignificant in the high-institutional-ownership subsample is *not* inconsistent with the attention-driven mispricing story, and our revised draft now presents this partition as the paper's mechanism evidence. <!-- SRC: style §6.3 (P1) — "may not be necessarily inconsistent" template; §6.8 (P5) — italics on the operative word -->

Following your suggestion, we have now added a new table, Table IA.2 in the Internet Appendix, which interacts ATTN with a high-institutional-ownership indicator (the top tercile of institutional ownership, measured from Thomson Reuters 13F holdings). <!-- SRC: style §5.2 (P2) — "we have now …"; §9.2 (P1) — "we have now added a new table" --> We discuss the results in a new paragraph at the end of Section 4.3 (page 21) of the revised manuscript [revised passage — CONFIRM], and reproduce the key estimates in Table R1 to this response for the ease of your reference. <!-- SRC: style §7.8 (P4) — revised-prose pointer; §9.7 (P6) — "for the ease of your reference" --> In the full sample, the coefficient on ATTN is 0.032 (t-stat. = 3.05). In the interaction specification, the coefficient on ATTN × High-IO is -0.011 (t-stat. = -1.05) and statistically insignificant, indicating that the predictive content of ATTN is concentrated outside the high-institutional-ownership stocks. In the low-IO subsample alone, the long-short spread is 0.44% per month (t-stat. = 2.62); in the high-IO subsample alone, it is 0.09% per month (t-stat. = 0.71). <!-- SRC: style §7.2 (P2) — column-by-column walk; §7.3 — t-statistics inline --> Overall, the predictability is concentrated precisely where retail investors' trading can move prices, consistent with your conjectured mechanism. <!-- SRC: style §5.7 (P1) — "consistent with your conjectured mechanism"; §9.6 (P2) — "Overall," takeaway --> We acknowledge your help in footnote [footnote number — CONFIRM]. <!-- SRC: style §8.10 (P6) — bilateral credit -->

On the economic magnitude, we also agree that the full-sample spread of 31 basis points per month that you reference is modest in absolute terms, and we acknowledge this explicitly in the revised discussion at the end of Section 4.3 (page 21). <!-- SRC: strategy §4.6 (P7) — "We acknowledge that this baseline effect is modest in absolute terms" --> Two points justify the economic magnitude of our findings. <!-- SRC: strategy §4.6 (P7) — anchor-rebuild sequence --> First, in the low-IO subsample, where the mechanism operates, the spread is 0.44% per month (t-stat. = 2.62), which is about 6.5% of the mean absolute deviation of monthly stock returns in our sample (6.8%). <!-- SRC: style §7.4 (P5/P6) — magnitude paired with benchmark --> Second, the full-sample spread averages across stocks where the mechanism operates and stocks where, as you note, retail investors cannot move prices; the subsample magnitudes in Table IA.2 are therefore the economically relevant ones for our story. <!-- SRC: strategy §4.6 — amplification/distributional anchor carries the claim --> We are revising the discussion of economic magnitude accordingly [revised passage and treatment of any language that reads the spreads as tradable-strategy returns — CONFIRM]. <!-- SRC: strategy §4.6 step 1 (P7) — unconditional removal of what the referee named; §7.8 (P4) --> We would be pleased to move Table IA.2 to the main paper if you prefer. <!-- SRC: style §6.9 (P3) — escape hatch -->

**In response to minor comments in your report:** <!-- SRC: style §2[6] (P2) — two-bucket minor header -->

***Minor Comments*** <!-- referee's own heading preserved -->

> *4. Page 12, second paragraph: "the their attention measure" — typo.*

Thank you for the careful reading of our paper. We have corrected this typo on page 12, second paragraph, of the revised manuscript. <!-- SRC: style §5.6 (P2) — typo concession template -->

> *5. The paper should cite Wang (2021) and Zhang (2022) when discussing the related literature in the Introduction; the current draft engages neither.*

Thank you for your suggestions on additional references. In the revised paper, we now cite Wang (2021) and Zhang (2022) in multiple places, including the Introduction (page 3, footnote 5) and the related-literature discussion (Section 2.1, page 8). <!-- SRC: style §5.1 (P4) — additional-references template -->

**References** <!-- SRC: style §2[7] (P1–P4) — letter carries its own References block -->

- Wang, [initials — CONFIRM], 2021, [title — CONFIRM], *Journal of Finance* [volume, pages — CONFIRM].
- Zhang, [initials — CONFIRM], 2022, [title — CONFIRM], *Journal of Financial Economics* [volume, pages — CONFIRM].

**Table R1: ATTN and institutional ownership — key estimates from Table IA.2 of the Internet Appendix (reproduced for the ease of your reference)** <!-- SRC: style §7.5 (P6) — mirror-table pattern -->

| | Estimate | *t*-statistic |
|---|---|---|
| ATTN coefficient, full sample | 0.032 | 3.05 |
| ATTN × High-IO (top-tercile institutional ownership) | -0.011 | -1.05 |
| Long-short spread, low-IO subsample | 0.44% per month | 2.62 |
| Long-short spread, high-IO subsample | 0.09% per month | 0.71 |

*Notes:* High-IO is an indicator for the top tercile of institutional ownership, measured from Thomson Reuters 13F holdings. The full table, including controls, sample sizes, and specification details, is Table IA.2 of the Internet Appendix, discussed in Section 4.3 (page 21) of the revised manuscript. [Additional table details — CONFIRM.]

Once again, we appreciate your detailed, constructive, and insightful feedback.

The authors. <!-- SRC: style §9.10 (P2/P3) — closing ritual -->
