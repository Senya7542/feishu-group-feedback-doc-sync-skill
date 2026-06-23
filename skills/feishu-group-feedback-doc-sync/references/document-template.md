# Document Template

Use this reference when creating or restructuring the Feishu feedback document.

## Top-Level Shape

1. Document title: `<Project Name> 群聊视频反馈整理`
2. Global reading guide callout at the top.
3. Global sync status callout below the reading guide.
4. Active/latest phase first.
5. Older phases below, newest-to-oldest by phase.

Recommended top blocks:

```xml
<title>{project_name} 群聊视频反馈整理</title>
<callout emoji="📌" background-color="light-blue" border-color="blue">
  <p><b>阅读方式：</b>最新阶段和最新日期在最上方；同一天的小版本归入同一日期，左侧目录可折叠旧日期。</p>
</callout>
<callout emoji="🕒" background-color="light-gray" border-color="gray">
  <p><b>自动同步状态：</b>最后更新 {yyyy-MM-dd HH:mm}；同步内容：项目群视频、策划反馈、同事反馈。</p>
</callout>
```

## Phase Layout

Each major project stage is an `h1`.

```xml
<h1>二、循环1阶段</h1>
<callout emoji="🎯" background-color="light-purple" border-color="purple">
  <p><b>阶段目标：</b>{short_goal}</p>
</callout>
```

Newest phase goes above older phases. New incoming videos are inserted under the configured `active_phase`.

## Date Layout

Dates are `h2` blocks with an icon. Same-day versions live under one date.

```xml
<h2>📅 2026-06-23</h2>
<callout emoji="📍" background-color="light-gray" border-color="gray">
  <p><b>当日概览：</b>最新版本 {version}；由项目群视频自动同步生成，等待后续反馈沉淀。</p>
</callout>
```

Use at least two blank paragraphs between different dates if the document feels dense.

## Version Layout

Each video version is an `h3`.

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

Feedback headers should remain `h4` even if they appear in the document outline. They make the right column easier to scan.

## Feedback Rendering

Render feedback as numbered checkboxes:

```xml
<checkbox done="false">1. 这里是第一条反馈</checkbox>
<checkbox done="false">2. 这里是第二条反馈</checkbox>
```

Do not preserve people's real names by default. Replace planner names with `策划` only when needed for readability.

## Feedback Images

For images contained in formal feedback:

- Insert images below the version video in the left column.
- Keep video first, then feedback images in message order.
- Re-render images from recorded image keys so edited feedback does not duplicate images.
- Use a consistent width such as 315px for vertical video screenshots/feedback images.
