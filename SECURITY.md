# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

This skill is a documentation + stdlib-Python tool pack. There are no runtime
services, network calls, or external dependencies, so the attack surface is
limited to the local scripts (`scripts/event_to_lens.py`) and the bundled
example data.

## Reporting a Vulnerability

If you discover a security issue in this skill pack — for example:

- a script that executes untrusted input unsafely,
- a dependency or CI misconfiguration that could leak secrets,
- any content that inadvertently exposes private or legally sensitive data,

please report it **privately** rather than opening a public issue.

1. Open a private security advisory on the GitHub repository, **or**
2. Email the maintainers via a GitHub issue marked "security (private)" if no
   advisory feature is available.

Please include:

- a short description of the issue,
- steps to reproduce (or the exact file/line reference),
- the potential impact,
- any suggested remediation if you have one.

We aim to acknowledge reports within **7 days** and to provide a remediation
timeline within **30 days**, depending on severity.

## Scope & Non-Goals

- This pack ships **no API keys, tokens, or credentials**. Do not add any.
  CI (`validate.yml`) does not require secrets.
- The bundled `examples/sample-event.json` is **fully anonymized** (A/B/C
  pseudonyms) and contains no real-person data. See `CONTRIBUTING.md` rule #1:
  all contributed content must remain anonymized.
- This policy covers the *software artifact* (scripts, CI, packaging). It does
  **not** constitute investment advice. See the disclaimer in `SKILL.md`.

## Hard Rules (enforced in CONTRIBUTING.md)

- No real personal names of living public figures in any committed file.
- No secrets, `.env`, or credential files committed (enforced by `.gitignore`).
- No new third-party runtime dependencies — keep the pack stdlib-only.
