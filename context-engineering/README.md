# context-engineering

**Use it when** one project runs across many chat threads and you keep losing track of what was decided.

## The problem

On long projects I worked in one thread per deliverable. Three things kept happening. I'd open a new thread by pasting every file I had. Decisions made in one thread never reached the others. And threads reopened debates that were already settled.

## What it does

Three modes. Claude picks the one that fits.

**Opener** (starting a thread): names the work, tells you exactly which files to load and in what order, states what is locked and what is open, and sets a one-sentence objective. If you're about to paste five documents, it stops you and asks what the first question is.

**Checkpoint** (mid-session): six short parts you can read in 90 seconds. Objective, done, in progress, unresolved, next action, constraint check.

**Closer** (ending a session): the edits to make to your master context file, written ready to paste, plus what carries over to the next thread.

## Set it up for yourself

The skill assumes one master context file per project that acts as the single source of truth. Open `SKILL.md` and replace the placeholder file names in the Opener section with your own.

## Design choices

- **The closer writes paste-ready edits.** A summary nobody copies anywhere is how decisions get orphaned.
- **Locked items are named.** When a thread reopens one, Claude asks what new information justifies it.
- **One next action.** A list of next steps is a way to avoid choosing.

## Limits

- It manages sessions. It doesn't move knowledge between projects. For that, see [cross-project-extraction](../cross-project-extraction/).
- You still have to paste the closer's edits into the master file yourself.
