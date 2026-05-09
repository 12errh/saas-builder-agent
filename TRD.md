# Technical Requirements Document (TRD)
## 1. Architecture Overview
ForgeFlow uses an event-driven orchestrator with modular agent workers.

### Layers
1. **Desktop UI Layer (PySide6/Qt6)**
2. **Orchestration Core**
3. **Agent Runtime Layer**
4. **Tool/MCP/Skills Integration Layer**
5. **Persistence + Telemetry Layer**
6. **Provider Abstraction Layer**

## 2. High-Level Components
- `ui/desktop`: Native app (wizard, checklists, run dashboard)
- `core/orchestrator`: state machine + workflow engine
- `core/agents`: specialized agent implementations
- `core/providers`: model provider adapters (NVIDIA, OpenRouter, others)
- `core/mcp`: MCP client, registry, permission policy
- `core/skills`: skills loader/executor
- `core/review`: lint, test, security, quality gates
- `core/recovery`: retry, checkpoint, resume
- `storage`: sqlite/postgres abstraction for runs and artifacts

## 3. Agent Contracts
Each agent exposes:
- Input schema (JSON)
- Output schema (JSON + markdown artifacts)
- Confidence/uncertainty score
- Retry policy hints

## 4. Orchestration Model
- Directed phase graph with guard conditions.
- States:
  - `DISCOVERY`
  - `SPEC_DRAFT`
  - `SPEC_REVIEW`
  - `WAIT_USER_APPROVAL`
  - `IMPLEMENT_PHASE_N`
  - `REVIEW_PHASE_N`
  - `SECURITY_PHASE_N`
  - `PROD_READINESS`
  - `HANDOVER`
  - `COMPLETE`

## 5. Data Models
### Project
- id, name, prompt, mode, created_at

### SessionRun
- id, project_id, current_state, status, provider_map, started_at, finished_at

### Artifact
- id, run_id, type (`PRD`, `TRD`, `DEV_PHASES`, `DESIGN`, `CODE_DIFF`, `REPORT`), path, version

### TaskExecution
- id, run_id, phase, agent_name, input_ref, output_ref, status, retries

### Incident
- id, run_id, type, severity, recovery_action, resolved

## 6. Provider Abstraction
Interface:
- `generate(messages, tools, schema, options)`
- `stream(...)`
- `healthcheck()`
- `cost_estimate()`

Required adapters:
- NVIDIA
- OpenRouter
- OpenAI-compatible generic adapter

## 7. MCP Integration
- MCP registry with allowlist policies.
- Context MCP support for latest docs retrieval (e.g., “context7-like docs MCP”).
- Tool-call guardrails with timeouts and failure handling.

## 8. Skills Integration
- Skills discovered from configured skill directories.
- Versioned metadata + compatibility checks.
- Deterministic execution sandbox where possible.

## 9. Reliability & Recovery
- Exponential backoff and jitter.
- Circuit breaker per provider/tool.
- Checkpoint after each successful state transition.
- Resume capability from last consistent checkpoint.

## 10. Security Design
- Secret storage via OS keyring/.env vault strategy.
- No secret logging.
- Signed artifact history.
- Dependency and SAST scans at phase gates.

## 11. Quality Gates
Per phase minimum gates:
- Unit/integration tests pass
- Lint + formatting pass
- Security scan threshold pass
- Critical review comments resolved

## 12. UI Technical Notes
- Qt6 widgets/QML hybrid optional.
- Event bus from orchestrator to UI for live status.
- Interactive checklist components for clarifying questions and approval toggles.

## 13. Observability
- Structured JSON logs
- Agent-level execution traces
- Metrics:
  - phase duration
  - retry counts
  - failure classes
  - model/token consumption

## 14. Deployment Targets
- Desktop app packaging:
  - Windows (MSIX/installer)
  - macOS (dmg/pkg)
  - Linux (AppImage/deb)

## 15. Open Technical Decisions
- SQLite vs Postgres for local+team mode
- Plugin API depth for third-party agents
- Optional cloud sync architecture
