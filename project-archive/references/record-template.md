# Chat Record Template

This is the page format for one archived chat. Both chat-archive and
project-archive use it. The reader is usually another AI (or a person)
picking up the user's work cold. It has never seen the chat and cannot ask
Claude what happened.

## The test

Before writing, and again after, ask:

1. Could a new AI continue this work without asking the user to repeat
   anything they already said in the chat?
2. Could it predict how the user would react to its first draft, because it
   has seen how they steered, what they rejected, and why?

If either answer is no, something important is missing. Add it.
If a section is padding that fails both tests, cut it.

## Length

Scale with the chat, not to a fixed number.

- Short chat (under ~10 turns): roughly 300 to 700 words
- Medium (10 to 40 turns): roughly 700 to 1,800 words
- Long (40+ turns): roughly 1,500 to 3,000 words, plus attached files

Final outputs quoted in full (section 5) do not count toward this.

## What to keep and what to cut

Keep:
- The user's words when they set direction, reject something, correct
  Claude, adds a constraint, or explains why. Quote these exactly.
- Every decision with its reason, and what was rejected on the way.
- Numbers, names, dates, links, file names, tool names.
- The final version of anything the next reader needs to continue.
- Things Claude flagged as uncertain or unverified.

Cut:
- Greetings, thanks, Claude restating what the user said.
- Tool mechanics (searches, retries, failed calls), unless the failure
  itself shaped a decision. Then one line.
- Drafts that a later version replaced. Keep only the final.
- Long Claude explanations the user did not engage with.
- Loops that ended where they started. Summarize in one line.

## Accuracy rules

- Attribute correctly. A Claude suggestion the user did not accept is not a
  decision. Mark each decision as one of: The user decided / Claude proposed,
  the user accepted / Claude proposed, still open.
- Never invent a reason. If the chat does not say why, write "reason not
  stated".
- Anything that is Claude's interpretation rather than something said
  gets labeled "Claude's read:".
- Describe how the user worked in this chat through what they did and said.
  No personality labels, no diagnoses, no psychology.
- Plain language. No em dashes. No hype words.
- Put every file name, domain, and path in backticks (`record-template.md`,
  `api.notion.com`). Notion turns bare names ending in .md, .ai, .com and
  similar into fake web links.
- Dates: only write dates you can see. If the chat's start date is not
  visible, give the last-activity date alone.

---

## Database properties

| Property | What goes in it |
|---|---|
| Name | 5 to 9 words naming what the chat produced or decided. Not "Chat about X". Example: "Spec for two Notion chat-export skills" |
| Date | Date of the chat's last activity |
| Status | Active (work continues) / Done / Parked |
| Tags | 2 to 4 short topic tags |
| Chat Link | The claude.ai/chat/... URL, or empty if unknown |
| Summary | One sentence: what happened and where it landed |

## Page body

Copy this structure. Section headings stay the same across every record
so a reader can jump straight to what they need.

```
> For the AI reading this: this is a curated handoff of one Claude chat,
> not a transcript. Start with the Handoff brief. Section 3 quotes the user's
> exact words. If something is missing, the original chat is linked at
> the bottom.

## 1. Handoff brief
**Goal:** what the user wanted and why they wanted it.
**Where it stands:** what is finished, what is mid-way.
**Next:** next steps the user stated or agreed to. "None stated" if none.

## 2. Decisions and why
- **[Decision]** | [reason] | rejected: [alternative, if any] | [who: The user decided / Claude proposed, the user accepted / still open]

## 3. How the user directed this work
- "[their exact words]" → [what it changed]
(4 to 10 items: constraints, corrections, pushback, rejections,
reframes, format or tone rules)

**Pattern in this chat:** 1 to 3 sentences on observable behavior.
Example: "Narrowed scope twice, both times toward simpler. Asked for
tests before trusting any claimed capability."

## 4. How the thinking moved
1. [What was on the table] → [what shifted it] → [where it landed]
(3 to 8 turning points, in order)

## 5. Key outputs
Final versions, in full, of anything needed to continue: the spec, the
prompt, the copy, the numbers. If one output runs past ~800 words,
attach it as a file and give a 3 to 5 line summary here instead.

## 6. Files and artifacts
| File | What it is | Where |
|---|---|---|
| name | one line | attached / Drive link / artifact link / not recoverable, see chat |

## 7. Open threads and unknowns
Unresolved questions, assumptions made, things flagged as unsure.

## 8. Left out of this record
1 to 2 lines on what was cut, so the reader knows where the gaps are.

<details>
<summary>Source</summary>
Chat link, project name, chat date, date exported, rough turn count.
</details>
```

Use Notion-flavored Markdown. If unsure of syntax for toggles, tables,
or file blocks, fetch `notion://docs/enhanced-markdown-spec` with the
Notion fetch tool before writing.

## Short example of sections 2 and 3 done well

```
## 2. Decisions and why
- **Drop the full transcript** | a receiving AI gets lost in raw chat
  and wastes its context | rejected: brief plus collapsed transcript |
  the user decided
- **Database inside each project page** | sortable and filterable,
  and skill 1 and skill 2 share one format | rejected: nested pages |
  Claude proposed, the user accepted

## 3. How the user directed this work
- "Do not build yet. Ask me clarifying questions" → scoping came
  before any file was written
- "not capturing the entire raw chat ... But Also, don't make it too
  short" → replaced the transcript with this curated format
- "I don't understand this question" → Claude re-asked in plain terms;
  they answered with how they already save excerpts (on demand)

**Pattern in this chat:** Set the goal through an analogy (client
hiring a second vendor), then let Claude propose structure and
corrected it at one key point.
```
