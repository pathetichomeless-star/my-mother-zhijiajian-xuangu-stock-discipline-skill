---
name: invest-decision-lens
description: 当用户想从任意事件、新闻、人物故事或投资标的中提炼「投资决策流程 / 交易纪律」时使用本 skill——尤其适用于：把一段多阶段叙事（冷门期锁定 → 被竞品/旧庄占据 → 解绑带负债 → 试水祛魅 → 重仓+尾部风险闸门 → 退出/维权/公开叙事）映射到股市建仓纪律；从热点事件、大佬长文、私人纠纷中抽离出可复用的「尽调→试水→风险闸门」框架与标的生命周期、叙事反向解读方法。触发词/句式（中英文均可）：尽调、试水、风险闸门、仓位管理、建仓纪律、投资流程、标的生命周期、信念-资本解耦、大股东叙事、情绪决策改流程决策、"从这个事能看到什么投资逻辑"、"对股票有什么启示"、"大佬发长文站台怎么看"、"把 XX 事件映射到我的交易"、"怎么把故事改成纪律"。本 skill 只提炼决策结构：不评判事件真伪或道德、不荐股、不做具体买卖建议、不对任何真实个人作事实认定或评价。
agent_created: true
---

# 投资流程透镜（Investment Decision Lens）

## Purpose
Turn any event or narrative into a reusable investment decision process. Help the user extract trading discipline from news, stories, or their own trades — not to judge whether the event is true or moral. The core move is converting "emotional decision-making" into "process decision-making" by inserting a gate that can say "no" at the peak of conviction.

## When to use
- Analyze a hot event, public-figure story, or news item through an investment lens.
- Need a stock entry / add-on / position-sizing decision framework or checklist.
- Mention: 尽调, 试水, 风险闸门, 仓位管理, 建仓纪律, 投资流程, 标的生命周期, 信念-资本解耦, 大股东叙事.
- Ask "从这个事能看到什么投资逻辑 / 对股票有什么启示 / 怎么把故事改成纪律".

## When NOT to use
- Direct stock picking or "which stock should I buy" requests — this skill does not select securities.
- Fundamental analysis of a specific listed company (financials, valuation, catalysts) — that is a different task.
- Explicit buy/sell/hold advice or portfolio management for a real account.
- Factual claims about, or moral judgment of, any real named individual or event.
- In those cases, handle directly or route to a research/quant skill; keep this skill for decision-*structure* extraction only.

## Core framework

### A. Three-stage position-building process
1. **Due Diligence (尽调)** — independent, falsifiable research before entry; investigate the *incentive structure*, not pretty facts; watch for "due-diligence theater".
2. **Pilot (试水)** — small-position probing, each stage carrying a *falsifiable hypothesis + kill switch*.
3. **Risk Gate (风险闸门)** — at the largest commitment, hand the decision to an *independent arbiter with a different objective function* (rule / model / another person / AI) holding veto power; rules written while calm, executed while euphoric (pre-commitment).

### B. Target-lifecycle mapping (master narrative template)
Any "target acquisition" arc decomposes into six stages, each mapped to a stock discipline (see `references/lifecycle-mapping.md`):
1. **Lock the target (cold-period watchlist)** — build a cognitive position while unnoticed; discipline: distinguish "story I like" from "company I understand".
2. **Occupied by a competitor / old blockholder** — target in someone else's main uptrend; discipline: don't force entry, wait for unbinding.
3. **Unbinding (breakup + fallout)** — "free" but carries hidden liabilities; discipline: unbinding ≠ cheap, audit residual risk first.
4. **First contact (pilot / disenchantment)** — crossing to a real position triggers disenchantment; discipline: verify thesis with small real capital, not long-held fantasy.
5. **Heavy position + tail risk gate** — upfront consideration is sunk and hard to recover; the tail ask triggers an independent veto; discipline: the gate must sit on *every* large outlay, not only the final step.
6. **Exit / litigation + public narrative** — recovery (position close) plus public narrative (short-report-style pressure); discipline: separate "recovery" from "narrative"; beware reflexivity backlash.

### C. Meta-rule: reversibility is the only master variable
Commitment size ∝ reversibility. Illiquid / irreversible positions → smaller size + harder gate.

## Deep principles (full expansion in references/)
1. **Conviction-Capital Decoupling** — insert friction between "I like it" and "I fund it".
2. **Incentives over Facts** — ask "who has the motive to pull me in"; adverse selection.
3. **Independent arbiter needs a different objective function** — you cannot be your own circuit breaker.
4. **Sunk cost & escalation of commitment** — exit on falsification, never average down.
5. **Size on worst case, not expected value** — never so large that one adverse outcome is fatal (Kelly).
6. **Narrative is a tool, cashflow is the foundation** — distinguish good story from good business; large positions are reflexive.
7. **Due-diligence theater detection** — research that cannot falsify the thesis is performance.
8. **Unacceptable risk = no trade, not smaller trade** — systemic risk is not dissolved by position size.
9. **Reverse-read stakeholder narratives** — when a founder/blockholder posts a long narrative, treat it as a *claim signal*, not a *fact signal*.

## Reverse-reading social-platform narratives (principle 9)
When a founder / large shareholder suddenly posts a long narrative on social media:
- **Persona maintenance (credibility arbitrage)** — mixing genuine industry commentary with a targeted narrative to lend the private claim legitimacy.
- **"Fiction + real-name" dual track** — blurring the line between novel and disclosure; a gray zone.
- **Sequencing** — hard legal/factual anchor first, soft narrative after (anchor then amplify).
- **Visual packaging** — IR / roadshow-style material.
- **Cross-border venue choice** — posting where regulation is looser (cross-platform message management).
Checklist: (1) does narrative decouple from cashflow? (2) is it blurring disclosure boundaries? (3) is personal IP backing a specific ask? All three are *warn*, not *follow*, signals.

## Workflow
1. Receive the event/target; state explicitly "we assess decision structure, not truth or morality".
2. Map it onto the three-stage framework and the six-stage lifecycle.
3. Apply the deep principles for deeper analysis; surface blind spots (confirmation bias, escalation of commitment).
4. Output the build-position checklist (stage / checks / veto condition / evidence source) from `references/decision-checklist.md`.
5. Converge to one executable discipline statement.

## Input & renderer (scripts/event_to_lens.py)
When the mapping converges, render it with the bundled script instead of free-writing, so every output keeps the same structure (six-stage table + checklist + convergence disciplines). The script only renders; it never makes the investment judgment for you.

Input JSON fields:
- `title` (str): analysis title.
- `summary` (str, optional): one-line framing of the event and your angle.
- `stages` (list[dict], exactly 6): each item `{ "stage", "name", "event", "stock_mapping", "discipline" }` — the six lifecycle stages (names are fixed; see the template).
- `principles_applied` (list[str], optional): deep-principle numbers hit, e.g. `["1", "3", "9"]`.
- `extra_notes` (str, optional): closing notes.

CLI:
- `python scripts/event_to_lens.py --input event.json > analysis.md`
- `python scripts/event_to_lens.py --template > event.json`  # print an empty scaffold to fill in
- `cat event.json | python scripts/event_to_lens.py`  # stdin mode

## Taboo & disclaimer
- Never predict the event's truth, never morally judge the people involved. Only extract decision-structure discipline.
- Case illustrations are anonymized adaptations of public network events; all persons are pseudonymized; no factual claims about any real individual are asserted, and nothing constitutes evaluation of any real person.
