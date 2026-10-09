#!/usr/bin/env python3
"""Base-controlled verifier. Candidate files are data and are never executed."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


class Failure(Exception):
    pass


def require(value: bool, message: str) -> None:
    if not value:
        raise Failure(message)


def safe_bytes(root: Path, relative: str) -> bytes:
    path = root / relative
    require(not path.is_symlink(), f"SYMLINK:{relative}")
    resolved = path.resolve(strict=True)
    require(resolved.is_relative_to(root), f"PATH_ESCAPE:{relative}")
    return resolved.read_bytes()


def digest(root: Path, relative: str) -> str:
    return hashlib.sha256(safe_bytes(root, relative)).hexdigest()


def load_json(root: Path, relative: str) -> dict[str, Any]:
    value = json.loads(safe_bytes(root, relative))
    require(isinstance(value, dict), f"JSON_OBJECT:{relative}")
    return value


def schema_validate(value: Any, schema: dict[str, Any], root: dict[str, Any], at: str = "$") -> None:
    if "$ref" in schema:
        node: Any = root
        for part in schema["$ref"].removeprefix("#/").split("/"):
            node = node[part]
        schema_validate(value, node, root, at)
        return
    kinds = schema.get("type")
    if kinds:
        kinds = [kinds] if isinstance(kinds, str) else kinds
        checks = {"object": lambda x: isinstance(x, dict), "array": lambda x: isinstance(x, list),
                  "string": lambda x: isinstance(x, str), "integer": lambda x: isinstance(x, int) and not isinstance(x, bool),
                  "boolean": lambda x: isinstance(x, bool), "null": lambda x: x is None}
        require(any(checks[kind](value) for kind in kinds), f"SCHEMA_TYPE:{at}")
    if "const" in schema:
        require(value == schema["const"], f"SCHEMA_CONST:{at}")
    if "enum" in schema:
        require(value in schema["enum"], f"SCHEMA_ENUM:{at}")
    if isinstance(value, dict):
        required = set(schema.get("required", []))
        require(required <= set(value), f"SCHEMA_REQUIRED:{at}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            require(set(value) <= set(properties), f"SCHEMA_EXTRA:{at}")
        for key, item in value.items():
            if key in properties:
                schema_validate(item, properties[key], root, f"{at}.{key}")
    if isinstance(value, list):
        require(len(value) >= schema.get("minItems", 0), f"SCHEMA_MIN_ITEMS:{at}")
        require(len(value) <= schema.get("maxItems", len(value)), f"SCHEMA_MAX_ITEMS:{at}")
        if schema.get("uniqueItems"):
            require(len({json.dumps(item, sort_keys=True) for item in value}) == len(value), f"SCHEMA_UNIQUE:{at}")
        for index, item in enumerate(value):
            schema_validate(item, schema.get("items", {}), root, f"{at}[{index}]")
    if isinstance(value, str):
        require(len(value) >= schema.get("minLength", 0), f"SCHEMA_MIN_LENGTH:{at}")
        if "pattern" in schema:
            require(re.search(schema["pattern"], value) is not None, f"SCHEMA_PATTERN:{at}")
    if isinstance(value, int) and not isinstance(value, bool) and "minimum" in schema:
        require(value >= schema["minimum"], f"SCHEMA_MINIMUM:{at}")


def task_envelope(root: Path, relative: str) -> dict[str, Any]:
    text = safe_bytes(root, relative).decode("utf-8")
    blocks = re.findall(r"## Task envelope\s*\n\s*```json\s*\n(.*?)\n```", text, re.S)
    require(len(blocks) == 1, "TASK_ENVELOPE_COUNT")
    value = json.loads(blocks[0])
    require(isinstance(value, dict), "TASK_ENVELOPE_OBJECT")
    return value


def source_rows(root: Path, relative: str) -> dict[str, tuple[str, str]]:
    rows: dict[str, tuple[str, str]] = {}
    for line in safe_bytes(root, relative).decode("utf-8").splitlines():
        cells = [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] not in {"Source ID", "---"} and not cells[0].startswith("---"):
            require(cells[0] not in rows, f"SOURCE_DUPLICATE:{cells[0]}")
            rows[cells[0]] = (cells[1], cells[2])
    return rows


def verify_sources(root: Path, registry_path: str, sources: list[dict[str, str]]) -> None:
    registry = source_rows(root, registry_path)
    for source in sources:
        require(source["id"] in registry, f"SOURCE_MISSING:{source['id']}")
        locator, binding = registry[source["id"]]
        require(locator == source["locator"] and source["binding"] in binding, f"SOURCE_BINDING:{source['id']}")
        if source["kind"] == "local":
            require(digest(root, locator) == source["binding"], f"SOURCE_BYTES:{source['id']}")


def git_output(root: Path, *args: str) -> str:
    result = subprocess.run(["/usr/bin/git", *args], cwd=root, text=True, capture_output=True, check=False)  # noqa: S603
    require(result.returncode == 0, f"GIT:{' '.join(args)}:{result.stderr.strip()}")
    return result.stdout


def changed_lines(root: Path, base: str, head: str) -> dict[str, int]:
    output = git_output(root, "diff", "--no-ext-diff", "--no-textconv", "--no-renames", "--numstat", base, head, "--")
    rows: dict[str, int] = {}
    for line in output.splitlines():
        added, deleted, path = line.split("\t", 2)
        require(added.isdigit() and deleted.isdigit(), f"BINARY_CHANGE:{path}")
        require(path not in rows, f"DUPLICATE_CHANGE:{path}")
        rows[path] = int(added) + int(deleted)
    names = set(git_output(root, "diff", "--no-ext-diff", "--no-renames", "--name-only", base, head, "--").splitlines())
    require(set(rows) == names, "CHANGE_SET_INCOMPLETE")
    return rows


def allowed(path: str, rules: list[str]) -> bool:
    return any(path.startswith(rule) if rule.endswith("/") else path == rule for rule in rules)


def verify_manifest(root: Path, measured: dict[str, int], manifest: dict[str, str]) -> None:
    require(set(measured) == set(manifest), "CONTENT_MANIFEST_COVERAGE")
    for path, expected in manifest.items():
        require(digest(root, path) == expected, f"CONTENT_BINDING:{path}")


def verify(candidate: Path, contract_path: Path, repository: str, head_repository: str, base: str, head: str, pr: int, branch: str) -> dict[str, Any]:
    candidate = candidate.resolve(strict=True)
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    require(contract.get("admission_enabled") is True, "ADMISSION_DISABLED")
    require(repository == contract["repository"], "REPOSITORY_IDENTITY")
    require(head_repository == repository, "HEAD_REPOSITORY_IDENTITY")
    require(branch == contract["work_unit"]["branch"], "BRANCH_IDENTITY")
    require(re.fullmatch(r"[0-9a-f]{40}", base) is not None and re.fullmatch(r"[0-9a-f]{40}", head) is not None, "SHA_FORMAT")
    require(git_output(candidate, "rev-parse", "HEAD").strip() == head, "HEAD_IDENTITY")
    authorized_paths = contract["authorized_candidate_paths"]
    exempt_files = contract["size_exempt_files"]

    envelope_schema = load_json(candidate, contract["task_envelope_schema"]["path"])
    require(digest(candidate, contract["task_envelope_schema"]["path"]) == contract["task_envelope_schema"]["sha256"], "ENVELOPE_SCHEMA_BINDING")
    envelope = task_envelope(candidate, contract["task_contract"])
    schema_validate(envelope, envelope_schema, envelope_schema)
    require(envelope["task_domains"] == [contract["route"]], "ROUTE_IDENTITY")
    require(set(envelope["approvals"]) >= set(contract["required_approvals"]), "APPROVAL_BINDING")
    require(envelope["authorized_candidate_paths"] == authorized_paths, "AUTHORIZED_PATHS_BINDING")
    require(envelope["source_binding"]["commit"] == contract["original_base_sha"], "ORIGINAL_BASE_BINDING")
    require(envelope["source_binding"]["excluded_plan_path"] in exempt_files, "EXEMPT_PATH_BINDING")

    verify_sources(candidate, contract["source_registry"], contract["fixed_sources"])

    deltas = changed_lines(candidate, base, head)
    for path, expected in exempt_files.items():
        require(path in deltas and digest(candidate, path) == expected, f"EXEMPT_FILE:{path}")
    measured = {path: count for path, count in deltas.items() if path not in exempt_files}
    require(all(allowed(path, authorized_paths) for path in measured), "MUTATION_SCOPE")
    assigned = {path for increment in contract["increments"] for path in increment}
    require(set(measured) <= assigned, "INCREMENT_MEMBERSHIP")
    verify_manifest(candidate, measured, contract["required_file_sha256"])
    counts = [sum(measured.get(path, 0) for path in increment) for increment in contract["increments"]]
    require(all(count <= contract["maximum_increment_lines"] for count in counts), "CHANGE_SIZE")

    lifecycle_schema = load_json(candidate, contract["lifecycle_schema"]["path"])
    require(digest(candidate, contract["lifecycle_schema"]["path"]) == contract["lifecycle_schema"]["sha256"], "LIFECYCLE_SCHEMA_BINDING")
    record = {**contract["work_unit"], "base_sha": base, "state": "CI_GREEN", "pr_number": pr,
              "pr_head_sha": head, "ci_context": "PR Verification", "ci_result": "PASS", "ci_head_sha": head,
              "codex_review_state": "NOT_STARTED", "evidence_reference": f"github://{repository}/pull/{pr}/{head}"}
    schema_validate(record, lifecycle_schema, lifecycle_schema)
    verifier_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {"result": "PASS", "merge_authority": False, "repository": repository, "base_sha": base,
            "head_sha": head, "pr_number": pr, "verifier_sha256": verifier_hash,
            "contract_sha256": hashlib.sha256(contract_path.read_bytes()).hexdigest(),
            "increment_line_counts": counts, "lifecycle_record": record}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--head-repository", required=True)
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--head-sha", required=True)
    parser.add_argument("--pr-number", type=int, required=True)
    parser.add_argument("--head-branch", required=True)
    args = parser.parse_args()
    try:
        result = verify(args.candidate, args.contract, args.repository, args.head_repository, args.base_sha, args.head_sha, args.pr_number, args.head_branch)
    except (Failure, OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(json.dumps({"result": "FAIL", "error": str(error)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
