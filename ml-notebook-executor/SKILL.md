---
name: ml-notebook-executor
description: >-
  A notebook-building executor - second
  half of a two-step ML workflow, after new-dataset-workflow has read a
  dataset and named a direction. Use when the user is ready to build a
  complete, submission- or practice-ready Colab notebook - "build the
  notebook," "write the assignment notebook," confirming a reader's
  recommendation, or handing over a dataset (CSV plus target) to model
  end to end. Also trigger on graded assignment, team assignment, Kaggle-lesson, or
  exam-prep notebooks when the goal is runnable code with narrative, not
  explanation. Declares its audience first - student, grader or executive
  - which sets voice, structure and what gets cut. Produces real EDA,
  justified cleaning, a baseline, an algorithm ladder where each rung
  names the prior rung's weakness, tuning, a justified metric, a
  comparison, a recommendation and limitations - executed top-to-bottom
  with zero errors before delivery. Not for pre-modeling reading
  (new-dataset-workflow) or model-free analysis.
---

# ML Notebook Executor - the build-and-prove half

This is the **second half** of a two-step machine learning process. The `new-dataset-workflow` skill reads a dataset, names the catch, and points toward a starting algorithm - then stops on purpose, before any code exists, so the user can disagree with the direction while it's still cheap to change. This skill picks up from there: it actually builds the notebook, trains the models, proves the numbers, and hands over something that runs.

The boundary matters in both directions. This skill never does the first-look reading from scratch if a reader pass already happened - re-deriving "here's what's in the columns" is wasted work and risks contradicting what the user already confirmed. And it never stops at an explanation - if the output isn't a working, executed notebook file, this skill hasn't finished its job.

## Before you start: five things to establish

**1. Who is going to read this?**

Decide this before anything else, because it sets the structure, the voice, and what gets cut -
and getting it wrong means rebuilding the artifact rather than rewording it.

Read `references/audience-modes.md` and pick one of three modes: **STUDENT** (the user learning the
material), **GRADER** (a professor marking it against a rubric), or **EXECUTIVE** (a
decision-maker deciding whether to act). The reference file defines each mode's voice, structure,
cut-list, deliverable and self-check.

Two things that catch people out, both covered in detail in that file:

- **EXECUTIVE mode does not produce a notebook as its primary deliverable.** It produces a
  findings-first brief, with an executed notebook demoted to a defensible appendix. Building a
  notebook and merely tightening its prose is not executive mode.
- **The same finding can be the highest-value content in one mode and deleted entirely in
  another.** When those pull in opposite directions, the declared audience resolves it.

Whichever mode is chosen, state it in the artifact itself so the tone is declared rather than
inferred.

If the request is genuinely ambiguous - or if two audiences are both real, like a graded notebook
whose findings also get presented - ask rather than guessing, and expect that the honest answer is
sometimes "build both."

**2. Do you have the reader's findings, or do you need to do a fast version yourself?**

If the `new-dataset-workflow` output is present earlier in this conversation (or the user pastes/summarizes it), treat its diagnosis - size, class balance, the catch, the recommended starting point - as your working starting point. But don't blindly trust its printed numbers as final: you're about to build a notebook whose every number must trace to code executed *in that notebook's own run*, so re-run the load and the handful of numbers that drive real decisions (row/column count, target balance, missing-value count) as part of your own exploration, before writing narrative around them. If a number you get differs from what the reader reported, say so - don't silently pick one.

If no reader pass happened and the user has jumped straight here with a CSV, do a fast, abbreviated version of the reader's steps yourself first (shape, dtypes, target balance, obvious dirt) - you cannot write an honest cleaning or EDA narrative for data you haven't actually looked at. This doesn't need the reader's full conversational writeup; it just needs to happen before you build.

**3. Is this a graded submission, or a practice/exam-prep notebook?**

This is the GRADER-versus-STUDENT fork from step 1, and it changes what the notebook must contain (see `references/graded-assignment-checklist.md`), so get it right rather than assuming. Signals it's graded: mentions of a named assignment, "team assignment," a due date, "rubric," "submit," team member names, or an assignment PDF sitting in the conversation or project knowledge. Signals it's practice: "Kaggle lesson," "exam prep," "session prep," "just want to try this," no deadline or grading language. If it's genuinely ambiguous, ask directly - a wrong guess here means redoing structural parts of the notebook later (team-name cell, rubric self-check, etc.), which is expensive to undo.

**4. Classification or regression?**

