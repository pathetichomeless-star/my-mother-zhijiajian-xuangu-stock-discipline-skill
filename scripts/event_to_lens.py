#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""投资流程透镜：把结构化事件映射渲染为分析文档。

把任意事件按六阶段生命周期拆解后，用本脚本生成统一的 markdown 分析稿，
保证每次输出结构一致、不遗漏框架要点。仅做结构化渲染，不替你做判断。

用法:
  python event_to_lens.py --input event.json > analysis.md
  python event_to_lens.py --template        > event.template.json
  cat event.json | python event_to_lens.py
"""
import argparse
import json
import sys

# 三条收敛纪律：无论输入什么事件，渲染输出都会把这三句钉在文末，
# 防止使用者把"故事"误当"纪律"。
HARD_DISCIPLINES = [
    "标的生命周期纪律：锁定（冷门期建认知头寸）→ 等竞品解绑（不硬挤）→ 验残留风险（解绑≠便宜）→ "
    "小仓试水祛魅 → 大钱前置对价必设退出机制 → 尾部加价交给独立闸门 → 退出分清追偿与叙事。",
    "闸门前置纪律：风险闸门要用在每一笔大钱（含预付对价），不是只在最后一步。",
    "叙事反向纪律：别人（尤其利益方）的公开长篇叙事，先当“诉求信号”而非“事实信号”处理。",
]

# 建仓决策 Checklist 的七行固定模板。
# 每行四列含义：(阶段, 检查项, 一票否决条件, 证据来源)
CHECKLIST_ROWS = [
    ("尽调", "是否独立、可证伪？是否调查了激励结构？", "研究不能证伪 thesis / 未识别对方动机", "财报、产业链、激励方披露"),
    ("试水", "是否小仓试探？有无可证伪假设？", "无 kill switch / 假设不可证伪", "模拟仓 / 极小仓实盘反馈"),
    ("风险闸门", "谁/什么规则有否决权？目标函数是否独立？", "无独立仲裁者 / 规则未在冷静时写下", "预先承诺的纪律文档"),
    ("仓位", "是否基于最坏情况回撤？", "单一不利结果可致命", "尾部情景测算"),
    ("可逆性", "仓位 size 是否与可逆性成正比？", "不可逆仓位过大", "流动性 / 锁定期评估"),
    ("分账户", "利润与本金是否分账户？", "“仅退款”心态（既要收益又要本金）", "心理账户记录"),
    ("叙事反向", "利益方长篇叙事：脱节？越界？背书具体诉求？", "三者任一命中且无对冲", "叙事 vs 现金流核对"),
]


def render(data):
    """把结构化事件数据渲染为分析稿 markdown。

    参数 data 需包含：
      - title(str)：标题
      - summary(str, 可选)：一句话概述
      - stages(list[dict])：六项，每项 {stage, name, event, stock_mapping, discipline}
      - principles_applied(list[str], 可选)：命中的深层原则编号
      - extra_notes(str, 可选)：附记
    返回拼接好的 markdown 字符串。本函数仅做结构化渲染，不替你做任何投资判断。
    """
    out = []
    title = data.get("title", "未命名事件 · 投资流程透镜分析")
    out.append("# %s\n" % title)
    summary = data.get("summary")
    if summary:
        out.append(summary + "\n")
    out.append("> 本分析仅提炼决策结构，不评判事件真伪或道德。案例如涉真实人物，应匿名化并加 disclaimer。\n")

    out.append("## 六阶段生命周期映射\n")
    out.append("| 阶段 | 事件节点 | 股市映射 | 纪律 |")
    out.append("|------|----------|----------|------|")
    for s in data.get("stages", []):
        cell = "%s. %s" % (s.get("stage", ""), s.get("name", ""))
        out.append("| %s | %s | %s | %s |" % (
            cell, s.get("event", ""), s.get("stock_mapping", ""), s.get("discipline", "")))
    out.append("")

    out.append("## 建仓决策 Checklist\n")
    out.append("| 阶段 | 检查项 | 一票否决条件 | 证据来源 |")
    out.append("|------|--------|--------------|----------|")
    for row in CHECKLIST_ROWS:
        out.append("| %s | %s | %s | %s |" % row)
    out.append("")

    pa = data.get("principles_applied")
    if pa:
        out.append("## 命中的深层原则\n")
        for p in pa:
            out.append("- 原则 %s" % p)
        out.append("")

    out.append("## 收敛纪律\n")
    for d in HARD_DISCIPLINES:
        out.append("- %s" % d)
    out.append("")

    notes = data.get("extra_notes")
    if notes:
        out.append("## 附记\n")
        out.append(notes + "\n")
    return "\n".join(out)


def print_template():
    """打印一个空 JSON 模板（stage 名称采用标准六阶段），供用户自行填写后喂给 --input。"""
    scaffold = {
        "title": "事件标题",
        "summary": "一句话概括事件与你的视角。",
        "stages": [
            {"stage": 1, "name": "冷门期锁定标的", "event": "（填入事件节点）", "stock_mapping": "（填入股市映射）", "discipline": "（填入纪律）"},
            {"stage": 2, "name": "被竞品/旧庄占据", "event": "", "stock_mapping": "", "discipline": ""},
            {"stage": 3, "name": "解绑（带隐性负债）", "event": "", "stock_mapping": "", "discipline": ""},
            {"stage": 4, "name": "首次接触/试水", "event": "", "stock_mapping": "", "discipline": ""},
            {"stage": 5, "name": "重仓 + 尾部闸门", "event": "", "stock_mapping": "", "discipline": ""},
            {"stage": 6, "name": "退出维权/公开叙事", "event": "", "stock_mapping": "", "discipline": ""},
        ],
        "principles_applied": ["1", "3", "9"],
        "extra_notes": "可选。",
    }
    print(json.dumps(scaffold, ensure_ascii=False, indent=2))


def main():
    """CLI 入口：--input 读文件 / --template 打印空模板 / 否则从 stdin 读取 JSON 并渲染。"""
    ap = argparse.ArgumentParser(description="投资流程透镜：结构化事件映射 → 分析文档")
    ap.add_argument("--input", help="JSON 文件路径；省略则从 stdin 读取")
    ap.add_argument("--template", action="store_true", help="打印空 JSON 模板")
    args = ap.parse_args()

    if args.template:
        print_template()
        return

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            raw = f.read()
    else:
        raw = sys.stdin.read()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        sys.stderr.write("JSON 解析失败: %s\n" % e)
        sys.exit(1)

    sys.stdout.write(render(data))


if __name__ == "__main__":
    main()
