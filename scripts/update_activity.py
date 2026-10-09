#!/usr/bin/env python3
"""Render a dated, repository-owned chart from GitHub's public contribution page.

Standard library only. Missing or unfamiliar data fails before existing assets
are replaced. Contributions are GitHub's calendar counts, not commit counts.
"""

import argparse
from datetime import date, timedelta
from html import escape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.request import Request, urlopen


DEFAULT_USER = "yashsrivastava0"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "profile"


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.counts = {}
        self.tooltip_id = None
        self.tooltip_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "data-date" in attrs and "data-level" in attrs:
            day = date.fromisoformat(attrs["data-date"])
            cell_id = attrs.get("id")
            if not cell_id or cell_id in self.cells:
                raise ValueError("Calendar contains missing or duplicate cell IDs")
            self.cells[cell_id] = day
        if tag == "tool-tip":
            self.tooltip_id = attrs.get("for")
            self.tooltip_text = []

    def handle_data(self, data):
        if self.tooltip_id is not None:
            self.tooltip_text.append(data)

    def handle_endtag(self, tag):
        if tag == "tool-tip" and self.tooltip_id is not None:
            text = " ".join("".join(self.tooltip_text).split())
            match = re.fullmatch(r"(No|\d[\d,]*) contributions? on .+\.", text)
            if match and self.tooltip_id in self.cells:
                day = self.cells[self.tooltip_id]
                if day in self.counts:
                    raise ValueError(f"Duplicate contribution date: {day}")
                number = match.group(1)
                self.counts[day] = 0 if number == "No" else int(number.replace(",", ""))
            self.tooltip_id = None
            self.tooltip_text = []


def parse_calendar(html):
    parser = CalendarParser()
    parser.feed(html)
    parser.close()
    if not parser.cells or len(parser.counts) != len(parser.cells):
        raise ValueError("GitHub calendar format is missing or unrecognized; keeping last snapshot")
    return parser.counts


def summarize(counts, as_of, username):
    """Eleven completed Monday-based weeks and the current partial week."""
    start = as_of - timedelta(days=as_of.weekday() + 7 * 11)
    days = [start + timedelta(days=i) for i in range((as_of - start).days + 1)]
    missing = [day for day in days if day not in counts]
    if missing:
        raise ValueError(f"Incomplete calendar: missing {len(missing)} days, starting {missing[0]}")
    daily = [{"date": str(day), "count": counts[day]} for day in days]
    weekly = []
    for i in range(12):
        week_start = start + timedelta(days=i * 7)
        week_end = min(week_start + timedelta(days=6), as_of)
        entries = [counts[day] for day in days if week_start <= day <= week_end]
        weekly.append({"start": str(week_start), "end": str(week_end), "count": sum(entries)})
    return {
        "username": username,
        "source": f"https://github.com/users/{username}/contributions",
        "as_of": str(as_of),
        "window_start": str(start),
        "window_end": str(as_of),
        "total": sum(item["count"] for item in daily),
        "active_days": sum(item["count"] > 0 for item in daily),
        "days_observed": len(daily),
        "last_week_partial": as_of.weekday() != 6,
        "weekly": weekly,
        "daily": daily,
    }


