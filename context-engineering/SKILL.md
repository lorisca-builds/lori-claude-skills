---
name: context-engineering
description: >
  A session architecture skill for long, multi-thread projects. Three modes: opener,
  checkpoint, closer. Trigger when (1) the user starts a new thread or deliverable:
  "starting D3", "new thread for X", "help me set up this session", "what do I need to
  load"; (2) the user runs a checkpoint: "context engineering checkpoint", "where are we",
  "what have we been doing", "what's next", "catch me up", "status check"; (3) the user
  ends a session: "session close", "let's wrap up", "what do I save", "update the master
  context"; (4) the user pastes several "read this / read that" instructions at the start
  of a message. Intercept before they front-load everything. Identify which mode applies
  and run it. Do not wait to be asked.
---

# Context Engineering

The user works across multiple threads - one per deliverable, one master per project. This skill
manages the architecture of those sessions: what to load at the start, how to track progress
mid-session, and what to save at the end.

Three modes. Identify which applies. Run it.

---

## MODE 1 - OPENER

**Triggers:** Starting a new thread, new deliverable, new working session.
Phrases: "starting D3", "new thread", "let's work on X", "help me set up", "what do I need to load"

**What to do:**

1. **Identify the work** - What deliverable or topic is this thread for? What's the deadline?

2. **Tell the user exactly what to load** - Based on the work, specify which project files Claude
   needs to read at the start of the thread. Be explicit. Don't say "load relevant files" -
   say "read these three files in this order."

   Standard load for a deliverable thread (edit these to match your own files):
   - `[Project]_Master_Context.md` - always first
   - `[Project]_Feedback.md` - always second, if you keep one
   - The most recent team discussion or session notes file
   - The brief for this deliverable

3. **State what's locked vs. open** - What decisions have already been made that should NOT
   be re-debated in this thread? What is still genuinely open?

4. **Name the objective** - One sentence. What does "done" look like for this thread?

5. **Flag front-loading risk** - If the user is about to paste 5 documents at once, intercept:
   "Before you load everything - what's the first question you actually need answered?
   Let's load only what's needed for that."

---

## MODE 2 - CHECKPOINT

**Triggers:** Mid-session status check.
Phrases: "context engineering checkpoint", "where are we", "what have we done", "status check",
"catch me up", "what's the objective", "what's next"

**What to produce - in this order, no more:**

**Objective:** One sentence. What is this thread trying to accomplish?

**Done:** What has been completed or decided in this session. Locked items only - things
that should not be re-opened.

**In progress:** What is actively being worked on right now.

**Unresolved:** Specific open questions or tensions that need to be resolved before the
thread can close. Name each one explicitly. If a tension has appeared more than once
without resolution, flag it: "This has been open since [when]. It needs a call."

**Next action:** One concrete next step. Not a list. The single thing that, if done,
moves the work forward most.

**Constraint check:** Is anything blocking progress that hasn't been named yet?
(missing data, team decision needed, file not yet read, etc.)

Keep the checkpoint tight. It should be readable in 90 seconds.

---

## MODE 3 - CLOSER

**Triggers:** End of session, wrapping up.
Phrases: "session close", "let's wrap up", "what do I save", "update master context",
"closing this thread"

**What to produce:**

1. **Session summary** - 3-5 bullets. What happened in this session that materially
   changed the project state? Not process notes - decisions, pivots, new insights only.

2. **Master context updates** - Exactly what needs to change in the master context file.
   Format as ready-to-paste edits:
   - "Add to Decisions Made: [exact text]"
   - "Update Working Thesis to: [exact text]"
   - "Add to Thread Log: [thread name] | [topic] | [key output]"
   - "Update Deliverable Tracker: D[X] status → [new status]"

3. **Unresolved items** - What did NOT get resolved and needs to carry into the next thread
   or session? These become the opener agenda for next time.

4. **Handoff note** - One sentence: "Next session should start by [specific action]."

Do not produce a long summary. The master context file is the permanent record.
The closer output is the bridge to get there.

---

## ARCHITECTURE REFERENCE

**the user's project structure:**
```
Project (Claude.ai)
├── Master Context files (one per active project)
│   ├── ProjectA_Master_Context.md
│   └── ProjectB_Master_Context.md
├── Thread per deliverable (D1, D2, D3...)
├── Thread per topic (brainstorm, team discussions)
└── This master thread = strategy layer + skill building
```

**Rule:** Decisions made in deliverable threads must be written back to the master context
at session close. If they aren't, they get lost between threads.

**Rule:** The master context is the single source of truth. If it contradicts a thread,
trust the master context unless the thread explicitly marks something as a "decided pivot."

---

## ANTI-PATTERNS TO CATCH

**Front-loading:** The user pastes 4+ files/documents at once before stating what they need.
→ Intercept. Ask: "What's the first question?" Load only what's needed for that.

**Checkpoint drift:** A "context engineering checkpoint" turns into a long summary no one reads.
→ Keep it to the 6-part structure above. Cut anything that isn't objective/done/in-progress/
unresolved/next action/constraint.

**Orphaned decisions:** Good decisions get made in a thread but never written to master context.
→ Every closer must produce explicit master context update language, not just a summary.

**Re-opening locked items:** A thread starts re-debating something already decided.
→ Name it: "This was decided in [thread/date]. The decision was [X]. What's the new
information that would justify reopening it?"
