# Review checklist

Only relevant when step 3 in SKILL.md concluded this notebook is a reviewed deliverable: a take-home exercise, a model handed to a risk or validation reviewer, a team deliverable that a lead signs off, or client work with acceptance criteria. Everything here is in addition to the standard structure in `notebook-structure.md` - it doesn't replace any of it.

## Find the real criteria - don't assume last time's still apply

A reviewed deliverable usually comes with its own brief: acceptance criteria, a scoring guide, a list of questions the reviewer wants answered. Find and read the current one before building anything. Criteria can differ between deliverables even when the general shape (method choice, code explanation, measured improvement, notebook mechanics) looks familiar. If no criteria are available anywhere, ask for them rather than reusing a remembered set from a previous piece of work - that's a guess dressed up as knowledge, exactly the kind of thing `new-dataset-workflow` warns against for dataset statistics, and the same discipline applies here.

Once you have them, re-read them fully before building (not just skim) and check the finished notebook against every criterion as the final self-check step in SKILL.md describes.

## Owner and contributor line

The title cell names who owns the work and who contributed, with an explicit placeholder if those names aren't known yet - e.g. `**Owner:** [Name] · **Contributors:** [Names]`. A reviewer needs to know who to ask, and an unowned notebook reads as unfinished. Never stall the build to collect names. Leave the placeholder and move on. A solo practice notebook needs no owner line.

## AI-use disclosure belongs to the user

The user follows their organization's or client's policy and decides whether and where a disclosure goes. Don't add a disclosure cell on your own, and don't leave one out on your own either. If nothing has been said about it for a reviewed deliverable, ask before delivering.

## "Restart and run all" is a hard gate

A specific, common failure: a variable defined in one cell, then that cell gets edited or deleted later, but the notebook keeps running fine on your own screen because the variable is still sitting in the kernel's memory from before. It fails the instant a reviewer opens a fresh copy and runs top to bottom. The general execution guardrail in SKILL.md already covers this, but for a reviewed deliverable there is no credit for "it worked when I ran it." A notebook that doesn't execute clean in a fresh kernel can't be verified at all, so a reviewer has no reason to trust any number in it.

## Load from the delivered data file, not a live pull

The final version loads data from a plain local filename that ships alongside the notebook - never a live URL fetch, even if a URL fetch was used for convenience while exploring. A reviewer's environment may not have the same network access this build environment does, and a live source can change under them, which makes the results impossible to reproduce.

## Match the house style

If the team has existing notebooks, a style guide or a reviewer's own examples in project knowledge, skim them for vocabulary, depth and layout before writing markdown. The goal is a notebook that reads like it belongs in that team's repository, not a generic tutorial. Don't introduce a method or term the reader can't evaluate unless the brief asks for it (see the note in `algorithm-ladders.md`).

## Build toward the walkthrough

If the deliverable includes a spoken walkthrough or a live review (check the brief - don't assume), the notebook's narrative should set up everything that conversation needs, even though running it isn't part of this skill's job. That means a clear, unambiguous final recommendation, the metric choice explained in a way that survives being said out loud, code explained at the concept level as well as the line level, and the improvement reasoning (tuning, algorithm choice) stated plainly enough to summarize in a sentence or two per step.
