# Source registry

Every routed source must resolve exactly once and match its declared binding. A missing, duplicate, stale, ambiguous, or mismatched source returns `BLOCKED/SOURCE_BINDING`.

| Source ID | Locator | Binding | Authority state |
| --- | --- | --- | --- |
| `PLAN-V0.2` | `plans/wingman-governance-router-plan-v0.2.md` | SHA-256 `eb45e3381ead580cf41db4e2cbf1d6667dfb55d869c1208620caf7db5fa9905f` | Bootstrap authority only |
| `DESIGN-V0.3` | Persistent sealed Design Authority Record | root `b4a1a02fc333b7c212186d7b07fb9d2b5536afaf2ae7434c20371ce097c3d10f` | Governing product authority |
| `PRD-V0.2` | Persistent PRD artifact | SHA-256 `a0283859f2b128c9ef0adcb25922901e135e0aeed64ba42900d8b83701f48be1` | Subordinate to sealed design |
| `READINESS-V0.1` | Persistent readiness register | SHA-256 `b2a97363962c7745e45e46c7e519b403d347a61f0cb55a6ed65aeba4cf9656b8` | Evidence; not authority |
| `ENGINEERING-53` | `.governance/engineering-rules.md` | source SHA-256 `deb95b212e0d3fae948e6cd0b9b932ede58cbaeef0170ccc8257b7a80a117793` | Governing after repository adoption |
| `GOOGLE-DESC` | `https://google.github.io/eng-practices/review/developer/cl-descriptions.html` | current external identity unresolved | Source only; not adopted |
| `GOOGLE-SMALL` | `https://google.github.io/eng-practices/review/developer/small-cls.html` | current external identity unresolved | Source only; not adopted |
| `GOOGLE-STYLE` | `https://google.github.io/styleguide/` | applicable language identities unresolved | Source only; not adopted |
| `GOOGLE-STANDARD` | `https://google.github.io/eng-practices/review/reviewer/standard.html` | current external identity unresolved | Source only; not adopted |
| `GOOGLE-LOOK` | `https://google.github.io/eng-practices/review/reviewer/looking-for.html` | current external identity unresolved | Source only; not adopted |

The user-supplied routing and portable-governance specifications are normalized and bound by `PLAN-V0.2`. Conversation labels record provenance but do not independently authorize mutation.

Google references become governing only after an adoption record binds their exact approved identities and applicable language guides. Until then, every `CR-*` adoption-dependent gate returns `BLOCKED/REVIEW_SOURCE_NOT_ADOPTED`.
