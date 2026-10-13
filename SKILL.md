---
name: project-blueprint
description: 从零散想法、自然语言需求或已有项目构思出发，优先检索并比较真实的高质量开源项目、Agent Skills、免费工具、官方文档与现成工作流，形成可验证的需求、技术选型、架构、任务清单、风险成本分析和可交给 Codex/其他智能体直接实施的项目文档。适用于“帮我把这个想法变成项目计划”“先找 GitHub 成熟方案再设计”“生成 README/AGENTS.md/TASKS.md 和项目脚手架”“重构一份既有项目方案”等；不直接替代实施阶段的编码工作。
license: MIT
compatibility: Works with Codex and other Agent Skills-compatible agents. Online research requires a browser/search tool; scaffold scripts use Python 3.9+ standard library.
metadata:
  author: Project Blueprint contributors
  version: "1.1.0"
  language: zh-CN
---

# Project Blueprint — 从零散需求到可落地项目规格

## 任务边界

输入可以是一句话、零散 idea、对话记录、参考截图、现有仓库或过往需求文档；无需用户先把需求整理好。输出是有证据的**项目蓝图与实施交接包**，而不是立即去开发所有功能。用户明确要求直接实现时，再进入实施阶段；否则不要擅自部署、安装复杂依赖、付费、注册账户或改动既有代码。

核心价值：**先检索并评估成熟方案 → 最大化复用 → 研究后确定架构 → 输出可执行规格和交接文件。** 不要一开始就以“我们自己从零造轮子”为默认方案。

## 隐私与发布边界

- 默认只读取当前对话、用户明确提供的附件，以及当前任务已指定的项目目录；不要遍历用户主目录、父目录、其它仓库、同步盘、凭据目录或无关配置。
- 不在文档、日志、测试证据或搜索词中保留凭据、个人联系方式、账号标识、设备名称、绝对主目录路径、私有 URL、签名 URL 或未公开源码。优先使用角色别名、仓库相对路径和脱敏摘要。
- 联网检索时先把私有项目名称、客户/组织名称、内部错误信息和独特代码片段抽象成通用技术词；只有用户明确授权将具体内容发送给该外部服务时才可使用原文。
- 生成本地文件不等于获准公开。上传、发布、创建公开仓库或向第三方服务提交内容前，必须获得针对该动作的明确授权并执行发布检查。
- 涉及私有输入、联网研究或公开发布时，读取并遵守 `references/PRIVACY_AND_PUBLICATION.md`。

## 工作流程（按顺序完成）

### 0. 扫描现有上下文与偏好

- 读取当前对话、用户提供的上传文件、已指定项目目录及其中相关的 README、AGENTS.md、TASKS.md；本地 Skills 只先读取名称/元数据，除非任务确实需要其正文。不得因为“可访问”就扩大范围。
- 尊重用户已经确认的设备、平台、成本、工作流、目录布局和设计选择；不要重复询问已知事实。
- 若正在为已有项目追加功能，先做 *gap analysis*，保护已有文件与约定；不要盲目重建项目。
- 给当前意图选择 `light`（简单工具）/ `standard`（一般项目）/ `full`（跨设备、多 Agent、长期工程）三个深度级别，必要时采用 `research-only`。

### 1. 将散乱想法转换成结构化需求

- 区分：原话与诉求、确认的约束、隐含目标、假设、开放问题、不在范围内的功能。
- 为需求编号 `REQ-001...`；逐条定义优先级（MUST/SHOULD/COULD）、验收标准及来源（user / research / assumption）。
- 避免把示例值变成硬编码要求；“比如 A/B 两账户”通常意味着 0..N 可扩展，除非用户明确限制。
- 对不确定细节先作可逆假设并标记；只有会改变大方向的关键事实才提出简短澄清。不要用长表单阻塞计划。
- 使用 `references/REQUIREMENTS.md` 中的完整指南。

### 2. **研究优先：先寻找高质量现成方案**

**必须在最终技术选型之前执行。** 有网络时实际检索；没有网络时标注“未实时核实”，不要虚构搜索结果、版本、价格、Star 数或项目维护状态。搜索查询遵守隐私最小化：不提交私有原文、凭据、内部 URL、真实账号或可识别个人/组织的细节。

检索顺序：
1. 同类**完整开源项目**（能否直接采用或 fork？）
2. 可组合的成熟**开源框架/SDK/CLI**
3. **Agent Skills / MCP 工具 / 插件 / 模板**（先盘点本地已装和用户筛选过的）
4. **官方文档**与示例仓库
5. 免费/自托管替代品、可选商业服务

优先官方 GitHub 原仓库、官方文档、官方发行与许可证；社区评论用于发现风险，不单独证明功能。候选至少覆盖 2–3 种实质不同的路径；大型项目最好比较 4–8 个候选。逐条验证真实能力、OS 兼容、更新维护、许可证、可扩展性、费用（软件/API/云/使用限额）、安全、锁定程度和安装成本。**Stars 只是信号，不是结论。**

必须生成比较矩阵和证据链接，明确标注 `verified`、`inferred`、`unverified`、`rejected`。保留有价值但未采用的方案。详见 `references/DISCOVERY.md` 与 `references/ECOSYSTEM.md`。

### 3. 选择“复用优先”的方案

