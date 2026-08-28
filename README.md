# invest-decision-lens

把任意事件 / 新闻 / 人物故事 / 投资标的，用「投资流程透镜」拆成一套可复用的建仓决策纪律。
核心是把**情绪决策**改装成**流程决策**——在最高信念处插入一个能说“不”的闸门。

> 本 skill 只提炼「决策结构」，不评判事件真伪或道德；案例一律匿名化，不对任何真实个人作事实认定或评价。

---

## 它能做什么

- 把热点事件 / 人物故事映射成投资纪律（尽调 → 试水 → 风险闸门）。
- 用「标的生命周期六阶段」模板拆解任意“标的获取”叙事。
- 反向解读创始人 / 大股东在社交平台的公开长篇叙事。
- 一键生成统一的建仓决策 Checklist 与分析稿（见 `scripts/`）。

## 核心框架

### 1. 三段式建仓流程
1. **尽调（Due Diligence）**——独立、可证伪的研究；调查**激励结构**而非漂亮事实；警惕“尽调剧场”。
2. **试水（Pilot）**——小仓试探，每阶段带**可证伪假设 + kill switch**。
3. **风险闸门（Risk Gate）**——最大仓位前，交给**目标函数不同的独立仲裁者**（规则/模型/他人/AI）一票否决；冷静时写、狂热时执行（预先承诺）。

### 2. 标的生命周期六阶段（主叙事模板）
锁定（冷门期认知头寸）→ 被竞品占据（场外等）→ 解绑（验残留风险）→ 首次接触试水（祛魅）→ 重仓 + 尾部闸门（每笔大钱设防）→ 退出维权（分清追偿与叙事）。

### 3. 元规则
**可逆性（Reversibility）是唯一主变量**：承诺规模 ∝ 可逆性；流动性差 / 不可逆仓位 → 更小 size + 更硬 gate。

## 九条深层原则
1. 信念-资本解耦　2. 调查激励而非事实　3. 独立仲裁者需不同目标函数
4. 沉没成本与承诺升级　5. 仓位基于最坏情况而非期望值（Kelly）
6. 叙事是工具、现金流是地基　7. 尽调剧场鉴别　8. 风险不可接受=不交易
9. 反向解读利益方叙事（诉求信号 ≠ 事实信号）

## 文件结构
```
invest-decision-lens/
├── SKILL.md                       # 主逻辑：框架、原则、工作流、禁忌
├── README.md                      # 本文件
├── LICENSE                        # MIT License
├── CONTRIBUTING.md                # 贡献约定（含匿名化硬约束）
├── .gitignore                     # 忽略缓存/构建产物
├── RELEASE_NOTES.md               # v1.0.0 发布说明（可作 GitHub Release 正文）
├── CHANGELOG.md                    # 版本记录
├── SECURITY.md                    # 漏洞上报策略与安全边界
├── tests/
│   ├── test_render.py             # 渲染输出断言 + 匿名化守卫（stdlib unittest）
│   └── test_cli.py                # CLI 模式测试（--template / stdin / --input / 非法 JSON）
├── references/
│   ├── decision-checklist.md       # 八原则深度展开 + 建仓 Checklist 模板
│   └── lifecycle-mapping.md        # 六阶段生命周期映射详解 + 匿名化案例
├── scripts/
│   └── event_to_lens.py           # 结构化事件映射 → 分析文档渲染器
├── examples/
│   ├── sample-event.json          # 脚本输入样例（人物-资本叙事 · 匿名化）
│   ├── sample-output.md           # 脚本渲染结果（由 sample-event.json 生成）
│   ├── sample-event-tech.json     # 跨行业样例：硬科技/AI 算力上市建仓（证明框架可迁移）
│   ├── sample-output-tech.md      # 脚本渲染结果（由 sample-event-tech.json 生成）
│   ├── sample-event-pe.json       # 跨资产类别样例：一级市场老股转让/pre-IPO（证明框架跨资产类别）
│   ├── sample-output-pe.md        # 脚本渲染结果（由 sample-event-pe.json 生成）
│   ├── sample-event-commodity.json # 跨结构样例：周期品/大宗商品 底部反转（标的=供需周期本身）
│   └── sample-output-commodity.md  # 脚本渲染结果（由 sample-event-commodity.json 生成）
└── .github/
    ├── dependabot.yml             # 每周自动检查 GitHub Actions 依赖更新
    └── workflows/
        └── validate.yml           # CI：推送/PR 时校验 JSON 并跑通渲染
```

