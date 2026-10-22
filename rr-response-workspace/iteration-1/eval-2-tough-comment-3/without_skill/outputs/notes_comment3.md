# Drafting Notes — Response to Referee 1, Comment 3

Companion to `response_comment3.md`. Inputs used: `referee_report_R1.txt` and `changelog.md` only. The letter cites only changelog items marked Completed; everything else is flagged below.

## 1. The strategic problem, and why the draft takes this line

Comment 3 packs two attacks that feel lethal together: the mechanism's own subsample test "fails" in Table 5, and the headline spread is too small to trade. Reasoning from the mechanism itself:

- The retail-attention mispricing story requires (a) retail flow with price impact and (b) slow arbitrage correction. Both conditions vary cross-sectionally with institutional ownership: retail's share of volume is low and price efficiency is high where institutions dominate (Boehmer–Kelley logic).
- Therefore the mechanism *predicts* attenuation of the spread in high-IO stocks. The referee states this prediction himself, observes Table 5 matches it, and then calls the match a contradiction. The contradiction is in the comment, not in the paper — but saying so bluntly wins nothing. The draft's true vulnerability is that it presented Table 5 as a bare robustness check with no interpretation, which invited exactly this reading.
- Magnitude: the referee demands a direct answer, so the letter concedes tradability outright (a monthly sort on a transient signal cannot clear round-trip plus borrow costs) and defends the number on the mispricing margin instead: 0.31%/mo vs. 6.8% MAD of monthly returns, 3.7%/yr annualized, same order as the long-run value premium, and the same net-of-cost failure shared by established anomalies (momentum after Lesmond et al. 2004).
- The unifying move (end of §3.2): persistence of the spread where correction is expensive and its disappearance where institutional capital sits are two faces of one limits-of-arbitrage fact. The referee's two objections jointly *are* the mechanism's signature. This turns his strongest comment into the paper's mechanism evidence.

Concession economy: exactly two concessions, each made once — (i) the exposition failure on Table 5 was ours; (ii) the strategy is not net-of-cost profitable. No groveling, no re-hedging after results.

## 2. Evidence ledger (every number in the letter)

| Item in letter | Source | Basis |
|---|---|---|
| 31 bps full-sample spread (0.31%) | Referee's own reading of Table 5 | [KNOWN, from report] |
| Low-IO spread 0.44%/mo, t = 2.62 | changelog, Completed (Table IA.2) | citable |
| High-IO spread 0.09%/mo, t = 0.71; top-tercile IO, TR 13F | changelog, Completed | citable |
| Full-sample ATTN coeff. 0.032, t = 3.05 | changelog, Completed | citable |
| ATTN × High-IO = −0.011, t = −1.05 | changelog, Completed | citable |
| MAD of monthly returns 6.8% | changelog, Completed | citable |
| 3.7%/yr (0.31×12); 5.3%/yr (0.44×12) | computed | [COMPUTED] |
| 4.6% and 6.5% of MAD (0.31/6.8; 0.44/6.8) | computed | [COMPUTED] |
| "differ by a factor of nearly five" (0.44/0.09 = 4.9) | computed | [COMPUTED] |
| Value premium "on the order of 35–40 bps/mo" long-run | external knowledge | [KNOWN, MED confidence — verify against current FF HML series before sending] |
| Turnover/cost claim (qualitative only) | reasoning | [INFERRED] — no turnover stat exists in changelog; letter deliberately avoids quoting a turnover number |

## 3. External facts to verify before the letter goes out

1. Novy-Marx & Velikov transaction-costs paper — exact title and venue (I believe RFS ~2016). Already flagged inline in the letter's reference list.
2. Value-premium long-run monthly average (~35–40 bps) — pull the current Ken French HML series and use the exact figure and window.
3. Boehmer & Kelley (2009, RFS), Nagel (2012, RFS), Lesmond–Schill–Zhou (2004, RFS), Shleifer–Vishny (1997, JF) — page ranges in the letter's mini reference list are from memory; check against the bibliography.
4. Whether "low-IO subsample" in Table IA.2 is the bottom IO tercile or the complement of the top tercile — the letter mirrors the changelog's wording and defines only the high-IO side as top tercile. State the low-IO construction precisely in both letter and Table IA.2 notes.

## 4. Deliberate omissions (and why)

- **No entanglement with Comment 1.** The liquidity-provision analysis is In Progress; per changelog rules it gets placeholders in its own response, not here. Substantively, I did *not* argue that the IO split discriminates against the Wang (2021) channel: liquidity-provision premia also concentrate in illiquid, low-IO stocks, so the split cannot separate the two mechanisms cleanly. Claiming it does would hand the referee an easy second-round kill. The letter only makes the one-way statement (a *strong* high-IO spread would have favored the alternatives).
- **No Comment 2 / Table 3 numbers.** Not Started per changelog; also Table 3's ~40 bps vs. Table 5's 31 bps presumably differ by specification, which is Comment 2's business. Mixing them here would create an unexplained discrepancy inside this response.
- **No fabricated turnover or cost-adjusted-return figures.** None exist in the changelog; the referee's turnover point is conceded qualitatively.
- **No claim that the paper "now states" the costs concession** — that edit is not in the changelog, hence the placeholder rather than a citation.

## 5. Placeholders in the letter (must resolve before sending)

1. [NOTE TO AUTHORS] — confirm the Section 4.3, p. 21 paragraph discloses the insignificant interaction (t = −1.05). Disclosing it ourselves, once, in active voice, is cheaper than the referee discovering it.
2. [PLACEHOLDER] — the costs/MAD sentence to append to the same paragraph. Add the edit to the changelog as Completed, then un-placeholder the letter.

## 6. Predicted second-round asks (prep list, in priority order)

1. **Size control.** IO correlates strongly with market cap; referee can say attenuation is a large-cap effect, not an institutional-arbitrage effect. Prep: IO interaction within size terciles, or double sorts IO×size, or size as FM control in the interaction spec.
2. **Formal spread test.** Our interaction is insignificant (t = −1.05); the referee may note the heterogeneity itself is not significant. Prep: bootstrap or pooled test of the low-IO vs. high-IO spread difference in the *portfolio* space (not just the FM coefficient).
3. **Turnover and cost-adjusted returns.** Once we concede costs, he may ask for the actual number. Prep: annual one-way turnover of the sort, Frazzini-style or Novy-Marx–Velikov-style cost adjustment, breakeven cost level.
4. **Longer horizons.** If attention-driven reversal persists at quarterly holding, turnover falls. Run before claiming.
5. **Arbitrage-cost proxies.** Short interest / borrow fees / IO dispersion as moderators would convert the limits-of-arbitrage story from interpretation to evidence.
6. **Consistency sweep.** Once Comment 2 (sign vs. Zhang 2022) is resolved, make sure the reframed "mispricing where retail can move prices" language agrees everywhere (abstract, intro, Table 5 notes).

## 7. Voice and format choices

Direct answers first in both sub-responses (the referee explicitly demanded "answer directly"). Verbatim comment quoted before the response. Concession once, no trailing hedges after results. The reframing of the referee's own premise ("The referee's premise is also our premise") states agreement before disagreement. Em-dashes restricted; no filler transitions; enumeration used only where literally three comparisons exist.
