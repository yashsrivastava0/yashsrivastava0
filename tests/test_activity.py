"""Check real failure modes in the contribution parser and chart pipeline."""

from datetime import date, timedelta
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError
import xml.etree.ElementTree as ET

from scripts.update_activity import main, parse_calendar, render_svg, summarize, write_snapshot


def calendar_html(days):
    cells = []
    for i, (day, count) in enumerate(days.items()):
        count_text = "No contributions" if count == 0 else f"{count:,} contribution" + ("s" if count != 1 else "")
        cells.append(
            f'<td id="day-{i}" data-date="{day}" data-level="0"></td>'
            f'<tool-tip for="day-{i}">{count_text} on October 1st.</tool-tip>'
        )
    return "<table>" + "".join(cells) + "</table>"


def complete_window(as_of):
    start = as_of - timedelta(days=as_of.weekday() + 7 * 11)
    return {start + timedelta(days=i): i % 4 for i in range((as_of - start).days + 1)}


class ActivityTests(unittest.TestCase):
    def test_zero_singular_plural_and_comma_counts(self):
        counts = {date(2026, 10, 1) + timedelta(days=i): n for i, n in enumerate([0, 1, 25, 1234])}
        self.assertEqual(parse_calendar(calendar_html(counts)), counts)

    def test_unrelated_tooltips_are_ignored(self):
        counts = {date(2026, 10, 8): 1}
        html = '<tool-tip for="menu">Open menu</tool-tip>' + calendar_html(counts)
        self.assertEqual(parse_calendar(html), counts)

    def test_login_page_or_changed_markup_cannot_become_zero_activity(self):
        for html in ["<h1>Sign in</h1>", '<td id="one" data-date="2026-10-08" data-level="0"></td>']:
            with self.subTest(html=html), self.assertRaises(ValueError):
                parse_calendar(html)

    def test_duplicate_dates_are_rejected(self):
        one_day = calendar_html({date(2026, 10, 8): 1})
        with self.assertRaises(ValueError):
            parse_calendar(one_day + one_day.replace("day-0", "day-1"))

    def test_week_totals_and_partial_week_match_daily_source(self):
        as_of = date(2026, 10, 8)
        counts = complete_window(as_of)
        result = summarize(counts, as_of, "yashsrivastava0")
        self.assertEqual(result["window_start"], "2026-07-20")
        self.assertEqual(len(result["weekly"]), 12)
        self.assertEqual(result["total"], sum(counts.values()))
        self.assertEqual(sum(w["count"] for w in result["weekly"]), result["total"])
        self.assertEqual(result["active_days"], sum(n > 0 for n in counts.values()))
        self.assertEqual(result["weekly"][-1]["end"], str(as_of))
        self.assertTrue(result["last_week_partial"])

    def test_window_crosses_year_boundary_and_complete_sunday(self):
        as_of = date(2026, 1, 4)
        result = summarize(complete_window(as_of), as_of, "yashsrivastava0")
        self.assertTrue(result["window_start"].startswith("2025-"))
        self.assertEqual(result["days_observed"], 84)
        self.assertFalse(result["last_week_partial"])

    def test_missing_day_is_not_silently_filled_with_zero(self):
        as_of = date(2026, 10, 8)
        counts = complete_window(as_of)
        del counts[as_of - timedelta(days=3)]
        with self.assertRaisesRegex(ValueError, "Incomplete calendar"):
            summarize(counts, as_of, "yashsrivastava0")

    def test_theme_and_mobile_outputs_have_accessible_xml(self):
        as_of = date(2026, 10, 8)
        result = summarize(complete_window(as_of), as_of, "example<&>")
        ns = {"s": "http://www.w3.org/2000/svg"}
        for dark in (False, True):
            for mobile in (False, True):
                with self.subTest(dark=dark, mobile=mobile):
                    root = ET.fromstring(render_svg(result, dark, mobile))
                    self.assertEqual(root.attrib["width"], "400" if mobile else "900")
                    self.assertIn("example<&>", root.find("s:title", ns).text)
                    self.assertIn("not commit totals", root.find("s:desc", ns).text)
                    self.assertEqual(len(root.findall("s:rect/s:title", ns)), 12)

    def test_repeatable_writes_touch_only_activity_files(self):
        as_of = date(2026, 10, 8)
        result = summarize(complete_window(as_of), as_of, "yashsrivastava0")
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            untouched = output / "hero.png"
            untouched.write_bytes(b"existing art")
            write_snapshot(result, output)
            before = {p.name: p.read_bytes() for p in output.iterdir()}
            write_snapshot(result, output)
            self.assertEqual(before, {p.name: p.read_bytes() for p in output.iterdir()})
            self.assertEqual(untouched.read_bytes(), b"existing art")

    def test_zero_activity_has_no_positive_bars(self):
        as_of = date(2026, 10, 8)
        counts = {day: 0 for day in complete_window(as_of)}
        result = summarize(counts, as_of, "yashsrivastava0")
        root = ET.fromstring(render_svg(result))
        ns = {"s": "http://www.w3.org/2000/svg"}
        bars = [rect for rect in root.findall("s:rect", ns) if rect.find("s:title", ns) is not None]
        self.assertEqual(result["total"], 0)
        self.assertEqual(result["active_days"], 0)
        self.assertTrue(all(float(rect.attrib["height"]) == 0 for rect in bars))

    def test_network_failure_keeps_last_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            previous = output / "activity-dark.svg"
            previous.write_text("last valid snapshot")
            with patch("sys.argv", ["update_activity.py", "--output", temp]), \
                    patch("scripts.update_activity.urlopen", side_effect=URLError("unavailable")), \
                    self.assertRaises(URLError):
                main()
            self.assertEqual(previous.read_text(), "last valid snapshot")


if __name__ == "__main__":
    unittest.main()
