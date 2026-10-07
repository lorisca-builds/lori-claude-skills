---
name: ml-business-insight
description: Turns finished EDA output into the business argument that drives every modeling choice after it. Use after the data is cleaned and explored and before any model is fitted in coursework or any ML project. Trigger on "what does this mean for the business", "so what", "turn this into insight", "business insight", "I've done my EDA now what", "what should I model", "which metric should I use", "help me frame this", "is this worth modeling", or whenever the user pastes EDA output and asks what it means. Produces a decision sentence, the one constraint that drives every later choice, a justified metric pair, and a deliberately capped modeling plan, written for a non-technical reader with no jargon. Refuses to manufacture a business case when none exists. Does not build notebooks, fit models, or read raw unexamined data - that last one is new-dataset-workflow's job.
---

# ML Business Insight

The bridge between "I have looked at the data" and "I know what to model and why". It runs once,
after cleaning and EDA, before the first model is fitted.

Its output is a block the user can paste straight into their notebook as the markdown cell that sits above
the modeling section. Everything downstream should be traceable to it.

## Where this sits

`new-dataset-workflow` reads unexamined data and says where to start. This skill runs later, on
data that has already been cleaned and explored, and converts those findings into an argument.
`ml-notebook-executor` runs after this and builds. If the EDA has not happened yet, say so and stop.

## What you need before answering

Ask for these if they are missing. Do not proceed on assumptions.

- The target's distribution, printed. Counts or percentages, not "it's imbalanced".
- The row and column count after cleaning, and what was dropped.
- Which columns are text and which are numbers.
- Two or three relationships EDA surfaced, with the actual numbers.
- What the dataset is, in one line, and where it came from.

If the user has the charts but not the numbers, ask them to print the numbers. Charts cannot be quoted in
a text cell and the numbers can.

## Step 1 - The decision

The business decision is not sitting in the data. It comes from asking who acts on the prediction.
Generating it from column names alone is where empty jargon comes from.

Write it in this shape and nothing else:

> If [a specific role] knew [the target] in advance, they would [do what differently].

A specific role means a credit officer, a shift manager, a triage nurse. Never "stakeholders",
never "the business", never "decision makers".

Then put it through three questions and show the answers.

**Who receives the prediction.** A person you can picture.

**What do they do today without it.** This is the one that kills fake decisions. If you cannot say
what happens today, there is nothing to improve. For the Adult census data the answer was that the
bank mails everybody, because it has no way to tell.

**What would they do instead.** A different action. "Mail a quarter of the list" is different.
"Make a better decision" is not, and neither is "gain valuable insights".

If the decision fails any of the three, say so plainly and name the alternative target column that
would pass. If no column passes, say the dataset does not support a decision worth modeling and
recommend switching. That is a legitimate output of this skill and it saves hours.

## Step 2 - The one constraint

Most datasets have exactly one property that constrains everything after it. Name it in a sentence,
with its number, and say what it forces.

Common ones and what each forces:

- A lopsided target forces the metric away from accuracy and makes the majority-class baseline the
  most valuable cell in the notebook.
- Heavy text columns force one-hot encoding and push toward the tree family.
- A small number of rows forces simpler models and makes variance the enemy.
- A column that would not be known at prediction time forces its removal, and spotting it is the
  sharpest thing in the whole analysis.
- Two columns that duplicate each other force a drop, because splitting one signal across two
  columns muddies importance later.

Always run the leakage question explicitly: is any column something the decision maker would not
actually have at the moment they need the prediction, or partly a copy of the answer.

## Step 3 - The metric, chosen because of step 2

At least two metrics, and each one justified by the constraint, not by a list. Say which is the
headline and why. Define each in one plain sentence at first use.

On a lopsided target, name the trap out loud: predicting the majority class for everybody scores
well on accuracy and finds none of the cases anyone cares about. That sentence does more work than
any amount of metric theory.

Say what a wrong answer costs in each direction, in the language of the decision from step 1. A
false alarm sends an expensive offer to the wrong person. A miss leaves a real prospect unfound. The
metric follows from which one hurts more.

