# ml-notebook-audit

**Use it when** a notebook is drafted and you want it checked before you submit or share it.

Step 4 of 4 in the [ML notebook set](../README.md#ml-notebook-workflow).

## The problem

By the time a notebook is finished, I can't see it anymore. I know what I meant, so I read that instead of what's on the page. The costly mistakes are also boring to check by hand: a sentence that says 90% above code that prints 80%.

## What it does

It reports. It never rewrites. Seven passes:

1. **Sequence:** is the order sound? It flags EDA before cleaning and any decision made before the train/test split.
2. **The chain:** does each model have a stated reason to exist?
3. **Number matching:** every number in the text is checked against code output.
4. **Dead weight:** which cells could go without changing a conclusion?
5. **Language:** undefined jargon and adjectives with no number behind them.
6. **Mechanical:** filenames, imports, variables that only exist in memory.
7. **The stranger read:** five sentences stating the argument the notebook actually makes.

The seventh is the most useful part. If those five sentences don't match what you thought you wrote, the problem is structural.

Findings come ranked in three bands: would make it ungradeable, loses marks directly, polish.

## What it won't do

- Rewrite cells or add analysis.
- Claim the notebook runs. It can't execute it, and it says so.
- Run a partial audit on a notebook with cleared outputs and call it complete.

## Limits

- Needs the executed notebook or its PDF export, with outputs.
- A fresh top-to-bottom run is still on you. The report ends by telling you to do it.