评估三条路径：
- `adopt`：现成项目可直接使用，仅配置或少量胶水层。
- `compose`：组合多个现成工具，自己只做缺失的编排/适配层。
- `build`：关键需求没有合适现成实现，需要自研。

对复杂需求提出 2–3 条架构路线，解释取舍，推荐**能满足需求的最小长期可维护方案**。区分 MVP、后续扩展、明确不做事项。考虑安全、迁移、可恢复、审计、费用、可测试、用户现有环境。

**只能把真实、已验证的命令/接口称为“现成命令”；建议开发的命令/配置必须标注为 proposed。**

### 4. 设计项目结构、接口和运行流程

- 优先画清数据流、控制流、调用链、状态机；避免为了“完整架构图”制造空模块。
- 每个模块说明责任、边界、输入输出、依赖、错误处理、验证路径。
- 对跨模型、跨账户、跨系统项目，区分 orchestration、adapter、specialist workflow、tool、skill。
- 显式设计持久化、resume、断点检查、平台差异和长任务优雅停止（如适用）。
- **将未来扩展放入独立接口与文件索引**，至少留 `EXTENSIONS.md`、`TASKS.md` Future Backlog，而不是埋在聊天文本里。

详见 `references/DESIGN.md`。

### 5. 生成 Codex/Agent 可执行的文档包

按规模选择文档，不要求机械生成一大堆空文件：

- `light`: `README.md`, `TASKS.md`, `AGENTS.md`。
- `standard`: 以上 + `docs/REQUIREMENTS.md`, `docs/RESEARCH.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/TESTING_AND_OPERATIONS.md`, `docs/COST_AND_LICENSE.md`, `docs/SOURCES.md`, `PROGRESS.md`, `HANDOFF.md`。
- `full`: 再加 `docs/EXTENSIONS.md`, `docs/RISKS.md` 和必要的独立子系统设计文档。

文档要求：有具体决定、候选证据、可运行/可验证的实施路径；`TASKS.md` 每一阶段具有依赖、交付物、验收、Mock/Integration/Real 分级；`AGENTS.md` 规定 Agent 的文件优先级、默认自主权、付费及危险操作禁止、失败处理、checkpoint；`PROGRESS/HANDOFF` 为稳定可续接的信息源。默认产出必须适合在当前授权范围内共享：使用相对路径和非识别性别名，不复制秘密或与实现无关的个人信息。

模板位于 `assets/templates/`；详细验收清单见 `references/DELIVERABLES.md` 与 `references/QUALITY_GATES.md`。

### 6. 脚手架（仅在用户要求创建文件时）

可调用随包提供的 Python 标准库脚本，零第三方依赖：

```bash
python scripts/scaffold.py --name "My Project" --output ./my-project --mode full --dry-run
python scripts/scaffold.py --name "My Project" --output ./my-project --mode full
python scripts/validate_project.py ./my-project
python scripts/audit_publication.py ./my-project
```

- 已有文件**默认跳过，不覆盖**。脚手架仅创建占位模板，**不等于已完成项目设计**；随后必须把研究结论和真实需求写进去。
- 如现有项目含相关文档，优先更新而不是重复创建。
- 不自动安装下载到的 GitHub 代码，不执行来源不明的脚本。

### 7. 自审、交接、下一步

提交前核验：
- 用户每个 MUST 需求均能追踪到设计、计划与验收；示例值没有被误当成硬约束。
- 每个技术选型存在可复核来源、替代方案与拒绝理由；未核实内容透明标注。
- 无需付费的路线先行，付费/许可/部署/算力隐性成本明确列出。
- 准备共享或公开时，已人工检查隐私与知识产权，并运行 `scripts/audit_publication.py`；扫描通过不能替代人工审查。
- 文档之间的路径、文件名、章节编号、状态和技术名词一致。
- 实现状态诚实：`DESIGNED`, `SCAFFOLDED`, `MOCK_VERIFIED`, `INTEGRATION_VERIFIED`, `PRODUCTION_READY` 不可混淆。
- 存在可从新 Codex 会话直接执行的下一步任务，不需要重述整个聊天。

最后简要输出选型结论、生成文件路径、关键风险、仍待验证事项、第一条可以立即执行的任务。不要以“请等我后台生成”收尾。

## 反模式

- 没有检索就主观推荐陌生依赖，或者为用户已经有的功能重写一套。
- 推荐项目只因为 Star 多，忽略授权/维护/平台/真实 API。
- 一边声称“全部免费”，一边暗中使用按 Token 计费 API、搜索服务、云服务。
- 只贴一个大 Prompt 或图而没有可执行任务、证据、验收与交接。
- 自动创建大量仅含 TODO / `pass` 的文件并称为“实现完成”。
- 未经允许直接安装、运行任意第三方仓库，或修改用户的登录状态、凭据与收费设置。

## 按需读取的参考

- `references/REQUIREMENTS.md`：需求抽取、优先级、变更追踪。
- `references/DISCOVERY.md`：检索策略、候选评分、核实规则。
- `references/ECOSYSTEM.md`：值得优先评估的开源项目与技能来源。
- `references/DESIGN.md`：架构权衡、技术边界、ADR。
- `references/DELIVERABLES.md`：文档矩阵、模板、任务格式。
- `references/QUALITY_GATES.md`：自检、证据与非虚假完成标准。
- `references/PRIVACY_AND_PUBLICATION.md`：私有输入边界、外部查询脱敏和发布前检查。
