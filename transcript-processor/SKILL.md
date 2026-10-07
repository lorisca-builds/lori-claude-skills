---
name: transcript-processor
description: Universal transcript processor - turns raw transcripts (Apple Voice Memo, Otter, Zoom, pasted text) into clean structured session notes. Trigger when (1) the user pastes raw conversational text with filler words ("um", "like", "you know"), false starts, run-ons, or mistranscriptions; (2) they say "process this transcript", "clean this up", "process this voice memo", "session notes from this", "transcribe"; (3) they upload a transcript file (.txt, .vtt, .srt, .md); (4) they paste a transcript and mention a reference file (slides, notes, website) to process it against. Five modes - class-lecture, interview, team-discussion, mentoring-session, voice-memo - each loads its template from references/ before drafting. Trigger eagerly. Better to fire and confirm the mode than miss a transcript.
---

# Transcript Processor

A universal transcript skill. Three jobs: clean it, structure it by mode, save it to a file with consistent naming.

## When this fires

Any of:
- Raw transcript pasted (conversational text with fillers, false starts, mistranscriptions)
- Explicit phrasing: "process this transcript", "clean this up", "session notes", "process the voice memo"
- Transcript file uploaded
- Transcript + reference file mentioned together

If pasted text is over ~200 words and has the markers of speech (filler words, run-on sentences, "uh", "like", "you know", false starts), assume it's a transcript and fire. Don't wait for the explicit word "transcript."

## Mode detection

Five modes. Pick one before drafting. Load the matching reference file.

| Mode | Trigger signals | Reference |
|---|---|---|
| **Class / lecture** | Professor named, "session X", "class Y", course code, lecture-style monologue | `references/class-lecture.md` |
| **Interview** | "Interview with X", external party named (industry contact, executive, customer), Q&A pattern, single interviewee | `references/interview.md` |
| **Team discussion** | Multiple peers named, "team meeting", "team discussion", decisions being made, action items implied | `references/team-discussion.md` |
| **Mentoring session** | Faculty feedback context, "professor said", "mentoring session", "feedback meeting", one expert reviewing student work | `references/mentoring-session.md` |
| **Voice memo** | Single speaker (the user alone), casual conversation with one other person, brain dump | `references/voice-memo.md` |

**If ambiguous:** ask one question with the two most likely modes. Don't guess.

**If a reference file is mentioned** (slides, prior notes, website, project file): note it explicitly. Use it for disambiguation, terminology, context. Do not let it override the transcript - what was *said* is the primary source.

## Universal rules - apply across all modes

### Cleaning
- Remove: "um", "uh", "like" (as filler), "you know", "I mean" (as filler), false starts ("I think - I mean -"), repeated words from stuttering
- Keep: every meaningful sentence, every example, every counterexample, every digression that contains substance
- Cleaning is editorial, not summarization. The goal is the same content, readable.
- If a phrase reads naturally with "like" or "you know" preserved (rhetorical, not filler), keep it.

### Mistranscriptions (Apple Voice Memo / auto-transcription errors)
- Fix obvious typos from context: a garbled name becomes the speaker's real name if the slides or project files confirm it. "Bossage" → "Postage" if context is operations.
- Use reference files (slides, prior project context) to disambiguate names, companies, technical terms.
- Never invent words to fill gaps. If a word is unclear and context doesn't resolve it, mark it: `[unclear: sounds like "X"]` and flag at the end.

### Speaker attribution
- **Never guess.** If unclear who said what, mark `[Speaker unclear]` and list candidates at the end of the file under "Attribution questions."
- For voice memos / solo recordings, attribution is implicit (the user). No tagging needed unless someone else is in the recording.
- For interviews and team discussions, attribution is structural - get it right or flag it.

### Anonymization
- Default: real names. (These files stay in the user's own workspace.)
- Switch to Person 1-5 only if: (a) the user asks, (b) the output is clearly headed for a reflective diary or peer review, (c) the user names this in the request.

### Fabrication rule
- If something wasn't said, it doesn't go in the notes.
- No "implied meaning," no "the speaker probably meant," no filling in for clarity. If clarity requires inference, mark it: `[inferred from context]` or add a separate "Open questions" section.

## Output

### File naming
Auto-name using `{Context}_{Type}_{Date}.md`. Examples:
- `Fintech_Class2_Session_Notes.md`
- `ClientX_JaneDoe_Interview_Apr16.md`
- `D2_Team_Discussion_Apr12.md`
- `Voice_Memo_May11.md`

If context isn't obvious from the transcript or the conversation, default-name and ask the user to correct.

Save to `/mnt/user-data/outputs/`. Use `present_files` after saving.

### Structure
Load and apply the matching reference file's template. Don't improvise on structure - the templates exist because they map to how the user uses the files downstream.

### Length and tone
- Plain English. No academic framing.
- Preserve voice - if a professor uses a specific phrase ("TechFin not FinTech"), keep it as a quote.
- Direct quotes get quotation marks. Paraphrases don't.
- Tables only when comparing options or tracking decisions. Not for narrative content.

## Process

1. **Identify mode.** Check signals. If ambiguous, ask once.
2. **Note reference files.** If any are attached or mentioned, list them explicitly before processing. Confirm whether to cross-reference now or after the clean.
3. **Load the matching reference file** from `references/`.
4. **Process the transcript** following the template and universal rules.
5. **Save and present** the file. Auto-name; the user corrects if wrong.
6. **End with a short checklist** if anything needs the user's input:
   - Attribution questions (who said X?)
   - Unclear words/phrases
   - Decisions that seemed to be made but weren't confirmed
   - Anything you marked `[inferred]` or `[unclear]`

## What this skill never does

- Never summarizes when asked to process. Cleaning and structuring is the job. Summarization is a separate request.
- Never adds analysis or interpretation unless the user asks. The output is a record, not a take.
- Never silently merges what was said with what's in reference files. If the transcript says something the slides don't, the transcript wins. Note the gap if useful.
- Never auto-chains into another skill. Suggest, wait, proceed.
- Never invents speaker names. `[Speaker unclear]` is always a valid output.
