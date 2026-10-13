# Project Blueprint Skill

[English](README.md)

`project-blueprint` 能将零散想法、对话内容或既有项目转化为有研究依据、可直接实施的项目蓝图。它会先检索可复用的开源方案，再生成可追溯的需求、架构、任务、风险、成本与交接文档。

本技能以简体中文为主，也可使用用户的语言回应。

## 包含内容

- 以开源优先的调研流程，以及“采用 / 组合 / 自建”的方案比较；
- 带优先级、来源和验收标准的需求定义；
- 轻量、标准与完整三种文档模式；
- 不依赖第三方包的 Python 脚手架与结构校验；
- 面向本地上下文和外部研究的最小化隐私规则；
- 用于发现潜在密钥和个人标识符的离线发布审计。

除非另有明确授权，本技能不会自动安装第三方项目、创建账号、产生费用、发布内容，或实现完整应用。

## 安装

请将本仓库克隆到名为 `project-blueprint` 的目录；该目录名必须与技能 frontmatter 保持一致：

```bash
git clone https://github.com/LHYubiquitous/project-blueprint-skill.git ~/.codex/skills/project-blueprint
```

安装后的目录为：

```text
~/.codex/skills/project-blueprint/
```

其他兼容 Agent Skills 的运行时也可能从以下位置发现个人技能：

```text
~/.agents/skills/project-blueprint/
```

对于这些运行时，请将仓库克隆或复制到上述准确路径，而不是接受 Git 默认的 `project-blueprint-skill` 目录名。

运行中的 agent 可能需要开启新一轮对话或新会话才能发现技能。可以显式调用 `$project-blueprint`，也可以在符合的项目规划请求中让 Codex 自动选择它。

## 校验

脚本仅依赖 Python 3.9+ 标准库：

```bash
python3 -B scripts/validate_skill.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/audit_publication.py .
```

创建一份项目文档草稿：

```bash
python3 -B scripts/scaffold.py --name "Example" --output ./example --mode standard --dry-run
python3 -B scripts/scaffold.py --name "Example" --output ./example --mode standard
python3 -B scripts/validate_project.py ./example
python3 -B scripts/audit_publication.py ./example
```

该扫描器采用保守策略，无法识别所有机密或第三方材料的形式。因此，干净的扫描结果只能补充人工审查，不能替代人工审查。

## 隐私模型

技能默认只使用当前对话、用户提供的附件和已明确限定范围的项目目录。它要求 agent 不扫描无关用户目录、不在产物中包含凭据或个人标识符，也不在网页搜索查询中发送保密细节。将内容公开发布仍须另行授权。

完整规则见 [PRIVACY_AND_PUBLICATION.md](references/PRIVACY_AND_PUBLICATION.md)。

## 许可证

MIT。调研参考图中提到的第三方项目仅为外部候选项，并非随本技能捆绑的依赖，也不代表对其背书。
