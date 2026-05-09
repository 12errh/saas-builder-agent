# ForgeFlow Agent Studio — Product Requirements Document (PRD)

## 0) Document Control
- **Version:** v2.0
- **Date:** May 9, 2026
- **Status:** Draft for stakeholder review
- **Owner:** Product + Platform Engineering
- **Related docs:** `TRD.md`, `DEV_PHASES.md`

---

## 1) Executive Summary
ForgeFlow Agent Studio is a desktop-native orchestration product that converts a user prompt (e.g., “build an X app”) into production-grade deliverables through a multi-agent workflow.

The product uses an explicit, reviewable lifecycle:
1. Requirement discovery via interactive checklist/panel flows.
2. Spec generation (PRD/TRD/DEV phases/Design brief).
3. Human review and approvals with optional auto-proceed mode.
4. Phase-by-phase implementation with mandatory test/review/security gates.
5. Production readiness validation (auth/legal/privacy/cookies/ops).
6. SEO and analytics setup/verification.
7. Final handover package and operational documentation.

---

## 2) Problem Statement
Current coding assistants are often:
- Prompt-reactive but not process-reliable.
- Weak at clarifying requirements before coding.
- Inconsistent at production hardening.
- Poor at lifecycle governance (specs, reviews, approvals, handover).

### Desired outcome
A “systematic builder” where the user can trust:
- requirements are clarified,
- specs are deep and actionable,
- implementation is iterative and auditable,
- and production risks are minimized before handoff.

---

## 3) Product Vision & Principles
### Vision
Enable builders to ship production-ready applications end-to-end with an orchestrated AI team rather than ad hoc prompt chains.

### Principles
1. **Spec-first engineering**: no coding before approved specs.
2. **Human control by default**: explicit approval gates and override paths.
3. **Defense-in-depth quality**: code review + security + production checklist.
4. **Provider and tool portability**: multi-provider LLM abstraction and MCP compatibility.
5. **Transparent reasoning artifacts**: every phase outputs audit-ready artifacts.
6. **Recovery-first operations**: resumable runs, retries, graceful degradation.

---

## 4) Goals, Non-Goals, and Success Criteria
### 4.1 Goals (MVP)
- Build a desktop-native orchestrator with modern minimal UI.
- Produce high-quality planning artifacts from user prompt + clarifications.
- Execute phased implementation with automated and agentic quality gates.
- Support NVIDIA and OpenRouter model providers.
- Include MCP and skill support as first-class capabilities.
- Provide production-readiness and SEO/analytics completion paths.

### 4.2 Non-Goals (MVP)
- Fully autonomous enterprise compliance certification.
- Full mobile-native app generation as first-class target.
- Multi-organization cloud tenancy management portal.

### 4.3 Quantitative Success Criteria (first 90 days)
- ≥ 80% of projects complete spec approval in ≤ 30 minutes.
- ≥ 70% of generated projects pass all phase gates without manual code rewrite > 20%.
- 0 unresolved critical vulnerabilities at handover.
- ≥ 90% successful resume from interrupted runs.
- User CSAT ≥ 4.2/5 for “spec clarity” and “handover quality”.

---

## 5) Personas and Primary Jobs-to-be-Done
### Persona A: Founder/Builder
- Wants to move from idea to deployable product quickly.
- Needs clear guidance when trade-offs are unclear.

### Persona B: Engineering Lead
- Needs reproducible architecture/specs and governance.
- Cares about test/security/compliance checklists.

### Persona C: Agency Delivery Team
- Needs repeatable process across many client projects.
- Values traceability and handover docs.

### Jobs-to-be-Done
- “When I describe a product, help me define and build it with production discipline.”
- “Ensure nothing critical is missed before launch.”
- “Make handover understandable for my team.”

---

## 6) End-to-End User Journey
### Stage 1 — Project Kickoff
- User enters prompt and target type (web/desktop/service).
- User selects “guided mode” or “fast mode”.

### Stage 2 — Clarification Wizard (mandatory)
- Interactive panel with checkboxes, radio groups, and short forms.
- Categories:
  - Product scope
  - Users/roles
  - Core workflows
  - Integrations
  - Data sensitivity
  - Auth model
  - Deployment preference
  - Tech preference (Supabase vs custom backend)

### Stage 3 — Spec Generation
- Spec agent produces:
  - Product requirements
  - Technical architecture and standards
  - Phased implementation plan
  - Design brief (`DESIGN.md`) with researched inspiration references

### Stage 4 — Review & Approval
- Review agent checks realism, missing edge cases, contradictory requirements.
- User can:
  - request edits,
  - approve and continue,
  - enable auto-continue for later gates.

### Stage 5 — Build Execution
- Coding agent executes phase N.
- Reviewer + vulnerability agents evaluate outputs.
- Fix loop continues until pass thresholds are met.

### Stage 6 — Production Readiness
- Production checklist across auth/legal/cookies/privacy/observability/performance.

### Stage 7 — SEO & Analytics
- SEO agent proposes keyword map, metadata, schema, page-level recommendations.
- Analytics integration checklist (GA4/Search Console) with executable steps or user guide.

