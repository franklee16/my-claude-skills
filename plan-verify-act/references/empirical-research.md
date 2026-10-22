# Empirical Research Playbook — economics & finance

Deep verification rules for econometric subtasks. This extends Section 2
(Data analysis) of `verification-playbook.md`; read that first for the
generic rules (row-count reconciliation, independent re-derivation, seeds).
This file assumes a research-grade deliverable: a paper table, a referee
response, or a result someone will build on.

Organizing principle: verify in the order errors propagate — sample
construction errors invalidate everything downstream, so they are checked
first and hardest. A significant coefficient on a corrupted sample is not
a finding; it is a liability.

## Table of contents
1. Sample construction & data integrity
2. Regression mechanics
3. Identification-strategy-specific checks (DiD, IV, RDD, matching)
4. The robustness battery
5. Asset-pricing specifics
6. Table & output verification
7. Red flags that mandate investigation before celebration

---

## 1. Sample construction & data integrity

- **Assert panel uniqueness explicitly**: exactly one row per (unit, time)
  key. Duplicate firm-years from a bad merge silently double-weight
  observations and shrink standard errors. `assert`, don't assume.
- **Merge diagnostics on every join**: report match rate, and INSPECT a
  sample of non-matches — are they random or systematic (e.g., all
  financial firms, all pre-2003, all dual-class)? For CRSP–Compustat,
  use the CCM link table with valid link-date ranges, never a raw
  ticker/cusip merge; check for gvkey–permno many-to-many cases.
- **Look-ahead bias**: accounting variables must be lagged to when they
  were publicly known (e.g., the Fama-French convention of matching
  fiscal-year-end t-1 data to returns from July t). Verify the lag
  structure by printing 3 example firm-rows and hand-checking the dates.
- **Survivorship & delisting**: confirm the sample includes dead firms;
  for returns, confirm delisting returns are incorporated (their omission
  inflates performance, especially among small stocks).
- **Winsorization/trimming**: documented (which variables, which
  percentiles, by year or pooled?), applied AFTER sample selection but
  BEFORE estimation, and consistent across all tables. Print pre/post
  min/max for each winsorized variable to confirm it actually bit.