Read this off the reader's target-column diagnosis if you have it, or check the target column's dtype and number of distinct values yourself: a small set of repeated categories means classification; a continuous number with many unique values means regression. `references/algorithm-ladders.md` covers the escalation path and the true honest tradeoffs for each - read whichever branch applies (or both, if you're building notebooks on multiple candidate datasets that split across the two).

**5. If this is coursework, what has the course taught by now?**

The confirmed-taught toolkit grows every session - check project knowledge (session notes, session slide PDFs, any transcripts the user has uploaded) for what's been covered *as of today*, not what was covered when this skill was written. Don't reach for a method the class hasn't seen yet unless project knowledge clearly confirms it's landed (e.g. once neural network sessions happen, that's a new rung this skill doesn't yet know about - update `references/algorithm-ladders.md` accordingly rather than guessing).

## Build the notebook

Four reference files carry the actual content decisions - read the ones that apply before writing a single cell:

- **`references/audience-modes.md`** - **read this one first, always.** Who the artifact is for, and what that changes: voice, structure, cut-list, and which deliverable to produce at all. The other three files describe the full STUDENT/GRADER arc; this one tells you whether that arc is the right shape for this reader in the first place.
- **`references/notebook-structure.md`** - the fixed section-by-section arc every notebook follows (business framing → load → EDA → cleaning → baseline → algorithm ladder → tuning → metric justification → comparison → recommendation → limitations), with the classification/regression forks marked where they diverge.
- **`references/algorithm-ladders.md`** - which models to escalate through, in which order, and the honest reasoning for each rung - including the real possibility that a fancier method loses, which happens on real data and should never be papered over.
- **`references/narrative-style.md`** - the plain-language rules every markdown cell must follow. This is the difference between a notebook that explains and one that just narrates code.

If this is a graded submission, also read **`references/graded-assignment-checklist.md`** before you start - it covers the things that are invisible in the content itself (team-name placeholders, rubric self-checks, the AI-disclosure question) but will cost real points if skipped.

## Get the numbers before you write about them

Work in this order, because it's the only way to avoid narrating numbers that turn out to be wrong: write a scratch script first that loads the data, cleans it, trains every model on the ladder, and prints every score you'll reference. Run it. Only once you have real printed numbers in front of you should you write the markdown that discusses them - and write the markdown to match the numbers you got, not the numbers you expected to get. If a tuning grid or model ranking surprises you (a "worse" algorithm wins, or tuning barely moves the needle), that surprise is worth keeping in the notebook honestly rather than smoothing it into a tidier story that didn't happen.

Assemble the actual `.ipynb` with `nbformat` - alternating `nbformat.v4.new_markdown_cell(...)` and `nbformat.v4.new_code_cell(...)` in the order your structure calls for, then `nbformat.write(nb, path)`. There's no bundled builder script for this step because the content is different every time; the pattern itself is simple enough not to need one.

## Execute and verify - the non-negotiable step

Run `scripts/execute_notebook.py <notebook path(s)>`. It restarts a completely fresh kernel and executes every cell top to bottom, exactly the way a grader (or the user, or Colab) would - then reports pass/fail and only overwrites the file with baked-in outputs on success.

This step is not optional and not a formality. The most common technical failure in submitted notebooks is a notebook that only works because of a variable still sitting in memory from a cell that was later edited or deleted - invisible on your own screen, fatal the moment someone opens a fresh copy. If execution fails, fix the cell that broke (or an earlier cell it silently depended on) and **re-run the whole notebook from scratch again** - not just the one cell - because a partial re-run can hide the exact problem you're trying to catch.

After a clean execution, go back through the markdown cells and check every number you wrote against what the executed output actually printed. Numbers drift during iteration (you tune a grid, the "best" combination changes, a chart's peak moves) - this reconciliation pass is where you catch stale prose before delivery, not after.

## Self-check before calling it done

**If graded:** find the actual current rubric (in the conversation, project knowledge, or by asking) and re-read it once, line by line, against your finished notebook - every "excellent"/top-band criterion, not just the ones you feel confident about. State explicitly, in your closing summary, anywhere you're not fully certain the notebook hits the top band, and why. Never silently claim full marks you haven't actually checked.

**If practice (STUDENT):** the test is whether someone with zero ML background could read the notebook and explain the dataset's story back in their own words - what it's predicting, why the metric was chosen, why the winning model won. If a section only makes sense to someone who already knows the material, it needs another pass.

**If EXECUTIVE:** the test is whether someone who has never heard of a decision tree could read the brief alone - no notebook, nobody standing next to it - and state the recommendation, what it's worth, and the main risk, without a single follow-up question. Then sweep the brief for leaked method vocabulary (model names, metric names, "overfitting," "tuning," "features"); any survivor is a sentence that needs rewriting, not a term that needs a footnote.

## Deliver

**STUDENT / GRADER:** send the finished `.ipynb` (plus the dataset CSV, if the notebook expects a local file it doesn't already have).

**EXECUTIVE:** send the brief as the headline deliverable and the notebook as its appendix - in that order, and say which is which. Delivering the notebook first buries the thing the reader actually needs behind the thing they'll never open. If you built notebooks for more than one candidate dataset and noticed something that would matter to choosing between them, flag it plainly in your closing summary - but the choice between datasets belongs to the user (and their team, if it's a team assignment), not to this skill.

## Guardrails

- **Never write a number in markdown that didn't come from an executed cell.** If a cell prints `0.776`, the prose says "about 0.78," not a number you estimated before running anything.
- **Never skip the fresh-kernel execution, and never treat a partial re-run as equivalent to a full one.** This is the single check that catches the "worked on my screen, breaks for the grader" failure mode.
- **Leave AI-use disclosure to the user.** Don't add or omit a disclosure cell on your own judgment. The user follows their course or employer policy and decides where the disclosure goes. If it's a graded submission and nothing has been said, ask.
- **Never assume a rubric's point values or exact wording carry over from a previous assignment.** If it's graded, find and read the actual current rubric before building. If none exists yet in the conversation or project knowledge, ask for it rather than guessing from memory of a past one.
- **Never load data from a URL or a hardcoded local path.** Always a plain relative filename, so the notebook survives being handed to Colab with just the CSV sitting alongside it.
- **Never build before the audience is declared, and never leave it implied.** An artifact aimed at nobody in particular is the one failure mode that no amount of correct modeling redeems. State the intended reader inside the artifact itself.
- **Never let method vocabulary leak into an EXECUTIVE brief's main body.** Not simplified - absent. Model names, metric names, and words like "overfitting" or "hyperparameter" all belong in the appendix notebook.
- **Don't silently guess on audience, graded-vs-practice, or classification-vs-regression when it's genuinely unclear.** Getting either wrong means rebuilding structural parts of the notebook after the fact, which costs more than asking up front.
- **Don't force a tidy narrative onto real results.** If boosting loses to a random forest, or a simple linear model beats an ensemble, say so plainly - that honest result shows up on real datasets, and forcing every notebook toward "the fanciest model won" would be dishonest, not polished.
