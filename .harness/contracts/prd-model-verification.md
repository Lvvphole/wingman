# PRD model verification increment

This increment adds a bounded abstract model. It does not establish product implementation conformance, release acceptance, or merge authority.

## Task envelope

```json
{
  "task_domains": ["PRD_MODEL_VERIFICATION"],
  "source_sections": ["PRD 7", "PRD 10", "PRD 11", "PRD 13", "PRD 17", "PRD 20", "PRD 35"],
  "workpiece_paths": ["verification/prd_model.py", "verification/test_prd_model.py"],
  "selected_evidence_ids": ["DESIGN_AUTHORITY", "PRODUCT_PRD"],
  "authorized_candidate_paths": [
    "verification/prd_model.py",
    "verification/test_prd_model.py",
    ".harness/task-envelope.schema.json",
    ".harness/work-unit-lifecycle.schema.json",
    ".governance/source-registry.md",
    ".harness/contracts/prd-model-verification.md"
  ],
  "approvals": ["OWNER_AUTHORIZED_VERIFICATION_COMPLETION"],
  "source_binding": {
    "commit": "7919a77437c9ff6f80e606649582627f461a6674",
    "staged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "unstaged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "untracked_manifest_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "dirty_submodule_manifest_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "excluded_plan_path": ".harness/contracts/prd-model-verification.md"
  }
}
```

## Acceptance boundary

The protected-base verifier can admit only the exact file set and hashes in its reviewed contract. Candidate code remains untrusted data in the privileged workflow. A passing result has `merge_authority: false`.
