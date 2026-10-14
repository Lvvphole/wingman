from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


PATH = Path(__file__).with_name("lint_candidate.py")
SPEC = importlib.util.spec_from_file_location("lint_candidate", PATH)
assert SPEC and SPEC.loader
LINT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LINT)


class CandidateLintTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.root, check=True)
        (self.root / "README.md").write_text("# Base\n", encoding="utf-8")
        self.commit("base")
        self.base = self.sha()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def commit(self, message: str) -> None:
        subprocess.run(["git", "add", "-A"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", message], cwd=self.root, check=True)

    def sha(self) -> str:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=self.root, text=True).strip()

    def lint_after(self, path: str, data: bytes) -> list[str]:
        (self.root / path).write_bytes(data)
        self.commit("candidate")
        return LINT.lint(self.root, self.base, self.sha())

    def test_clean_text_passes(self) -> None:
        self.assertEqual([], self.lint_after("file.json", b'{"ok": true}\n'))

    def test_invalid_json_fails(self) -> None:
        self.assertTrue(any(error.startswith("SYNTAX:file.json") for error in self.lint_after("file.json", b"{bad}\n")))

    def test_python_syntax_fails_without_execution(self) -> None:
        self.assertTrue(any(error.startswith("SYNTAX:file.py") for error in self.lint_after("file.py", b"if:\n")))

    def test_missing_final_newline_fails(self) -> None:
        self.assertIn("FINAL_NEWLINE:file.md", self.lint_after("file.md", b"# Missing"))


if __name__ == "__main__":
    unittest.main()
