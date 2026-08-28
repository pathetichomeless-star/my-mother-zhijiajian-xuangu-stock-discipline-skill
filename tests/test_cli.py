#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI-mode assertions for invest-decision-lens.

Covers the two code paths that the render tests don't exercise through the
public surface:
  - `--template` prints a valid JSON scaffold that renders cleanly, and
  - feeding the same data via stdin vs `--input` yields identical output, and
  - invalid JSON is rejected with a non-zero exit (not a stack trace).

Uses subprocess + sys.executable so it runs under the same interpreter in both
CI (setup-python) and local, with no extra dependencies.
"""
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "scripts", "event_to_lens.py")
SAMPLE = os.path.join(ROOT, "examples", "sample-event.json")


def _run(args, stdin=None):
    return subprocess.run(
        [sys.executable, SCRIPT] + args,
        input=stdin,
        capture_output=True,
        text=True,
    )


class TestCLI(unittest.TestCase):
    def test_template_is_valid_json_scaffold(self):
        r = _run(["--template"])
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(r.stdout)  # must parse
        self.assertIn("title", data)
        self.assertIn("summary", data)
        self.assertIn("stages", data)
        self.assertEqual(len(data["stages"]), 6)
        for s in data["stages"]:
            for k in ("stage", "name", "event", "stock_mapping", "discipline"):
                self.assertIn(k, s)

    def test_template_renders_cleanly(self):
        r = _run(["--template"])
        data = json.loads(r.stdout)
        rendered = _run([], stdin=json.dumps(data, ensure_ascii=False))
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn("六阶段生命周期映射", rendered.stdout)
        # all six stage names survive a round-trip
        for name in ("冷门期锁定标的", "被竞品/旧庄占据", "解绑（带隐性负债）",
                     "首次接触/试水", "重仓 + 尾部闸门", "退出维权/公开叙事"):
            self.assertIn(name, rendered.stdout)

    def test_stdin_matches_input_file(self):
        with open(SAMPLE, encoding="utf-8") as f:
            payload = f.read()
        via_file = _run(["--input", SAMPLE])
        via_stdin = _run([], stdin=payload)
        self.assertEqual(via_file.returncode, 0, via_file.stderr)
        self.assertEqual(via_stdin.returncode, 0, via_stdin.stderr)
        self.assertEqual(via_file.stdout, via_stdin.stdout)

    def test_invalid_json_is_rejected(self):
        r = _run([], stdin="{ this is not json")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("JSON", r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
