# {{PROJECT_NAME}} — Agent Instructions

> Status: DESIGN DRAFT. This document governs implementation after approval.

## Read first

1. `README.md`
2. `docs/REQUIREMENTS.md` (if present)
3. `docs/RESEARCH.md` (if present)
4. `docs/ARCHITECTURE.md` (if present)
5. `TASKS.md`
6. `PROGRESS.md` and `HANDOFF.md` (if present)

## Non-negotiables

- Use existing, evaluated open-source/free tools before implementing duplicate functionality.
- Requirements and thresholds are editable unless the user explicitly fixes them; do not hardcode illustrative examples.
- No credentials in code/logs/docs; no paid APIs, purchases, publication, destructive system changes, or new high-privilege installs without explicit approval.
- Read only the files and directories in the task's stated scope. Do not crawl home, parent, sibling, cloud-sync, credential, or unrelated repository paths merely because they are accessible.
- Use repository-relative paths and non-identifying aliases in durable artifacts. Redact personal contacts, account/device identifiers, internal URLs, signed URLs, and private source or logs that are not required for the deliverable.
- Generalize confidential details before web search. Local file creation does not authorize uploading, pushing, or public publication.
- Follow official docs for version-sensitive APIs; distinguish `verified`, `inferred`, and `proposed`.
- A mock passing is not proof that real account/OAuth/integration works.
- Maintain checkpoints, logs, tests, clear failure outcomes and resumable task state.
- Avoid unrelated refactors and infinite modifications; verify each milestone.

## Implementation workflow

1. Inspect environment/repo, never overwrite existing work without permission.
2. Confirm key external interfaces and dependencies.
3. Implement a small testable vertical slice; run tests and document output.
4. Update `TASKS.md`, `PROGRESS.md`, `HANDOFF.md` after each milestone.
5. Report blocked human actions and continue independent tasks.

## Scope and authorization

[项目专项安全要求、允许读取/写入的工作空间、外部服务和发布范围 — 由规划阶段补充；不要记录秘密值]
