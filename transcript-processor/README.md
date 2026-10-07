# transcript-processor

**Use it when** you have a raw transcript and want clean, structured notes you can trust.

## The problem

Voice memo and meeting transcripts are full of filler, false starts and misheard words. Asking for a cleanup usually got me a summary, which loses the examples and digressions I wanted to keep. Worse, gaps got filled in with things nobody said, and quotes ended up attributed to the wrong person.

## What it does

Three jobs: clean it, structure it by type, save it with a consistent file name.

It picks one of five modes and loads that mode's template from `references/`:

| Mode | For |
|---|---|
| Class / lecture | One person teaching |
| Interview | Q&A with one outside person |
| Team discussion | Peers making decisions |
| Mentoring session | An expert giving feedback on your work |
| Voice memo | You alone, or a casual conversation |

Cleaning is editing. Every meaningful sentence, example and counterexample stays.

## What it won't do

- Summarize when you asked it to process.
- Guess who said something. It writes `[Speaker unclear]` and lists the candidates at the end.
- Invent a word to fill a gap. It writes `[unclear: sounds like "X"]`.
- Let your slides or notes override what was said. The transcript wins, and it notes the difference.
- Add interpretation you didn't ask for.

It ends with a short checklist of anything that needs your input.

## Set it up for yourself

The templates in `references/` reflect how I use each kind of note. Edit the section headings to match how you use yours. File names follow `{Context}_{Type}_{Date}.md`.

## Limits

- Real names are kept by default. Ask for "Person 1, Person 2" if the notes are going somewhere shared.
- It fixes a misheard name only when a reference file or the context confirms it.
