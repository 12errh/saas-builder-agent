# Product Requirements Document (PRD)
## Project
**Name:** ForgeFlow Agent Studio  
**Goal:** Build a production-grade multi-agent coding platform that can plan, design, implement, review, secure, and hand over complete web, mobile-adjacent desktop, and desktop-native applications from a single user prompt.

## 1. Vision
ForgeFlow turns a natural language prompt ("build me X") into a complete, auditable delivery pipeline:
1. Interactive discovery with checkbox/panel clarifications.
2. Spec generation (PRD/TRD/Phased plan/Design.md).
3. User review + optional auto-continue.
4. Phase-by-phase implementation with QA/security/review loops.
5. Production readiness checks (legal, auth, privacy, cookies, observability).
6. SEO and analytics setup guidance/integration.
7. Handover package (README, deployment runbook, architecture guide).

## 2. Target Users
- Solo founders
- Startup product teams
- Agencies
- Internal platform teams
- Technical PMs and engineering leads

## 3. Core Product Principles
- **Spec-first development**
- **Human-in-the-loop control with optional automation**
- **Safety and reliability by default**
- **Provider-agnostic LLM orchestration** (must support NVIDIA + OpenRouter)
- **MCP-native extensibility**
- **Progressive learning system from past runs** (policy-compliant memory)

## 4. Scope
### In Scope (MVP)
- Desktop-native orchestrator app (Python + Qt6 recommended)
- Prompt intake and interactive clarification UI
- Multi-agent orchestration engine
- Spec generator agent outputs:
  - PRD
  - TRD
  - Phase plan
  - Design.md (with web research-backed inspiration)
- Review agent + approval gating
- Coding agent with phase execution and testing
- Code reviewer + vulnerability tester loops
- Production readiness agent
- SEO/analytics agent
- Handover generator
- Retry/recovery for failures (network/tool/provider)
- MCP and skills support by default

### Out of Scope (MVP)
- Fully autonomous billing management
- Browser extension
- Multi-tenant cloud SaaS control plane
- Full mobile-native generation (deferred to later)

## 5. Key User Flows
1. **Prompt to Project**
   - User enters prompt.
   - Clarification panel appears with selectable options + free text.
   - User confirms requirements.

2. **Spec Generation**
   - Spec Generator builds PRD/TRD/Dev phases/Design.md.
   - Design.md includes modern/minimal direction and external inspiration.

3. **Review and Decide**
   - Review Agent validates realism and production constraints.
   - User chooses:
     - Notify-only at each gate, or
     - Auto-continue mode

4. **Build It**
   - User clicks **Build It**.
   - Coding agent implements phase-by-phase.
   - After each phase, reviewer/security agents validate and request fixes.

5. **Production and Handover**
   - Production agent verifies launch checklist.
   - SEO agent adds/validates SEO + analytics/search console guidance.
   - Handover artifacts generated.

## 6. Functional Requirements
### FR-1 Interactive Clarification
- Checkbox/radio/panel-based question sets.
- Domain-specific templates (web app, desktop app, API service, marketplace, etc.).
- Must support “custom backend vs Supabase” decision path.

### FR-2 Multi-Spec Generation
- Automatically create structured docs:
  - `PRD.md`
  - `TRD.md`
  - `DEV_PHASES.md`
  - `DESIGN.md`

### FR-3 Orchestration + Agent Roles
- Orchestrator manages task graph and gating.
- Required specialized agents:
  - Clarifier
  - Spec Generator
  - Review Agent
  - Coding Agent
  - Code Reviewer
  - Vulnerability Tester
  - Production Readiness Agent
  - SEO Agent
  - Handover Agent

### FR-4 Iterative Implementation Loop
- For each phase:
  - Implement
  - Run checks/tests
  - Review
  - Security scan
  - Fix loop until pass threshold met

### FR-5 Reliability and Recovery
- Recover from network errors, model downtime, tool failures.
- Persistent checkpoints and resumable runs.

### FR-6 Skills + MCP
- Native MCP support (including context/documentation MCPs).
- Skill registry and execution policies.

### FR-7 Multi-Provider LLM Support
- Must include NVIDIA and OpenRouter providers.
- Also support OpenAI-compatible interfaces.

### FR-8 Production Hardening
- Validate auth flows, legal pages, cookies/consent, error boundaries, monitoring.

### FR-9 SEO and Analytics
- Keyword research workflow.
- Metadata/schema generation.
- GA4 and Search Console integration or setup guide.

## 7. Non-Functional Requirements
- **Security:** secrets isolation, least privilege, sandboxing, audit logs.
- **Performance:** sub-2s UI interactions; async long-running jobs.
- **Scalability:** modular agent execution + queue-friendly architecture.
- **Observability:** structured logs, traces, token/tool usage metrics.
- **Compliance readiness:** policy templates for privacy and data handling.

## 8. UX Requirements
- Modern, minimal UI
- Dark/light mode
- Clear progress pipeline (Discovery → Spec → Review → Build → Launch)
- Explicit status for each phase and agent
- Human override at every gate

## 9. Success Metrics
- Time to first approved spec
- Successful phase completion rate
- Security issue detection rate pre-launch
- Deployment success rate
- User acceptance of generated handover docs

## 10. Recommended Desktop Stack
- **Python + Qt6 (PySide6)** for native desktop UI and robust cross-platform support.
- Why Qt6 over Qt5:
  - Longer runway and modern toolkit support.
  - Better long-term maintenance for new apps.

## 11. Risks
- Over-automation without sufficient user control.
- Provider-specific regressions.
- Hallucinated specs without constraints.
- Security review blind spots.

## 12. MVP Acceptance Criteria
- User can go from prompt to approved multi-doc spec.
- User can click Build It and receive phase-by-phase generated code with review loops.
- System can recover from simulated network/model failures.
- Production checklist + handover docs generated successfully.