## Step 4 - The fork that decides the model family

Decide this here, not later. Getting it wrong wastes the most time of any single mistake.

**Category target.** The tree family is the right home. Baseline, one simple model, one better model.

**Number target.** Trees are genuinely poor at this. On the scikit-learn Diabetes data, in my coursework, a tree scored
R² 0.13 to 0.14 while plain linear regression scored 0.45 and XGBoost 0.37. Start with linear
regression as the baseline and justify from there.

**Unstructured data, meaning images, text or audio.** Neural networks are the only real option, and
numeric inputs must be scaled and categoricals one-hot encoded or the network will not work.

## Step 5 - The capped plan

Name the plan and cap it in the same breath, because an uncapped plan is how notebooks sprawl.

Three model rungs maximum. Baseline, one simple model, one better model. A third only if you can
already say what the second is likely to get wrong. Each rung must exist because the rung below it
has a named weakness, not because it is the next algorithm you know.

One improvement lever, measured, and report the size of the gain honestly even when it is tiny.

State the stopping condition before you start: you stop when the next step stops paying, and you say
so in the notebook rather than quietly continuing.

Results from my own coursework argue for this. A seven node regularized tree matched the big unrestricted
one exactly. XGBoost improved when cut from 300 trees to 10. AdaBoost, the fancier method, lost to a
plain regularized tree. Simpler winning is a citable finding, not a preference.

## The output

Deliver exactly this, ready to paste. Nothing before it, nothing after it.

```
## What we are actually deciding

[Decision sentence.] Today, [what happens without the model]. With it, [the different action].

## What the data says

[The one constraint, with its number, in one sentence.]
[What that constraint forces, in one sentence.]
[One or two supporting findings from EDA, each with its number and each followed by what it means.]

## How we will judge success

[Headline metric], which asks [plain definition], because [reason tied to the constraint].
[Second metric], which asks [plain definition], because [reason].
A model that [describes the trap] would score [number] on accuracy and be useless, which is why
accuracy is not our headline.

## The plan, and where it stops

[Baseline]. [Simple model]. [Better model, and the weakness it treats.]
One improvement lever: [which one and why].
We stop when [condition].

## What could go wrong

[Risk one, in plain words.]
[Risk two.]
```

Keep the whole block under 300 words. If it runs longer, something in it is not earning its place.

## Hard rules

**Never state a number that is not in the output the user pasted.** This is the most punished failure in graded work: text saying 90% above code that prints 80%. If a number is needed and not
present, ask for it or leave a visible gap.

**Refuse rather than manufacture.** If the data does not support a decision anyone would act on, say
that. A skill that always produces a business case produces worthless ones.

**Two tests before delivering.** After every number in the block, the sentence "which means" must be
completable. After every technique named in the plan, "we needed this because" must be completable
without the answer being "because it is what you do". Cut anything that fails.

**Business language in the block, technical language only in code comments.** If a sentence would
not survive being read aloud to a non-technical manager, rewrite it. Define any term the moment it
first appears, then use it freely.

**No orphan adjectives.** Robust, powerful, state of the art, cutting edge, comprehensive. If no
comparison number follows, the word goes.

## If the user is working in Colab with Gemini rather than here

Give them this to paste, and nothing else:

> Here is my cleaned data summary and my EDA output. Do not write code.
>
> One: list the columns that could plausibly be predicted, and for each write "If [specific role]
> knew [column] in advance, they would [do what differently]". No "stakeholders", no "the business".
> Rank them by whether a real organisation would change what it does today.
>
> Two: name the single property of this data that will constrain every decision after this, and say
> what it forces. Flag any column I would not know at the moment of prediction.
>
> Three: recommend two metrics and justify each from that constraint, not from a list.
>
> Four: give me a modeling plan of no more than three models, where each one exists because the
> previous one has a named weakness. Tell me when to stop.
>
> Use only numbers that appear in what I pasted. If a step is standard practice but would not change
> the answer here, tell me to skip it.
