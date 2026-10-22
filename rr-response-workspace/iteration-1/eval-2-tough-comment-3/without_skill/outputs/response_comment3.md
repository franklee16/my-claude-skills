# Response to Referee 1 — Comment 3

Manuscript: "Retail Attention and the Cross-Section of Stock Returns" — JFQA MS# 26-10442

*Excerpt from the response letter covering Comment 3 only. Bracketed items in [PLACEHOLDER / NOTE TO AUTHORS] form await the corresponding manuscript edit or author confirmation; all other cited changes and numbers correspond to completed revisions.*

---

**Referee Comment 3:**

> *Here is what bothers me most. The paper's story is that retail attention drives mispricing. But retail investors cannot move prices in stocks dominated by institutions. If your mechanism were real, the predictability should disappear in the high-institutional-ownership subsample — and unless I am misreading your Table 5, that is exactly what happens: the long-short spread is insignificant there. Doesn't this contradict your story? Relatedly, even in the full sample the spread of 31 bps per month is tiny — the annual turnover of this strategy would not cover its transaction costs. Please answer directly, and justify the economic magnitude of your findings.*

**Summary response.** We answer both questions directly.

First, on Table 5: the pattern the referee describes is the mechanism's own prediction, and the apparent contradiction arises because the previous draft never said so. We presented the institutional-ownership split as a robustness exercise and left its role in the argument unstated, so the referee had to reconstruct the logic himself — and reasonably read the table as working against us. A retail-attention mispricing mechanism requires two conditions: retail flow that moves prices, and arbitrage capital that is slow to correct the resulting pressure. Both conditions fail in institution-dominated stocks, so predictability should attenuate there. Table 5 shows attenuation, and the revision now presents the split as a mechanism test, backed by a formal interaction in new Table IA.2.

Second, on magnitude: the referee is right about trading costs, and we say so plainly. Gross of costs, the full-sample spread is 0.31% per month; net of realistic round-trip and borrow costs at monthly rebalancing, it is not a profitable strategy. What the 0.31% measures is mispricing — attention reallocates expected returns by 3.7% per year, 4.6% of the mean absolute deviation of monthly returns in our sample (6.8%), and by 5.3% per year (6.5% of MAD) in the low-IO subsample where the mechanism says the effect lives. A spread of this size that persists next to trading costs is informative precisely because correcting it is expensive — the same limits to arbitrage that drive the institutional-ownership heterogeneity in §3.1.

---

## 3.1 The institutional-ownership split tests the mechanism, and Table 5 passes the test

The referee's premise is also our premise. Retail order flow has the largest price impact where retail's share of trading is highest, and prices are closer to efficient where institutional ownership is high (Boehmer and Kelley, 2009). Attention shocks are measured in both subsamples — app openings occur for institution-dominated stocks as well — but where institutions dominate, their trading corrects the pressure before it becomes predictable reversal; where retail's footprint is largest, the pressure persists and shows up as return predictability.

Consider what each possible outcome would have implied. A spread of full strength in the high-IO subsample would have been the result that damaged our story: attention predicting returns where retail cannot move prices points toward a priced risk or a correlated liquidity-provision process, the alternatives raised in Comment 1. An attenuated spread concentrated where retail's footprint is largest is the mispricing channel's signature. Table 5 delivers the second pattern; the previous draft reported it without its interpretation, and the fault for the misreading is ours.

In the revision we recast the discussion and add Table IA.2 in the Internet Appendix, discussed in a new paragraph at the end of Section 4.3 (page 21):

