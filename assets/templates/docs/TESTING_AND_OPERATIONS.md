# {{PROJECT_NAME}} — Testing & Operations

## Verification tiers

1. Schema/static tests
2. Mock/simulation tests
3. Integration tests with actual tools
4. Real end-to-end tests with approved accounts/data

`MOCK_VERIFIED` is not equivalent to `INTEGRATION_VERIFIED`.
Use synthetic data by default. Evidence from real integrations must redact personal identifiers, account IDs, credentials, internal URLs, and private payloads.

## Requirements test matrix

| Requirement | Scenario | How to verify | Evidence | Status |
|---|---|---|---|---|
| REQ-001 | ... | ... | ... | NOT RUN |

## Install / run / stop / rollback

[实际命令；尚未实现的命令标 PROPOSED]

## Failure, recovery and monitoring

[异常类型 → 检查 → 恢复 → 手工介入；不可伪造成功；日志只保留必要的脱敏证据]

## Security and cost validation

[付费路径、凭据泄露、破坏性操作、越权访问]
