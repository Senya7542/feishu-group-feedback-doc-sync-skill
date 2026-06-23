# Setup Guide

Use this reference when a teammate wants their own group feedback document and watcher.

## Minimum Inputs

Collect these before writing automation:

- `project_name`: Display name for the document title.
- `chat`: Feishu group name, URL, or `chat_id`.
- `target_doc`: Existing Feishu Wiki/Docx URL or permission to create a new document.
- `phases`: At least one phase title, such as `一、蓝图功能制作验证阶段` or `二、循环1阶段`.
- `active_phase`: The phase where newly detected videos should be inserted.
- `planner_people`: Names or `open_id`s whose formal feedback should become `策划反馈`.
- `self_people`: User names or `open_id`s whose edited summaries should also be accepted as `策划反馈`.
- `video_pattern`: How to derive versions from filenames/messages, for example `MMDDvN`.
- `poll_interval`: Default to 30-60 seconds.

If the user cannot provide `chat_id` or `open_id`s, resolve them through `lark-im` and `lark-contact`.

## First Setup Flow

1. Confirm Feishu plugin availability. If missing, point the user to https://centurygames.feishu.cn/docx/UvqadyC9goiE8bxjVG7c3QCNncd.
2. Resolve the project group through `lark-im +chat-search` or the available Feishu chat search command.
3. Resolve planner/self people to `open_id`.
4. Create or prepare the target document with the template rules.
5. Backfill recent group history before enabling the watcher.
6. Install the watcher only after a manual sync has succeeded.

## User-Facing Promise

Explain the behavior in plain terms:

- "When you send a video in the group, a new version section appears in the doc."
- "When formal planner feedback appears, it is added under `策划反馈`."
- "When teammate feedback appears with explicit labels, it is added under `同事反馈`."
- "Edited formal feedback updates the existing section instead of duplicating."
- "Images attached to formal feedback are placed below the video."

## Safe Defaults

- Hide person names in the document.
- Do not include source message links.
- Keep all automation state inside a project-local hidden folder.
- Use a non-popup background task on Windows.
- Log every sync attempt and maintain a heartbeat file.
