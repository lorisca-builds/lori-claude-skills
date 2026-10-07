# Interview Mode

For Q&A with external parties - industry contacts, executives, customers, researchers, subject-matter experts.

Name files so the project, the interviewee and the date are all visible.

## Template

```markdown
# {Project / Context} - {Interviewee Name} Meeting Transcript
**Date:** {Date}
**Participants:** {Team members + role}, {Interviewee + title + organization}
**Format:** {Team-initiated Q&A / interviewee briefing / scheduled call / customer interview}
**Note:** {Transcription source - auto-transcribed and reconstructed / verbatim / partial}

---

## 1. {Topic of first question block}

**Team asked:** {What was asked, paraphrased clearly. If the team's framing matters, preserve it.}

**{Interviewee}'s response:**
- {Substantive point 1}
- {Substantive point 2}
- Direct quote: "{verbatim if preserved}"

**Implication for {project / decision}:** {Only if the interviewee explicitly drew the implication. Otherwise leave it for the user.}

---

## 2. {Next topic block}

...

---

## Direct quotes worth citing later

{Pull-quote section - verbatim quotes that are short, sharp, and citeable. Speaker attribution preserved.}

- "{Quote 1}" - {Interviewee}
- "{Quote 2}" - {Interviewee}

---

## Data points / facts mentioned

{Numbers, statistics, named companies, named products, dates. Things that can be fact-checked or cited.}

- {Fact 1} (mentioned by {speaker})
- {Fact 2} (mentioned by {speaker})

---

## Follow-up questions for next interview

{Things that came up that weren't fully answered, or that the user flagged in the call as "we should ask more about this."}

---

## Attribution questions

{Unclear speaker moments. Mostly only relevant if the interview had multiple team members talking and the auto-transcription mixed them up.}
```

## Mode-specific rules

- **Preserve direct quotes wherever they're clear.** Interview quotes are the primary citable artifact. If the auto-transcription preserved the wording cleanly, keep the quote intact in quotation marks.
- **No conclusions beyond what was stated.** If the interviewee said "I imagine a caregiver doesn't need equipment," that's their reaction, not a strategic conclusion. Don't escalate it into a recommendation.
- **Separate team's framing from interviewee's response.** The team's question is paraphrased; the interviewee's response is preserved as faithfully as possible.
- **Track when the interviewee changed their mind.** If they said one thing early ("seems small") and reversed after new info ("I actually like that line of thinking"), capture both - the reversal is the data point.
- **Pull a "Data points / facts" section.** Interviewees drop numbers, company names, product details that get cited downstream. Make them easy to find.
- **Attribution gets harder with multiple team members.** Apple Voice Memo often mixes up which team member asked what. If the team-side attribution is unclear, mark it `[Team member unclear]` - the interviewee's response is what matters; who on the team asked the question often isn't critical.
- **Reference files are common in this mode.** Interviewees often refer to companies, products, websites, prior conversations. If reference files are attached (company webpages, prior interview notes), use them to disambiguate names and concepts. If a name is mentioned that's not in the reference files, flag for confirmation.

## Naming

`{Project}_{Interviewee_Lastname}_Interview_{Date}.md`

Examples:
- `ClientX_JaneDoe_Interview_Apr16.md`
- `MT_Bank_Jordan_Interview_Apr16.md`
- `Sourcing_SupplierContact_Interview_May03.md`

Date format matches the user's existing files (`Apr16`, `Apr21`).
