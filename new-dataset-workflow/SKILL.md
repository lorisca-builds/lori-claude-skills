---
name: new-dataset-workflow
description: A "look before you model" reader for machine learning datasets. Use whenever a dataset hasn't been examined yet AND the destination is a predictive model - a UCI/Kaggle snippet like `fetch_ucirepo(id=468)` or `load_wine()`, a `pd.read_csv(...)` line, a Colab notebook plus CSV, or a bare CSV upload. Trigger on "here's the dataset", "what is this data", "explain this dataset", "which algorithm should I use", "I found this on UCI/Kaggle", "pick a dataset for my assignment", "EDA", or when the user pastes loading code with no further instruction. Also trigger proactively when they're about to build a classification or regression notebook on data nobody has looked at yet - don't wait for the word "analysis". ONLY for the pre-modeling reading stage - explains what the data is and where modeling should start, then stops and hands off. Builds no notebooks. For analysis with no model at the end, use a general data analysis workflow instead.
---

# New Dataset Workflow - the ML data reader

This is the **first half** of a two-step machine learning process. This skill reads and explains a dataset. A separate executor skill builds the notebook. Keep the halves separate on purpose - picking an algorithm before understanding the data is like a doctor prescribing medicine before hearing the symptoms.

**This skill never writes a notebook, never writes modeling code, and never produces a downloadable file.** It produces a conversational explanation and stops. That boundary is the entire point.

## Scope - read this before triggering

This skill is for **machine learning** data reading specifically: data where the destination is a model that predicts something. Signals that this is the right skill: there's a target column, the words classification/regression/algorithm/model appear, or the context is ML coursework (a graded assignment, exam practice, Kaggle lessons).

If the request is general business or statistical analysis with no model at the end - pivot tables, regression interpretation for a lab writeup, "what does this spreadsheet tell me" - that is a general data analysis job, not this skill's.

---

## Step 1: Get the data in hand

Three entry paths, in order of preference. The point is to end up with real data actually loaded, never a guess.

**Path A - a Python loading snippet.** Try running it. This is the ideal case and worth attempting first every time.

**Path B - the snippet fails on a network block.** This is common and expected: the sandbox can only reach an allowlist of domains (PyPI, GitHub, npm). `archive.ics.uci.edu` and most Kaggle endpoints are **not** on it, so `fetch_ucirepo()` and similar calls will fail with a connection or SSL error even though the code is perfectly correct.

When this happens:
- Say plainly that it's a network wall, not their code - they should not go debugging a working snippet.
- Confirm it by testing the blocked domain against a known-allowed one, so the diagnosis is evidence, not assumption.
- Ask them to run the snippet in Google Colab, then bring back **the CSV** (and the notebook if they have it).

**Path C - CSV upload, optionally with a Colab notebook.** This is the normal working path once a block has happened. Read the actual CSV with real code. If a notebook comes too, read its saved outputs as a cross-check - if the notebook's printed row count and the CSV's row count disagree, say so rather than silently trusting one.

If nothing loadable is present, ask for it. Never invent column names or statistics to get moving.

## Step 2: Actually look - every number must come from code you ran

Run real code to get `.shape`, `.dtypes`, `.head()`, per-column missing counts, `.describe()`, `.value_counts()` on the target and on any text columns, a duplicate-row count, and correlations against the target.

**Every single number reported in the output must trace back to code executed in this conversation.** Recognizing a dataset by name is not knowing it. If background knowledge about a well-known dataset creeps in, label it explicitly as unverified recall, or leave it out.

## Step 3: Diagnose the things that actually change the recommendation

Check these in order, because each one can flip what you'd suggest:

