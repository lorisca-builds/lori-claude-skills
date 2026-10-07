# Narrative style - plain language, real content

This mirrors the same standard `new-dataset-workflow` holds itself to, because the two skills are meant to read as one continuous voice across a session: **simple words, not simple content.** The user is learning this material to be examined on it - a cartoonishly dumbed-down version they couldn't defend in front of their professor is worse than useless. The job is translation, not dilution.

## The core rules

**Assume zero prior ML background, with no shame about it.** Never write as if a term is already familiar. Never say "as you know" or "obviously."

**Define every technical term in the same breath you use it, not in a glossary at the end.** "A **hyperparameter** - a dial we set before training, rather than something the algorithm learns on its own" is the right shape. A term introduced and used three paragraphs before it's defined has already lost the reader.

**Use concrete analogies where they genuinely clarify - and only there.** "Boosting chains trees together like a tutor who reviews your last practice test and drills exactly what you got wrong" earns its place because it makes the *mechanism* click, not just the vibe. An analogy that's cute but doesn't actually explain how the thing works is padding - cut it.

**Every code cell gets a markdown cell before it explaining what it does and why it's needed** - not "this splits the data" but "we hold back 20% of the data as a test set because grading a model on data it already memorized proves nothing, the same way grading a student on the exact questions they practiced would." What, and why, together - a common rubric criterion, and just good writing regardless of whether the notebook is graded.

**Don't restate what's obvious from the code.** If a line reads `X_train, X_test = ...`, the markdown shouldn't just say "this splits X into train and test" - that's visible in the line itself. The markdown should add the *reasoning* the code alone can't carry: why this split ratio, why stratify, why this random seed choice matters for reproducibility.

**When results surprise you, say so honestly rather than smoothing them over.** "Tuning here only moved the score by a few tenths of a point - a sign we were already close to this model's ceiling" is more useful and more honest than pretending every tuning pass produces a dramatic before/after. Real modeling work is full of results like this, and pretending otherwise teaches the wrong lesson.

## A worked example of the shape

**Weak (don't write this):**
> This code trains a random forest and evaluates it on the test set.

**Better:**
> A single tree, even tuned, is fragile - its whole flowchart hinges on which question happens to win at the top, so a slightly different set of training students could produce a meaningfully different tree with different mistakes. A **random forest** fixes this by training many trees in parallel, each on its own random sample of students (with repeats allowed - a trick called **bootstrapping**), and letting them vote. Individual trees still make mistakes, but different trees make *different* mistakes, and the vote averages the noise away.

The second version names the specific weakness being fixed, defines the two new terms it introduces inline, and sets up the reader to interpret the numbers that follow - rather than just labeling what the code does.

## Formatting notes

- Numbers cited in prose should read as approximations with the real figure nearby ("roughly 0.77 accuracy" is fine right next to a cell that printed `0.776`) - but the real number must always be visible in an executed output somewhere on the page. Never state a number in prose that isn't backed by an executed cell.
- Keep code cells clean and commented, but let the *why* live in markdown, not in a wall of inline comments. A code comment explaining a genuinely non-obvious one-liner is fine; a comment repeating what the markdown above it already said is clutter.
- Section headers should read as plain-language questions or statements ("Why plain accuracy would mislead here," not "Metric Selection Methodology") wherever that reads naturally - this keeps the notebook feeling like an explanation rather than a technical report.