### Stage 8 — Handover
- Final readme, architecture docs, deployment runbook, operations guide, backlog recommendations.

---

## 7) Functional Requirements (Detailed)
### FR-01 Intake & Prompt Normalization
- Parse freeform prompt into structured project intent.
- Detect project archetype: SaaS, e-commerce, internal tool, portfolio, API, desktop utility.
- Confidence score and uncertainty notes must be displayed.

### FR-02 Clarification Engine
- Dynamic questionnaire generated from archetype and risk profile.
- Supports:
  - checkbox groups,
  - single-select options,
  - priority ranking,
  - free-text clarifications.
- Must track unresolved ambiguities.

### FR-03 Spec Generator
- Outputs required files with stable templates and section scoring.
- Each section includes:
  - assumptions,
  - decisions,
  - alternatives considered,
  - known risks.

### FR-04 Design Research + Design.md
- Agent researches modern/minimal reference patterns.
- Produces:
  - design principles,
  - color/typography system,
  - spacing/component behavior,
  - accessibility constraints,
  - interaction patterns.

### FR-05 Review Agent
- Evaluates requirement completeness and real-world constraints.
- Flags:
  - unrealistic timelines,
  - incompatible stack choices,
  - compliance/security blind spots,
  - missing deployment assumptions.

### FR-06 Build Orchestration
- Build starts only after approval.
- Phase execution pipeline:
  - task generation,
  - coding,
  - tests,
  - review,
  - vuln scan,
  - remediation,
  - gate pass/fail.

### FR-07 Quality & Security Agents
- Code Review Agent: architecture conformance, complexity, maintainability.
- Vulnerability Agent: dependency CVEs, secrets leaks, unsafe patterns.
- Production Agent: launch checklist and go/no-go report.

### FR-08 Retry/Recovery
- Detect and classify failures:
  - transient network/model/tool failure,
  - deterministic code/test failure,
  - policy/tool-permission failure.
- Resume from latest checkpoint without data loss.

### FR-09 Provider Abstraction
- First-class support:
  - NVIDIA
  - OpenRouter
- Optional additional provider adapters via same interface.

### FR-10 MCP & Skills
- MCP registry UI + policy constraints.
- Skills discovery, versioning, enable/disable controls per project.

### FR-11 User Controls
- Mode toggles:
  - review-at-every-gate,
  - notify-only,
  - auto-continue with rollback threshold.
- “Build It” CTA only shown after minimum spec quality threshold.

### FR-12 Output/Handover Artifacts
- Required deliverables:
  - README
  - architecture diagram/spec
  - setup/deploy runbook
  - test report
  - security summary
  - operations checklist

---

## 8) Non-Functional Requirements
### Performance
- UI interactions: < 200ms perceived response for local actions.
- Queue long-running tasks asynchronously; progress updates every ≤ 2s.

### Reliability
- ≥ 99% successful local state persistence.
- Recovery checkpoint every critical transition.

### Security
- Secret masking in logs.
- Principle of least privilege for tools/MCP.
- Signed artifact trail for audit.

### Usability
- Progressive disclosure UI.
- First-run onboarding in ≤ 5 minutes.

### Maintainability
- Modular agents and provider adapters.
- Strong typing and schema-validated agent I/O.

---

## 9) UX & Interaction Requirements (Modern Minimal)
- Clean two-column layout:
  - left: lifecycle timeline,
  - right: active stage panel.
- Consistent iconography and typography scale.
- Inline checklists and expandable rationale cards.
- Phase gate cards with clear pass/fail reasons.
- “Human decision required” states visually distinct.

---

## 10) Policy, Legal, and Compliance Checklist
MVP must include checks for:
- Privacy policy presence.
- Terms of service presence.
- Cookie notice/consent behavior where applicable.
- Auth/session management baseline checks.
- Basic logging/retention guidance.

---

## 11) Risks & Mitigations
1. **Overly generic specs** → enforce quality score + required sections.
2. **Hallucinated technical constraints** → require assumption tracing.
3. **Provider outage** → failover/fallback provider policy.
4. **Long-running failures** → heartbeat + resumable checkpoints.
5. **Security misses** → independent security gate with mandatory sign-off.

---

## 12) Acceptance Criteria (Release Gate)
A project is “done” only if:
1. Spec artifacts approved by user.
2. All dev phases marked complete.
3. Tests and quality gates pass.
4. Security report has no unresolved critical/high issues.
5. Production readiness checklist passes.
6. SEO/analytics tasks completed or user-ready guide generated.
7. Handover bundle exported successfully.

---

## 13) Recommended Stack Decision (Desktop App)
### Decision
Use **Python + Qt6 (PySide6)** for MVP desktop-native orchestrator.

### Rationale
- Fast iteration speed for agentic tooling.
- Native-feeling multi-platform UI.
- Mature event-driven model for orchestration dashboards.
- Easier integration with Python AI/tooling ecosystem.

### Rejected Alternative
- Qt5: older lifecycle and reduced long-term roadmap fit for a new build.

---

## 14) Open Product Questions
- Should collaborative multi-user project editing be in V1.5 or V2?
- How much “autonomy” should be allowed before mandatory human approval?
- Should SEO be mandatory for non-web targets?

