# Feishu Group Feedback Doc Sync Skill

这是一个给 Codex / Claude Code / CCSwitch 使用的 Skill，用来把飞书项目群里的视频版本、策划反馈、同事反馈和反馈图片整理成可自动更新的飞书文档。

## Skill

- Name: `feishu-group-feedback-doc-sync`
- Path: `skills/feishu-group-feedback-doc-sync`
- Main file: `skills/feishu-group-feedback-doc-sync/SKILL.md`

## CCSwitch 安装

在 CCSwitch 的 `Skills 管理 -> 仓库管理 -> 添加仓库` 中填写：

```text
Owner: Senya7542
Name: feishu-group-feedback-doc-sync-skill
Branch: main
Subdirectory: skills
```

刷新技能列表后搜索：

```text
feishu-group-feedback-doc-sync
```

## 前置要求

这套流程依赖公司 Agent 飞书授权插件。未安装或未授权时，先按以下文档配置：

https://centurygames.feishu.cn/docx/UvqadyC9goiE8bxjVG7c3QCNncd

## 使用方式

安装 Skill 后，对 Codex 或 Claude Code 说：

```text
Use $feishu-group-feedback-doc-sync to create a Feishu group feedback document for my project.
```

Skill 会引导填写项目群、目标文档、当前阶段、策划反馈人员、版本命名规则和后台同步方式。

## Privacy

建议保持仓库为 private。Skill 中包含公司内部飞书插件入口和团队文档自动化流程，不建议直接公开发布到公共注册表。