- The long-short spread is **0.44% per month in the low-IO subsample (t = 2.62)** and **0.09% per month in the high-IO subsample (top IO tercile, Thomson Reuters 13F; t = 0.71)**. The point estimates differ by a factor of nearly five, and the full-sample 0.31% decomposes into a low-IO effect above the full-sample average and a high-IO effect indistinguishable from zero. The high-IO estimate is economically small as well as imprecise, so the attenuation is visible in the point estimates, not only in significance.
- In the interaction specification, the full-sample ATTN coefficient is **0.032 (t = 3.05)** and the **ATTN × High-IO interaction is −0.011 (t = −1.05)**: the sign the mechanism predicts, though the interaction is not significant at conventional levels. We read Table IA.2 as attenuation consistent with the institutional-arbitrage logic, with the subsample contrast (0.44 vs. 0.09) as the economically meaningful comparison; interaction tests at this split have limited power, and the revised text reports the interaction's t-statistic alongside the subsample estimates so readers can judge both.

[NOTE TO AUTHORS: confirm the new Section 4.3 paragraph (p. 21) states the interaction's insignificance explicitly, so letter and text match.]

## 3.2 Economic magnitude

Direct answer first, as the referee requests: gross of costs, the full-sample spread is 0.31% per month. Attention is transient, so monthly sorts turn over quickly, and round-trip costs plus the borrow costs of the short leg exhaust the gross return. We agree that the strategy is not implementable net of costs at monthly frequency, and the revision says so rather than leaving the reader to infer it.

[PLACEHOLDER — add to the end of the Section 4.3 paragraph (p. 21): one sentence stating that the spread is evidence of mispricing, with the MAD comparison, and that a monthly long-short implementation does not clear realistic transaction costs. Letter and manuscript should land together.]

What remains is to justify the magnitude, on three margins where the number is informative:

1. **Against return variation.** The mean absolute deviation of monthly stock returns in the sample is 6.8%. The full-sample spread of 0.31% per month is 4.6% of that MAD; the low-IO spread of 0.44% is 6.5%. The attention sort separates high- from low-ATTN stocks by an expected-return spread equal to a meaningful share of typical monthly price movement.

2. **Against established premiums.** 0.31% per month compounds to roughly 3.7% per year, the same order as the long-run average monthly value premium (on the order of 35–40 bps). The attention spread is not an outlier in either direction; it is the size at which cross-sectional predictability normally arrives.

3. **Against the cost reality of the anomalies literature.** Momentum's gross profits fail the same net-of-cost test (Lesmond, Schill, and Zhou, 2004), and most published anomalies are marginal once realistic price impact is charged (Novy-Marx and Velikov, 2016). Net-of-cost tradability separates who can harvest a distortion from whether prices are distorted. The natural harvesters here are low-cost arbitrage capitals — the institutions of §3.1.

Finally, the persistence of the spread is itself part of the evidence. If 31 bps per month were freely harvestable it would already be arbitraged away (Shleifer and Vishny, 1997); returns to supplying liquidity against attention-driven flow are earned exactly when correction is costly and constrained (Nagel, 2012). The spread survives in the low-IO subsample, where correcting it is expensive, and disappears in the high-IO subsample, where institutional capital sits closest to the stock. The referee's two objections — the insignificant high-IO spread and the cost-constrained full-sample spread — are two faces of one fact: attention-driven mispricing is created where retail is present and corrected where institutions are.

Both changes are in the revised manuscript: the recast discussion and Table IA.2 at the end of Section 4.3 (page 21), with the magnitude discussion above.

---

### References cited in this response (for the letter's reference list)

- Boehmer, E., and E. Kelley, 2009, Institutional investors and the informational efficiency of prices, *Review of Financial Studies* 22, 3563–3594.
- Lesmond, D., M. Schill, and C. Zhou, 2004, The illusory value of momentum profits, *Review of Financial Studies* 17, 349–380.
- Nagel, S., 2012, Evaporating liquidity, *Review of Financial Studies* 25, 2005–2039.
- Novy-Marx, R., and M. Velikov, 2016, Who's afraid of transaction costs? A realistic evaluation of anomaly profits. [AUTHOR: verify exact title and venue]
- Shleifer, A., and R. Vishny, 1997, The limits of arbitrage, *Journal of Finance* 52, 35–55.
