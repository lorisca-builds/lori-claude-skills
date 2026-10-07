---
name: chat-archive
description: >
  Archives one Claude chat to Notion as a curated handoff record, so the user can
  hand the work to another AI, tool, or person without copy-pasting the chat
  or re-uploading files. Trigger on "archive this chat", "export this chat",
  "save this thread to Notion", "send this chat to Notion", "hand this off",
  "make a handoff page", "I want another agent to pick this up", or
  /chat-archive. Also trigger when the user points at an older chat ("archive
  the chat where we built X"). The record keeps goal, decisions and reasons,
  their own directions quoted, the final outputs, and the files, and drops
  the raw back-and-forth. For a whole project, use project-archive instead.
---

# Chat Archive

The user is a client handing a project to a second vendor. This skill writes
the handoff folder: one Notion page per chat, inside their Claude Project
Archive, that another AI can read cold and keep working from.

The record is curated, not a transcript. A receiving AI buried in 80 raw
turns loses the thread and burns its context. But a thin summary loses
how the user thinks, which is the part they care most about keeping. The
format in `references/record-template.md` sits between the two.

## Step 1: Read the template

Read `references/record-template.md` before anything else. It defines the
page structure, the length targets, what to keep and cut, and the
accuracy rules. Everything below assumes it.

## Step 2: Identify the chat and its context

**Which chat.** Default is the chat you are in right now. You already
have it in context. If the user names an older chat, find it with
`conversation_search` (or `recent_chats` for a time reference), then read
it with `read_conversation`. For an explicit archive request, read the
whole chat: keep paging with `next_page_token` until it ends.

When reading an old chat, know what comes through: The user's messages, your
replies, and the inputs you sent to tools (including the full text of
files you wrote with create_file). Tool results and the user's uploaded
attachments do not come through.

**Project name.** Take it from the system prompt ("This session is bound
to the claude.ai Project ..."). If the chat is not in a project, use
"General".

**Chat link.** You cannot look up the link of the chat you are in. Use a
claude.ai/chat/ link if the user pasted one. The ID after /chat/ can go
straight into `read_conversation`. A claude.ai/share/ link cannot be read
(it returns an empty page): find the chat with `conversation_search` on
its topic instead, record the /chat/ link from the result, and say which
chat you used in the confirmation. For older chats, the search
results include the link. Otherwise leave Chat Link empty and mention it
in the confirmation.

## Step 3: Gather the files

Build the list for section 6 of the record. Handle each kind like this:

| Kind | Where to look | How it gets into Notion |
|---|---|---|
| Files you made in this chat | `/mnt/user-data/outputs/` | see upload rules below |
| Published artifacts | links in the chat, or `Artifact` action "list" | link only |
| the user's uploads | `/mnt/user-data/uploads/`, `/mnt/project/` | list them. Attach text files. Binary: follow upload rules |
| Files from an old chat | the create_file inputs in the transcript | text files: rebuild the final version and attach. Binary made by a script: mark "not recoverable, see chat" |

**Upload rules.**

1. Text files (md, html, csv, json, txt, svg, code) up to 200 KB: use
   `notion-create-attachment` with `content` and `filename`. Place the
   returned `markdown_source` on the page. HTML goes in an `<embed>`
   block, other files in a `<file>` block.
2. Binary files (pdf, docx, xlsx, pptx, images): call
   `notion-create-file-upload`, then POST the file with curl to the
   returned `upload_url`, with the returned headers and the file in the
   `file` form field. Then place it on the page.
   This is the normal path. It needs `api.notion.com` allowed in the
   user's network settings (see the README).
3. If step 2 fails with `host_not_allowed`, the network setting has been
   changed or is not active in this session. For a small file (under about 50 KB), upload
   it with Google Drive `create_file` using `base64Content` and
   `disableConversionToGoogleType: true`, and link the Drive file in the
   table. For anything larger, list it as "download from chat link" and
   tell the user in the confirmation.

Published artifacts are private until the user shares them. Say so in the
Where column so the receiving reader knows why a link might not open.

## Step 4: Write the record

Follow the template. Before writing section 3, reread every message the user
sent in the chat. Their directions are spread across the whole chat, often
in short replies, and they are the part most easily lost.

Run the two-question test from the template on your draft before
publishing.

## Step 5: Find or create the Notion structure

Load Notion tools with `tool_search` if they are not loaded.

1. Search Notion for the page "Claude Project Archive". If missing,
   create it as a top-level page with a two-line explanation that it
   holds handoff records organized by project.
2. Look under it for a page titled with the project name. If missing,
   create it. Give it a "Project brief" heading (leave a one-line
   placeholder if project-archive has not run yet) and a database named
   "Chats" with the properties from the template: Name
   (title), Date (date), Status (select: Active, Done, Parked), Tags
   (multi-select), Chat Link (url), Summary (text). Load
   `notion-create-database` with `tool_search` and follow its syntax.
   Try to place it inline on the project page. If the tool can only make
   a full-page database, that is fine: say so once in the confirmation
   so the user can switch it in Notion.
3. Fetch the database to get its `collection://` data source ID.

If you created the archive page in this run, the confirmation says it
is a private top-level page that the user can move.

**Avoid duplicates.** Search the Chats database for the same chat link,
or the same Name if the link is empty. If a record exists, update that
page (`notion-update-page`) instead of creating a new one, and tell the user
it was updated.

## Step 6: Create the page

Use `notion-create-pages` with the data source as parent. Properties
follow the template. Date properties use `date:Date:start` and
`date:Date:is_datetime: 0`. The body goes in `content`. Do not repeat
the title in the body.

## Step 7: Confirm

One short message, then return to whatever the user was doing:

> 🗄️ Archived to **[Project] → [Name]**. [link]

Add a line only for gaps: no chat link (ask them to paste it and you will
add it), files that could not be attached, or artifacts that need
sharing. Nothing else. No recap of the page.

## Anti-patterns

- **Dumping the transcript.** The record is a handoff, not a log.
- **Summarizing the user's directions instead of quoting them.** Their words
  carry their thinking. "They wanted it simpler" loses what "Do not build
  yet. Ask me clarifying questions" keeps.
- **Treating Claude suggestions as decisions.** Check who said it.
- **Cutting final outputs to save space.** The next reader needs the
  actual spec or prompt, not a description of it.
- **Guessing a chat link or file location.** Leave it empty and say so.
- **Writing to memory.** This skill writes to Notion only.
