# ml-notebook-executor

**Use it when** the direction is agreed and you want a complete, runnable notebook.

Step 3 of 4 in the [ML notebook set](../README.md#ml-notebook-workflow).

## The problem

Two things kept going wrong with AI-built notebooks. The text described numbers the code didn't produce. And the notebook ran on my screen but broke on a fresh run, because a variable only existed in memory from a cell that had since changed.

A third problem was audience. A notebook written for a grader is the wrong thing to hand an executive.

## What it does

1. **Declares the reader first:** student, grader or executive. That choice sets the voice, the structure and what gets cut. Executive mode produces a findings-first brief with the notebook as an appendix.
2. **Gets the numbers before writing about them.** It runs a scratch script that trains every model and prints every score, then writes the text to match.
3. **Builds an algorithm ladder** where each new model exists because the one before it has a named weakness. If the simpler model wins, it says so.
4. **Executes the finished notebook in a fresh kernel**, top to bottom, with `scripts/execute_notebook.py`, and re-checks every number in the text against the output.

## What's in the folder

- `SKILL.md`: the process
- `references/audience-modes.md`: the three reader modes
- `references/notebook-structure.md`: the section-by-section arc
- `references/algorithm-ladders.md`: which models to climb through, for classification and regression
- `references/narrative-style.md`: plain-language rules for text cells
- `references/graded-assignment-checklist.md`: extra checks for graded work
- `scripts/execute_notebook.py`: the fresh-kernel run

## What it won't do

- Write a number in text that didn't come from an executed cell.
- Treat a partial re-run as proof the notebook works.
- Load data from a URL or a hardcoded path.
- Force a tidy story onto messy results.

## A note on AI disclosure

My original version told Claude never to mention AI use inside the notebook, because I handled disclosure separately for my course. The public version leaves that decision to you and tells Claude to ask. Follow your own course or employer policy.

## Limits

- The ladder covers decision trees, bagging, boosting and their regression counterparts. Extend `algorithm-ladders.md` for anything else.
- Needs code execution, plus `nbformat` and `nbclient` or `nbconvert` available in the sandbox.
