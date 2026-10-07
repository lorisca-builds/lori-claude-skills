---
name: "project-archive"
description: >
  Builds or updates a Notion wiki for a whole Claude project: one project
  page (titled with the project name) with a project brief on top and a
  database of curated handoff records, one per chat. Use it to document
  past projects such as school courses, capstones, or client work, or to
  hand a whole project to another AI or person. Trigger on "archive this
  project", "document this project", "build the wiki for this project",
  "export this project to Notion", "project handoff", or /project-archive.
  Must run from inside the project being archived. Documentation only: it
  does not analyze the work for portfolio or assignments. For a single chat,
  use chat-archive instead.
---

# Project Archive

This builds the shared folder for a whole engagement. The project page
is the cover memo. The Chats database is the file drawer. A receiving AI
reads the brief first, then opens only the chat records it needs.

## Step 1: Read the template

Read `references/record-template.md`. Every chat record in the wiki uses
it. It also defines the accuracy rules, which apply to the project brief
too.

## Step 2: Confirm the project

Take the project name from the system prompt ("This session is bound to
the claude.ai Project ..."). The chat tools only see chats in the current
project, so this skill cannot archive a different project from here. If
the session is not in a project, tell the user to open the project they want
and run it there.

## Step 3: Find or create the Notion structure

Load Notion tools with `tool_search` if needed.

1. Find "Claude Project Archive". Create it as a top-level page if
   missing.
2. Find the project page under it. If missing, create it with a
   "Project brief" section and an inline database "Chats": Name (title),
   Date (date), Status (select: Active, Done, Parked), Tags
   (multi-select), Chat Link (url), Summary (text). Load
   `notion-create-database` and follow its syntax. Place it inline on
   the project page if the tool allows. If it can only make a full-page
   database, mention it once at the end.
3. If the database exists, query it and collect the Chat Link values
   already archived.

## Step 4: List the chats and let the user choose

Call `recent_chats` with `n: 20`, paging with `before` set to the oldest
`updated_at` of each batch, up to 5 calls. Drop chats already in the
database, and drop the chat you are running in.

Show the user a numbered list: title, date, one-line gist from the summary.
Ask which to include ("all", or numbers). Some chats are dead ends or
off-topic and they should not have to wade through their records later.
This is the only question the skill asks.

If there are more than 100 chats, say the list may be incomplete and
offer to search by topic for the rest.

## Step 5: Gather project-level files

- **Project files** in `/mnt/project/`: The user's uploaded sources
  (assignment briefs, readings, drafts). Attach text files. Binary files
  follow the upload rules below. List everything in the project page's
  file table.
- **Published artifacts**: `Artifact` action "list". Only link ones
  that appear in the chats being archived. Note they are private until
  shared.

**Upload rules** (same as chat-archive):
1. Text files up to 200 KB: `notion-create-attachment` with `content`.
2. Binary: `notion-create-file-upload`, then curl POST to the returned
   `upload_url` with the returned headers and the file in the `file`
   field. This is the normal path. It needs `api.notion.com` allowed in the
   user's network settings (see the README).
3. If that fails with `host_not_allowed`: files under about 50 KB go to
   Google Drive with `create_file` (`base64Content`,
   `disableConversionToGoogleType: true`) and get linked. Larger files
   are listed as not attached, and the user is told once at the end.

## Step 6: Archive the chats in batches

Reading many full chats fills the working context fast, and records get
thinner as it fills. Work in batches of about 3 long chats or 5 short
ones per turn, oldest first so the story builds in order.

For each chat:
1. `read_conversation` from the start, paging with `next_page_token`
   until the end. The user asked for the whole project, so full reads are
   expected here.
2. Recover files: text files written with create_file show their full
   content in the tool inputs. Rebuild the final version and attach it.
   Files made by scripts (docx, pptx, pdf) are not recoverable: list
   them as "not recoverable, see chat".
3. Write the record with the template and create it in the Chats
   database. Chat Link comes from the chat's url.
4. Keep a 3 to 5 line note for yourself of each chat's goal, decisions,
   and the user's key directions. You will need these for the brief, and the
   full chat will not stay in view.

After each batch, report progress in one line ("Archived 4 of 11. Say
continue for the next batch.") and stop. Continue when the user says so.

## Step 7: Write the project brief

After the last batch, write the brief at the top of the project page,
above the database. Use the batch notes plus the records. Structure:

```
> For the AI reading this: start here. Each row in Chats below is a
> curated handoff of one chat. Open only the ones you need.

## Project brief
**What this project was:** course, client, or goal, and the time span.
**Final deliverables:** what was produced, with links.
**Key decisions across the project:** decision | reason | which chat.
**How the user directed this project:** 4 to 8 patterns seen across chats,
each backed by one short quote and the chat it came from.
**Open threads:** unfinished work and unresolved questions.

## Files
| File | What it is | Where |

## Chats
(the database)
```

The same accuracy rules apply. Patterns in how the user worked must be
backed by quotes, not labels.

**On re-runs:** add only new chats, then revise the brief to fold them
in. Replace the brief, do not append a second one.

## Step 8: Confirm

> 🗄️ **[Project]** archived: [N] chats, [M] files. [link]

Add one line for anything not attached or any chat left out. Nothing
else.

## Anti-patterns

- **Doing portfolio or assignment analysis.** That is a separate job
  that uses this wiki as input.
- **Archiving every chat without asking.** The user picks.
- **Reading all chats before writing any record.** Batch, or the late
  records get thin.
- **A brief that just stacks the chat summaries.** The brief is about
  the project as a whole: its arc, its outputs, and how the user steered.
- **Writing to memory.** Notion only.
