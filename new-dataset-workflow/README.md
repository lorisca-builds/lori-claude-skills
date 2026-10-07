# new-dataset-workflow

**Use it when** you have a dataset you haven't looked at yet and the goal is a predictive model.

Step 1 of 4 in the [ML notebook set](../README.md#ml-notebook-workflow).

## The problem

I was learning machine learning on a one-year MBA, and the easy mistake was picking an algorithm before understanding the data. Claude would happily go along with it and describe a well-known dataset from recall, with numbers nobody had checked.

The skill puts it this way: picking an algorithm before understanding the data is like a doctor prescribing medicine before hearing the symptoms.

## What it does

It reads the data and explains it. It builds nothing.

1. Gets the real data loaded. If the sandbox can't reach the source, it proves that's a network block, tells you your code is fine, and asks for the CSV.
2. Runs real code for shape, types, missing values, target balance, duplicates and correlations.
3. Names the things that change the recommendation: size, ID codes stored as numbers, class imbalance, a dataset that is too easy.
4. Picks at least two metrics, each tied to something it found.
5. Says where modeling should start and why, then stops and asks if you agree.

The output follows a fixed plain-language structure that ends with "What I'm not sure about."

## What it won't do

- State a number that didn't come from code run in the conversation.
- Write modeling code or a notebook. That pause is where you get to disagree before code exists.
- Skip the inspection because you're in a hurry.

## Limits

- Built around tree-based models for tabular data, because that is what I was studying.
- Hands off to [ml-notebook-executor](../ml-notebook-executor/) for the build.
