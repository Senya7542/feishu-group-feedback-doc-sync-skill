# Automation Implementation

Use this reference when generating or modifying the local sync automation.

## Local Files

Create project-local files similar to:

```text
tools/<project>_feedback_sync.py
tools/<project>_feedback_supervisor.py
tools/install_<project>_feedback_watcher_task.ps1
.<project>_feedback_sync/
  state.json
  watcher.lock
  watcher-heartbeat.json
  supervisor-heartbeat.json
  logs/
  media/
  tasks/
```

Keep state and media caches in the project workspace, not in global temp folders.

## Sync Script Responsibilities

The sync script should:

- Read `CHAT_ID`, `TARGET_DOC`, `ACTIVE_PHASE_TITLE`, `PLANNER_OPEN_IDS`, and `SELF_OPEN_IDS` from config or constants generated during setup.
- Fetch recent group messages with `lark-im`.
- Sort messages by position/time before processing.
- Detect video messages first and create version sections.
- Detect text/post feedback after videos so feedback attaches to the latest earlier version.
- Download video/image resources from IM.
- Upload media to the Feishu document with `lark-doc` media insertion.
- Fetch inserted media blocks back as XML and reinsert them into the desired layout.
- Maintain processed message IDs, version metadata, feedback records, and hashes.
- Update a sync status callout with latest update time accurate to minute.

## Feedback Image Rule

Image feedback must go through the same record-based render path as edited feedback.

Required behavior:

1. Extract image keys from message content, usually `[Image: img_xxx]`.
2. Download each image from IM.
3. Upload it to the document.
4. Store the resulting image XML/source token in the feedback record.
5. Render all feedback images below the video in message order.
6. On re-sync, reuse stored image XML when the image key has not changed.

## Watcher

The watcher should:

- Run one sync every 30-60 seconds.
- Use a lock file so only one watcher processes the document.
- Write heartbeat JSON containing status, PID, chat ID, target doc, interval, and update time.
- Log to a project-local file.
- Never open a visible console window during normal operation.

On Windows, prefer:

- `pythonw.exe` for the scheduled supervisor
- `subprocess.CREATE_NO_WINDOW`
- A hidden Scheduled Task with `-AtLogOn`
- A supervisor that restarts the watcher when heartbeat is stale

Before installing a scheduled task:

- Stop existing watcher/supervisor processes for the same project.
- Remove stale heartbeat.
- Run one manual sync successfully.

## Verification

Always verify with fresh commands:

- Compile the sync script, for example `python -m py_compile tools/<project>_feedback_sync.py`.
- Run one manual sync.
- Fetch the latest version section and confirm video, feedback headers, and images exist.
- Run the sync again and confirm no duplicate content appears.
- Check watcher task state and heartbeat after installation.

## Common Failure Modes

- Video appears but feedback does not: classifier too strict, missing planner `open_id`, or feedback message came before video.
- Text feedback appears but image is missing: image keys are only processed in explicit feedback path; route any image-bearing formal feedback through record-based sync.
- Duplicates appear: missing message ID/hash tracking or edited messages are appended instead of re-rendered.
- Console pops up every minute: scheduled task is launching `python.exe` or PowerShell visibly; switch to hidden task and `pythonw.exe`.
- Old phase receives new videos: active phase anchor search is not scoped to `ACTIVE_PHASE_TITLE`.
