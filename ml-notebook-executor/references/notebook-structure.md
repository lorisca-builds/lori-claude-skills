# Notebook structure - the fixed narrative arc

Every notebook this skill builds follows the same shape, whether the destination is a graded team submission or a solo practice notebook, and whether the target is a category (classification) or a number (regression). The two problem types diverge in specific spots - marked below - but the arc itself doesn't change, because the arc *is* the pedagogical point: understand before cleaning, clean before modeling, baseline before comparing, and justify every choice in plain language before the reader hits the code that implements it.

Treat this as a checklist of sections, not a rigid cell-by-cell script - a section can span several code/markdown cell pairs if the content needs it (a hyperparameter search, for instance, usually needs its own explanation cell, its own loop/grid cell, and its own "here's what the chart shows" cell after).

## 1. Title cell

State what the notebook does and what dataset it uses, in one or two sentences. If this is a graded team submission, include an explicit placeholder for team member names (e.g. `**Team members:** [Team Member Names Here]`) - don't ask the user to fill it in before you finish; leave the placeholder and move on. If it's a solo practice notebook, skip the placeholder entirely; there's no team to name.

## 2. The business problem, in plain language

What real-world decision does this prediction serve, and who would act on it? This is not decoration - it's the frame that makes every later section's audience obvious ("assume zero ML background" only works if the reader knows *why* they should care). Ground it in something concrete: a business, an institution, a person making a decision with limited information. Avoid restating the dataset's UCI/Kaggle description verbatim; translate it into a scenario.

## 3. Load the data, take a first look

Load from a plain relative filename (see the guardrail in SKILL.md - never a URL, never a hardcoded absolute path). Print shape. Then, in markdown, explain in plain words what one row *is* and what the columns mean, grouped sensibly if there are many. Name the target column explicitly and say what predicting it well would actually let someone do.

Flag anything about the raw file itself that a reader would trip over if unexplained - unusual delimiters, stray whitespace in values, columns whose "numbers" are actually category codes wearing a numeric costume. If the reader pass already surfaced this, don't rediscover it from scratch - verify it's still true and move on.

## 4. Real exploratory data analysis (EDA)

Every claim here must come from a number a code cell actually printed in this run - no exceptions, and no reusing a number from the reader's earlier pass without re-running it, since a fresh notebook run is a fresh source of truth.

**For classification:** compute and show the target's class balance (`.value_counts(normalize=True)`). This number is not optional - it is what determines the entire metric-selection argument in Section 9, so get it on the page early and refer back to it explicitly later rather than re-deriving it.

**For regression:** show the target's distribution (a histogram, plus mean/median/spread) - is it roughly symmetric, skewed, does it have a long tail of extreme values? This matters for the same reason class balance matters in classification: it determines which error metric will actually reflect what "doing well" means (a metric sensitive to large errors behaves very differently on a skewed target with rare huge values versus a tight, symmetric one).

Then look at relationships to the target - group-by comparisons for classification (how do the numbers differ between classes?), correlations or grouped means for regression. Explain what each finding *means* in plain terms, not just what the number is. This is the section that proves the data actually contains a learnable pattern, which is the whole justification for building a model at all.

## 5. Cleaning and preparing the data

List every real issue found - missing values (including disguised ones like `"?"` placeholders), duplicate rows, redundant columns, category codes that need converting to a model-readable form, anything else - and justify the fix for each one *before* the code cell that performs it. "We drop rows with unknowns because X, and here's the tradeoff we're accepting" is the required shape; "here's some cleaning code" with no justification is not.

If a column looks redundant with another (two encodings of the same information), verify it programmatically before dropping it - don't drop on a hunch. If dropping a chunk of rows for missing data, check afterward that the class balance (or target distribution) didn't shift meaningfully - that's the honest way to confirm the fix didn't quietly change the problem you're solving.

## 6. Split into training and test data

Explain *why* a held-out test set matters (a model graded on data it memorized proves nothing) before the split code. For classification, `stratify=` on the target is worth explaining explicitly - it exists precisely because Section 4 already showed the classes are imbalanced. Fix a random seed here and note that the same seed is used everywhere randomness appears in the notebook, for reproducibility.

