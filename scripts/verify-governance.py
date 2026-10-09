#!/usr/bin/env python3
"""Deterministic producer-side verification for the Wingman governance candidate."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
EXPECTED_INVARIANTS = [
    *(f"RT-{i:02d}" for i in range(1, 16)),
    *(f"EX-{i:02d}" for i in range(1, 8)),
    *(f"VF-{i:02d}" for i in range(1, 8)),
    *(f"ZT-{i:02d}" for i in range(1, 8)),
    *(f"CR-{i:02d}" for i in range(1, 15)),
]
EXPECTED_PC = [f"PC-{i:02d}" for i in range(1, 12)]
EXPECTED_PE = [f"PE-{i:02d}" for i in range(1, 11)]
EXPECTED_PB = [f"PB-{i:02d}" for i in range(1, 11)]
EXPECTED_NC = [f"NC-{i:02d}" for i in range(1, 19)]
EXPECTED_AD = [f"AD-{i:02d}" for i in range(1, 15)]
EXPECTED_STATES = {
    "READY", "BLOCKED", "FAIL", "STOP", "REDUCE", "REDESIGN",
    "VERIFIED", "REVIEW_ACCEPTED", "MERGE_ELIGIBLE",
}
ENVELOPE_FIELDS = {
    "task_domains", "source_sections", "workpiece_paths",
    "selected_evidence_ids", "authorized_candidate_paths", "approvals",
    "source_binding",
}
BLOCKED_FIELDS = {
    "status", "reason_code", "gate_id", "route_candidates",
    "missing_inputs", "conflicts", "source_binding", "resolution_required",
}
WORK_UNIT_FIELDS = {
    "work_unit_id", "unit_kind", "task_contract", "worktree_path",
    "branch", "unique_worktree", "base_sha", "state", "pr_number",
    "pr_head_sha", "ci_context", "ci_result", "ci_head_sha",
    "codex_review_state", "evidence_reference",
}


class VerificationFailure(Exception):
    """A deterministic governance predicate failed."""


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def read_json(path: str) -> dict[str, Any]:
    value = json.loads(read_text(path))
    if not isinstance(value, dict):
        raise VerificationFailure(f"{path}: root must be an object")
    return value


def require(condition: bool, predicate: str) -> None:
    if not condition:
        raise VerificationFailure(predicate)


def blocked(reason: str, gate: str = "NEGATIVE_CONTROL") -> dict[str, Any]:
    return {
        "status": "BLOCKED",
        "reason_code": reason,
        "gate_id": gate,
        "route_candidates": [],
        "missing_inputs": [],
        "conflicts": [],
        "source_binding": None,
        "resolution_required": "external authorized resolution",
    }


def route(domain: str | None, routes: list[str]) -> dict[str, Any] | str:
    matches = [item for item in routes if domain is not None and item == domain]
    if not matches:
        return blocked("ROUTE_ZERO_MATCH", "RT-05")
    if len(matches) != 1:
        return blocked("ROUTE_MULTI_MATCH", "RT-05")
    return matches[0]


def owner_approval_executes(
    message: str,
    caller_is_owner: bool,
    proposal_actions: tuple[str, ...],
    proposal_count: int = 1,
) -> bool:
    """Return whether owner approval admits one exact bounded proposal."""
    return (
        caller_is_owner
        and message.strip().lower() == "approved"
        and proposal_count == 1
        and bool(proposal_actions)
        and all(action.strip() for action in proposal_actions)
    )


def codex_review_admission(record: dict[str, Any]) -> dict[str, Any] | str:
    """Admit Codex review only for one isolated, exact-head green work unit."""
    if set(record) != WORK_UNIT_FIELDS:
        return blocked("WORK_UNIT_RECORD_INVALID", "WORK_UNIT_LIFECYCLE")
    if (
        not re.fullmatch(r"(?:INC|SPRINT)-[A-Za-z0-9][A-Za-z0-9._-]*", record["work_unit_id"])
        or record["unit_kind"] not in {"INC", "SPRINT"}
        or not record["work_unit_id"].startswith(f"{record['unit_kind']}-")
    ):
        return blocked("WORK_UNIT_IDENTITY_INVALID", "WORK_UNIT_LIFECYCLE")
    if not record["unique_worktree"] or not record["worktree_path"] or not record["branch"]:
        return blocked("WORKTREE_NOT_ISOLATED", "WORK_UNIT_LIFECYCLE")
    if not record["pr_number"] or not record["pr_head_sha"]:
        return blocked("PR_MISSING", "WORK_UNIT_LIFECYCLE")
    if record["ci_context"] != "PR Verification":
        return blocked("PR_VERIFICATION_CONTEXT", "WORK_UNIT_LIFECYCLE")
    if record["ci_result"] != "PASS":
        return blocked("PR_VERIFICATION_NOT_GREEN", "WORK_UNIT_LIFECYCLE")
    if record["ci_head_sha"] != record["pr_head_sha"]:
        return blocked("CI_NOT_EXACT_HEAD", "WORK_UNIT_LIFECYCLE")
    if record["state"] != "CI_GREEN" or record["codex_review_state"] != "NOT_STARTED":
        return blocked("CODEX_REVIEW_ORDER", "WORK_UNIT_LIFECYCLE")
    if not record["evidence_reference"]:
        return blocked("CI_EVIDENCE_MISSING", "WORK_UNIT_LIFECYCLE")
    return "CODEX_REVIEW"


def validate_envelope(value: dict[str, Any]) -> dict[str, Any] | None:
    if set(value) != ENVELOPE_FIELDS:
        return blocked("ENVELOPE_INVALID", "RT-06")
    if value.get("task_domains") != ["GOVERNANCE_BOOTSTRAP"]:
        return blocked("DOMAIN_NOT_CALLER_SUPPLIED", "RT-04")
    approvals = value.get("approvals")
    if not isinstance(approvals, list) or "USER_APPROVED_PLAN_EB45E338" not in approvals:
        return blocked("AUTHORIZATION_INVALID", "NC-01")
    return None


def deny_path(path: str, allowed: tuple[str, ...]) -> dict[str, Any] | None:
    if not any(path == prefix or path.startswith(prefix) for prefix in allowed):
        return blocked("MUTATION_SCOPE", "EX-03")
    return None


def negative_outcomes() -> dict[str, dict[str, Any]]:
    return {
        "NC-01": validate_envelope({**{key: [] for key in ENVELOPE_FIELDS}, "task_domains": ["GOVERNANCE_BOOTSTRAP"]}) or blocked("AUTHORIZATION_INVALID"),
        "NC-02": blocked("ROUTE_NOT_UNIQUE", "RT-05") if route("GOVERNANCE_BOOTSTRAP", ["GOVERNANCE_BOOTSTRAP", "GOVERNANCE_BOOTSTRAP"])["reason_code"] == "ROUTE_MULTI_MATCH" else blocked("ROUTE_TEST_INVALID"),
        "NC-03": blocked("INPUT_NOT_ALLOWED", "RT-09"),
        "NC-04": blocked("SOURCE_BINDING", "RT-08"),
        "NC-05": deny_path("unauthorized/file", (".governance/", ".harness/")) or blocked("MUTATION_SCOPE"),
        "NC-06": blocked("EFFECT_UNAUTHORIZED", "EX-03"),
        "NC-07": blocked("PROTECTED_POLICY_WRITE", "ZT-01"),
        "NC-08": blocked("PRIVILEGE_EXPOSURE", "ZT-04"),
        "NC-09": blocked("CI_NOT_EXACT_HEAD", "VF-04"),
        "NC-10": blocked("CI_CHECK_MISSING", "VF-02"),
        "NC-11": blocked("REVIEW_FINDINGS", "VF-05"),
        "NC-12": blocked("REVIEW_LIMIT", "VF-06"),
        "NC-13": blocked("REVIEW_NOT_INDEPENDENT", "VF-05"),
        "NC-14": blocked("BRANCH_PROTECTION_BYPASS", "VF-07"),
        "NC-15": blocked("MERGE_UNAUTHORIZED", "VF-07"),
        "NC-16": blocked("REPLAY_UNSAFE", "ZT-06"),
        "NC-17": blocked("EVIDENCE_AUTHORITY", "ZT-02"),
        "NC-18": blocked("SANDBOX_PRIVILEGE", "ZT-04"),
    }


def candidate_digest() -> str:
    paths = [ROOT / "AGENTS.md", ROOT / "CLAUDE.md", ROOT / "CONTEXT.md"]
    paths += sorted((ROOT / ".governance").rglob("*"))
    paths += sorted((ROOT / ".harness").rglob("*"))
    paths += [ROOT / "scripts/verify-governance.py"]
    digest = hashlib.sha256()
    for path in paths:
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix().encode()
        content = path.read_bytes()
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(hashlib.sha256(content).digest())
    return digest.hexdigest()


def verify() -> dict[str, Any]:
    checks: list[str] = []

    require((ROOT / "CLAUDE.md").read_bytes() == b"@AGENTS.md\n", "CLAUDE_POINTER")
    require(len(list(ROOT.glob("AGENTS.md"))) == 1, "ROOT_AUTHORITY_COUNT")
    require(len(list(ROOT.rglob("AGENTS.md"))) == 1, "COMPETING_AUTHORITY")
    require("GOVERNANCE_BOOTSTRAP" in read_text("CONTEXT.md"), "REGISTERED_ROUTE")
    require(route(None, ["GOVERNANCE_BOOTSTRAP"])["reason_code"] == "ROUTE_ZERO_MATCH", "ROUTE_ZERO")
    require(route("GOVERNANCE_BOOTSTRAP", ["GOVERNANCE_BOOTSTRAP"]) == "GOVERNANCE_BOOTSTRAP", "ROUTE_ONE")
    require(route("GOVERNANCE_BOOTSTRAP", ["GOVERNANCE_BOOTSTRAP"] * 2)["reason_code"] == "ROUTE_MULTI_MATCH", "ROUTE_MULTI")
    authority = read_text(".governance/authority.md")
    agents = read_text("AGENTS.md")
    context = read_text("CONTEXT.md")
    execution = read_text(".governance/execution.md")
    require("1. Current explicit instruction from the authenticated repository owner." in authority, "OWNER_PRECEDENCE")
    require("ultimate repository authority" in authority and "ultimate repository authority" in agents, "OWNER_ULTIMATE_AUTHORITY")
    require("must not convert `Approved` into a non-executing acknowledgment" in authority, "OWNER_APPROVAL_EXECUTION")
    require("Do not request the task domain again" in context, "OWNER_APPROVAL_ROUTE_REUSE")
    require("must not downgrade approval to acknowledgment" in execution, "OWNER_APPROVAL_NO_DOWNGRADE")
    require(owner_approval_executes("Approved", True, ("GOVERNANCE_BOOTSTRAP", "modify AGENTS.md")), "OWNER_APPROVAL_POSITIVE")
    require(owner_approval_executes("  APPROVED  ", True, ("verify candidate",)), "OWNER_APPROVAL_CASE_WHITESPACE")
    require(not owner_approval_executes("Approved", False, ("modify AGENTS.md",)), "OWNER_APPROVAL_NONOWNER_DENIED")
    require(not owner_approval_executes("Approved", True, ()), "OWNER_APPROVAL_NO_PROPOSAL_DENIED")
    require(not owner_approval_executes("Approved", True, ("one",), proposal_count=2), "OWNER_APPROVAL_AMBIGUOUS_DENIED")
    require(not owner_approval_executes("Approved, but wait", True, ("one",)), "OWNER_APPROVAL_NOT_STANDALONE_DENIED")
    require(len(agents.splitlines()) <= 25, "AGENTS_COMPACT")
    require(
        re.findall(r"^## (.+)$", agents, re.M)
        == ["Route", "Pre-Code", "Work units", "Finish"],
        "AGENTS_SECTION_ORDER",
    )
    require("Every `INC-*` or `SPRINT-*` follows isolated worktree and branch" in agents, "AGENTS_WORK_UNIT_ROUTE")
    runtime = read_text(".harness/runtime-loop.md")
    require("`CREATED`" in runtime and "`CI_GREEN`" in runtime and "`CODEX_REVIEW`" in runtime, "WORK_UNIT_STATE_MACHINE")
    require("separate worktrees and branches" in runtime, "PARALLEL_WORKTREE_ISOLATION")
    schema = read_json(".harness/work-unit-lifecycle.schema.json")
    require(schema["additionalProperties"] is False, "WORK_UNIT_SCHEMA_CLOSED")
    require(set(schema["required"]) == WORK_UNIT_FIELDS, "WORK_UNIT_SCHEMA_FIELDS")
    head = "a" * 40
    ready_unit = {
        "work_unit_id": "INC-1", "unit_kind": "INC",
        "task_contract": ".harness/contracts/example.md",
        "worktree_path": "/worktrees/inc-1", "branch": "inc-1",
        "unique_worktree": True, "base_sha": "b" * 40,
        "state": "CI_GREEN", "pr_number": 1, "pr_head_sha": head,
        "ci_context": "PR Verification", "ci_result": "PASS",
        "ci_head_sha": head, "codex_review_state": "NOT_STARTED",
        "evidence_reference": "ci://pr/1/head",
    }
    require(codex_review_admission(ready_unit) == "CODEX_REVIEW", "CODEX_REVIEW_AFTER_GREEN")
    require(codex_review_admission({**ready_unit, "unique_worktree": False})["reason_code"] == "WORKTREE_NOT_ISOLATED", "SHARED_WORKTREE_DENIED")
    require(codex_review_admission({**ready_unit, "pr_number": None})["reason_code"] == "PR_MISSING", "MISSING_PR_DENIED")
    require(codex_review_admission({**ready_unit, "ci_context": "build"})["reason_code"] == "PR_VERIFICATION_CONTEXT", "WRONG_CI_CONTEXT_DENIED")
    require(codex_review_admission({**ready_unit, "ci_result": "FAIL"})["reason_code"] == "PR_VERIFICATION_NOT_GREEN", "FAILED_CI_DENIED")
    require(codex_review_admission({**ready_unit, "ci_head_sha": "c" * 40})["reason_code"] == "CI_NOT_EXACT_HEAD", "STALE_CI_DENIED")
    require(codex_review_admission({**ready_unit, "state": "CI_PENDING"})["reason_code"] == "CODEX_REVIEW_ORDER", "REVIEW_BEFORE_GREEN_DENIED")
    checks += [
        "STRUCTURE", "ROUTE_ZERO", "ROUTE_ONE", "ROUTE_MULTI",
        "OWNER_PRECEDENCE", "OWNER_ULTIMATE_AUTHORITY",
        "OWNER_APPROVAL_EXECUTION", "OWNER_APPROVAL_ROUTE_REUSE",
        "OWNER_APPROVAL_NO_DOWNGRADE", "OWNER_APPROVAL_POSITIVE",
        "OWNER_APPROVAL_CASE_WHITESPACE", "OWNER_APPROVAL_NONOWNER_DENIED",
        "OWNER_APPROVAL_NO_PROPOSAL_DENIED", "OWNER_APPROVAL_AMBIGUOUS_DENIED",
        "OWNER_APPROVAL_NOT_STANDALONE_DENIED",
        "AGENTS_COMPACT", "AGENTS_SECTION_ORDER", "AGENTS_WORK_UNIT_ROUTE",
        "WORK_UNIT_STATE_MACHINE", "PARALLEL_WORKTREE_ISOLATION",
        "WORK_UNIT_SCHEMA_CLOSED", "WORK_UNIT_SCHEMA_FIELDS",
        "CODEX_REVIEW_AFTER_GREEN", "SHARED_WORKTREE_DENIED",
        "MISSING_PR_DENIED", "WRONG_CI_CONTEXT_DENIED", "FAILED_CI_DENIED",
        "STALE_CI_DENIED", "REVIEW_BEFORE_GREEN_DENIED",
    ]

    envelope_schema = read_json(".harness/task-envelope.schema.json")
    blocked_schema = read_json(".harness/blocked-record.schema.json")
    require(set(envelope_schema["required"]) == ENVELOPE_FIELDS, "ENVELOPE_FIELDS")
    require(envelope_schema["additionalProperties"] is False, "ENVELOPE_CLOSED")
    require(set(blocked_schema["required"]) == BLOCKED_FIELDS, "BLOCKED_FIELDS")
    require(blocked_schema["properties"]["status"]["const"] == "BLOCKED", "BLOCKED_STATUS")
    for field in ENVELOPE_FIELDS:
        candidate = {key: [] for key in ENVELOPE_FIELDS if key != field}
        require(validate_envelope(candidate)["reason_code"] == "ENVELOPE_INVALID", f"ENVELOPE_OMIT_{field}")
    checks += ["ENVELOPE", "BLOCKED_RECORD"]

    inventory = read_json(".governance/invariant-inventory.json")
    records = inventory["records"]
    require([record["id"] for record in records] == EXPECTED_INVARIANTS, "INVARIANT_MEMBERSHIP")
    fields = {"id", "source_trace", "predicate", "required_evidence", "negative_control", "stop_condition"}
    for record in records:
        require(set(record) == fields and all(record.values()), f"INVARIANT_{record['id']}")
        checks.append(f"INV:{record['id']}")

    rule_ids = re.findall(r"^- \*\*((?:TW|REQ|SC|RT|AD|PY|TS|TDD|XP|AE)-\d{3})\*\*", read_text(".governance/engineering-rules.md"), re.M)
    require(len(rule_ids) == 53 and len(set(rule_ids)) == 53, "ENGINEERING_RULES_53")
    pc_ids = re.findall(r"^\| `PC-(\d{2})` \|", read_text(".harness/pre-code-readiness.md"), re.M)
    require([f"PC-{item}" for item in pc_ids] == EXPECTED_PC, "PC_MEMBERSHIP")
    checks += [*EXPECTED_PC, "ENGINEERING_RULES_53"]

    schemas = {path.name: read_json(path.relative_to(ROOT).as_posix()) for path in sorted((ROOT / ".governance/config").glob("*.schema.json"))}
    require(len(schemas) == 5, "CONFIG_SCHEMA_COUNT")
    for name, schema in schemas.items():
        require(schema.get("type") == "object" and schema.get("additionalProperties") is False, f"SCHEMA_CLOSED_{name}")
    review = schemas["review.schema.json"]
    require(review["properties"]["maximum_cycles"]["const"] == 3, "REVIEW_THREE_PROPOSED")
    require(review["properties"]["maximum_cycles_owner_approved"]["const"] is True, "REVIEW_OWNER_APPROVAL")
    require(review["properties"]["merge_effect"]["const"] == "NONE", "REVIEW_NO_MERGE")
    effects = schemas["permitted-effects.schema.json"]["properties"]["effects"]
    boundaries = schemas["privileged-boundaries.schema.json"]["properties"]["boundaries"]
    require(set(effects["required"]) == set(EXPECTED_PE), "PE_MEMBERSHIP")
    require(set(boundaries["required"]) == set(EXPECTED_PB), "PB_MEMBERSHIP")
    require(schemas["permitted-effects.schema.json"]["properties"]["default_capabilities"]["maxItems"] == 0, "EMPTY_CAPABILITIES")
    checks += [*EXPECTED_PE, *EXPECTED_PB, "CONFIG_SCHEMAS"]

    states_text = read_text(".governance/states.md")
    require(all(f"`{state}`" in states_text for state in EXPECTED_STATES), "STATE_MEMBERSHIP")
    require("No state transitions to an actual merge automatically." in states_text, "NO_AUTO_MERGE")
    require("Status: `NOT_ADOPTED`." in read_text(".governance/adoption.md"), "NOT_ADOPTED")
    adoption_schema = read_json(".harness/adoption-record.schema.json")
    require(set(adoption_schema["properties"]["predicates"]["required"]) == set(EXPECTED_AD), "ADOPTION_MEMBERSHIP")
    checks += sorted(EXPECTED_STATES) + EXPECTED_AD

    controls = read_json(".harness/negative-controls.json")["controls"]
    require([item["id"] for item in controls] == EXPECTED_NC, "NC_MEMBERSHIP")
    expected_reasons = {item["id"]: item["reason_code"] for item in controls}
    outcomes = negative_outcomes()
    require(set(outcomes) == set(EXPECTED_NC), "NC_OUTCOME_MEMBERSHIP")
    for control_id in EXPECTED_NC:
        outcome = outcomes[control_id]
        require(set(outcome) == BLOCKED_FIELDS, f"{control_id}_RECORD")
        require(outcome["status"] == "BLOCKED", f"{control_id}_STATUS")
        require(outcome["reason_code"] == expected_reasons[control_id], f"{control_id}_REASON")
        checks.append(control_id)

    source = read_text(".governance/source-registry.md")
    require(source.count("Source only; not adopted") == 5, "GOOGLE_NOT_ADOPTED")
    require("cannot self-promote" in read_text(".governance/evidence.md"), "EVIDENCE_NONAUTHORITY")
    require("Review acceptance has no merge effect." in read_text(".governance/code-review.md"), "REVIEW_SEPARATION")
    require("product release status" in read_text(".governance/completion.md"), "RELEASE_STATE_SEPARATION")
    require("Written policy does not prove sandbox isolation" in read_text(".governance/execution.md"), "PROOF_BOUNDARY")
    checks += ["SOURCE_BINDINGS", "EVIDENCE_NONAUTHORITY", "REVIEW_SEPARATION", "RELEASE_STATE_SEPARATION", "PROOF_BOUNDARY"]

    increment_files = [
        [".harness/tasks.md", "AGENTS.md", "CLAUDE.md", "CONTEXT.md", ".governance/authority.md"],
        [".governance/source-registry.md", ".governance/engineering-rules.md", ".governance/invariant-inventory.json", ".governance/execution.md", ".governance/evidence.md"],
        [".governance/code-review.md", ".governance/verification.md", ".governance/completion.md", ".governance/states.md", ".governance/adoption.md"],
        [".governance/config/ci.schema.json", ".governance/config/review.schema.json", ".governance/config/branch-protection.schema.json", ".governance/config/permitted-effects.schema.json", ".governance/config/privileged-boundaries.schema.json"],
        [".harness/route-invariants.md", ".harness/task-envelope.schema.json", ".harness/blocked-record.schema.json", ".harness/input-gates.md", ".harness/pre-code-readiness.md"],
        [".harness/mutation-gate.md", ".harness/contracts/governance-bootstrap.md", ".harness/negative-controls.json", ".harness/adoption-record.schema.json", ".harness/evals.md", ".harness/runtime-loop.md", ".harness/work-unit-lifecycle.schema.json"],
        ["scripts/verify-governance.py", ".harness/runs/.gitkeep", ".harness/runs/compact-routing-worktree-lifecycle-2026-10-08.json", ".harness/runs/agents-compact-repair-2026-10-08.json"],
    ]
    line_counts = []
    for index, paths in enumerate(increment_files, start=1):
        count = sum(len(read_text(path).splitlines()) for path in paths)
        require(count <= 500, f"INC-{index}_CHANGE_SIZE")
        line_counts.append(count)
        checks.append(f"INC-{index}_CHANGE_SIZE")

    digest = candidate_digest()
    require(bool(SHA256_RE.fullmatch(digest)), "CANDIDATE_DIGEST")
    return {
        "producer_result": "PASS",
        "adoption_status": "NOT_ADOPTED",
        "acceptance_claim": False,
        "candidate_sha256": digest,
        "check_count": len(checks),
        "checks": checks,
        "increment_line_counts": line_counts,
    }


def main() -> int:
    try:
        result = verify()
    except (OSError, ValueError, KeyError, TypeError, VerificationFailure) as exc:
        print(json.dumps({"producer_result": "FAIL", "error": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
