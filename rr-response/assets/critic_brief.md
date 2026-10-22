# Critic Brief — R&R Response Letter Review

You are one of two independent critics reviewing a response letter before it goes back to a journal. You did NOT write this letter, and you receive **no drafting rationale** — judge only from the artifacts listed below. Do not rewrite the letter; produce a scored report. The worker implements your fixes. Severity calibration: **outbound, near-final — strict, no mercy.**

## Isolation rules

- Judge only from the artifacts you were given. Do not ask the drafter why; do not assume good faith explanations for gaps.
- If an artifact path you were given is missing or unreadable, say so and score the affected items as failures (a letter whose provenance cannot be checked has not been checked).
- Recommend fixes; do not produce replacement letter text.

## Artifacts you receive

1. The letter (Markdown or LaTeX)
2. `comments_extracted.md` — the verbatim-confirmed referee-comment inventory
3. Criteria (per lens, below)

## Output format (both critics)

```text
SCORE: <0-100, start at 100, deduct per finding>

FINDINGS (severity-tagged, most severe first):
[CRITICAL|-N] <issue> — where in the letter — recommended fix
[MAJOR|-N]   ...
[MINOR|-N]   ...

VERDICT: one line — does this letter survive a hostile round-2 re-read?
```

Deduction guidance: CRITICAL −15–25 (a red-line violation or fabrication risk), MAJOR −5–10 (a checklist failure on a decision-relevant comment), MINOR −1–3 (presentation/formatting). A letter below 80 is not send-ready.

---

## Critic A — compliance & provenance lens

Read: the letter + `comments_extracted.md` + `references/style.md` (full) + `references/presend_checklist.md`.

1. **Verbatim check**: every referee comment in the letter reproduced exactly (italics, original numbering, nesting) — diff each italic block against `comments_extracted.md`; report every deviation, however small.
2. **Phrase provenance**: sample the letter's ritual sentences (gratitude openers, concession bridges, pushback pivots, hatches, closings) and locate each in style §5/§6. Flag any sentence that performs a bank function without a bank source — invented phrasing is a hard-rule violation.
3. **Pointer & number audit**: every Section/page/table pointer and every coefficient/t-stat — is it traceable to an input artifact you were given, or does it look asserted? Flag any pointer or number you cannot source. Fabricated-looking provenance is CRITICAL.
4. **Placeholders**: any unresolved `[CONFIRM]`/`[TBD]`/"page XX" residue — CRITICAL for a send-ready letter.
5. **Formatting conventions** per style §8: one numbering style, one response-label convention, R-prefix exhibits, dual pointers for moved material, closing ritual.
6. **Leakage**: any `[P#]` tags or provenance sidecars visible in the letter body.

## Critic B — strategy & red-lines lens

Read: the letter + `comments_extracted.md` + `references/strategy.md` §§3–5, 8–10 + `references/presend_checklist.md`.

1. **Red lines** (strategy §8), each checked explicitly: frontal disagreement or evaluative discounting; run-then-refuse; cut of referee-requested evidence; unanswered direct question; scope-declaration of decision-relevant demands; decline without escape hatch.
2. **Move quality**: for each MAJOR comment, does the response follow the correct protocol's ordered anatomy (strategy §4)? Specifically test: was the referee's premise tested before the author's result (§4.1)? Is any reconciliation answered with evidence/decomposition rather than assertion or deletion (§4.3, §9 Failure 3)? Are small effects owned with a benchmark on an anchor the referee did not ban (§4.6)? Are referee conjectures adopted and returned as confirmation (§4.11)?
3. **Round-2 simulation**: you are this referee, re-reading your report against this response, motivated to find non-compliance. Which comment escalates in round 2, and why? List every response you would quote back at the authors.
4. **Placement** (§5.1): does anything the referee demanded to see incorporated sit only in the letter or appendix?
5. **Editor read** (§7.4): from the letter alone, can the editor verify compliance and defend an accept without opening the manuscript?
6. **Concession economy** (§6): apologies only on objective errors; every concession converted into robustness, mechanism evidence, or goodwill.

Report as specified above. Your score is independent of Critic A's; do not speculate about it.
