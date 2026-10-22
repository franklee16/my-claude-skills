---
name: plan-verify-act
description: Systematic methodology for executing complex, multi-step tasks - how to decompose a large ambiguous task into verifiable subtasks, how to verify your own work at each step, and how to decide the next action (continue, retry, backtrack, replan, or ask the user). Use this skill whenever a task involves 3+ dependent steps, multiple files or tools, ambiguous requirements, long-running work, research-then-produce workflows, or any situation where a mistake early on could silently corrupt everything downstream. Trigger it even if the user just says "do X" where X is obviously big - they should not have to ask for planning explicitly.
---

# Plan-Verify-Act: Executing Complex Multi-Step Tasks

This skill codifies a working methodology for agents facing tasks too large to
complete in one pass. The core insight: agent failures on complex tasks are
rarely caused by inability to do any single step. They are caused by (a) losing
track of the actual goal, (b) errors early in the chain propagating silently,
and (c) continuing to execute a plan that reality has already invalidated.
Everything below exists to counter those three failure modes.

The methodology is a loop, not a waterfall:

```
UNDERSTAND → PLAN → [ ACT → VERIFY → DECIDE ]* → FINAL VERIFY → DELIVER
                          ↑____________|
                    (loop until done or blocked)
```

---

## Phase 0: Triage — does this task need the full loop?

Not every task deserves ceremony. Overhead on simple tasks is its own failure
mode. Apply the full methodology when ANY of these hold:

- 3+ steps where later steps depend on earlier outputs
- Multiple files, tools, or data sources involved
- The requirement is ambiguous enough that two reasonable agents would
  produce different deliverables
- Estimated work exceeds what fits comfortably in one "sitting" of attention
- An early mistake would be expensive to discover late (e.g., wrong data
  loaded → entire analysis invalid)

If none hold: just do the task, verify once at the end, deliver. Skip to
"Final verification" below.

## Phase 1: Understand before decomposing

Decomposing a misunderstood task produces a well-organized wrong answer.
Before writing any plan:

1. **Restate the goal in one sentence** — the deliverable and its consumer.
   "Produce X, in format Y, so that the user can do Z." If you cannot fill
   in Z, you do not understand the task yet.
2. **Extract explicit constraints** from the request: format, length, tools
   to use or avoid, deadlines, style. List them verbatim — you will check
   against this exact list at the end, not against your memory of it.
3. **Surface the unknowns.** Write down what you do NOT know that the plan
   depends on: does the file exist? what schema does the data have? does the
   API support this? Unknowns fall into two classes:
   - *Resolvable by exploration* → resolve them YOURSELF, cheaply, before
     planning (list the directory, read the file header, run `--help`).
   - *Resolvable only by the user* (preferences, missing credentials,
     genuinely ambiguous intent that changes the deliverable) → ask NOW,
     batched into one message, not one question at a time across five turns.
4. **Reconnaissance before commitment.** Spend a small, bounded amount of
   effort (a few tool calls) inspecting the actual environment: real file
   contents, real data shapes, real API responses. Plans built on assumed
   state are the #1 source of mid-task replanning.

The threshold for asking the user: ask when the answer would change WHAT you
build; do not ask when it only changes HOW and any reasonable choice is
acceptable (make the choice, note it as an assumption, move on).

## Phase 2: Decompose into verifiable subtasks

Decomposition quality is measured by one property: **each subtask has a
completion test you can run without human judgment.** "Analyze the data" is
not a subtask; "produce summary stats table for all 12 columns, with no
column silently dropped" is.

Rules for cutting the task:

- **Cut along dependencies, not topics.** Order subtasks so each one's
  inputs are the verified outputs of earlier ones. A dependency graph that
  is mostly linear is a feature — it tells you exactly where to backtrack.
- **Front-load the risky and the load-bearing.** Do the step most likely to
  fail, or whose failure invalidates the most downstream work, FIRST — even
  if it is not first in the natural narrative order. Discovering in step 8
  that the data needed in step 2 doesn't exist wastes steps 2–7.
- **Make each subtask end in an artifact** — a file, a passing test, a
  confirmed fact — not a mental state. Artifacts survive context loss;
  "I now understand the schema" does not.
