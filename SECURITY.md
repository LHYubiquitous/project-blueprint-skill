# Security Policy

## Reporting

Do not place live credentials, private repository content, signed URLs, personal information, or exploitable details in a public issue. Use a private GitHub Security Advisory when available, or contact the repository maintainer through a private channel published on their GitHub profile.

## If sensitive data was exposed

Revoke or rotate affected credentials first. Removing a value from the latest commit does not remove it from Git history, forks, caches, logs, or external services. Review the complete history and affected services before considering the incident resolved.

## Scope

Security reports may cover the bundled Python scripts, unsafe file traversal, secret leakage in generated artifacts, unintended external disclosure, or instructions that bypass user authorization.

The offline publication scanner is a defense-in-depth check, not a guarantee that a repository contains no confidential or third-party material.
