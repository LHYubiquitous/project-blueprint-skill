# Architecture & Decision Guidelines

## 路线比较

比较至少三种方向（如果只有两种合理，则说明原因）：Adopt、Compose、Build。对每个方向写：能力覆盖、迁移与锁定、部署成本、维护责任、风险、进入 MVP 的工作量、为何拒绝/选择。

## 设计切分

- **Domain / Specialist Agent**：特定领域的计划、Skills、质量门槛。
- **Orchestrator**：任务队列、状态、资源选择、暂停/恢复。
- **Adapter / Provider**：外部模型、工具或供应商接口。
- **Persistence**：事件、任务、产物、断点；不得只依赖对话历史。
- **Observer**：运行状态和外部告警；整机断电要求故障域外监控。
- **Security / Billing**：授权路径、凭据、工具权限、费用上限。

不是所有项目都需要全部组件。避免空接口泛滥。跨设备/复杂异步系统优先设计状态机、lease、幂等和单主协调。

## ADR 模板

```text
ADR-001: [选择题]
Status: accepted / proposed / superseded
Context: 哪个真实需求与约束引起此决策
Options: A / B / C（有来源）
Decision: ...
Why: ...
Trade-offs: ...
Revisit when: ...
```

## 非编码类项目

对于科研综述/知识库/数据调研等，同样要求来源、质量 Gate、增量产物、可恢复状态、阶段验收；代码层架构应按实际需要简化，避免硬套后端服务结构。
