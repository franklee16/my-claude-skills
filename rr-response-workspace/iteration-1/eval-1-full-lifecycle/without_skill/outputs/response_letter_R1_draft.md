# Responses to the Report from Referee 1 on the Manuscript Titled "Retail Attention and the Cross-Section of Stock Returns" (JFQA MS# 26-10442, Revised)

> **DRAFT — NOT FOR SUBMISSION.** All items marked **[PLACEHOLDER — …]** depend on analyses that are not yet run (see `response_plan_R1.md`) or on pointers to be confirmed against the revised manuscript. Numbers *not* marked as placeholders come from the completed items in the revision changelog and may be cited. Sentences describing in-progress work are written in completion voice so the letter reads as it will at submission; they must not be submitted until the underlying results exist and every placeholder is resolved. Delete this note before submission.

---

Thank you very much for your detailed and constructive report on our manuscript, and for the care with which you read the paper. Your comments pressed us on the interpretation of our attention measure, on the relation between our results and the prior literature, and on the economic magnitude of our findings. The paper has clearly improved because of the resulting changes. For ease of reference, we paste your comments below in italics, followed by our response to each comment.

**Summary of major changes in this version of the paper:**

1. **The liquidity-provision channel (Comment 1).** We obtained daily bid-ask spreads and dollar volume for 2020–2024 from Bloomberg and constructed the liquidity-provision return measure of Wang (2021), following the specification in his Table 2. We use this measure to test whether ATTN retains stand-alone predictive content once the liquidity-provision channel is controlled for, in three steps: we first replicate the liquidity-provision predictability in our own sample; we then enter the measure as a control in our baseline tests and as a conditioning variable in conditional portfolio sorts; and we re-estimate our baseline results with ATTN orthogonalized to the measure. The results are reported in **[PLACEHOLDER — Table/Section of the revised manuscript]** and in Table R1 to this response.

2. **Sample extension through December 2024 (Comment 1a).** All tests are re-run on the extended sample, which covers the attention episodes of 2023–2024 and adds power to the liquidity-provision comparison and to the institutional-ownership moderation below.

3. **Reconciliation with Zhang (2022) (Comment 2).** We replicate Zhang (2022) in our sample, starting from his exact specification, and rotate each element of the specification toward ours one at a time (measure, filters, horizon, weighting). The full grid is reported in Table R2 to this response, and the revised Section 2.1 states explicitly how our Table 3 relates to his findings. **[PLACEHOLDER — grid results pending.]**

4. **Institutional-ownership moderation (Comment 3).** We have added Table IA.2 in the Internet Appendix, which interacts ATTN with a high-institutional-ownership indicator (top tercile of institutional ownership from Thomson Reuters 13F holdings). In the full sample, the baseline ATTN coefficient is 0.032 (t-stat. = 3.05) and the ATTN × High-IO interaction is −0.011 (t-stat. = −1.05). In subsample splits, the long-short spread is 0.44% per month (t-stat. = 2.62) among low-IO stocks and 0.09% per month (t-stat. = 0.71) among high-IO stocks. These results are discussed in a new paragraph at the end of Section 4.3 (page 21).

5. **Economic magnitude (Comment 3).** We now state explicitly that the full-sample spread does not survive transaction costs, and we benchmark the magnitude of the spread against the distribution of monthly returns in our sample. **[PLACEHOLDER — pointer to the new magnitude discussion.]**

6. **References and typos (Comments 4 and 5).** Wang (2021) and Zhang (2022) are now cited in the Introduction (page 3, footnote 5) and in the related-literature discussion (Section 2.1, page 8). The typo on page 12 is corrected.

**In response to comments in your report:**

---

*1. Throughout the paper, the "ATTN" measure is constructed from daily app openings per stock. But app openings rise when trading volume rises, and Wang (2021, JF) shows that returns to liquidity provision — rebalancing activity by market makers around high-volume days — generate substantial return predictability on its own. In other words, your measure may simply be picking up liquidity-provision returns rather than attention-driven mispricing. If both mechanisms are at work, your headline result does not establish that attention matters. Please provide evidence that ATTN has stand-alone predictive content beyond liquidity-provision returns.*

Thank you very much for pointing out this very important issue. We agree that whether ATTN has predictive content stand-alone from liquidity-provision returns is the central question for our paper, and we have organized this revision around answering it with new evidence.

Your concern can be stated as a conditional. If app openings rise mechanically with trading volume, and if the returns to liquidity provision documented by Wang (2021) predict the cross-section of returns on their own, then ATTN may be picking up liquidity-provision returns rather than attention-driven mispricing, and our headline result would not establish that attention matters. We agree that if both premises hold, this indeed poses an empirical threat to the stand-alone predictive content of ATTN. We have therefore designed the revision to test each premise directly.

