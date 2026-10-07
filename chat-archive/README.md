# chat-archive

**Use it when** you want to hand one Claude chat to another AI, tool or person without pasting the transcript.

Pairs with [project-archive](../project-archive/).

## The problem

Moving work out of a chat was all friction. I'd copy-paste the conversation and re-upload the files, and whoever picked it up had to dig through 80 turns to find the three decisions that mattered.

I described it as being a client who hires a second vendor. The new vendor needs a handoff folder to get up to speed.

A raw transcript buries the reader. A short summary loses how I think and how I steered the work, which is the part I most want carried over. My instruction when we built it: "not capturing the entire raw chat ... But also, don't make it too short."

## What it does

It writes one curated Notion page per chat, under a top-level page called "Claude Project Archive."

The record keeps the goal, the decisions with their reasons, your own directions quoted word for word, the final outputs and the files. It drops the back-and-forth.

Every record has to pass two tests before it's saved:

1. Could a new AI continue this work without asking you to repeat anything?
2. Could it predict how you'd react to its first draft?

## Set it up for yourself

- Connect Notion to Claude.
- To attach PDFs, Word files and decks directly, allow `api.notion.com` in Claude's network settings. Without it, the skill falls back to Google Drive links for small files and lists the rest.
- The first run creates the "Claude Project Archive" page as a private top-level page. Move it wherever you like.

## Design choices

- **Quotes over summaries.** "She wanted it simpler" loses what "Do not build yet. Ask me clarifying questions" keeps.
- **Who decided what.** A suggestion from Claude that you never accepted is not recorded as a decision.
- **A database per project.** Records can be sorted and filtered, and both archive skills share one format.
- **Notion only.** It doesn't write to Claude's memory.

## Limits

- Claude can't look up the link of the chat it's in. Paste it if you want it on the record.
- `claude.ai/share/` links can't be read. The skill searches for the chat by topic and tells you which one it used.
- Files made by scripts in an old chat can't be recovered. They're listed as such.
- It relies on Claude's past-chat search and Notion tools, so it works in the Claude app and not in every environment.
