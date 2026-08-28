# 贡献指南（Contributing）

感谢有兴趣完善 **invest-decision-lens**。请遵循以下约定：

## 1. 匿名化是硬约束
- **案例不得出现任何真实个人姓名、昵称或可识别身份的细节**（含中英文）。
- 用 `A / B / C` 等代号，或“某公众人物 / 某标的 / 竞品”等通用表述。
- 必须保留 disclaimer：本案例为公开事件的匿名化改编，仅作决策结构类比，不认定事实、不评价真实个人。
- 原因：本 skill 默认公开发布；指认真实个人（尤其涉诉、被当事人标注“虚构”的私人指控）存在名誉权与法律风险。

## 2. 结构约定
- 新增案例放入 `examples/`，JSON 字段见 `examples/sample-event.json`（六阶段 + 纪律 + 命中原则）。
- 框架改动优先改 `SKILL.md` 与 `references/`，保持“三段式 + 六阶段生命周期 + 九原则”主干不变。
- 九条深层原则的编号保持稳定；新增原则请顺延编号，并同步更新 `SKILL.md` 与 `decision-checklist.md`。

## 3. 提交前校验
- 运行 `python scripts/event_to_lens.py --input examples/<your>.json` 确认能渲染。
- push / PR 会自动跑 `.github/workflows/validate.yml`；请先在本地跑通再提交。

## 4. 许可
- 本仓库采用 MIT。提交即表示你同意以 MIT 许可分发你的贡献。
