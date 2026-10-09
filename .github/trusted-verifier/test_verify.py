from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


PATH = Path(__file__).with_name("verify.py")
SPEC = importlib.util.spec_from_file_location("trusted_verify", PATH)
assert SPEC and SPEC.loader
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class TrustedVerifierTests(unittest.TestCase):
    def test_committed_envelope_not_synthetic_input(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            contract = root / "contract.md"
            contract.write_text("## Task envelope\n\n```json\n{bad}\n```\n", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                VERIFY.task_envelope(root, "contract.md")

    def test_source_binding_checks_actual_local_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.md").write_text("changed", encoding="utf-8")
            binding = "0" * 64
            (root / "registry.md").write_text(
                f"| `SOURCE` | `source.md` | SHA-256 `{binding}` | Governing |\n",
                encoding="utf-8",
            )
            source = [{"id": "SOURCE", "kind": "local", "locator": "source.md", "binding": binding}]
            with self.assertRaisesRegex(VERIFY.Failure, "SOURCE_BYTES"):
                VERIFY.verify_sources(root, "registry.md", source)

    def test_binary_change_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
            (root / "file").write_text("base", encoding="utf-8")
            subprocess.run(["git", "add", "file"], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "base"], cwd=root, check=True)
            base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            (root / "file").write_bytes(b"\x00changed")
            subprocess.run(["git", "commit", "-qam", "binary"], cwd=root, check=True)
            head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
            with self.assertRaisesRegex(VERIFY.Failure, "BINARY_CHANGE"):
                VERIFY.changed_lines(root, base, head)

    def test_complete_schema_rejects_invalid_types(self) -> None:
        schema = {"type": "object", "additionalProperties": False, "required": ["sha", "isolated", "pr"],
                  "properties": {"sha": {"type": "string", "pattern": "^[0-9a-f]{40}$"},
                                 "isolated": {"type": "boolean"}, "pr": {"type": "integer", "minimum": 1}}}
        for value in ({"sha": "a", "isolated": True, "pr": 1},
                      {"sha": "a" * 40, "isolated": "yes", "pr": 1},
                      {"sha": "a" * 40, "isolated": True, "pr": -1},
                      {"sha": "a" * 40, "isolated": True, "pr": 1, "extra": 1}):
            with self.subTest(value=value), self.assertRaises(VERIFY.Failure):
                VERIFY.schema_validate(value, schema, schema)


if __name__ == "__main__":
    unittest.main()
