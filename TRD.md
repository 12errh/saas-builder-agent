# ForgeFlow Agent Studio — Technical Requirements Document (TRD)

## 0) Document Control
- **Version:** v2.0
- **Date:** May 9, 2026
- **Status:** Engineering draft
- **Owner:** Platform Architecture

---

## 1) System Overview
ForgeFlow is a local-first desktop orchestration system coordinating multiple specialized agents to transform product prompts into production-grade software artifacts.

### 1.1 Architecture Style
- Event-driven orchestration engine
- Stateful workflow graph with resumable checkpoints
- Plugin-friendly adapters for providers, MCP servers, and skills

### 1.2 Core Runtime Guarantees
- Deterministic state transitions
- Idempotent retry behavior for tool/provider calls
- Immutable run artifacts with version history

---

## 2) Logical Architecture
### 2.1 Layers
1. **Desktop UI Layer (PySide6/Qt6)**
2. **Application Services Layer** (project/session management)
3. **Orchestration Layer** (workflow graph, gates, retries)
4. **Agent Execution Layer** (specialized agents)
5. **Integration Layer** (MCP, skills, git, test tools)
6. **Model Provider Layer** (NVIDIA, OpenRouter, extensible adapters)
7. **Persistence & Telemetry Layer**

### 2.2 Component Map
- `ui/desktop`
- `core/orchestrator`
- `core/agents`
- `core/providers`
- `core/mcp`
- `core/skills`
- `core/review`
- `core/security`
- `core/recovery`
- `storage`
- `telemetry`

---

## 3) Agent Topology and Contracts
### 3.1 Required Agents
- Clarification Agent
- Spec Generator Agent
- Review Agent
- Coding Agent
- Code Review Agent
- Vulnerability Agent
- Production Readiness Agent
- SEO Agent
- Handover Agent

### 3.2 Agent Interface Contract
Every agent must implement:
- `input_schema` (JSON Schema)
- `output_schema` (JSON Schema)
- `execute(context) -> artifact_bundle`
- `quality_score` (0-100)
- `confidence_score` (0-1)
- `retry_classification` metadata

### 3.3 Artifact Bundle Contract
Standard fields:
- `artifact_type`
- `version`
- `created_at`
- `source_inputs`
- `content`
- `assumptions`
- `open_questions`

---

## 4) Workflow State Machine
### 4.1 Canonical States
1. `PROJECT_INIT`
2. `DISCOVERY_ACTIVE`
3. `DISCOVERY_RESOLUTION`
4. `SPEC_DRAFTING`
5. `SPEC_REVIEW_INTERNAL`
6. `SPEC_REVIEW_USER`
7. `READY_TO_BUILD`
8. `PHASE_EXECUTION_N`
9. `PHASE_REVIEW_N`
10. `PHASE_SECURITY_N`
11. `PHASE_GATE_DECISION_N`
12. `PROD_READINESS`
13. `SEO_ANALYTICS`
14. `HANDOVER_PACKAGING`
15. `COMPLETE`
16. `FAILED_RECOVERABLE`
17. `FAILED_TERMINAL`

### 4.2 Transition Rules
- No transition into `READY_TO_BUILD` unless required specs are approved.
- Each phase must pass review + security gates before incrementing phase index.
- `FAILED_RECOVERABLE` attempts policy-based recovery; otherwise escalates.

---

## 5) Data Model Specification
### 5.1 Entities
#### Project
- `project_id` (UUID)
- `name`
- `prompt_raw`
- `project_type`
- `owner`
- `created_at`

#### RunSession
- `run_id` (UUID)
- `project_id`
- `state`
- `status`
- `active_phase`
- `provider_config`
- `started_at`
- `ended_at`

#### Artifact
- `artifact_id`
- `run_id`
- `type`
- `path`
- `checksum`
- `version`
- `quality_score`

#### GateResult
- `gate_id`
- `run_id`
- `phase`
- `gate_type` (test/review/security/prod)
- `status`
- `findings`
- `resolution_ref`

#### Incident
- `incident_id`
- `run_id`
- `category`
- `severity`
- `recovery_strategy`
- `recovered`

---

## 6) Provider Abstraction and Routing
### 6.1 Required Providers
- NVIDIA adapter
- OpenRouter adapter

### 6.2 Provider Interface
- `generate(messages, tool_context, response_schema, options)`
- `stream(messages, tool_context, options)`
- `healthcheck()`
- `estimate_cost(request_shape)`

### 6.3 Routing Policy
- Route by task type:
  - planning/spec tasks
  - code generation
  - review/security reasoning
- Fallback chain configurable per workspace.
- Circuit breaker after consecutive failures.

---

## 7) MCP Integration Requirements
### 7.1 Registry
- MCP server catalog with trust level and capability tags.
- Enable/disable per project.

### 7.2 Policy Enforcement
- Allowlist command patterns.
- Per-tool timeout and retry policy.
- Redaction layer for sensitive outputs.

### 7.3 Context Documentation MCP
- Support context-document MCP endpoint ingestion to fetch latest docs.
- Persist source references in artifact metadata.

---

## 8) Skills Runtime
- Skill discovery from configured directories.
- Manifest validation.
- Compatibility matrix (runtime version, permissions, dependencies).
- Execution log attached to phase artifacts.

---

## 9) Build/Review/Security Gate Design
### 9.1 Phase Pipeline
1. Task decomposition
2. Code synthesis
3. Local validation (lint/tests/type checks)
4. Code review agent analysis
5. Security scan agent analysis
6. Remediation loop
7. Gate decision

### 9.2 Gate Thresholds
- Test pass rate: 100% required for critical path tests
- Lint errors: 0
- High/critical vulnerabilities: 0 unresolved
- Review severity score under threshold before merge/phase advance

---

## 10) Reliability Engineering
### 10.1 Failure Classes
- Provider/network transient
- Tool timeout
- Invalid schema output
- Deterministic test failure
- Permission/policy failure

### 10.2 Recovery Strategy
- Exponential backoff with jitter
- Retry budgets per class
- Checkpoint restore with deterministic replay context
- Manual intervention request if retry budget exhausted

### 10.3 State Durability
- Save checkpoints on every state transition and artifact commit.
- Journal actions for replay/audit.

---

## 11) Security Requirements
- Secrets managed via environment/keychain integration.
- No plaintext secrets in logs/artifacts.
- Dependency and SAST scans integrated at phase gates.
- Optional DAST hook for web targets before handover.

---

## 12) Observability and Telemetry
### Metrics
- Phase duration
- Retry count by class
- Gate failure causes
- Token/cost usage by provider
- Incident frequency and mean time to recovery

### Logs
- Structured JSON logs with correlation IDs.
- Agent execution traces and tool call lineage.

---

## 13) UI Technical Requirements
- PySide6 desktop shell.
- Real-time event stream from orchestrator to UI state panels.
- Gate visualization cards (status, blockers, next action).
- Approval controls with audit trail.

---

## 14) Packaging & Distribution
- Windows installer (MSIX or equivalent)
- macOS package (DMG/PKG)
- Linux package (AppImage + optional DEB)

---

## 15) Testing Strategy (System-Level)
- Unit tests for orchestration transitions.
- Contract tests for provider adapters and agent schemas.
- Fault-injection tests for recovery flows.
- End-to-end golden-path tests:
  - prompt → spec approval → phase build → handover.

---

## 16) Open Technical Decisions
- Local-only DB vs optional team Postgres mode.
- Depth of plugin API for third-party agents.
- Cloud sync architecture and encryption model.

