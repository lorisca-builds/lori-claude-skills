---
name: ml-notebook-audit
description: Audits a finished machine learning notebook draft for sequence, argument and narrative before submission. Use when a notebook is drafted and the user wants it checked rather than extended in coursework or any ML deliverable. Trigger on "audit my notebook", "check my notebook", "review my draft", "does this hang together", "is my narrative consistent", "check the sequence", "do my numbers match", "pre-submission check", "read this as a stranger", "is this over-engineered", or whenever the user uploads a drafted .ipynb or its PDF export and asks whether it is ready. Reports findings ranked by what costs marks, and reflects back the argument the notebook actually makes so they can compare it to the one they intended. Never rewrites the notebook and never adds analysis - that is ml-notebook-executor's job. Cannot certify that code runs, only flag likely breaks.
---

# ML Notebook Audit

Runs on a finished draft. Reports, does not rewrite. The point is to find the gap between the
argument the user thinks they made and the one that is actually on the page.

Pairs with `ml-notebook-executor`, which builds. If the notebook is half-finished or they want more
analysis, hand back to that skill and stop.

## What you need

The executed notebook, `.ipynb` preferred, or its PDF export. Both carry the outputs.

**If the outputs have been cleared, say so immediately and ask for the executed version.** Without
outputs, the number-matching pass is impossible, and that pass finds the failure that costs the most
marks. Do not run a partial audit and present it as complete.

## What this skill cannot do

It cannot execute the notebook, so it cannot certify that it runs. It can flag missing imports,
variables used before assignment in visible code, and filename mismatches, but the only real proof
is a fresh runtime run from top to bottom, and that is the user's job. Say this once, in the report, and
do not imply otherwise.

## Pass 1 - Sequence

Check the order against this spine and flag departures:

load, look, clean, EDA, split, baseline, model ladder, one improvement, test once, recommendation,
limitations.

Two departures are serious rather than stylistic, and both need naming as such:

**EDA before cleaning.** Statistics computed on dirty data are wrong, so the EDA is measuring noise.
Flag it and say that.

**Any decision made before the split.** Anything chosen by looking at the whole dataset, including
the test portion, has leaked. Feature selection, encoding fitted on everything, imputation values.

Also check that the test set is touched exactly once, at the end. If it appears earlier, the final
number is not clean and the notebook should not claim it is.

## Pass 2 - The chain

The difference between reasoning and a catalog is whether each step exists because the previous one
has a named weakness.

For every model after the baseline, find the sentence that says what the model before it got wrong.
If there is no such sentence, flag it. If the text reads "we also tried", "additionally we ran", or
lists algorithms without motivation, flag it as a catalog and quote the line.

Check that the argument closes. Somewhere the notebook must say why the winner won, in a sentence
that is not just "it scored highest".

## Pass 3 - Number matching

This is the failure graders punish hardest, and it is mechanical, so do it thoroughly.

Extract every number from every markdown cell. For each, find it in a code cell's output. Report
every one that does not match, with the markdown cell it is in, the number claimed, and the number
actually printed.

Also check chart titles, axis labels and printed strings inside code, since a stale label like
"max depth = 3" sitting over code that uses 14 is the same failure in miniature.

Report the count checked and the count matched, so coverage is visible.

## Pass 4 - Dead weight

For each cell, ask whether deleting it would change a decision or a conclusion. If not, propose
cutting it and say why.

Flag these patterns explicitly:

- More than three model families where fewer make the same point.
- A section built around a technique that produced no improvement. Reporting a null result is
  strong, but it belongs in a sentence, not a section.
- More than one tuning dial where the second and third changed nothing.
- Repeated exploratory cells left in from drafting.
- Numbered sections past about twelve, which usually means the argument has been diluted.

Do not flag something as dead weight if it carries the argument. A baseline that scores well and
finds nothing looks trivial and is the most valuable cell in most notebooks.

## Pass 5 - Language

Text cells are for a non-technical reader. Code comments are where technical language lives.

Flag every term used before it is defined in plain words. Flag orphan adjectives with no comparison
number attached: robust, powerful, state of the art, comprehensive, cutting edge. Flag any sentence
that would not survive being read aloud to a manager who has never written code.

Flag numbers presented in transformed units that were never translated back. Nobody has intuition
for a value expressed in standard deviations. Give it in real dollars, real hours, real people.

Flag any number stated without a "which means" clause nearby. The number is not the finding.

## Pass 6 - Mechanical

- The filename in `read_csv` against the actual file, character for character, watching for a
  trailing "(1)".
- Every variable used is assigned somewhere in the visible code. A variable that exists only in the
  live session is the invisible bug: the notebook works on their screen and dies on the grader's.
- All imports present and at the top.
- Cells in an order that runs top to bottom.
- Their name in the notebook.
- AI use disclosed, if the course or employer policy asks for it.

## Pass 7 - The stranger read

Read the notebook as someone who has never seen it, and produce this before anything else in the
report:

> **The argument your notebook actually makes.** Five sentences, in the notebook's own order,
> using only what is on the page.

Then say, in one line, where a first-time reader would get lost or have to re-read.

This is the highest-value output of the skill. If the five sentences do not match what the user thought
they wrote, the problem is structural, and no amount of line editing fixes it.

## The report

Deliver in this order and nothing else.

1. **The argument your notebook actually makes.** The five sentences from pass 7.
2. **Where a reader gets lost.** One or two lines.
3. **Findings**, ranked by cost, in three bands:
   - **Would make it ungradeable.** Code that will not run, a missing file, a variable that only
     exists in memory. Nothing else can be evaluated if these are present.
   - **Loses marks directly.** Number mismatches, a model with no named reason, EDA before cleaning,
     the test set touched more than once, undefined jargon in a business text cell.
   - **Polish.** Dead weight, orphan adjectives, untranslated units.
4. **What was checked and found clean.** Name the passes that came back with nothing, so coverage is
   visible and they are not left wondering.
5. **The one thing to fix first**, if they only have time for one.

Each finding gets three things and no more: where it is, what is wrong, and the fix in one line.

## Hard rules

**Report, do not rewrite.** Do not produce corrected cells unless asked. The moment this skill starts
writing content it stops being an audit and starts being a second draft.

**Do not add analysis.** If the notebook is missing a step, say it is missing. Do not fill it in.

**Quote, do not paraphrase.** Every finding names the cell and quotes the line. A finding they cannot
locate is not actionable.

**Say what you could not check.** If outputs are missing, if a file is not available, if the audit
could not verify something, list it. Silence reads as a pass.

**End with the run instruction, every time.** The audit does not replace it:

> Close the notebook completely, reopen it, reload the dataset, and run from the top to the bottom
> in a fresh runtime. That single move catches the filename mismatch and the variable that only
> exists in memory, and nothing in this report is a substitute for it.
