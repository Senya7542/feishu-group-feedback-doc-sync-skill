# 飞书群聊反馈文档同步 Skill

这是给 Codex / Claude Code / CCSwitch 使用的 Skill，用来把飞书项目群里的视频版本、策划反馈、同事反馈和反馈图片整理成可自动更新的飞书文档。

## Skill 信息

- Skill 名称：`feishu-group-feedback-doc-sync`
- 仓库路径：`feishu-group-feedback-doc-sync`
- 主入口：`feishu-group-feedback-doc-sync/SKILL.md`

## CCSwitch 安装

在 CCSwitch 的 `Skills 管理 -> 仓库管理 -> 添加技能仓库` 中填写：

```text
仓库 URL: Senya7542/feishu-group-feedback-doc-sync-skill
分支: main
```

也可以把仓库 URL 填成完整地址：

```text
https://github.com/Senya7542/feishu-group-feedback-doc-sync-skill
```

添加仓库后回到技能列表，点击刷新，然后搜索：

```text
feishu-group-feedback-doc-sync
```

找到“飞书群聊反馈文档同步”后点击安装。

## 前置要求

这套流程依赖公司内部的 Agent 飞书授权插件。未安装或未授权时，先按下面文档完成配置：

https://centurygames.feishu.cn/docx/UvqadyC9goiE8bxjVG7c3QCNncd

## 使用方式

安装 Skill 后，对 Codex 或 Claude Code 说：

```text
使用 $feishu-group-feedback-doc-sync 为我的项目群创建并维护飞书群聊视频反馈整理文档。
```

Codex 会继续追问项目群、目标文档、当前阶段、策划反馈人员、版本命名规则和是否需要后台自动同步。

## 注意事项

这个仓库可以公开给团队通过 CCSwitch 安装。文档中的飞书链接需要公司内部权限，外部访问者无法打开；真正执行同步前，本机仍然需要安装并授权公司 Agent 飞书插件。
