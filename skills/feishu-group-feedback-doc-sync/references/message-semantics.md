# Message Semantics

Use this reference when deciding whether a group message should become document content.

## Video Messages

A message is a version video when it contains a downloadable video/file resource and can produce a version name.

Preferred version derivation:

1. Use explicit `MMDDvN` in filename or message text, such as `0616v2`.
2. If absent, derive `MMDDvN` from the message date and next available version number for that date.
3. If the user corrects version names, update state and document headings rather than creating new duplicate versions.

Insert the video immediately even when no feedback exists yet.

## Formal Planner Feedback

Classify as `策划反馈` when any of these is true:

- The message contains explicit labels: `策划反馈`, `线下反馈`, `面聊反馈`, `反馈整理`, `整理反馈`.
- The sender is in configured planner `open_id`s and the text contains feedback intent.
- The configured owner/self sends a labeled summary of offline planner feedback.

Accept images in the same formal feedback message and place them below the video.

## Colleague Feedback

Classify as `同事反馈` when the message contains explicit labels such as:

- `同事反馈`
- `同事补充反馈`
- A user-approved equivalent phrase for the team

Do not treat casual discussion from teammates as `同事反馈` unless explicitly labeled or the user has approved a narrower rule.

## Discussion To Ignore

Ignore these as feedback unless explicitly labeled:

- Questions about the project or implementation: `吗`, `么`, `怎么`, `是不是`, `是否`, `有没有`, `是吗`
- Acknowledgements: `好的`, `收到`, `有的`, `可以`, `ok`, `嗯`
- Short fragments without feedback content
- Messages that merely clarify earlier discussion
- Internal meeting notes that the user says belong to an older version

When unsure, be conservative: leave it out and mention that the rule can be tuned.

## Numbered Feedback

If a formal feedback message starts with numbered items, split it into separate checkbox items:

```text
反馈整理：
1. 弹出来加速的小兵动画速率不要太快
2. 地编调整，画面中道路尽量是直的
3. 初始偏移值加大
```

Render as:

```xml
<checkbox done="false">1. 弹出来加速的小兵动画速率不要太快</checkbox>
<checkbox done="false">2. 地编调整，画面中道路尽量是直的</checkbox>
<checkbox done="false">3. 初始偏移值加大</checkbox>
```

Do not collapse all numbered items into one checkbox.

## Edited Messages

Track formal feedback records by message ID and content hash.

When a message changes:

- Recompute feedback items and image keys.
- Update the existing record.
- Re-render the affected `策划反馈` or `同事反馈` section.
- Re-render feedback images for the affected version.
- Avoid appending duplicates.