- **Filters reconcile**: the sample-selection paragraph's arithmetic
  (start N → each filter's deletions → final N) must be reproduced by the
  code's actual row counts, filter by filter. This is the single most
  common table-vs-text inconsistency referees find.
- **Unit and scale audit**: Compustat in millions vs thousands, returns in
  percent vs decimal, CPI-deflated or nominal — print summary stats and
  check magnitudes against a known benchmark (e.g., median firm size,
  mean monthly return ≈ 1%).

## 2. Regression mechanics

- **N accounting**: the regression's reported N must equal the analysis
  sample's N minus (a) listwise deletion from missing regressors — know
  which variable eats the most — and (b) singletons dropped by fixed
  effects. If N differs across columns of a table, either harmonize the
  sample or state why; coefficient comparisons across different samples
  conflate specification and composition effects.
- **Within-variation check for FE models**: confirm the regressor of
  interest actually varies within the FE cells. A firm-invariant treatment
  with firm FE, or a shock absorbed by industry×year FE, produces a
  coefficient identified off measurement error or nothing at all. Check:
  regress X on the FE set and inspect the residual variance.
- **Clustering matches the assignment level**: SEs clustered at the level
  at which treatment/shocks are assigned or serially correlated (state
  policy → cluster by state, not firm). With few clusters (rule of thumb
  < ~40), conventional cluster-robust SEs over-reject — use wild cluster
  bootstrap and report it.
- **Recompute one t-stat by hand** from the reported coefficient and SE;
  confirm stars follow the stated thresholds. Catches stale copy-paste
  between estimation output and the table.
- **Economic magnitude translation**: convert the headline coefficient to
  an interpretable quantity (a 1-SD move in X → Y% of the outcome's mean
  or SD) and sanity-check it against the literature. A "significant"
  effect implying implausible economics (e.g., a governance tweak moving
  Tobin's Q by 50%) usually signals a units error or a corrupted sample.
- **Functional form basics**: log(0) observations silently dropped?
  log(1+x) justified vs distorting? Ratios with near-zero denominators
  creating extreme values that survive winsorization?

## 3. Identification-strategy-specific checks

### Difference-in-differences
- **Pre-trends shown, not asserted**: estimate the event-study version
  with leads; leads should be individually and jointly insignificant AND
  economically small — a flat-but-noisy pre-period is weak evidence, and
  a monotone pre-trend that "isn't significant" is a red flag.
- **Staggered adoption → TWFE is suspect**: with heterogeneous treatment
  effects, static two-way FE mixes clean and forbidden (already-treated
  as controls) comparisons. Verify with a heterogeneity-robust estimator
  (Callaway–Sant'Anna, Sun–Abraham, or a stacked design) and report the
  Goodman-Bacon decomposition if TWFE is retained. If the robust
  estimator disagrees with TWFE, the TWFE number is not the finding.
- Treatment timing hand-checked for 5 units against the primary source
  (statute effective date vs passage date is a classic off-by-one-year).
- Control group composition explicit: never-treated vs not-yet-treated,
  and whether results survive restricting to one or the other.

### Instrumental variables
- **First-stage strength with modern standards**: report the effective
  F-statistic (Montiel Olea–Pflueger); the old "F > 10" rule of thumb is
  insufficient — with a single instrument, apply the tF adjustment (Lee,
  McCrary, Moreira, Porter) or Anderson–Rubin confidence sets for
  weak-IV-robust inference.
- First stage sign and magnitude economically sensible, not just strong.
- **Exclusion restriction stress-test**: write down the two most plausible
  violation channels and check what you can (reduced-form effect in
  subsamples where the channel is shut off; controls for the confounder's
  observables). An untested exclusion story stated once in the text is a
  claim, not a verification.
- Report the reduced form; if the reduced form is not visible in the raw
  data, distrust a significant 2SLS estimate.
- LATE interpretation: identify who the compliers are and whether the
  estimate generalizes to the population the paper's claims are about.

### Regression discontinuity
- Manipulation test on the running variable (McCrary / Cattaneo–Jansson–Ma
  density test) — bunching at the cutoff invalidates the design.
- Covariate balance at the cutoff shown for predetermined characteristics.
- Bandwidth sensitivity: results reported at the CCT optimal bandwidth AND
  at half/double; local linear with robust bias-corrected inference,
  not high-order global polynomials.
- Placebo cutoffs away from the true threshold return nulls.

### Matching / propensity scores
- Post-match balance table (standardized differences < ~0.1), common
  support inspected, and the estimand stated (ATT vs ATE).
- Results not fragile to caliper/neighbor-count choices.

## 4. The robustness battery

Purpose discipline: each robustness check must target a NAMED threat to
the main result, not pad the appendix. For each check, verify:

- **Consistency across the table**: robustness columns' N, sample period,
  and dependent variable match the main specification unless the check is
  precisely about changing them. A robustness table whose N silently
  differs from the baseline by 30% is testing something else.
- Alternative FE structures and alternative clustering levels reported —
  results should not live or die on one clustering choice.
- **Subsample stability**: split by time (especially pre/post major
  regime events in the sample window) and by size; a "full-sample" result
  driven entirely by micro-caps or one crisis year needs to say so.
- **Influence diagnostics**: drop each cluster/year one at a time (or
  DFBETA screen); no single unit should own the result.
- **Placebos with teeth**: fake treatment dates, unaffected outcomes, or
  permutation/randomization inference where cluster counts are small —
  the placebo must be capable of failing.
- **Coefficient stability to observables** (Oster's delta / Altonji-style
  bounds) when the design is selection-on-observables: report how much
  selection on unobservables would be needed to zero the effect.
- Alternative variable constructions (the other standard proxy in the
  literature) — if the result holds only under your bespoke measure,
  that is a finding about the measure.

## 5. Asset-pricing specifics

- **Portfolio sorts**: report both value- and equal-weighted returns;
  use NYSE breakpoints where standard; check whether the spread portfolio
  is driven by the short leg in micro-caps (limits-to-arbitrage vs
  tradable anomaly is a different paper).
- **Alphas**: Newey–West SEs with a stated, justified lag; GRS test for
  joint significance across portfolios; alphas against the current
  standard factor sets, not only CAPM/FF3.
- **Fama–MacBeth**: SEs corrected for autocorrelation of the coefficient
  series; check the average cross-sectional R² is in a sane range.
- Returns hygiene: log vs simple consistent throughout; delisting returns
  in; currency and dividend treatment stated; no overlapping-horizon
  returns without the corresponding SE correction (Hansen–Hodrick/NW).
- **Data-snooping posture**: for a "new factor/anomaly" claim, apply a
  multiple-testing haircut mentally (Harvey–Liu–Zhu: t > ~3 as the bar)
  and check out-of-sample or post-publication sub-period performance.

## 6. Table & output verification

- One-click reproducibility: a single script rebuilds every number in the
  table from raw data; if any number was hand-edited, it is unverified.
- Cross-table consistency: summary-stats N = regression sample N (or the
  difference explained); the same variable has the same mean everywhere
  it appears.
- Text-table agreement: every magnitude claimed in prose recomputed from
  the table it cites; "roughly 20%" claims traced to the exact cells.
- Signs, decimals, and units uniform within a table; SEs vs t-stats in
  parentheses stated correctly in the notes; variable definitions in the
  appendix match the code's actual construction.

## 7. Red flags that mandate investigation before celebration

Treat each of these as a verification FAILURE until affirmatively
explained — the DECIDE step should not return CONTINUE past them:

- t-statistics > ~15 in observational firm-level data (usually duplicated
  rows, mechanical relation, or clustering at the wrong level)
- R² near 1 outside of accounting identities; R² of exactly the same
  value across different specifications (stale output pasted twice)
- Coefficient flips sign across adjacent, similar specifications with no
  economic story
- N identical across columns that add regressors with known missingness
  (suggests the sample wasn't re-selected — or, if intended, verify the
  harmonization was done deliberately)
- Results strengthen when fixed effects are ADDED in a setting where FE
  should absorb variation (possible bad-control or collider structure)
- The effect appears instantly at t=0 with no dynamics in a setting where
  the mechanism implies gradual adjustment
