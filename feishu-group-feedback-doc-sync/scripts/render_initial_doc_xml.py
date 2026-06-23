from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


def esc(value: object) -> str:
    return html.escape(str(value), quote=False)


def load_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def render(config: dict[str, Any]) -> str:
    project_name = config.get("project_name", "项目")
    title = config.get("title") or f"{project_name} 群聊视频反馈整理"
    updated_at = config.get("updated_at") or datetime.now().strftime("%Y-%m-%d %H:%M")
    phases = config.get("phases") or [
        {
            "title": config.get("active_phase", "一、当前阶段"),
            "goal": "沉淀项目群视频版本和反馈。",
        }
    ]

    parts: list[str] = [
        f"<title>{esc(title)}</title>",
        '<callout emoji="📌" background-color="light-blue" border-color="blue">',
        "<p><b>阅读方式：</b>最新阶段和最新日期在最上方；同一天的小版本归入同一日期，左侧目录可折叠旧日期。</p>",
        "</callout>",
        '<callout emoji="⏱" background-color="light-gray" border-color="gray">',
        f"<p><b>自动同步状态：</b>最后更新 {esc(updated_at)}；同步内容：项目群视频、策划反馈、同事反馈。</p>",
        "</callout>",
    ]

    for phase in phases:
        phase_title = phase.get("title", "未命名阶段")
        phase_goal = phase.get("goal", "沉淀该阶段的视频版本和反馈。")
        parts.extend(
            [
                f"<h1>{esc(phase_title)}</h1>",
                '<callout emoji="🎯" background-color="light-purple" border-color="purple">',
                f"<p><b>阶段目标：</b>{esc(phase_goal)}</p>",
                "</callout>",
                "<p></p>",
            ]
        )

    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="生成群聊反馈文档的初始飞书 Docx XML。")
    parser.add_argument("--config", required=True, type=Path, help="UTF-8 JSON 配置文件。")
    parser.add_argument("--output", type=Path, help="可选输出 XML 路径；不填时输出到 stdout。")
    args = parser.parse_args()

    xml = render(load_config(args.config))
    if args.output:
        args.output.write_text(xml, encoding="utf-8")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(xml)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