To evaluate this possibility, we obtained daily bid-ask spreads and dollar volume for 2020–2024 from Bloomberg and constructed the liquidity-provision return measure following the specification in Table 2 of Wang (2021). Our analysis proceeds in three steps.

First, we test your premise in our own sample: we replicate the liquidity-provision predictability in our universe and report its strength before defending our own result. **[PLACEHOLDER — premise-test results: coefficient and t-stat. of the LP measure's predictive content in our sample.]**

Second, we enter the liquidity-provision measure directly into our tests. We include it as an additional control in the baseline Fama-MacBeth regressions, and we repeat the portfolio sorts of Table 3 as conditional double sorts on the liquidity-provision measure. **[PLACEHOLDER — ATTN coefficient with and without the LP control, with t-statistics; conditional-sort alphas.]**

Third, we orthogonalize ATTN with respect to the liquidity-provision measure and re-estimate the baseline tests using the residualized measure. **[PLACEHOLDER — residualized-ATTN results.]**

**[PLACEHOLDER — concluding sentence, to be written from the results only, e.g.: "Overall, the above results suggest that the return predictability of ATTN is not subsumed by the liquidity-provision channel of Wang (2021)." Do not use any version of this sentence unless the numbers support it; if they do not, escalate before finalizing.]** The results are reported in **[PLACEHOLDER — Table/Section of the revised manuscript]** and in Table R1 to this response, and are discussed in **[PLACEHOLDER — new subsection, page]** of the revised manuscript.

In addition, the institutional-ownership moderation we report in response to your Comment 3 below offers a complementary distinction between the two channels; we extend that comparison to the liquidity-provision measure in **[PLACEHOLDER — pointer]**.

---

*1a. On a related note, the sample ends in December 2022. The 2023-2024 period saw several attention episodes that would sharpen your tests. Extending the sample would help, though I leave this to the authors.*

Thank you for this suggestion. We have extended the sample through December 2024. The extension covers the attention episodes of 2023–2024, and it adds power to the tests throughout the paper, including the liquidity-provision comparison above and the institutional-ownership moderation in response to Comment 3 below. All tables are updated on the extended sample, and the original-sample results are retained in the Internet Appendix for comparison. **[PLACEHOLDER — confirm final end date, list of updated tables, and IA placement.]**

---

*2. Table 3 of the paper reports that high-ATTN portfolios UNDERPERFORM low-ATTN portfolios by roughly 40 bps per month, which the authors interpret as attention-driven overpricing. This directly contradicts Zhang (2022, JFE), who finds that retail attention is associated with HIGHER subsequent returns on essentially the same stock universe, using the same CRSP/Compustat filters you describe in Section 2. Two papers using the same data cannot both be right about the sign. Please reconcile your Table 3 with Zhang (2022), or remove the portfolio-sorting section from the paper.*

Thank you for raising this important issue. We agree that the sign difference between our Table 3 and the findings of Zhang (2022) calls for an explicit reconciliation, and that this reconciliation has to be empirical. Two results built on the same underlying universe can carry opposite signs when they are constructed at different points of the specification space, with different attention measures, holding horizons, or weighting schemes. Which axis the sign turns on is an empirical question, and we agree the paper must show it rather than assert it.

Following your suggestion, we now cite and discuss Wang (2021) and Zhang (2022) in the Introduction (page 3, footnote 5) and in the related-literature discussion (Section 2.1, page 8) of the revised manuscript.

To reconcile the two sets of results, we replicate Zhang (2022) in our sample, starting from his exact specification (his attention measure, his CRSP/Compustat filters, his portfolio construction, and his holding horizons), and then rotate each element toward ours one at a time:

(1) Zhang's measure with Zhang's full specification in our sample: **[PLACEHOLDER — replication result, sign and t-stat.]**

(2) Zhang's measure with our filters and holding horizon: **[PLACEHOLDER.]**

(3) Our ATTN with Zhang's filters and holding horizon: **[PLACEHOLDER.]**

(4) Equal-weighted versus value-weighted portfolios, for both measures: **[PLACEHOLDER.]**

We report the full grid whatever it shows. **[PLACEHOLDER — reconciliation summary: the axis along which the sign flips and the resulting statement of how Table 3 relates to Zhang (2022); to be written from the grid results only. The grid is reported in Table R2 to this response and discussed in Section 2.1 and in the portfolio-sorting section of the revised manuscript.]**

---

*3. Here is what bothers me most. The paper's story is that retail attention drives mispricing. But retail investors cannot move prices in stocks dominated by institutions. If your mechanism were real, the predictability should disappear in the high-institutional-ownership subsample — and unless I am misreading your Table 5, that is exactly what happens: the long-short spread is insignificant there. Doesn't this contradict your story? Relatedly, even in the full sample the spread of 31 bps per month is tiny — the annual turnover of this strategy would not cover its transaction costs. Please answer directly, and justify the economic magnitude of your findings.*

Thank you very much for this comment, and for asking us to answer directly. We will. Your comment contains two questions: whether the institutional-ownership pattern contradicts our story, and whether the magnitude of the spread is economically meaningful. We take them in turn.

**On the subsample pattern.** You are reading Table 5 correctly: the long-short spread is statistically insignificant in the high-institutional-ownership subsample. Where the original draft fell short is that it left the meaning of this pattern implicit. Stated plainly, the pattern is what our mechanism predicts. Retail attention moves prices through retail order flow. In stocks dominated by institutions, the same attention-driven flow meets deeper arbitrage capacity, prices stay closer to fundamental value, and the attention-driven spread should be muted. The moderation you describe is therefore the mechanism's own signature in the cross-section. Your comment supplied the test, and we have now formalized it.

We apologize for leaving this implication implicit in the original draft rather than stating and testing it. Following your comment, we have added Table IA.2 in the Internet Appendix, which interacts ATTN with a high-institutional-ownership indicator (top tercile of institutional ownership from Thomson Reuters 13F holdings), together with a new paragraph at the end of Section 4.3 (page 21) of the revised manuscript. Three findings. The baseline ATTN coefficient in the full sample is 0.032 (t-stat. = 3.05). The ATTN × High-IO interaction enters with the negative sign the mechanism predicts, at −0.011 (t-stat. = −1.05). In the subsample splits, the long-short spread is 0.44% per month (t-stat. = 2.62) among low-IO stocks and 0.09% per month (t-stat. = 0.71) among high-IO stocks.

We want to be fully transparent about the strength of this evidence. The interaction is negative as predicted but statistically insignificant, so the subsample contrast is suggestive rather than significant at conventional levels, and the revised Section 4.3 says so explicitly. Two extensions sharpen the test: re-estimating the interaction with continuous institutional ownership in place of the tercile indicator, and re-estimating it on the extended sample, which covers the attention episodes of 2023–2024. **[PLACEHOLDER — continuous-IO interaction result; interaction on the extended sample.]**

**On the economic magnitude.** You are right, and we now say so in the paper: the full-sample spread does not survive transaction costs, and a strategy that traded on it would not be profitable after costs. **[PLACEHOLDER — pointer to the revised magnitude discussion.]** We would add two considerations on what the number means.

First, the spread measures mispricing, not the net profit of an implementable strategy. The object of the paper is the price impact of retail attention, and that object stands regardless of whether an arbitrageur could harvest it net of costs.

Second and more importantly, the transaction-cost arithmetic is part of the mechanism. A spread of this size persists in equilibrium precisely because it is too small, after costs, for arbitrageurs to remove. Your calculation therefore speaks to why the mispricing we document survives, and we have added this discussion to the revised manuscript.

As benchmarks for size: the full-sample spread of 0.31% per month equals about 4.6% of the mean absolute deviation of monthly returns in our sample (6.8%); the Table 3 portfolio spread you cite, at roughly 0.40% per month, equals about 5.9%; and the low-IO subsample spread of 0.44% per month equals about 6.5%. Annualized, the full-sample and low-IO spreads correspond to approximately 3.7% and 5.3% per year. We acknowledge that this baseline effect is modest in absolute terms, and we have toned the language of the paper accordingly. **[PLACEHOLDER — confirm tone-down edits in the Abstract and Introduction.]**

---

**In response to minor comments in your report:**

---

*4. Page 12, second paragraph: "the their attention measure" — typo.*

Thank you for the careful reading of our paper. We have corrected this typo on page 12; the passage now reads "their attention measure."

---

*5. The paper should cite Wang (2021) and Zhang (2022) when discussing the related literature in the Introduction; the current draft engages neither.*

Thank you for this suggestion. In the revised manuscript, we now cite Wang (2021) and Zhang (2022) in the Introduction (page 3, footnote 5) and in the related-literature discussion (Section 2.1, page 8).

---

**References**

Wang, [initials], 2021, [article title], *Journal of Finance* [volume, pages]. **[COMPLETE FROM THE PAPER BEFORE SUBMISSION]**

Zhang, [initials], 2022, [article title], *Journal of Financial Economics* [volume, pages]. **[COMPLETE FROM THE PAPER BEFORE SUBMISSION]**

---

Once again, we appreciate your detailed, constructive, and insightful feedback.

The authors.
