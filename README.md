# Project Blueprint Skill

[中文文档](README.zh-CN.md)

`project-blueprint` turns rough ideas, conversations, or an existing project into a research-backed, implementation-ready blueprint. It searches for reusable open-source solutions before recommending new code, then produces traceable requirements, architecture, tasks, risks, costs, and handoff documentation.

The skill is written primarily in Simplified Chinese and can respond in the user's language.

## What it includes

- Open-source-first discovery and adopt/compose/build comparisons
- Requirements with priorities, provenance, and acceptance criteria
- Lightweight, standard, and full documentation modes
- Dependency-free Python scaffolding and structural validation
- Privacy-minimizing rules for local context and external research
- An offline publication audit for likely secrets and personal identifiers

It does not automatically install third-party projects, create accounts, spend money, publish content, or implement an entire application unless the user separately authorizes that work.

## Install

Clone this repository into a directory named `project-blueprint`, which must match the skill frontmatter:

```bash
git clone https://github.com/LHYubiquitous/project-blueprint-skill.git ~/.codex/skills/project-blueprint
```

The resulting location is:

```text
~/.codex/skills/project-blueprint/
```

Other Agent Skills-compatible runtimes may instead discover personal skills from:

```text
~/.agents/skills/project-blueprint/
```

For those runtimes, clone or copy the repository to that exact destination rather than accepting Git's default `project-blueprint-skill` directory name.

A running agent may need a new turn or session to discover the skill. Invoke it explicitly with `$project-blueprint`, or let Codex select it for matching planning requests.

## Validate

The scripts use only the Python 3.9+ standard library:

```bash
python3 -B scripts/validate_skill.py
python3 -B -m unittest discover -s tests -v
python3 -B scripts/audit_publication.py .
```

To create a draft project documentation set:

```bash
python3 -B scripts/scaffold.py --name "Example" --output ./example --mode standard --dry-run
python3 -B scripts/scaffold.py --name "Example" --output ./example --mode standard
python3 -B scripts/validate_project.py ./example
python3 -B scripts/audit_publication.py ./example
```

The scanner is deliberately conservative and cannot recognize every form of confidential or third-party material. A clean result supplements rather than replaces manual review.

## Privacy model

The skill defaults to the current conversation, user-provided attachments, and the explicitly scoped project directory. It instructs agents not to crawl unrelated user directories, include credentials or personal identifiers in artifacts, or send confidential details in web-search queries. Public publication remains a separately authorized action.

See `references/PRIVACY_AND_PUBLICATION.md` for the complete policy.

## License

MIT. Third-party projects named in the research reference map are external candidates, not bundled dependencies or endorsed components.
