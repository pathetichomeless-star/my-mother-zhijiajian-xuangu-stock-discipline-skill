# Changelog

## v1.0.0 (2026-08-28)
- 初始发布：投资流程透镜（invest-decision-lens）skill。
- 核心框架：三段式建仓流程（尽调 → 试水 → 风险闸门）+ 标的生命周期六阶段 + 九条深层原则。
- `scripts/event_to_lens.py`：结构化事件映射 → 分析文档渲染器（纯 stdlib，无依赖）。
- `references/`：八原则深度展开、建仓 Checklist 模板、六阶段生命周期映射详解（含匿名化案例）。
- `examples/`：匿名化样例 JSON 与渲染输出。
- `.github/workflows/validate.yml`：CI 校验 JSON 解析、渲染、模板模式。
- `tests/test_render.py`：渲染输出断言测试（stdlib unittest，无需 pytest）。
- `LICENSE`（MIT）、`CONTRIBUTING.md`、`README.md`、`.gitignore`、`RELEASE_NOTES.md`、`SECURITY.md`。
- `.github/dependabot.yml`：每周自动检查 GitHub Actions 依赖更新。
- `examples/sample-event-tech.json` + `sample-output-tech.md`：跨行业匿名化样例（硬科技/AI 算力上市建仓），演示框架可迁移性。
- `examples/sample-event-pe.json` + `sample-output-pe.md`：跨资产类别匿名化样例（一级市场老股转让/pre-IPO），演示框架跨资产类别迁移（解绑期隐性负债 = 对赌/优先权）。
- `SKILL.md` 精修：重写 `description` 触发词（中英文双语、含“映射到交易/把故事改成纪律/大佬发长文怎么看”等自然语言句式，并显式声明“不荐股、不做买卖建议、不认定真实个人”以避免误触发）；新增 “When NOT to use” 段，明确排除选股、个股基本面分析、买卖建议等场景，提升路由精度。
- `scripts/event_to_lens.py` 补中文 docstring（render / print_template / main 及常量注释），提升可维护性。
- `tests/test_render.py` 新增**匿名化守卫测试**（`test_anonymization_enforced` + `test_rendered_output_is_anonymous`）：扫描全包是否出现真实人名，泄漏即失败，把“公开发布不指认真实个人”的硬约束自执行化。
- `tests/test_cli.py` 新增 **CLI 测试**：覆盖 `--template` 合法 JSON 骨架且可渲染、stdin 与 `--input` 输出一致、非法 JSON 被拒绝——弥补此前仅 CI shell 步骤“跑通”而未断言的缺口。
- CI 改为 `python -m unittest discover -s tests`，统一跑全部测试文件（渲染 / CLI / 匿名化守卫）。
- Bug 修复：`print_template()` 的第六阶段原名 `重仓+尾部闸门`（无空格）与各样例及 SKILL.md 的 canonical 名 `重仓 + 尾部闸门` 不一致；已统一为带空格版本，确保 `--template` 脚手架与全包阶段名对齐（由新增 CLI 测试 `test_template_renders_cleanly` 捕获）。
- `SKILL.md` 新增「Input & renderer」段：说明被唤起后如何调用渲染脚本、输入 JSON 字段（title/summary/stages/principles_applied/extra_notes）与三种 CLI 模式（`--input`/`--template`/stdin），使 skill 在对话中被触发时自包含、可直接执行。
- `examples/sample-event-commodity.json` + `sample-output-commodity.md`：跨结构匿名化样例（周期品/大宗商品 底部反转），标的为一段供需周期本身（非公司/人物），证明框架迁移边界是“任何有生命周期的标的”。tests/CI 自动覆盖。
- `tests/test_render.py` 改为数据驱动：自动覆盖 `examples/sample-event*.json` 全部样例。
- `.github/workflows/validate.yml` 改为循环渲染全部样例，而非仅 `sample-event.json`。
- 全包匿名化：不指认任何真实个人，规避公开发布的法律与声誉风险。
