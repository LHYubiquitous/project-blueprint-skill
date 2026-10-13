# Open-source & Free-first Reference Map

以下是**候选来源**，不是运行时自动安装的依赖；每个新项目必须重新验证当前版本、维护、许可证和适配性（整理于 2026-10-13）。

| 生态 | 地址 | 可复用能力 | 何时优先考虑 |
|---|---|---|---|
| GitHub Spec Kit | https://github.com/github/spec-kit | 需求规格→计划→任务→实施、跨多个编码 Agent | 需要规范软件工程文档或 agentic SDLC 时 |
| OpenSpec | https://github.com/Fission-AI/OpenSpec | explore/propose/apply，变更规格和增量任务 | 已有项目演进、可审计变更时 |
| Superpowers | https://github.com/obra/superpowers | brainstorming, writing-plans, TDD, 交接 | 需要高质量需求梳理、任务分解时 |
| Anthropic Agent Skills | https://github.com/anthropics/skills | SKILL.md 格式与 Skill Creator 实践 | 开发便携能力包时；检查单个 Skill 许可证 |
| Agent Skills Spec | https://agentskills.io/specification | 标准 frontmatter 与可携带资源目录 | 本 Skill 及跨 Agent 安装兼容 |
| OpenClaw Skills | https://docs.openclaw.ai/tools/skills | 本地/全局 Skills 发现和安装 | 用户需要本地 Agent 平台集成时 |

其它候选由具体需求驱动：Research 可查 OpenAlex/Crossref/arXiv 官方资料，产品/代理可查 LangGraph 等，但不得把“可能有用”转成默认强依赖。保证**不安装即能阅读和使用本 Skill 的大部分方法**；只有实际项目需要才建议安装上述工具。

推荐流程：先判断 Spec Kit/OpenSpec/Superpowers 是否已经覆盖任务；覆盖则直接使用并在文档中说明；有缺口时才自定义项目蓝图。不要将其代码不加分析整合或复制进本 Skill。