## 7. The baseline

**Classification:** always-guess-the-majority-class, scored on the test set. State the resulting accuracy plainly, and note explicitly what it fails to do (never right about the minority class this notebook may care most about) - that failure is the setup for the metric-selection argument later, so don't let this section pass without connecting the two.

**Regression:** always-guess-the-mean (or median) of the training target, scored on the test set with whatever error metric the notebook will use throughout (see algorithm-ladders.md for the honest tradeoffs among R², RMSE, and MAE). State the resulting score plainly as the floor every real model must beat.

## 8. The algorithm ladder

Follow `references/algorithm-ladders.md` for the specific models and order. The shape that matters regardless of which ladder: train an unregularized/default version first, let it show its real weakness (usually overfitting - memorizing training data at the cost of test performance), tune it, then move to the next model *only after naming, in plain language, the specific weakness of the previous model that justifies the move*. This "each step because of a named flaw in the last" structure is what turns a list of models into an actual argument - a rubric criterion in its own right for this course, and good practice regardless.

Use a consistent scoring helper across every model in the ladder (same train/test split, same metrics printed, same rounding) so the final comparison table in Section 10 is apples-to-apples without extra munging.

## 9. Hyperparameter tuning

Tune at least one model - normally whichever one is leading the ladder - over a real range of at least one hyperparameter, explained in plain language: what the dial controls, why this range, what changed as a result. Prefer a small grid over two interacting dials (e.g. tree count and learning rate for a boosting model) over tuning one dial in isolation, when the dials genuinely interact - and say so if the grid's winner sits on a "plateau" of similarly-scoring neighbors rather than a lucky spike, since that's the honest way to tell whether the tuning found something real or just noise.

## 10. Metric selection - the honest argument

This section earns its own real estate; don't compress it into a single sentence. Walk through:

- **What plain accuracy (classification) or a naive average error (regression) would hide**, using the *actual* numbers from Sections 4 and 7 - not a generic textbook warning, but "here, on this dataset, the naive baseline already scores X while doing Y-useless-thing."
- **The building-block metrics in plain words** - precision/recall/F1 for classification (defined per-class, in the same breath as introduced); R²/RMSE/MAE for regression (what each one actually measures, in a sentence a non-technical reader would get).
- **The headline metric this notebook adopts, and why it fits this dataset's actual shape** - traced back to the balance/distribution numbers from Section 4, not asserted from habit.
- A secondary metric reported alongside, for the intuitive "what would a non-technical stakeholder ask for first" reason.

Two notebooks in the same batch (e.g. two candidate datasets for the same assignment) do **not** need to land on the same metric - pick independently, per dataset, and say so if they differ.

## 11. Side-by-side comparison

One table, every model from the ladder plus the baseline, same metrics, same held-out test set. Sort by the headline metric so the winner is visually obvious. This is the evidence the final recommendation leans on - don't let the recommendation cite a number that isn't sitting right here in the table.

## 12. Final recommendation

State the winning model plainly, then justify it with **data** (the actual numbers from the comparison table), **logic** (the chain of named weaknesses from Section 8 that led here), and **intuition** (the judgment call, stated as a judgment call, about *why* this algorithm family suits this specific data's shape - not asserted as certainty). Then tie it to the business framing from Section 2: who uses this, what decision does it inform, and what's the concrete payoff (a number, if you can honestly produce one - a lift over random targeting, a share of at-risk cases caught, etc.).

Name the real tradeoff of the winner honestly (usually: less interpretable than a small tree) and say what you'd fall back to if that tradeoff mattered more in a given context.

## 13. Limitations

An honest, specific list - not a generic disclaimer paragraph. Data age, survey-versus-observed-behavior, sample size, anything found during cleaning that couldn't be fully resolved, fairness/protected-attribute concerns if demographic columns were used, correlation-versus-causation cautions where the recommendation could be misread as causal. Specific to *this* dataset, not boilerplate that would apply to any dataset.
