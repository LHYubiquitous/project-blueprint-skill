from __future__ import annotations

from contextlib import redirect_stderr
import io
import tempfile
import unittest
from pathlib import Path

from scripts import audit_publication


class PublicationAuditTests(unittest.TestCase):
    def test_clean_tree_has_no_findings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "Public documentation with relative paths only.\n",
                encoding="utf-8",
            )

            self.assertEqual(audit_publication.scan(root), [])

    def test_detects_private_identifiers_secrets_and_signed_urls(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            email = "alex" + "@example.com"
            home_path = "/Users/" + "alex/private-project"
            private_key = "-----BEGIN " + "PRIVATE KEY-----"
            github_token = "ghp_" + ("a" * 36)
            signed_url = "https://files.example.invalid/object?" + "X-Amz-Signature=" + ("b" * 64)
            (root / "notes.md").write_text(
                "\n".join((email, home_path, private_key, github_token, signed_url)),
                encoding="utf-8",
            )

            findings = audit_publication.scan(root)
            kinds = {finding.kind for finding in findings}

            self.assertTrue(
                {"email", "absolute-home-path", "private-key", "credential", "signed-url"}.issubset(kinds)
            )
            rendered = "\n".join(finding.excerpt for finding in findings)
            self.assertNotIn(github_token, rendered)
            self.assertNotIn(signed_url, rendered)

    def test_skips_vcs_directories_and_symlinks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            hidden = root / ".git"
            hidden.mkdir()
            hidden_secret = "sk-" + ("c" * 32)
            (hidden / "config").write_text(hidden_secret, encoding="utf-8")

            outside = root.parent / f"{root.name}-outside.txt"
            outside.write_text("person" + "@example.com", encoding="utf-8")
            self.addCleanup(outside.unlink, missing_ok=True)
            (root / "outside-link.txt").symlink_to(outside)

            self.assertEqual(audit_publication.scan(root), [])

    def test_flags_sensitive_filenames(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".env").write_text("DEBUG=false\n", encoding="utf-8")

            findings = audit_publication.scan(root)

            self.assertEqual([finding.kind for finding in findings], ["sensitive-filename"])

    def test_findings_do_not_echo_surrounding_line_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            private_context = "customer-alpha " + "person" + "@example.com" + " internal-project"
            (root / "notes.md").write_text(private_context, encoding="utf-8")

            findings = audit_publication.scan(root)

            self.assertEqual([finding.excerpt for finding in findings], ["[REDACTED]"])

    def test_invalid_root_returns_cli_usage_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing"

            with redirect_stderr(io.StringIO()):
                self.assertEqual(audit_publication.main([str(missing)]), 2)


if __name__ == "__main__":
    unittest.main()
