# 文档模板

创建或重排飞书反馈文档时读取本文件。

## 顶层结构

1. 文档标题：`<项目名> 群聊视频反馈整理`
2. 顶部放全局阅读说明框。
3. 阅读说明下方放全局同步状态框。
4. 当前最新阶段放在最上面。
5. 历史阶段放在下面，按新到旧排列。

推荐顶部块：

```xml
<title>{project_name} 群聊视频反馈整理</title>
<callout emoji="📌" background-color="light-blue" border-color="blue">
  <p><b>阅读方式：</b>最新阶段和最新日期在最上方；同一天的小版本归入同一日期，左侧目录可折叠旧日期。</p>
</callout>
<callout emoji="⏱" background-color="light-gray" border-color="gray">
  <p><b>自动同步状态：</b>最后更新 {yyyy-MM-dd HH:mm}；同步内容：项目群视频、策划反馈、同事反馈。</p>
</callout>
```

## 阶段布局

每个项目大阶段使用 `h1`。

```xml
<h1>二、循环 1 阶段</h1>
<callout emoji="🎯" background-color="light-purple" border-color="purple">
  <p><b>阶段目标：</b>{short_goal}</p>
</callout>
```

最新阶段放在旧阶段上方。新视频插入到配置里的 `active_phase` 下。

## 日期布局

日期使用带图标的 `h2`。同一天的小版本都放在同一个日期下。

```xml
<h2>📅 2026-06-23</h2>
<callout emoji="📍" background-color="light-gray" border-color="gray">
  <p><b>当日概览：</b>最新版本 {version}；由项目群视频自动同步生成，等待后续反馈沉淀。</p>
</callout>
```

如果文档显得拥挤，不同日期之间至少留两个空段落。

## 小版本布局

每个视频版本使用 `h3`。

```xml
<h3>🎞️ {version}</h3>
<grid>
  <column width-ratio="0.500000">
    <figure view-type="Preview"><source token="{video_token}" mime="video/mp4"/></figure>
  </column>
  <column width-ratio="0.500000">
    <callout emoji="🎬" background-color="light-blue" border-color="blue" text-color="blue">
      <p><b>本版定位</b></p>
      <ul>
        <li>自动同步项目群视频版本：{version}，时长 {duration}。</li>
        <li>策划反馈可以先留空；后续明确反馈或线下整理结论再继续沉淀。</li>
      </ul>
    </callout>
    <h4>策划反馈：</h4>
    <h4>同事反馈：</h4>
  </column>
</grid>
```

反馈标题保持 `h4`，即使它们会进入左侧目录。这样右侧栏更清晰，也方便折叠查看。

## 制作会展示版本布局

当某个版本收到用户或策划明确发送的 `制作会反馈` 时，把这个版本标记为制作会展示版本，并重渲染该版本的框架：

- 小版本标题从 `<h3>🎞️ {version}</h3>` 改为 `<h3>🚩 {version}（制作会）</h3>`。
- `本版定位` callout 改成更醒目的橙色系：`emoji="🚩"`、`background-color="light-orange"`、`border-color="orange"`、`text-color="orange"`。
- `本版定位` 里增加一句：`本版为制作会展示版本，用于集中呈现制作会确认和沉淀的调整方向。`
- 原 `策划反馈：` 标题改为 `制作会反馈：`，但内部记录仍可沿用 `策划反馈` 这个逻辑类型，方便复用原有策划反馈排序、图片和编辑更新逻辑。
- 同事反馈标题保持 `同事反馈：`。

推荐 XML：

```xml
<h3>🚩 {version}（制作会）</h3>
<callout emoji="🚩" background-color="light-orange" border-color="orange" text-color="orange">
  <p><b>本版定位</b></p>
  <ul>
    <li>自动同步项目群视频版本：{version}，时长 {duration}。</li>
    <li>本版为制作会展示版本，用于集中呈现制作会确认和沉淀的调整方向。</li>
    <li>制作会反馈会在下方持续更新；后续明确补充或线下整理结论继续沉淀。</li>
  </ul>
</callout>
<h4>制作会反馈：</h4>
<h4>同事反馈：</h4>
```

## 反馈渲染

反馈用编号复选框渲染：

```xml
<checkbox done="false">1. 这里是第一条反馈</checkbox>
<checkbox done="false">2. 这里是第二条反馈</checkbox>
```

默认不要保留真实人名。需要区分来源时，只用 `策划`、`同事` 这类泛称。

同一版本如果存在用户本人发送的 `反馈整理` 或 `整理反馈`，该整理稿是文档最终可见内容。此时只显示整理稿拆出的反馈复选框和整理稿自带图片，隐藏同版本早先的策划/同事零散反馈及其图片；如果没有用户整理稿，再分别显示 `策划反馈` 和 `同事反馈`。

## 反馈图片

正式反馈里包含图片时：

- 图片放在左侧视频下方。
- 顺序固定为：视频在最上面，反馈图片按消息顺序排列在下面。
- 从记录过的 image key 重新渲染图片，避免编辑反馈时重复插入。
- 竖屏视频截图或反馈图使用一致宽度，例如 315px。
