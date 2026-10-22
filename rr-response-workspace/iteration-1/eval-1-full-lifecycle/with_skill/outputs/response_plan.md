# Response Plan — JFQA MS# 26-10442, "Retail Attention and the Cross-Section of Stock Returns"

Round 1 R&R to Referee 1. Prepared 2026-10-21 from: `referee_report_R1.txt` (extraction: `comments_extracted.md`, verbatim gate confirmed), `editor_letter.txt`, `changelog.md`.

**Gates (test run):** verbatim gate and plan-approval gate auto-passed by the harness; this plan proceeds on the assistant's recommendation. Both are flagged below where Frank's decision would normally bind.

---

## Acceptance condition (Pass 1 — printed at top, orders everything)

From the editor letter, verbatim:

> "the success of any revision will depend on new supportive evidence that your measure has stand-alone predictive content beyond the liquidity-provision channel. Cosmetic changes will not be sufficient."

The referee states the same condition inside Comment 1 ("your headline result does not establish that attention matters"). **Comment 1 is the acceptance condition.** It gets the structural budget, the first slot in the summary-of-major-changes block, and its evidence goes in the **main text** (never letter-only or IA-only — the failed-letter Failure 6 rule: the only exhibit that answers the core demand is never parked).

**Current status: the acceptance condition is NOT yet satisfied.** The changelog marks Comment 1 analysis In Progress (data obtained, nothing run) and Comment 2 Not Started. The letter drafted under this plan is therefore a **draft with placeholders**, send-ready only when the checklist at the bottom reaches zero.

## Triage passes (summary)

- **Pass 2 coding:** table below. Amplitude by threat: C1 > C2 ≈ C3 > C1a > minors.
- **Pass 3 permissive language:** Comment 1a "though I leave this to the authors" licenses discretion. We comply anyway — the 2020–2024 Bloomberg pull that serves Comment 1 also serves the extension, so the marginal cost is low and it converts a permissive item into acceptance-condition support.
- **Pass 4 enthusiasm:** "the data are unusual and interesting" — the brokerage-app data is the paper's distinctive asset. The Comment 1 defense leans on it: app openings are measured from app activity, and the discriminator stage tests whether ATTN carries information volume-based measures do not.
- **Pass 5 cascade:** C1 cascades to the whole paper (substitution threat → protocol 4.1, not a one-shot answer). C2 cascades to Table 3 and the portfolio section (protocol 4.3; removal rejected, see below). C3's IO partition cascades *forward* as mechanism evidence — already monetized via Table IA.2.
- **Pass 6 referee's values, deliverable:** mechanism discipline (IO partition — delivered), engagement with Wang/Zhang (citations delivered; deeper engagement underway), direct answers (C3 response opens with the direct sentence), economic magnitude (partially deliverable now).

## §7.2 Arbitrage scan (one construction, many debts)

1. **Bloomberg 2020–2024 bid-ask/volume pull** pays: Comment 1 (Wang measure construction), Comment 1a (sample extension), and potentially Comment 2 (whether the Zhang sign difference is sample-period-driven). One acquisition, three debts.
2. **IO partition (Table IA.2, completed)** pays: Comment 3 mechanism (spread concentrated in low-IO), Comment 3 magnitude (0.44%/month anchor + 6.8% MAD benchmark), and the headline reinterpretation (full-sample 31 bps mixes stocks where the mechanism operates with stocks where it cannot).

## Unified response table

