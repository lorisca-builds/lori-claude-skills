# project-archive

**Use it when** you want a whole Claude project documented or handed off.

Pairs with [chat-archive](../chat-archive/), and uses the same record format.

## The problem

Finished projects pile up as dozens of chats with no index. The project brief, the decisions and the final files are spread across all of them. Handing that to another AI or a teammate meant explaining it from memory.

## What it does

It builds a Notion wiki for the project: a project page with a brief on top and a database of curated records, one per chat.

1. Lists the project's chats and asks which to include. That is the only question it asks.
2. Archives them in small batches, oldest first, so later records don't get thin as context fills up.
3. Attaches project files and links published artifacts.
4. Writes the project brief last: what the project was, final deliverables, key decisions, how you directed the work (each pattern backed by a quote), and open threads.

A reader starts with the brief and opens only the chat records they need. Running it again adds new chats and revises the brief.

## Set it up for yourself

Same as chat-archive: connect Notion, and allow `api.notion.com` in Claude's network settings if you want binary files attached directly.

## What it won't do

- Archive a project other than the one it's running in. Claude's chat tools only see the current project.
- Archive every chat without asking. Dead ends stay out.
- Analyze the work for a portfolio or an assignment. It documents. Analysis is a separate job that can use the wiki as input.

## Limits

- Large projects take several turns. It reports progress after each batch and waits for you to say continue.
- Past about 100 chats the list may be incomplete. It says so and offers to search by topic.
