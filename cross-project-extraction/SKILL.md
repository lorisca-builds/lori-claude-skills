---
name: cross-project-extraction
description: >
  Cross-project knowledge retrieval. Trigger on: "cross-project",
  "extract from [project]", "I need something from another project",
  "I think I built this before", "search this project for",
  "I brought this back", "does this answer my problem", or whenever
  the user moves a chat between projects to retrieve knowledge. Three
  modes: OUTBOUND, EXTRACT, INBOUND. Detect the mode from context and
  proceed. Never ask the user which mode they are in.
---

# Cross-Project Extraction

The user works across several Claude projects. Each project is its own
isolated knowledge base. Claude cannot see one project from inside
another. This skill manages planned travel between them: preparing
before leaving, searching on arrival, and making sense of the findings
on return.

**Three modes. Detect which one applies and run it without being asked.**

---

## THE TRAVEL METAPHOR (hold this always)

Each project is a city. The user is the traveler.
- **OUTBOUND** = packing before leaving home
- **EXTRACT** = searching the destination city
- **INBOUND** = returning home and unpacking

Every move between projects needs a **Handoff Block**: a copy-paste
object that carries context across the gap. Nothing lives in memory.
Everything travels in the block.

---

## MODE DETECTION

Read context. Route immediately. No asking.

| What's happening | Mode |
|-----------------|------|
| The user describes a current problem and suspects another project has what they need. They haven't moved yet. | **OUTBOUND** |
| The user has moved to a destination project. They paste a Search Brief or arrive fuzzy. | **EXTRACT** |
| The user is back home. They paste an Extract Block or describe what they found. | **INBOUND** |

If it is truly ambiguous, ask one question only:
> "Are you preparing to search, actively searching at the destination,
> or back home evaluating what you found?"

---

## PROJECT MAP (edit this for your own projects)

OUTBOUND uses this map to suggest a destination. Replace the examples
with your own projects and one line on what each one holds.

- **[Project A]** → [what lives there, e.g. personal working patterns and preferences]
- **[Project B]** → [e.g. coursework, frameworks, case structures, feedback]
- **[Project C]** → [e.g. writing voice, narrative structures, framing that worked]

If the map is still blank, ask the user which project they think has it.

---

## OUTBOUND MODE
*You're at home. Preparing to travel.*

**Step 1: Clarify the home problem**
If it is not already clear, ask at most 2 questions:
- What are you working on right now?
- What specific gap are you trying to fill?
- What would a useful answer look like: a framework, a workflow, a pattern, a decision?

If enough context exists, skip ahead.

**Step 2: Identify the destination**
Use the project map above. Name the most likely destination and confirm.
Don't make the user figure it out from scratch.

**Step 3: Produce the Search Brief Block**

```
╔══════════════════════════════════════════╗
║  SEARCH BRIEF - OUTBOUND                ║
╠══════════════════════════════════════════╣
║  Home project:     [project name]        ║
║  Destination:      [project name]        ║
║  Working on:       [1-sentence summary]  ║
╠══════════════════════════════════════════╣
║  WHAT I'M LOOKING FOR                   ║
║  [2-3 sentences. What shape would a     ║
║  useful answer take? Framework /        ║
║  workflow / pattern / decision?         ║
║  What makes it immediately usable?]     ║
╠══════════════════════════════════════════╣
║  SEARCH ANGLES                          ║
║  • [specific term or concept]           ║
║  • [related pattern or context]         ║
║  • [alternative framing]               ║
╠══════════════════════════════════════════╣
║  NOT LOOKING FOR                        ║
║  [What to ignore / false positives]     ║
╠══════════════════════════════════════════╣
║  STATUS: OUTBOUND - ready to travel     ║
╚══════════════════════════════════════════╝
```

**Step 4: Travel instruction**
> "Copy this block. Move this chat to **[destination project]**, or open
> a new chat there. Paste the block and say: 'cross-project-extraction'.
> Claude will detect EXTRACT mode and search from there."

---

## EXTRACT MODE
*You've arrived at the destination project.*

**Step 1: Read the brief (or build one)**
If a Search Brief Block is present, use it directly.
If the user arrives fuzzy, ask one question:
> "What's the problem you're trying to solve back home?
> What would a useful finding look like?"
Then build a working brief internally. Don't make the user write it.

**Step 2: Run the search**
Search the project's knowledge from 2 to 3 angles:
- **Specific**: the exact concept or term from the brief
- **Broader**: the related domain or pattern
- **Analogical**: what situation is this similar to?

