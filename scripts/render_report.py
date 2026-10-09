#!/usr/bin/env python3
"""Render a self-contained paywall research report from a selected template."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--template", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    required = ("title", "report_id", "generated_at", "body_html")
    missing = [key for key in required if not payload.get(key)]
    if missing:
        raise SystemExit(f"Missing required fields: {', '.join(missing)}")

    template_path = args.template or Path(__file__).resolve().parent.parent / "assets" / "paywall-report-template.html"
    template = template_path.read_text(encoding="utf-8")
    replacements = {
        "{{REPORT_TITLE}}": escape_text(str(payload["title"])),
        "{{REPORT_ID}}": escape_attr(str(payload["report_id"])),
        "{{GENERATED_AT}}": escape_text(str(payload["generated_at"])),
        "{{REPORT_BODY}}": str(payload["body_html"]),
        "{{EMBEDDED_COMMENTS}}": json.dumps(payload.get("comments", []), ensure_ascii=False).replace("</", "<\\/"),
    }
    for marker, value in replacements.items():
        template = template.replace(marker, value)
    unresolved = [marker for marker in replacements if marker in template]
    if unresolved:
        raise SystemExit(f"Unresolved template markers: {', '.join(unresolved)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(template, encoding="utf-8")


def escape_text(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def escape_attr(value: str) -> str:
    return escape_text(value).replace('"', "&quot;")


if __name__ == "__main__":
    main()