## 脚本用法
```bash
# 渲染分析稿
python scripts/event_to_lens.py --input examples/sample-event.json > examples/sample-output.md

# 跨行业样例（硬科技/AI 算力赛道）
python scripts/event_to_lens.py --input examples/sample-event-tech.json > examples/sample-output-tech.md

# 跨资产类别样例（一级市场老股转让 / pre-IPO）
python scripts/event_to_lens.py --input examples/sample-event-pe.json > examples/sample-output-pe.md

# 打印空 JSON 模板后自行填写
python scripts/event_to_lens.py --template > my-event.json

# 或从 stdin 喂入
cat my-event.json | python scripts/event_to_lens.py
```
脚本仅做结构化渲染，不替你做投资判断。输入为 JSON，字段见 `examples/sample-event.json`。包内附四个匿名化样例：人物-资本叙事（`sample-event.json`）、硬科技上市建仓（`sample-event-tech.json`）、一级市场老股转让/pre-IPO（`sample-event-pe.json`）、周期品/大宗商品底部反转（`sample-event-commodity.json`）。后三者分别用于演示同一框架的跨行业、跨资产类别、跨结构（标的=供需周期本身，而非公司/人物）迁移能力，证明迁移边界是“任何有生命周期的标的”。新增样例只需放入 `examples/sample-event*.json`，CI 与测试会自动覆盖。

## 触发方式
提及 尽调 / 试水 / 风险闸门 / 仓位管理 / 建仓纪律 / 投资流程 / 标的生命周期 / 信念资本解耦 / 大股东叙事，或问“从这个事能看到什么投资逻辑”。

## 许可与免责
案例为公开网络事件的匿名化改编，仅供决策结构类比。发布 / 使用时请勿指认真实个人、勿对事件事实作认定。

## CI
仓库自带 GitHub Actions（`.github/workflows/validate.yml`）：每次 push / PR 自动校验 `examples/*.json` 可解析、脚本能渲染样例、模板模式可用，并运行 `tests/test_render.py`（渲染输出断言）。上传到 GitHub 后无需额外配置即生效。

## Tests
```bash
python -m unittest discover -s tests
```
使用 stdlib `unittest`，无需安装 pytest。覆盖三类断言：
- **渲染测试**（`tests/test_render.py`）：每个样例输出含全部必含章节与六个阶段。
- **CLI 测试**（`tests/test_cli.py`）：`--template` 产出合法 JSON 骨架且可渲染、stdin 与 `--input` 输出一致、非法 JSON 被拒绝。
- **匿名化守卫**（`tests/test_render.py`）：扫描全包（除 `tests/` 自身）是否出现真实人名，一旦泄漏即失败——把“公开发布不指认真实个人”的硬约束工程化、自执行。

CI 通过 `python -m unittest discover -s tests` 跑全部测试文件（同理覆盖上述三类）。

## License
[MIT](LICENSE)。可自由使用、修改、再分发；请保留版权声明与许可文本。

## Security
安全漏洞请按 [SECURITY.md](SECURITY.md) 私下上报（不要开公开 issue）。本包无密钥、无网络调用、无第三方运行时依赖；CI 不需要 secrets。`dependabot.yml` 每周自动检查 Actions 依赖更新。

## Contributing
见 [CONTRIBUTING.md](CONTRIBUTING.md)。核心硬约束：**案例一律匿名化，不得出现真实个人姓名（含中英文）**，且须保留 disclaimer。提交前请本地跑通 `scripts/event_to_lens.py` 与 CI。
