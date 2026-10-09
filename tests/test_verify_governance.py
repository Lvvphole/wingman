from __future__ import annotations

import importlib.util
import io
import json
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "verify-governance.py"
MODULE_SPEC = importlib.util.spec_from_file_location("wingman_verify_governance", MODULE_PATH)
if MODULE_SPEC is None or MODULE_SPEC.loader is None:
    raise RuntimeError(f"Cannot load verifier from {MODULE_PATH}")
governance = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(governance)


def ready_work_unit() -> dict[str, object]:
    head = "a" * 40
    return {
        "work_unit_id": "INC-1",
        "unit_kind": "INC",
        "task_contract": ".harness/contracts/example.md",
        "worktree_path": "/worktrees/inc-1",
        "branch": "inc-1",
        "unique_worktree": True,
        "base_sha": "b" * 40,
        "state": "CI_GREEN",
        "pr_number": 1,
        "pr_head_sha": head,
        "ci_context": "PR Verification",
        "ci_result": "PASS",
        "ci_head_sha": head,
        "codex_review_state": "NOT_STARTED",
        "evidence_reference": "ci://pr/1/head",
    }


def valid_envelope() -> dict[str, object]:
    return {
        "task_domains": ["GOVERNANCE_BOOTSTRAP"],
        "source_sections": ["authority"],
        "workpiece_paths": ["README.md"],
        "selected_evidence_ids": ["EVIDENCE-1"],
        "authorized_candidate_paths": [".governance/"],
        "approvals": ["USER_APPROVED_PLAN_EB45E338"],
        "source_binding": {"commit": "a" * 40},
    }


class RouteTests(unittest.TestCase):
    def test_unique_route_is_admitted(self) -> None:
        self.assertEqual(
            governance.route("GOVERNANCE_BOOTSTRAP", ["GOVERNANCE_BOOTSTRAP"]),
            "GOVERNANCE_BOOTSTRAP",
        )

    def test_zero_and_multiple_matches_fail_closed(self) -> None:
        zero = governance.route(None, ["GOVERNANCE_BOOTSTRAP"])
        multiple = governance.route(
            "GOVERNANCE_BOOTSTRAP",
            ["GOVERNANCE_BOOTSTRAP", "GOVERNANCE_BOOTSTRAP"],
        )
        self.assertEqual(zero["reason_code"], "ROUTE_ZERO_MATCH")
        self.assertEqual(multiple["reason_code"], "ROUTE_MULTI_MATCH")


class ApprovalTests(unittest.TestCase):
    def test_only_owner_exact_single_bounded_approval_executes(self) -> None:
        accepted = governance.owner_approval_executes(" Approved ", True, ("publish PR",))
        rejected = [
            governance.owner_approval_executes("Approved", False, ("publish PR",)),
            governance.owner_approval_executes("Approved", True, ()),
            governance.owner_approval_executes("Approved later", True, ("publish PR",)),
            governance.owner_approval_executes(
                "Approved", True, ("publish PR",), proposal_count=2
            ),
        ]
        self.assertTrue(accepted)
        self.assertEqual(rejected, [False, False, False, False])


class ReviewAdmissionTests(unittest.TestCase):
    def test_exact_head_green_work_unit_is_admitted(self) -> None:
        self.assertEqual(governance.codex_review_admission(ready_work_unit()), "CODEX_REVIEW")

    def test_invalid_review_inputs_fail_with_specific_reasons(self) -> None:
        cases = {
            "unique_worktree": (False, "WORKTREE_NOT_ISOLATED"),
            "pr_number": (None, "PR_MISSING"),
            "ci_context": ("build", "PR_VERIFICATION_CONTEXT"),
            "ci_result": ("FAIL", "PR_VERIFICATION_NOT_GREEN"),
            "ci_head_sha": ("c" * 40, "CI_NOT_EXACT_HEAD"),
            "state": ("CI_PENDING", "CODEX_REVIEW_ORDER"),
            "evidence_reference": ("", "CI_EVIDENCE_MISSING"),
        }
        for field, (value, expected_reason) in cases.items():
            with self.subTest(field=field):
                outcome = governance.codex_review_admission(
                    {**ready_work_unit(), field: value}
                )
                self.assertEqual(outcome["status"], "BLOCKED")
                self.assertEqual(outcome["reason_code"], expected_reason)


class ContractValidationTests(unittest.TestCase):
    def test_envelope_requires_exact_fields_domain_and_approval(self) -> None:
        self.assertIsNone(governance.validate_envelope(valid_envelope()))

        missing = valid_envelope()
        missing.pop("source_binding")
        self.assertEqual(
            governance.validate_envelope(missing)["reason_code"], "ENVELOPE_INVALID"
        )

        wrong_domain = {**valid_envelope(), "task_domains": ["INFERRED"]}
        self.assertEqual(
            governance.validate_envelope(wrong_domain)["reason_code"],
            "DOMAIN_NOT_CALLER_SUPPLIED",
        )

        unauthorized = {**valid_envelope(), "approvals": []}
        self.assertEqual(
            governance.validate_envelope(unauthorized)["reason_code"],
            "AUTHORIZATION_INVALID",
        )

    def test_mutation_scope_rejects_unlisted_paths(self) -> None:
        allowed = (".governance/", ".harness/")
        self.assertIsNone(governance.deny_path(".governance/authority.md", allowed))
        denied = governance.deny_path("application/route.ts", allowed)
        self.assertEqual(denied["reason_code"], "MUTATION_SCOPE")

    def test_required_predicate_raises_named_failure(self) -> None:
        with self.assertRaisesRegex(governance.VerificationFailure, "EXACT_PREDICATE"):
            governance.require(False, "EXACT_PREDICATE")


class CommandResultTests(unittest.TestCase):
    def test_main_returns_failure_record_when_verification_fails(self) -> None:
        output = io.StringIO()
        with (
            patch.object(
                governance,
                "verify",
                side_effect=governance.VerificationFailure("TEST_FAILURE"),
            ),
            redirect_stdout(output),
        ):
            exit_code = governance.main()

        self.assertEqual(exit_code, 1)
        self.assertEqual(
            json.loads(output.getvalue()),
            {"producer_result": "FAIL", "error": "TEST_FAILURE"},
        )


if __name__ == "__main__":
    unittest.main()
