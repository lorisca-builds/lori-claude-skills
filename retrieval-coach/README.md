# retrieval-coach

**Use it when** you're in the right project and your search words keep missing.

## The problem

I'd know which project had the thing. I couldn't put it into words. I think in patterns first and the words come later, so what I typed was too vague to find anything. The gap was in translating the idea into a search term. The note itself was always there.

Asking Claude to "search for that thing about..." didn't help. It searched on my vague words and came back with the wrong note, or nothing.

I also didn't want a shortcut that did the finding for me every time. As I put it when I built this: "querying logic is a muscle I want to train, not just a shortcut."

## The idea

Talk first, search second. Claude asks one question to get a better handle on the thing, offers a few different angles on it, and only then searches. Afterward it shows how the vague description mapped to the keyword that worked, so the next search starts sharper.

## How it works

**Translation mode.** You know the thing exists and can't name it.

1. Claude asks one anchoring question from a new angle, such as "What problem were you solving when you first thought about this?"
2. It offers 2 or 3 keyword angles. These are different cuts of the idea, never synonyms.
3. It searches with the strongest one.
4. It debriefs.

**Discovery mode.** You're thinking out loud and something might surface.

- *Following:* while you're flowing, Claude tracks and waits for the "wait, actually..." moment, then names it and searches.
- *Sparking:* when you're circling, Claude asks one question from an unexpected side, such as "What's it definitely not about?"

**Coaching layer.** After every find, Claude shows the path from your description to the keyword. By default this is two or three sentences. When you're moving fast it is one. Say "fast" or "teach me" to switch.

## Example

> **You:** I know I have something on why I stall on big tasks.
>
> **Claude:** What were you trying to fix when you first wrote about it?
>
> **You:** I kept reorganizing my notes when I should have been writing.
>
> **Claude:** Three angles: "task initiation" (the mechanism), "avoidance" (the behavior), or "reorganizing" (your own word). Which is closest?
>
> **You:** Avoidance.
>
> **Claude:** Found it: your note "Avoidance loops." The mapping was "stall on big tasks" → "avoidance," because you'd named the behavior and not the feeling.

## Design choices

- **One question at a time.** More than one and the conversation becomes a form.
- **Angles, not synonyms.** Rephrasing the same vague words finds the same nothing. A different cut of the idea is what unlocks it.
- **Sparking lives inside Discovery.** I first thought it needed its own mode. It turned out to be the same goal with Claude taking a more active role, so it became a second gear.
- **The debrief is always there, and its length adapts.** Skipping it would turn this back into a shortcut.
- **Narrow scope to start.** It was built for searching project knowledge. The same moves work for SQL and research, and the skill says so, but project search is what it was tested on.

## What it won't do

- Search on the first keyword you give without checking it's the right one.
- Ask you to "describe it more."
- Spark while you're still flowing.

## Limits

- It can only find what is saved in the project you're in. For another project, use [cross-project-extraction](../cross-project-extraction/).
- Mode detection is Claude's read of the conversation. If it guesses wrong, tell it.
