# Project Documentation Contract

## 输出映射

| 文件 | 必须回答的问题 |
|---|---|
| README.md | 为什么做、为谁做、MVP 边界、技术路线、如何开始 |
| AGENTS.md | Agent 读取顺序、真实权限、自主程度、测试/交接规范 |
| TASKS.md | 分阶段依赖、具体任务、证据与验收状态、真实 vs 模拟 |
| docs/REQUIREMENTS.md | 原始诉求到编号需求、约束、边界场景、假设 |
| docs/RESEARCH.md | 检索到什么、真实竞品比较、采用/拒绝依据 |
| docs/ARCHITECTURE.md | 控制流、数据流、组件、状态机、部署和迁移 |
| docs/DECISIONS.md | 关键 ADR 和变更原因 |
| docs/TESTING_AND_OPERATIONS.md | 质量门槛、模拟/真实测试、异常与部署 |
| docs/COST_AND_LICENSE.md | 费用来源、许可证、隐性成本、默认防护 |
| docs/SOURCES.md | 官方来源、链接、查证日期和支持的结论 |
| docs/EXTENSIONS.md | 未来功能、接口文件、实施阶段、依赖与安全 |
| docs/RISKS.md | 严重程度、可能性、监测与缓解 |
| PROGRESS.md | 已确认完成/未完成/阻塞/测试 |
| HANDOFF.md | 新 Agent 从哪个文件、哪个测试、哪项任务开始 |

## 任务粒度

每个阶段写 Goal、Dependencies、Files/Changes、Steps、Verification、Definition of Done、Status。复杂 Agent 任务以最小可独立验收变更为单元；不要无意义地把每一个思考动作拆成 checkbox。

## 生成模式

- light：README/AGENTS/TASKS。
- standard：再加 REQUIREMENTS/RESEARCH/ARCHITECTURE/DECISIONS/TESTING/COST/SOURCES/PROGRESS/HANDOFF。
- full：再加 EXTENSIONS/RISKS，按复杂子系统需要增设文件夹。

**所有文件默认是草稿设计，不是已实现成果。** 代码不存在时必须标记 `NOT_IMPLEMENTED`，已有示例命令区别 `PROPOSED` 与 `VERIFIED`。避免同一主张在多个文件间重复上千字；只引用主文档。