| ID | Comment (short) | Threat × Type | Global class | Style bucket | Move / Protocol | Evidence needed | Change status | Placement | Hatch |
|----|-----------------|---------------|--------------|-------------|-----------------|-----------------|---------------|-----------|-------|
| R1-C4 (#1) | ATTN may proxy liquidity-provision returns (Wang 2021); provide stand-alone content | MAJOR × identification-threat (substitution) | NEW ANALYSIS | (c) concede-question-reframe-via-new-evidence + (f) pushback-with-evidence | **4.1 Grant-the-Threat**, 5 stages: grant threat → build data → premise test → proxy test (double sort, controls) → mechanism discriminator | Wang measure (underway); premise replication in our sample; double sorts; discriminator outcomes | **In Progress** (Bloomberg data obtained; nothing run) | Key table + conclusion in **main text** new subsection; premise/grid in letter R-tables | None needed (full compliance) |
| R1-C6 (#2) | Table 3 sign contradicts Zhang (2022); reconcile or remove the section | MAJOR × interpretation-disagreement / contribution-positioning | NEW ANALYSIS | (c) concede-question-reframe-via-new-evidence + (e) clarify-not-inconsistent | **4.3 Replication Grid**: replicate Zhang in exact spec on our universe → grid over differing axes → hedged synthesis ("Overall, the above comparison suggests…") | Replication of Zhang; grid design (axes named only after replication); synthesis paragraph | **Not Started** | Grid in letter R-tables + IA; synthesis paragraph in manuscript (§2.1 / Table 3 discussion) | "We would be pleased to [expand/move] if you prefer" on placement choices |
| R1-C7 (#3) | (a) high-IO insignificance vs. story — "Doesn't this contradict your story?"; (b) 31 bps tiny vs. transaction costs — "justify the economic magnitude" | MAJOR × mechanism-question + magnitude attack | (a) NEW ANALYSIS + CLARIFICATION; (b) CLARIFICATION | (a) (d) concede-the-mechanism-and-run-with-it; (b) (f) hedged pushback + (g) partial concede | (a) **4.11 Conjecture Promotion + magnitudes** ([P1] C8 pattern): answer directly, credit the referee's conditional, formalize as Table IA.2; (b) **4.6 Own-the-Smallness**: concede modest in print, rebuild on low-IO anchor + MAD benchmark | (a) DONE — Table IA.2 numbers from changelog; (b) benchmark computable (0.44/6.8 ≈ 6.5%); tradability treatment decision pending | (a) **Completed**; (b) **Partial** | Table IA.2 in IA with main-text address (§4.3, p. 21); smallness acknowledgment inside manuscript; mirror R1 in letter | Promote IA.2 to main text "if you prefer"; tradability revision choices |
| R1-C5 (#1a) | Sample ends 2022; extend to 2023–2024 ("I leave this to the authors") | MODERATE × robustness-demand | NEW ANALYSIS | (a)/(b) comply + exceed | Q4 exceed-the-ask: extension also hardens the Comment 1 test (same data pull) | Extended-sample re-estimation of main tables | **In Progress** (data pulled, cleaning) | Revised manuscript tables; status reported in letter | None (complying) |
| R1-C9 (#4) | Typo p. 12 "the their" | MINOR × presentation | MINOR | (a) full-concede + act | Q2 one-sentence exact compliance, precise pointer | None | **Completed** (p. 12) | Manuscript p. 12 | n/a |
| R1-C10 (#5) | Cite Wang (2021), Zhang (2022) in Introduction | MINOR × presentation/citation | MINOR | (a) full-concede + act | Q2 full-concede; opens the compliance ledger | None | **Completed** (p. 3 fn. 5; §2.1 p. 8) | Intro + §2.1 | n/a |

Letter ordering follows the referee's own numbering (1, 1a, 2, 3, then Minor 4, 5). Summary-of-major-changes block ordered to mirror the acceptance condition: 1 (liquidity-provision analysis) → 3 (IO mechanism) → 2 (Zhang reconciliation) → 1a (extension) → minors. [Editor-first ordering: the editor named Comment 1; the referee's own "bothers me most" is 3; 2 third.]

## Major moves and runner-ups (decision forum)

**C1 — 4.1 Grant-the-Threat (recommended).** Runner-up: argue from correlation structure without constructing the Wang measure (cheaper). Rejected: fails the editor's explicit "Cosmetic changes will not be sufficient"; a substitution threat to the headline always gets the full protocol ([P4] archetype). Contingency to monitor: if the premise test or double sort comes back adverse (ATTN subsumed), the plan itself must be re-argued — that is a user escalation at results time, not a letter drafting question. No hedges in the letter may pre-commit to a favorable outcome; placeholders hold the result slots.

**C2 — 4.3 Replication Grid (recommended).** Runner-up: take the referee's remove-option (delete the portfolio-sorting section). Rejected on three grounds: (i) red line 3 — never cut the evidence the referee asked to see reconciled; removing the sorting section converts a results question into a trust question ([P8] Failure 3, the single most documented failure move); (ii) it guts the paper's cross-sectional evidence; (iii) the sign conflict between two published/under-review papers is resolved by locating its source, which only the grid can do. The remove-option is declined *silently in effect* — the letter simply pursues the reconciliation path, which is the referee's first-listed option; no sentence evaluates the removal option. Trade-off accepted: grid is costly and its outcome uncertain.

**C3a — 4.11 Conjecture Promotion + magnitudes (recommended).** Runner-up: 4.8 Ambiguity rewrite ("reflect the ambiguity in what we should expect"). Rejected: the referee's conditional is *confirmed* by our own data (low-IO spread 0.44%, t = 2.62; high-IO 0.09%, t = 0.71); claiming ambiguity would dodge his direct question and waste free mechanism evidence. The direct question ("Doesn't this contradict your story?") is answered in the first sentences, using the attested conjecture-alignment vehicles; the referee's conditional is granted before the answer.

**C3b — 4.6 Own-the-Smallness (recommended).** Concede modest magnitude in the manuscript; rebuild on the low-IO spread benchmarked against the 6.8% mean absolute deviation of monthly returns (0.44% ≈ 6.5% of MAD); the full-sample 31 bps (referee's number) is reframed as mixing mechanism-relevant and mechanism-irrelevant stocks. Transaction-cost piece: **decision needed** (below).

## Escalation check (hard gates)

- Saying the referee is wrong? **No** — every move grants the premise and runs tests. C3's answer grants the referee's own conditional before answering.
- Cutting evidence the referee asked to see reconciled? **No** — C2 takes the reconciliation path.
- Declining an essential incorporation? **No** — full compliance on C1, C1a, C2; C3 exceeds by adding Table IA.2.
- Unanswered direct questions? **No** — C3 has two ("Doesn't this contradict your story?", "justify the economic magnitude"); both open with direct sentences.

**DISAGREE escalations: none.** Proceeding autonomously per the harness.

## Open decisions for Frank (blocked on results or user choice; not blocking the draft)

1. **C1 adverse-result contingency** — if the double sort shows ATTN subsumed by the Wang measure, the fallback (attenuation + t-stability defense, magnitude framing, or deeper redesign) must be chosen before any letter ships.
2. **C3b transaction-cost treatment** — (i) verify whether any draft passage claims strategy tradability; if yes, remove or caveat it (Own-the-Smallness step 1); (ii) decide whether to add an explicit cost discussion or anchor magnitude purely on the MAD benchmark.
3. **Table IA.2 promotion** — currently IA with main-text address (§4.3, p. 21; [P7] pattern). Promotion to main text would strengthen the mechanism claim at the cost of space; the letter carries a standing hatch either way.
4. **Referee credit footnote** — Rule 7 credit-as-endowment: acknowledge the referee in a manuscript footnote on Table IA.2. Letter carries a placeholder; add the footnote number when inserted.
5. **References completion** — Wang (2021, JF) and Zhang (2022, JFE) full citations needed for the letter's References block (never fabricated).
6. **§4.3 revised-paragraph paste** — the letter pastes revised prose as proof of completion; the paragraph text must be pulled from the revised manuscript at finalize.

## Letter conventions chosen (style §2/§8)

- Skeleton: title block → "Dear Referee," → opening framing ([P1] gratitude + improvement + convention) → summary of major changes (Arabic 1., 2., …) → detailed responses → minor comments ([P2] two-bucket header) → References → Table R1 (mirror of IA.2) → closing ritual ([P2]/[P3]) + "The authors."
- Response label convention: plain prose (majority default). Comment blocks `> *…*` verbatim from `comments_extracted.md`, referee's own numbering preserved (1, 1a, 2, 3, 4, 5; Major/Minor headers preserved bold-italic).
- R-exhibits: bare "R1" naming. Table R1 = mirror of IA.2 key estimates "for the ease of your reference" ([P6] mirror pattern). Future C1/C2 tables join the R-sequence when run (draft carries placeholders).
- Provenance sidecars `<!-- SRC: style §x -->` on every bank-borrowed sentence (never in visible text; no bracketed source tags, which the audit treats as leakage).
- Numbers policy: coefficients/t-stats only from the changelog; the referee's own numbers (40 bps, 31 bps) attributed to him; the only computed quantity is 0.44/6.8 ≈ 6.5%.

## Send-readiness checklist (letter ships only when all resolve to zero placeholders)

- [ ] C1: Wang measure constructed; premise replication, double sort, discriminator run; main-text subsection written; Tables R2+ appended; every `[TBD]` filled
- [ ] C1a: 2023–2024 cleaning done; main tables re-estimated; results filled in
- [ ] C2: Zhang replication + grid run; two-axes synthesis drafted; manuscript paragraph added; `[CONFIRM]` pointers resolved
- [ ] C3b: tradability decision executed; revised magnitude passage pasted
- [ ] §4.3 revised paragraph pasted into the letter; referee-credit footnote number confirmed
- [ ] References completed (Wang 2021, Zhang 2022 full citations)
- [ ] Phase 4: `letter_audit.py` clean; critics A/B scored ≥ 80 (skipped in this test run); Frank's final confirmation. Never sent by the assistant.
