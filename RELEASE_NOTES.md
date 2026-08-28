# invest-decision-lens v1.0.0

## 这是什么
把任意事件 / 新闻 / 人物故事 / 投资标的，用「投资流程透镜」拆成一套可复用的建仓决策纪律。
核心理念：把**情绪决策**改装成**流程决策**——在最高信念处插入一个能说“不”的闸门。

## 核心能力
- **三段式建仓流程**：尽调（Due Diligence）→ 试水（Pilot）→ 风险闸门（Risk Gate）
- **标的生命周期六阶段模板**：锁定（冷门期认知头寸）→ 被竞品占据（场外等）→ 解绑（验残留风险）→ 首次接触试水（祛魅）→ 重仓 + 尾部闸门（每笔大钱设防）→ 退出维权（分清追偿与叙事）
- **九条深层原则**：信念-资本解耦、调查激励而非事实、独立仲裁者需不同目标函数、沉没成本与承诺升级、仓位基于最坏情况、叙事 vs 现金流、尽调剧场鉴别、风险不可接受=不交易、反向解读利益方叙事
- **社交平台叙事反向解读检查表**：把创始人/大股东的长篇叙事当“诉求信号”而非“事实信号”
- **可运行脚本** `scripts/event_to_lens.py`：结构化 JSON → 统一格式分析文档渲染器（纯 stdlib，无依赖）
- **内置匿名化案例**：全程化名、不指任真实个人，规避公开发布的法律与声誉风险

## 文件结构
```
invest-decision-lens/
├── SKILL.md / README.md / LICENSE / CONTRIBUTING.md / .gitignore / RELEASE_NOTES.md
├── references/   (decision-checklist.md, lifecycle-mapping.md)
├── scripts/      (event_to_lens.py)
├── examples/     (sample-event.json, sample-output.md)
└── .github/workflows/validate.yml
```

## 快速开始
```bash
# 渲染样例
python scripts/event_to_lens.py --input examples/sample-event.json > examples/sample-output.md
# 生成空模板
python scripts/event_to_lens.py --template > my-event.json
```
push / PR 时 GitHub Actions 会自动校验 JSON 并跑通渲染。

## 许可与免责
- 许可：[MIT](LICENSE)
- 案例为公开网络事件的匿名化改编，仅供**决策结构类比**；不认定事实、不评价真实个人。
- 发布 / 使用时请勿指认真实个人、勿对事件事实作认定。
