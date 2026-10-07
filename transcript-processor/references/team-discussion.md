# Team Discussion Mode

For peer-to-peer working sessions - team meetings, brainstorms, decision-making sessions, cross-team coordination.

Gold standard: `D1_Team_Discussion_Apr11.md`, `D2_Team_Discussion_Apr12.md`, `D3_Team_Discussion_Apr15.md`, `BK_CrossTeam_Session_Apr21.md`.

## Template

```markdown
# {Project} - {Team or Group} {Session Label} Working Session
**Date:** {Date}
**Duration:** {Approximate duration if known}
**Participants:** {Names in order they appear, with backgrounds in parens if relevant}
**Purpose:** {What this meeting was for - define {deliverable}, brainstorm {topic}, decide {question}}

---

## 1. {First topic discussed}

### Starting point
{Where the discussion began. What was already agreed coming in.}

### {Sub-topic / decision branch}
{Cleaned narrative. Multiple voices integrated.}

**Critical distinction {Name} raised:** {When someone clarifies something that changes the framing, preserve it with attribution.}

### {Comparison table when applicable}

| Option | Status | Reason |
|---|---|---|
| Option A | Eliminated | {Why} |
| Option B | Selected | {Why} |
| Option C | Deferred | {What needs to be answered first} |

---

## 2. {Next topic}

...

---

## Decisions locked

{Things the team committed to in the session.}

- {Decision 1}
- {Decision 2}

---

## Decisions deferred

{Things discussed but not resolved. Note what needs to happen to resolve them.}

- {Open decision 1} - needs: {what's missing}
- {Open decision 2} - needs: {what's missing}

---

## Action items

| Owner | Action | Deadline |
|---|---|---|
| {Name} | {Task} | {Date or "before next session"} |

---

## Tensions surfaced

{Disagreements that didn't resolve, philosophical splits, points where the team is not aligned but moved on anyway. Important to capture - these come back.}

---

## Attribution questions

{Unclear speaker moments. Common in team discussions with similar voices on auto-transcription.}
```

## Mode-specific rules

- **Capture decisions, not just discussion.** A team discussion is a decision-making artifact. The most important output is "what did we decide" - make it findable.
- **Distinguish locked vs. deferred.** A decision that everyone nodded along to but no one committed to is not locked. Use language like "the team gravitated toward X but did not formally lock it."
- **Action items need owners and timing.** "Someone should look into this" is not an action item. If ownership and timing weren't named, flag it in "Decisions deferred" instead.
- **Tensions are signal, not noise.** When two team members disagreed and one yielded, capture both views. The dissenter's logic often comes back later. Don't smooth disagreements into consensus.
- **Comparison tables for elimination.** When the team weighs options and rules some out, use a table. The "reason eliminated" column is what saves time later when someone asks "why didn't we do X?"
- **Background context preserved.** If someone's background matters to why their view carried weight (Khaled's banking expertise, Emma's influencer network), preserve the context the first time they're mentioned.
- **Attribution will get fuzzy.** Team discussions with 5-6 voices on Apple Voice Memo will produce attribution errors. Flag `[Speaker unclear]` and list candidates. Don't guess to keep flow.

## Naming

`{Project}_{Session_Label}_Team_Discussion_{Date}.md`

Or for cross-team: `{Project}_CrossTeam_{Date}.md`

Examples:
- `D1_Team_Discussion_Apr11.md`
- `D3_Team_Discussion_Apr15.md`
- `Strategy_A2_Team_Discussion_Apr7.md`
- `BK_CrossTeam_Session_Apr21.md`