- **Right-size the granularity.** Subtasks should be 1 unit of focused
  work each. Fewer than ~3: you probably didn't need this skill. More than
  ~10 at one level: group them into phases and decompose the current phase
  only — planning distant steps in detail is wasted work because early
  results will change them (see "rolling-wave" below).
- **Rolling-wave planning.** Plan near steps concretely, far steps as
  named placeholders. "Phase 3: write report (details after analysis
  done)" is honest; a detailed report outline before seeing results is
  fiction that you will feel pressure to conform to.

Record the plan in a durable medium — a TodoList if the environment has one,
otherwise a `PLAN.md` file in the working directory. The plan must be
somewhere you will re-read, because its second function (after organizing
work) is re-anchoring you to the goal after long tool-call sequences.
Each entry: subtask, its completion test, its status.

## Phase 3: The execution loop

For each subtask, run ACT → VERIFY → DECIDE. Never chain two ACTs on
dependent work without a VERIFY between them.

### ACT
Do one subtask. While acting:
- Prefer reversible moves. Work in scratch space, write to final
  destinations only after verification. Never destructive operations
  (delete, overwrite, force-push) on user data without explicit approval.
- If mid-action you notice the plan's assumption is wrong, STOP the action.
  Finishing a step you already know is wrong is pure waste — go to DECIDE.

### VERIFY
Verification is cheap insurance against expensive propagation. Three tiers,
apply the highest tier the subtask warrants:

1. **Sanity tier (always, costs seconds):** Does the output exist? Is it
   non-empty? Right rough size/shape/type? Did the command exit cleanly?
   Read back what you just wrote — at least skim it.
2. **Functional tier (for anything executable or computable):** Run it.
   Execute the code on real input. Re-derive one number by an independent
   path. Open the generated file and check it renders. **A script that
   checks the property beats eyeballing it** — scripts are rerunnable after
   every future change, eyeballs are not.
3. **Requirement tier (for the subtasks that face the user):** Check the
   output against the *original request's constraint list from Phase 1* —
   not against your plan. Plans drift; the request is ground truth. This
   catches the classic failure of perfectly executing a plan that quietly
   diverged from what was asked.

Two principles that make verification actually work:

- **Verify against an independent source.** Checking your work using the
  same reasoning that produced it mostly re-confirms your own mistake. Use
  a different method: recompute by another formula, test with a known-answer
  case, compare against documentation, run the code instead of reading it.
- **Actively hunt for your failure, don't passively confirm success.** Ask
  "what is the most likely way this step went wrong?" and test THAT
  specifically (off-by-one at boundaries, encoding issues, silently dropped
  rows, stale cached state, wrong file version). One targeted negative test
  is worth five reassuring positive ones.

See `references/verification-playbook.md` for concrete per-domain checklists
(code, data analysis, documents, research/web claims, file operations) —
read the section matching your current subtask type when you need specifics.
For econometric work — regressions, causal identification (DiD/IV/RDD),
robustness checks, asset-pricing tests — additionally read
`references/empirical-research.md`, which extends the data-analysis
checklist to research-grade standards in economics and finance.

### DECIDE
After verifying, choose exactly one of five moves. The decision rule:

| Situation | Move |
|---|---|
| Verification passed | **CONTINUE** — mark subtask done in the plan, start the next |
| Failed; cause understood; fix is local | **RETRY** — fix and re-verify. Change something on every retry; identical retries are prohibited |
| Failed; cause lies in an EARLIER subtask's output | **BACKTRACK** — reopen that subtask, fix, then re-verify every subtask downstream of it (their inputs changed) |
| Failed or blocked; the plan's assumptions are wrong | **REPLAN** — return to Phase 2 with what you now know. Salvage verified artifacts; discard invalidated ones explicitly |
| Blocked on something only the user can resolve, or the fix requires exceeding your mandate | **ESCALATE** — ask the user, presenting: what you tried, what you found, the specific decision you need from them, and your recommended option |

Hard limits that prevent pathological loops:

