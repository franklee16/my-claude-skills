# Verification Playbook — per-domain checklists

Read only the section matching the subtask you are verifying. Each checklist
is ordered cheapest-first; stop early only if the subtask is low-stakes.

## Table of contents
1. Code
2. Data analysis / statistics
3. Documents & presentations (docx, pptx, pdf, md)
4. Research & web-sourced claims
5. File and system operations
6. Long-form writing
7. Multi-agent / delegated work

---

## 1. Code

- **Run it.** Never verify code by reading it. Execute on real input, not
  just the happy-path toy input.
- Test the boundaries specifically: empty input, single element, maximum
  size, unicode, malformed input. Off-by-one lives at boundaries.
- If you fixed a bug: first write a check that FAILS on the old code, then
  confirm it passes on the new code. A fix you never saw fail proves nothing.
- Check exit codes AND stderr — many tools "succeed" with warnings that are
  actually your bug.
- After editing a file, re-read the edited region; after multiple edits,
  run the whole thing again (edits interact).
- Prefer writing a small test script over a one-off manual check whenever
  the same property will need re-checking after future changes.

## 2. Data analysis / statistics

- **Row-count reconciliation at every transformation.** N_in, N_dropped
  (with reason), N_out must add up at each step. Silent row loss is the
  most common silent corruption in analysis pipelines.
- Print and READ the head, dtypes, and summary stats immediately after
  loading. Column read as string that should be numeric, dates parsed
  wrong, and encoding damage all show up here in seconds.
- Re-derive one headline number by an independent route (different formula,
  different tool, hand computation on a 5-row subset).
- Check units, scales, and signs against domain intuition: a t-stat of 40,
  an R² of 0.99 in observational data, a negative price — investigate,
  don't celebrate.
- Missing values: know the count per key variable and the HANDLING (dropped?
  imputed? propagated as NaN into means?) before trusting any aggregate.
- Duplicates on the intended key: `assert` uniqueness rather than assuming.
- For regressions: confirm the N reported by the model equals the N you
  think you fed it; listwise deletion regularly eats samples silently.
- Fixed seed for anything stochastic, so verification is reproducible.

## 3. Documents & presentations

- **Open the produced file** (render pptx/docx to images or PDF and look at
  the pages, or at minimum extract and read the text back). Generation
  succeeding ≠ document correct.
- Check for: text overflowing boxes, tables cut off at page/slide edges,
  broken image links, placeholder text ("Lorem", "TODO", "XXX") left in.
- Numbers appearing in the document must be traced to the verified analysis
  output — copy-paste from an earlier draft is a classic stale-number bug.
- Cross-references: every "see Table 2" points at a Table 2 that exists and
  is the right one; figure numbering is sequential after edits.
- Formatting constraints from the request (font, length, template, citation
  style) checked explicitly, one by one.

## 4. Research & web-sourced claims

- Distinguish three confidence classes in your notes: (a) verified against
  a primary source, (b) single secondary source, (c) your inference. Only
  (a) gets stated without hedging in the deliverable.
- Load-bearing facts (numbers, dates, quotes, "X said Y") need the primary
  source fetched and read — search-result snippets truncate and mislead.
- Two sources that copy each other are one source. Check independence
  before counting corroboration.
- Recency check: is this the CURRENT state (prices, versions, office-
  holders, APIs) or a snapshot that may be stale? Date every fact.
- Record the URL/source next to each claim as you go; reconstructing
  attribution at the end is error-prone and expensive.

## 5. File and system operations

- Before: confirm the target exists and is what you think (`ls -la`, head
  the file). Paths from memory are guesses; paths from a fresh listing
  are facts.
- Destructive operations (rm, overwrite, force flags) on anything the user
  provided: require explicit user approval; otherwise copy-then-modify.
- After: confirm the effect happened — re-list the directory, check the
  file size is plausible, verify the archive actually contains the files
  (`unzip -l`), confirm the process actually terminated.
- Idempotency check for anything that might be rerun: will running this
  step twice corrupt state (append twice, double-transform)?
- Working directory discipline: scratch work in a temp/work dir; only
  verified finals moved to the delivery location.

## 6. Long-form writing

- Re-read the brief AFTER writing the draft, then reread the draft against
  it — constraint by constraint (length, audience, tone, required sections,
  banned content).
- Verify internal consistency: names, numbers, and claims made in section 1
  still match what section 5 says after all the edits.
- Every factual claim inherits the verification status from Section 4 above;
  eloquence does not upgrade an unverified claim.
- Read the piece once as the target reader (not as the author): does the
  opening orient them, does each section earn its place, does it answer the
  actual question asked?

## 7. Multi-agent / delegated work

If you delegate subtasks to subagents or other tools:

- Give the subagent the subtask's completion test, not just the task —
  otherwise you inherit its unverified claim of success.
- **Never trust "done" reports; verify the artifact.** Apply the relevant
  checklist above to the subagent's output exactly as you would to your
  own, because to you it IS untrusted input.
- Check interfaces at every boundary: the format subagent A produced is the
  format subagent B assumed. Integration failures cluster at hand-offs.
- If a subagent fails repeatedly, the same 3-retry rule applies: rewrite
  the instructions (your model of the task was wrong), do it yourself, or
  escalate — do not resubmit the identical prompt.