def render_svg(snapshot, dark=False, mobile=False):
    width, height = (400, 224) if mobile else (900, 192)
    palette = {
        "bg": "#0d1117" if dark else "#f6f8fa",
        "line": "#30363d" if dark else "#d1d9e0",
        "text": "#f0f6fc" if dark else "#172431",
        "muted": "#a4b1bf" if dark else "#526171",
        "accent": "#67e8f9" if dark else "#087e91",
        "bar": "#155e75" if dark else "#afe0e7",
    }
    formatted_date = date.fromisoformat(snapshot["as_of"]).strftime("%b %d, %Y")
    partial = snapshot["last_week_partial"]
    title = f"{snapshot['username']}: {snapshot['total']} GitHub contributions across 12 weeks"
    description = (
        f"{snapshot['window_start']} through {snapshot['window_end']}. "
        f"{snapshot['active_days']} active days out of {snapshot['days_observed']} observed days. "
        "Counts from the signed-out GitHub contribution calendar; they are not commit totals. "
        + ("The final week is partial." if partial else "All weeks are complete.")
    )
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
        f'<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="12" '
        f'fill="{palette["bg"]}" stroke="{palette["line"]}"/>',
    ]

    def text(x, y, value, size=12, color="muted", weight=400, anchor="start"):
        parts.append(
            f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
            f'fill="{palette[color]}">{escape(str(value))}</text>'
        )

    if mobile:
        text(20, 29, "GITHUB ACTIVITY", 13, "accent", 700)
        text(20, 49, f"GitHub contributions · as of {formatted_date}", 11)
        text(20, 92, f'{snapshot["total"]:,}', 34, "text", 700)
        text(20, 111, "contributions / 12 weeks", 11)
        text(260, 92, snapshot["active_days"], 30, "text", 700)
        text(260, 111, "active days", 11)
        plot_x, plot_width, baseline, max_height, gap = 20, 360, 190, 54, 7
    else:
        text(24, 31, "GITHUB ACTIVITY", 13, "accent", 700)
        text(24, 86, f'{snapshot["total"]:,}', 44, "text", 700)
        text(24, 110, "contributions / 12 weeks", 14)
        text(24, 140, f'{snapshot["active_days"]} active days', 14, "text", 600)
        text(24, 167, f"As of {formatted_date}", 11)
        parts.append(f'<path d="M244 28V165" stroke="{palette["line"]}"/>')
        text(272, 31, "WEEKLY GITHUB CONTRIBUTIONS", 11, "muted", 600)
        text(872, 31, "Final week partial" if partial else "12 complete weeks", 11, anchor="end")
        plot_x, plot_width, baseline, max_height, gap = 272, 600, 140, 76, 12

    step = plot_width / 12
    bar_width = step - gap
    maximum = max(1, *(week["count"] for week in snapshot["weekly"]))
    parts.append(f'<path d="M{plot_x} {baseline+1}h{plot_width}" stroke="{palette["line"]}"/>')
    for i, week in enumerate(snapshot["weekly"]):
        x = plot_x + i * step
        bar_height = max(2, week["count"] / maximum * max_height) if week["count"] else 0
        color = palette["accent"] if i == 11 else palette["bar"]
        week_note = " (partial week)" if i == 11 and partial else ""
        label = f'{week["start"]}–{week["end"]}: {week["count"]} contributions{week_note}'
        parts.append(
            f'<rect x="{x:g}" y="{baseline-bar_height:g}" width="{bar_width:g}" '
            f'height="{bar_height:g}" rx="3" fill="{color}"><title>{escape(label)}</title></rect>'
        )
        if not mobile:
            text(x + bar_width / 2, baseline - bar_height - 7, week["count"], 11, "text", anchor="middle")
            if i % 3 == 0 or i == 11:
                stamp = date.fromisoformat(week["start"]).strftime("%b %d")
                text(x + bar_width / 2, 165, stamp, 10, anchor="middle")
    if mobile:
        text(20, 211, date.fromisoformat(snapshot["window_start"]).strftime("%b %d"), 10)
        text(200, 211, "WEEKLY · LAST WEEK PARTIAL" if partial else "WEEKLY CONTRIBUTIONS", 9, anchor="middle")
        text(380, 211, date.fromisoformat(snapshot["window_end"]).strftime("%b %d"), 10, anchor="end")
    parts.append("</svg>\n")
    return "\n".join(parts)


def write_snapshot(snapshot, output):
    files = {"activity.json": json.dumps(snapshot, indent=2) + "\n"}
    for mobile in (False, True):
        for dark in (False, True):
            name = "activity" + ("-mobile" if mobile else "") + ("-dark" if dark else "-light")
            files[name + ".svg"] = render_svg(snapshot, dark, mobile)
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".activity-", dir=output) as staging:
        for name, content in files.items():
            Path(staging, name).write_text(content, encoding="utf-8")
        for name in files:
            os.replace(Path(staging, name), output / name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default=DEFAULT_USER)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--input", type=Path, help="Use a saved GitHub calendar response for offline validation")
    parser.add_argument("--as-of", type=date.fromisoformat, help="Last date to include; defaults to latest observed date")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", args.username):
        parser.error("Invalid GitHub username")
    if args.input:
        html = args.input.read_text(encoding="utf-8")
    else:
        request = Request(
            f"https://github.com/users/{args.username}/contributions",
            headers={"User-Agent": "Profilehub-Activity/1.0", "Accept-Language": "en-US"},
        )
        with urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8")
    counts = parse_calendar(html)
    as_of = args.as_of or max(counts)
    if as_of > date.today():
        raise ValueError("Calendar snapshot cannot include future days")
    snapshot = summarize(counts, as_of, args.username)
    write_snapshot(snapshot, args.output)
    print(f'Saved activity through {as_of}: {snapshot["total"]} contributions, {snapshot["active_days"]} active days')


if __name__ == "__main__":
    main()