- **Max ~3 retries per subtask.** After 3 failed attempts at the same
  subtask, the problem is almost never the attempt — it's your model of the
  problem. Force a move up the ladder: BACKTRACK or REPLAN or ESCALATE.
- **Sunk-cost rule:** the amount of work already invested in a plan is
  never a reason to keep following it. Only the plan's current validity is.
- **Scope-guard:** if the fix you're contemplating grows the task beyond
  what was asked (rewriting a module to fix a typo-level bug), that is an
  ESCALATE, not a heroic RETRY.

### Checkpoint hygiene (every few subtasks)
- Update the plan document to reflect reality — a stale plan is worse than
  none, because you will trust it.
- Re-read the original request once. Long executions drift; this is the
  cheapest drift-correction available.
- For long tasks, tell the user where you are at natural phase boundaries —
  brief, factual, no play-by-play of every tool call.

## Phase 4: Final verification and delivery

Before declaring done:

1. **Walk the Phase-1 constraint list item by item** against the actual
   deliverable. Every explicit requirement gets an explicit check. The most
   common end-stage failure is delivering something excellent that is
   missing one thing the user literally asked for.
2. **Fresh-eyes pass:** inspect the deliverable as its consumer, not its
   author. Open the file the way the user will. Run the code the way the
   user will. Read the report top-to-bottom once.
3. **Integration check:** individually-verified parts can still fail
   jointly (file A references a path file B renamed). Test the whole, not
   just the parts.
4. **Disclose honestly.** State what was verified and HOW, what is assumed,
   and what was not done and why. An agent that says "I tested X by running
   Y; I did not test Z" is more useful than one that says "all done!" —
   unverified claims of success are the most damaging output an agent can
   produce, because the user builds on them.

## Anti-patterns (each is a real, recurring agent failure)

- **Plan-and-pray:** writing a beautiful plan, then executing all steps
  back-to-back with verification "at the end." Defeats the entire purpose —
  errors propagate through every downstream step before detection.
- **Verification theater:** "The code looks correct" without running it;
  "the file was created" without reading it. If verification cannot fail,
  it isn't verification.
- **Assumption smuggling:** silently resolving an ambiguity in Phase 3 that
  should have been surfaced in Phase 1, then building on it.
- **Identical retry:** rerunning the same failing action hoping for a
  different result. Every retry must embody a hypothesis about the failure.
- **Success inflation:** reporting a subtask complete when it is "mostly
  working." Partial completions must be recorded as partial in the plan,
  or the DECIDE table operates on false inputs.
- **Interrogation dribble:** asking the user questions one at a time across
  many turns instead of batching, or asking things you could resolve with
  one cheap tool call.
- **Context amnesia:** never re-reading the original request after the
  first turn. The request is ground truth; the plan is a derivative of it.

## Minimal worked example

Task: "Take the attached survey CSV, clean it, run the regressions from my
notes, and give me a Word document with the results."

- *Phase 0:* multi-step, dependent, files involved → full loop.
- *Phase 1:* Deliverable = .docx of regression results for [consumer: the
  user's paper]. Constraints: use THEIR spec from notes, Word format.
  Unknowns: CSV schema (resolvable myself → inspect now), which of two
  regression specs in the notes is intended (only user knows, and it changes
  the deliverable → ask now, batched with any other question).
- *Phase 2:* (1) inspect CSV, confirm expected columns exist [test: all
  variables named in notes are present]; (2) clean, log every row dropped
  [test: row counts reconcile]; (3) run spec, [test: N in output matches
  cleaned N; one coefficient re-derived via a second method]; (4) build
  docx [test: file opens, contains all tables, matches format constraint].
  Riskiest first: step 1 is already first — good.
- *Phase 3:* after step 2, verification finds 40% of rows dropped —
  suspicious. DECIDE: not CONTINUE; cause is an encoding issue in step 1's
  read. BACKTRACK to step 1, fix encoding, re-verify step 2 (downstream).
- *Phase 4:* walk constraints: their spec ✓, Word format ✓, all requested
  tables present ✓. Disclose: "dropped 3% of rows for missing X (list in
  appendix); did not winsorize since notes didn't specify — flag if wanted."
