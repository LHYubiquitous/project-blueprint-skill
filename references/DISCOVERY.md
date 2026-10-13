# Open-source-first Discovery Playbook

## 检索策略：先复用，后自研

1. 用户已经安装、筛选过的工具与 Skills（检查当前可访问本地目录、配置、仓库）。
2. GitHub 同类成熟产品（`topic`、`awesome`、README、Release、Issues、LICENSE）。
3. Github 专业工作流，如 Spec Kit、OpenSpec、Superpowers、BMAD。
4. 一般框架/SDK/CLI，提供最小可运行实现。
5. 开源 Skills 与 Agent Skills 标准。
6. 官方 API 文档、价格、许可证和部署要求。
7. 开源替代缺口及未来扩展。

查询词要覆盖功能词、替代别名、平台、语言、free/open source/self-hosted、任务类型；至少有一次**找“完全现成解决方案”**的查询，不能只搜索特定库的 SDK。未联网时明确报告资料未经实时验证。

## 真实性分级

- **Verified**：官方仓库/官方文档直接支持，记录链接和查询日。
- **Tested**：在当前环境执行过命令/测试；记录测试输出。
- **Inferred**：由技术约束合理推断，注明原因。
- **Unverified**：尚未检查或无法打开来源。
- **Rejected**：因许可证、安全、维护或需求冲突不采用。

不得伪造 Stars、最新 release、成本、支持平台。动态指标要有日期。

## 候选比较矩阵

| Candidate | URL/License | 用途 | 功能覆盖 | 维护/成熟度 | Win/Mac | 完全免费? | 安全风险 | 接入工作量 | 结论 |
|---|---|---|---|---|---|---|---|---|---|

**评分建议（总 100）**：需求吻合 30、成熟/维护 15、实际接入成本 15、许可与长期可迁移 10、免费/总拥有成本 15、安全可靠 10、跨平台 5。任何因授权/安全产生的硬约束可直接 veto，不以 Star 数抵消。

候选按 `adopt`（用原项目）、`compose`（组合已有）、`build`（自研）分类。对推荐方案至少保留两种真实替代及拒绝理由。

## 避免安全与费用陷阱

- 许可证：区分 MIT/Apache/BSD、GPL/AGPL、source-available、商用限制；没有 LICENSE 不等于默认自由复用。
- 不自动执行在线安装一键脚本；先审核来源与权限。
- “本体免费”不等于 API/模型/搜索/云/存储/数据免费。
- 避免把 ChatGPT 订阅用量与 OpenAI API 用量混为一谈。
- 检查官方是否允许 OAuth / 第三方客户端 / 多账号流程。不要建议规避供应商限制。
- GitHub README 功能可能尚未发布；核实真实 Release、文档或样例。

## 研究产物

- `docs/RESEARCH.md`：发现、候选、调研结论、替代方案。
- `docs/SOURCES.md`：逐条可点击链接、获取日期、支撑哪个决定。
- `docs/DECISIONS.md`：选择与拒绝记录。
- `docs/COST_AND_LICENSE.md`：逐项的零成本、付费与未知成本。
