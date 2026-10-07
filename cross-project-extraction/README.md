# cross-project-extraction

**Use it when** you solved something in one Claude project and need it in another.

## The problem

I work across several Claude projects. One holds notes on how I work, one holds my coursework, one holds my writing. What I figure out in one project stays locked there, because Claude can't see one project from inside another.

I tried a single master context file shared across projects. It was too broad. Most of the time I only needed one niche workflow, and loading everything to get it was wasteful.

So my workaround was manual. I'd move a chat into the other project and ask Claude to search the files there. It worked, but I'd arrive without a clear ask, pull back too much, and lose track of the original problem by the time I got home.

## The idea

Treat it as a trip with checkpoints. The way I described it while building: "I'm telling the driver that we're going to travel and stop at certain checkpoints and try to find it at every checkpoint."

Each project is a city. You pack before you leave, search when you arrive, and unpack when you get home. Since Claude has no memory across projects, a copy-paste block carries the context between stops.

## How it works

| Mode | Where you are | What Claude does | What you carry out |
|---|---|---|---|
| Outbound | Home project | Asks at most two questions and suggests the destination | Search Brief |
| Extract | Destination project | Searches from 2 or 3 angles and keeps the best 1 or 2 results | Extract Block |
| Inbound | Home project | Restates the original problem, then judges the findings | Synthesis Note, or a Sharpened Brief for another trip |

Claude works out which mode you're in from context. You never have to say.

A typical run:

1. At home, say "I think I built this before in another project."
2. Claude writes a Search Brief. Copy it.
3. Open the destination project, paste the brief, and say "cross-project-extraction."
4. Claude searches and writes an Extract Block. Copy it.
5. Go back home, paste it, and Claude tells you how to use what you found.

## Set it up for yourself

Open `SKILL.md` and fill in the **Project Map** section with your own projects and one line on what each one holds. Claude uses it to suggest where to look. If you leave it blank, Claude will ask you instead.

## Design choices

- **A copy-paste block instead of memory.** It is the only thing that survives the move between projects. It also forces the ask to be written down before you leave.
- **One file with three sections.** An earlier version split the modes into separate skill files. That added moving parts and nothing else, so it went back to one file.
- **A separate skill from session management.** Managing a long session and moving knowledge between projects are different problems.
- **One or two results, never a dump.** You'll recognize the right thing when you see it. A wall of results makes that harder.
- **A short note on why the search worked.** After each find, Claude says in two sentences which query hit and why. I wanted to get better at querying, not only get the answer.

## What it won't do

- Search before it knows what you're looking for.
- Keep sending you back to the same project. After two misses it suggests another project or a reframe.
- Let the original problem drift. Inbound always restates it first.

## Limits

- The copy-paste is manual. This is a protocol for working within Claude's project isolation. It does not remove it.
- It can only find what is saved in the destination project's knowledge.
- The project map goes stale as your projects change. Update it when you add one.
