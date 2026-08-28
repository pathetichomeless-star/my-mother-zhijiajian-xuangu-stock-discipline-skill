#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render-output assertions + anonymization guard for invest-decision-lens.

Runs with the stdlib only (unittest), so CI does not need pytest:
    python tests/test_render.py

It imports the renderer from scripts/event_to_lens.py and checks that the
output for every bundled example (examples/sample-event*.json) contains every
mandatory section and stage, so a broken template fails the build instead of
shipping silently. New cases are picked up automatically -- just drop another
sample-event*.json into examples/.

The anonymization guard scans the whole skill tree (except this tests/ dir,
which necessarily contains the forbidden-pattern list) and fails the build if
any real-person name leaks in -- the single biggest legal risk of publishing
this skill publicly.
"""
import glob
import json
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from event_to_lens import render  # noqa: E402

EXAMPLE_GLOB = os.path.join(ROOT, "examples", "sample-event*.json")

MANDATORY_SECTIONS = [
    "六阶段生命周期映射",
    "建仓决策 Checklist",
    "收敛纪律",
    "标的生命周期纪律",
    "闸门前置纪律",
    "叙事反向纪律",
]

# Stage names are fixed by the template; every example must carry all six.
SIX_STAGES = [
    "冷门期锁定标的",
    "被竞品/旧庄占据",
    "解绑（带隐性负债）",
    "首次接触/试水",
    "重仓 + 尾部闸门",
    "退出维权/公开叙事",
]

# Forbidden real-person signals. NOTE: this list itself contains the strings it
# forbids, which is why the anonymization scan must exclude the tests/ dir.
FORBIDDEN_PATTERNS = [
    "孙宇晨", "景甜", "张继科", "张起淮", "孙割",
    "Justin", "Tron", "TRON", "Forbes", "Jike",
    "Zhang", "Jing", "波场", "TRX",
]
FORBIDDEN_RE = re.compile("|".join(re.escape(p) for p in FORBIDDEN_PATTERNS), re.IGNORECASE)

# Directories the anonymization scan must skip.
SCAN_EXCLUDE_DIRS = {"tests", ".git", "__pycache__"}
SCAN_EXTS = {".md", ".py", ".json", ".yml", ".txt"}


class TestRender(unittest.TestCase):
    def _load_all_examples(self):
        paths = sorted(glob.glob(EXAMPLE_GLOB))
        self.assertGreater(len(paths), 0, "no sample-event*.json found in examples/")
        return paths

    def test_all_examples_render_nonempty(self):
        for path in self._load_all_examples():
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            out = render(data)
            self.assertTrue(out.strip(), "empty render for %s" % path)
            self.assertIn(data.get("title", ""), out, "title missing in %s" % path)

    def test_mandatory_sections_present(self):
        for path in self._load_all_examples():
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            out = render(data)
            for needle in MANDATORY_SECTIONS:
                self.assertIn(needle, out, "missing section %r in %s" % (needle, path))

    def test_all_six_stages_present(self):
        for path in self._load_all_examples():
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            out = render(data)
            for stage in SIX_STAGES:
                self.assertIn(stage, out, "missing stage %r in %s" % (stage, path))

    def _anonymization_scan(self):
        hits = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            # prune excluded dirs in place so os.walk skips them
            dirnames[:] = [d for d in dirnames if d not in SCAN_EXCLUDE_DIRS]
            for fn in filenames:
                if os.path.splitext(fn)[1] not in SCAN_EXTS:
                    continue
                fp = os.path.join(dirpath, fn)
                try:
                    with open(fp, encoding="utf-8") as fh:
                        text = fh.read()
                except (OSError, UnicodeDecodeError):
                    continue
                m = FORBIDDEN_RE.search(text)
                if m:
                    hits.append("%s -> %s" % (fp, m.group(0)))
        return hits

    def test_anonymization_enforced(self):
        """Fail the build if any real-person name leaks into the published tree."""
        hits = self._anonymization_scan()
        self.assertEqual(hits, [], "真实人名泄漏，违反匿名化硬约束:\n" + "\n".join(hits))

    def test_rendered_output_is_anonymous(self):
        """Rendered examples must not surface forbidden names either."""
        for path in self._load_all_examples():
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            out = render(data)
            m = FORBIDDEN_RE.search(out)
            self.assertIsNone(m, "渲染输出含真实人名 %s in %s" % (m.group(0) if m else "", path))


if __name__ == "__main__":
    unittest.main(verbosity=2)