**Step 3: Evaluate candidates**
For each result ask internally: does this address the gap? Is it the
right shape? Is it usable or only a fragment?
Surface the 1 or 2 most relevant only. Don't dump everything.

**Step 4: Produce the Extract Block**

If found:
```
╔══════════════════════════════════════════╗
║  EXTRACT BLOCK                          ║
╠══════════════════════════════════════════╣
║  Destination project:  [project name]   ║
║  Original brief:       [1-line summary] ║
╠══════════════════════════════════════════╣
║  WHAT I FOUND                           ║
║  [Synthesized summary. Not a quote      ║
║  dump - portable and usable.]           ║
╠══════════════════════════════════════════╣
║  WHY IT'S RELEVANT                      ║
║  [1-2 sentences connecting this to      ║
║  the original problem.]                 ║
╠══════════════════════════════════════════╣
║  SOURCE                                 ║
║  [File or document it came from]        ║
╠══════════════════════════════════════════╣
║  GAPS / CAVEATS                         ║
║  [What this doesn't answer.]            ║
╠══════════════════════════════════════════╣
║  STATUS: EXTRACT - ready to return      ║
╚══════════════════════════════════════════╝
```

If nothing found:
```
╔══════════════════════════════════════════╗
║  EXTRACT BLOCK - NO MATCH               ║
╠══════════════════════════════════════════╣
║  Searched:    [queries tried]           ║
║  Result:      Nothing relevant found    ║
╠══════════════════════════════════════════╣
║  SUGGESTED NEXT CHECKPOINT              ║
║  [Which other project might have this?] ║
╠══════════════════════════════════════════╣
║  STATUS: EXTRACT - no match, rerouting  ║
╚══════════════════════════════════════════╝
```

**Step 5: Query coaching note**
After surfacing results, add 2 sentences at most:
> *"I searched [query] first because [why]. Then [query 2] found it because
> [reason]. Next time, try [principle] when the concept has no fixed name."*
Skip this if the user is moving fast.

**Step 6: Travel instruction**
> "Copy this block. Move back to **[home project]**.
> Paste it and say: 'cross-project-extraction'.
> Claude will detect INBOUND mode and evaluate from there."

---

## INBOUND MODE
*You're back at home. Evaluating what you found.*

**Step 1: Restate the original problem**
One sentence before evaluating anything. This prevents drift after several trips.

**Step 2: Evaluate the extract**
- Does this directly address the gap?
- Is it usable right away or does it need adapting?
- What's missing?

**Step 3: Produce a Synthesis Note OR a Sharpened Brief**

If sufficient:
```
╔══════════════════════════════════════════╗
║  SYNTHESIS NOTE                         ║
╠══════════════════════════════════════════╣
║  Original problem:   [1-line]           ║
║  What was found:     [1-line]           ║
╠══════════════════════════════════════════╣
║  HOW TO USE THIS                        ║
║  [Concrete. Specific to current work.   ║
║  Not generic advice.]                   ║
╠══════════════════════════════════════════╣
║  WHAT THIS CHANGES                      ║
║  [How does this shift current work?]    ║
╠══════════════════════════════════════════╣
║  STATUS: INBOUND - synthesis complete   ║
╚══════════════════════════════════════════╝
```

If insufficient:
```
╔══════════════════════════════════════════╗
║  SHARPENED BRIEF - RETURN TRIP          ║
╠══════════════════════════════════════════╣
║  What was found:      [1-line]          ║
║  Why it's not enough: [1-2 sentences]  ║
╠══════════════════════════════════════════╣
║  WHAT I STILL NEED                      ║
║  [Narrower and sharper than original.]  ║
╠══════════════════════════════════════════╣
║  NEW SEARCH ANGLES                      ║
║  • [tighter query 1]                    ║
║  • [tighter query 2]                    ║
╠══════════════════════════════════════════╣
║  STATUS: INBOUND - needs another trip   ║
╚══════════════════════════════════════════╝
```

**Step 4: Travel instruction (if another trip is needed)**
> "Copy the Sharpened Brief. Move back to **[destination project]**.
> Paste it and say: 'cross-project-extraction'. Claude will run
> EXTRACT again with sharper angles."

---

## ANTI-PATTERNS TO CATCH

**Fuzzy arrival without a brief**
→ One clarifying question before searching. Never search blind.

**Over-extracting**
→ 1 or 2 results at most. The user will recognize what they need. Give
them something to recognize, not a wall to sort through.

**Drift on return**
→ Always restate the original problem in INBOUND Step 1.

**Infinite loops**
After 2 failed extracts from the same project:
> "This project may not have what you need. Try [other project]
> or reframe the problem itself?"
