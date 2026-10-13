# Project Blueprint Skill — Local Installation

This is a portable Agent Skills directory. It needs no additional LLM API keys or paid tools. Its project scaffold uses Python 3.9+ **standard library only**. Research quality depends on your agent's actual search/browser permissions.

## Codex user-level install

Target: `~/.codex/skills/project-blueprint/` on Windows or macOS. Keep the directory name `project-blueprint` so it matches the skill's frontmatter. A running Codex session may need a new turn or session to discover the newly added skill.

```bash
git clone https://github.com/LHYubiquitous/project-blueprint-skill.git ~/.codex/skills/project-blueprint
```

Some Agent Skills-compatible runtimes discover user skills from `~/.agents/skills/project-blueprint/` instead. Verify the documented skill path and allowlist for the runtime you use.

Alternative manual installation:

```text
~/.codex/skills/project-blueprint/
  SKILL.md
  references/
  scripts/
  assets/templates/
```

OpenClaw may also install local skill directories using its current `openclaw skills install <local-path> --global`; see official docs for your installed version. You do **not** need OpenClaw merely to use this Skill in Codex.

## Verify the local copy

From the installed skill directory:

```bash
python3 -B scripts/validate_skill.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/audit_publication.py .
```

The audit is offline and does not upload scanned content. Review its results manually before publishing generated documents.

## Invocation examples

- `$project-blueprint 请把这些零散需求变成一个可交给 Codex 实施的项目，先找质量高的免费开源方案。`
- `Use project-blueprint to compare existing open-source alternatives before designing a cross-platform agent workflow.`
- `先只做 research-only，列项目候选并比较维护/许可/成本，不创建文件。`

To scaffold a draft project:

```bash
python /path/to/project-blueprint/scripts/scaffold.py --name "Example" --output ./example --mode full
python /path/to/project-blueprint/scripts/validate_project.py ./example
```

A generated skeleton is intentionally **not** an implemented program or verified research output. The skill instructs the agent to replace the draft content with sourced, project-specific decisions.

Official sources:
- https://agentskills.io/specification
- https://docs.openclaw.ai/tools/skills
- https://github.com/github/spec-kit
- https://github.com/Fission-AI/OpenSpec
- https://github.com/obra/superpowers
