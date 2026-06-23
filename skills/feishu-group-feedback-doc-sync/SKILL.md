---
name: feishu-group-feedback-doc-sync
description: Create or maintain Feishu/Lark project group feedback documents that auto-organize group chat video versions, planner feedback, colleague feedback, edited feedback messages, and feedback images into a latest-first visual review doc. Use when users ask Codex or CCSwitch to reproduce the VfxForge/GOT-style Feishu group feedback workflow, build a project video/feedback archive from a Feishu group, create a reusable review document template, or set up real-time group-to-doc synchronization.
---

# Feishu Group Feedback Doc Sync

## Overview

Use this skill to turn a Feishu project group into a structured feedback document: videos become version sections, formal feedback becomes numbered checkboxes, feedback images appear under the video, and the document stays updated by a local watcher.

This skill depends on the company's Agent Feishu authorization plugin. If the current machine has not installed it or cannot use Feishu tools, tell the user to install or authorize the plugin first and give this document: https://centurygames.feishu.cn/docx/UvqadyC9goiE8bxjVG7c3QCNncd

## Companion Skills

When executing this workflow, also use:

- `feishu` as the route into official `lark-cli`
- `lark-im` for group search, message search, media download, and sender/member resolution
- `lark-doc` for Docx/Wiki creation, fetch, update, and media insertion
- `lark-drive` when creating/importing files or changing document title/permissions
- `lark-contact` when named people must be resolved to `open_id`

Use user identity (`--as user`) by default because the user's own access controls determine which group messages and resources can be read.

## Workflow

1. Gather setup facts from the user or Feishu:
   - Project/group name or `chat_id`
   - Target Feishu document URL/token, or permission to create a new document
   - Project name and initial phase names
   - Who counts as planner/design feedback, usually one or more planner names or `open_id`s
   - Whether to hide personal names in the document
   - Video naming pattern, such as `0616v1`, `0616v2`, or filename-derived versions
   - Desired polling interval and whether a background watcher should be installed

2. Prepare the document:
   - If no target document exists, create one with `lark-doc`.
   - Build an initial structure from `references/document-template.md`.
   - Put global reading instructions and sync status above all phases.
   - Keep newest phase and newest date near the top.

3. Backfill existing history:
   - Search/list recent group messages.
   - Detect video/file messages and assign version IDs.
   - Detect formal feedback and feedback images using `references/message-semantics.md`.
   - Insert historical versions under the correct phase/date.

4. Generate local automation:
   - Create a project-local sync script plus state directory.
   - Use Feishu official `lark-cli` through the Agent Feishu plugin; do not call private APIs directly.
   - Use a local state file to remember processed message IDs, version metadata, feedback records, image keys, hashes, and last document update minute.
   - On Windows, install a hidden scheduled task that launches a supervisor with `pythonw.exe`.
   - For non-Windows machines, use the platform's background mechanism only after confirming with the user.

5. Verify end to end:
   - Run one manual sync.
   - Confirm the document contains a sync status callout, latest phase, latest date, video preview, feedback headers, and any feedback images.
   - Run a second sync and confirm no duplicates.
   - Check watcher heartbeat/logs if a watcher was installed.

## What To Load

- Read `references/setup-guide.md` before starting a new user's setup.
- Read `references/document-template.md` when creating or restructuring the Feishu document.
- Read `references/message-semantics.md` when classifying group messages or tuning feedback rules.
- Read `references/automation-implementation.md` when generating or modifying the local watcher.
- Read `references/request-template.md` when the user wants a copyable prompt for teammates.

## Core Rules

- Do not put message source links, sender names, or noisy provenance in the user-facing document unless the user explicitly asks.
- Show planner/design feedback as `策划反馈`; show other accepted feedback as `同事反馈`.
- Treat normal questions, acknowledgements, and discussion as discussion, not formal feedback.
- If the user edits a previous formal feedback message, update the existing feedback record instead of appending a duplicate.
- If a feedback message contains an image, download it from IM, upload it to the document, and render it below that version's video.
- Keep the document visually scannable: phase heading, date heading, version heading, video on the left, status/feedback on the right, numbered checkbox feedback under `h4` headers.
- New videos must appear even if feedback has not arrived yet; leave feedback sections empty or with a concise "waiting for feedback" note only in the version positioning callout.

## Installation Sharing

When packaging this skill for teammates, share the whole `feishu-group-feedback-doc-sync` folder. The receiving machine should place it under its Codex skills directory, usually:

```text
C:\Users\<User>\.codex\skills\feishu-group-feedback-doc-sync
```

Then the teammate can ask:

```text
Use $feishu-group-feedback-doc-sync to create a Feishu group feedback document for my project group.
```
