---
name: linkedin-connection-note
description: Draft LinkedIn connection request notes for the user in their voice, with a hard 300-character limit verified by an actual count. Use whenever they ask for a connection request, connect note, LinkedIn outreach note, or a message to send with a connection invite, even if they do not say "300 characters". Connection-first, never pitch-first.
---

# LinkedIn Connection Note

## Purpose

Draft connection-request notes for the user. Every note must fit LinkedIn's 300-character limit, checked with a real count before delivery. A note that reads well but counts 301 gets cut.

This skill covers the connection request only. Follow-up messages after someone accepts, emails, and recruiter outreach are out of scope for this skill.

## Workflow

1. Get the recipient's name, current title and company, and the context (a job they applied to, a talk, an event, a mutual). Verify these against the user's own contact tracker, the thread, or a tool result. Never guess a name, title or company. If no verifiable contact exists, say so plainly instead of drafting to a placeholder.
2. Pick one angle per recipient:
   - Org-owner angle (hiring manager or leader)
   - Peer-ops angle (same function)
   - Local or colleague angle (same city, first-team-member story)
3. Draft the note: one genuine hook and one small, low-friction ask. The hook is the real shared thing (a motto, a talk, a mutual, a specific observed need). It is never their track record.
4. Count characters with a tool, for example `python3 -c "v='''note'''; print(len(v))"`. Trim until the count is 300 or less. Em dashes and apostrophes count as one character each.
5. Deliver each note in its own code block so they can copy it. State the verified count under each one.

## Voice

- Fun prospective teammate, character-first, research shown implicitly.
- Never a pitch about a past job. Frame what they build and own, if anything.
- Plain phrasing. No corporate flattery, no "I hope this message finds you well."

## Rules

1. The 300-character cap is non-negotiable.
2. Connection-first, never pitch-first. No metric proof points in a cold note, such as SLA cuts or volume stats. They read desperate and pitchy. The note opens the door. Proof points and any coffee-chat ask belong in the follow-up after acceptance, and only if they ask for one.
3. One hook plus one small ask per note. Nothing more fits.
4. They send everything themselves. Never send or connect on their behalf. LinkedIn stays read-only unless they authorize a specific action.
5. If the user keeps an outreach log, add an entry only after they confirm an actual send, and only with their approval. A drafted note is not a sent note.