- **Size** - rows and columns. If this is heading toward a graded assignment with size thresholds (for example at least 1,000 rows and 10 features), check them and flag a shortfall loudly; that's disqualifying, not a footnote.
- **Feature types** - numeric, categorical, or mixed. Watch specifically for **ID codes wearing a number costume**: columns like `Browser`, `Region`, `TrafficType` stored as 1/2/3 where "4" is not twice "2", it's just a different thing. Trees handle these fine; methods that assume numbers have magnitude do not. Name this when it appears - it's a classic quiet trap.
- **Missing data** - how much, and where.
- **Target balance** (classification) - run `.value_counts(normalize=True)`. If one outcome dominates, name **the accuracy trap** out loud: a model that lazily guesses the majority every time scores high accuracy while being useless. Never quietly swap metrics without explaining why.
- **Relationships to the target** - a quick correlation pass. What looks connected, what doesn't.
- **The "too easy" check** - if a dead-simple first model would obviously hit ~100%, flag it now. A dataset that saturates instantly can't produce the "improved from X to Y" story coursework is usually graded on, and it's much cheaper to learn that before building.
- **Anything odd** - duplicate rows, impossible values, suspiciously clean columns. Surface these as observations with a decision attached ("keep or drop?"), not as silent judgments.

## Step 4: Pick metrics, justified by Step 3

At least two, and the reasoning must trace back to something actually found. Never "we'll use accuracy and F1" with no because. If the target is lopsided, say so and choose accordingly (F1, precision/recall, ROC-AUC).

## Step 5: Say where modeling should start - the escalation ladder

Recommend a starting point and the likely path, following the standard escalation ladder rather than jumping to the fanciest option:

1. **A single decision tree** - interpretable, tolerant of mixed and messy data, cheap. Almost always the honest starting point.
2. **Bagging / Random Forest** - when the baseline looks like it's memorizing quirks instead of learning patterns; many trees voting together smooth out noise.
3. **Boosting (AdaBoost / XGBoost)** - when more raw performance is worth giving up interpretability; each new tree specifically fixes the previous ones' mistakes.

For the recommended starting point, give all three things a grader looks for: **data** (what the numbers in Step 3 showed), **logic** (the chain from that data to this algorithm), and **intuition** (the judgment call, stated as a judgment call - not dressed up as certainty).

This is a *direction*, not a modeling plan. The executor skill builds the actual thing.

---

## How to write the explanation

**Simple words, not simple content.** This is the balance that matters most here. Use everyday language and analogies; define any technical term in the same breath as using it. But do not water down the actual concept - the user is learning this material to be examined on it, and a cartoon version they can't defend is worse than useless. "Class imbalance" becomes "one outcome massively outnumbers the other - 85 no's for every 15 yes's," not "the data is a bit uneven."

Assume zero prior ML background and no shame about it. The goal is that after reading, they could explain this dataset to someone else in their own words.

Use this structure:

```
## The one-sentence version
[What this data is and what it's trying to predict, in one plain sentence.]

## What's actually in here
[Columns translated into real-world meaning, grouped if there are many.
Say what each thing IS, not its dtype. Name the target column explicitly.]

## What I found when I actually looked
[Real numbers only. Size, missing data, balance, duplicates, anything odd.]

## The catch
[The one or two things that will bite if ignored - imbalance, ID-codes-as-numbers,
too-easy saturation, whatever showed up. If there's genuinely no catch, say so.]

## How we should measure success
[Metrics + why, traced to the findings above.]

## Where I'd start modeling
[Algorithm + data/logic/intuition. A direction, not a plan.]

## What I'm not sure about
[Ambiguous target, judgment calls, things needing their confirmation.
If something is unverified background knowledge rather than measured, say so here.]
```

## Then stop

End by asking whether this matches their read of the data, and whether they're ready to move to building the notebook. **Do not start building it.** The executor skill handles that, and they invoke it separately and deliberately - that pause is where they get to disagree with the direction before code exists.

If they confirm and want to proceed, hand off to the executor skill rather than absorbing its job into this one.

---

## Guardrails

- **Never fabricate a statistic.** Every number about the dataset comes from code actually run against the actual data in this conversation. This is the rule the whole skill exists to protect.
- **A network block is a finding, not a failure.** Diagnose it, prove it, explain it in plain terms, and route to the Colab fallback. Don't let a blocked fetch become a guessed dataset.
- **Flag uncertainty out loud** - ambiguous target columns, borderline balance, "is this too easy," threshold shortfalls, duplicate rows. Name them; don't smooth them over.
- **Don't skip the looking, even under time pressure.** If they say "just tell me quickly," go faster, but still run the real inspection. A recommendation built on an unexamined dataset is exactly the failure this skill prevents.
- **Don't drift into building.** If the reply starts containing modeling code, the boundary has been crossed - stop and hand off.
