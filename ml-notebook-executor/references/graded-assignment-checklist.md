# Graded assignment checklist

Only relevant when Step 2 in SKILL.md concluded this notebook is for a graded team submission (whatever the assignment is called in the current term or course). Everything here is in addition to the standard structure in `notebook-structure.md` - it doesn't replace any of it.

## Find the real rubric - don't assume last time's numbers still apply

A graded assignment usually comes with its own rubric PDF or doc, uploaded to the conversation or sitting in project knowledge. Find and read the actual current one before building anything. Point values, criterion names, and band thresholds can differ between assignments even when the general shape (algorithm selection, code explanation, performance improvement, notebook mechanics) rhymes. If no rubric is available anywhere, ask for it rather than reusing a remembered one from a previous assignment - that's a guess dressed up as knowledge, exactly the kind of thing `new-dataset-workflow` warns against for dataset statistics, and the same discipline applies here.

Once you have it, re-read it fully before building (not just skim) and check the finished notebook against every top ("excellent") band line item as the final self-check step in SKILL.md describes.

## Team member placeholder

The title cell needs an explicit, unmissable placeholder for team member names - e.g. `**Team members:** [Team Member Names Here]` - since rubrics often penalize missing names even when everything else was correct. Never ask the user to supply the names before finishing the notebook; leave the placeholder and move on. This is different from a solo practice notebook, which has no team and needs no placeholder at all.

## No AI-disclosure content inside the notebook

AI-use disclosure belongs to the user. They follow their course or employer policy and decide where the disclosure goes. Don't add a disclosure cell on your own, and don't leave one out on your own either. If nothing has been said about it for a graded submission, ask before delivering.

## The "restart and run all" rule is a hard grading gate here

A specific, common failure: a variable defined in one cell, then that cell gets edited or deleted later, but the notebook keeps running fine on your own screen because the variable is still sitting in the kernel's memory from before. It fails the instant a grader opens a fresh copy and runs top to bottom. The general execution guardrail in SKILL.md already covers this, but for a graded submission there is no partial credit for "it worked when I ran it" - a notebook that doesn't execute clean in a fresh kernel is graded as if no notebook was submitted at all for some criteria, since a broken notebook makes it impossible to verify anything else in it.

## Load from the submitted CSV, not a live pull

The final version must load data from a plain local filename that will sit alongside the notebook at submission time - never a live URL fetch, even if a URL fetch was used for convenience while exploring. This is both a rubric requirement and a practical one: a grader's environment may not have the same network access this build environment does.

## Match the professor's own notebook style

If style-reference materials exist in project knowledge (the professor's own walkthrough notebooks, session PDFs), skim them for vocabulary and depth before writing markdown - the goal is a notebook that reads like it belongs in this specific class, not a generic tutorial. Don't introduce a method or term the class hasn't covered unless project knowledge clearly confirms it has (see the note in `algorithm-ladders.md`).

## Build toward the video, even though this skill doesn't make the video

If the assignment's deliverables include a video walkthrough (check the actual assignment instructions - don't assume), the notebook's narrative should set up everything that video needs to cover, even though building the video itself isn't part of this skill's job: a clear, unambiguous final recommendation; the metric-selection reasoning explained in a way that translates to spoken explanation; code explained at the concept level as well as the line level; and the improvement reasoning (tuning, algorithm choice) stated plainly enough to summarize out loud in a sentence or two per step.
