# Phase Execution Plan (Strict Order)

To avoid skipping ahead, implementation follows this lock-step order:

1. **Phase 0 complete first**
   - Scaffold + packaging + baseline tests
   - State persistence primitive
   - Desktop shell bootstrap
2. **Phase 1 after Phase 0 is fully complete**
   - Prompt classification
   - Clarifying questionnaire
   - Discovery persistence
3. **Phase 2 after Phase 1 is complete**
   - Spec generation artifacts
4. **Phase 3 after Phase 2 is complete**
   - Review/approval gates

## Current Status
- Phase 0: ✅ Complete
- Phase 1: ✅ Complete
- Phase 2: ✅ Complete
- Phase 3: 🟡 In Progress

## Enforcement
- `TaskTracker.can_start_phase(phase)` blocks starting a phase unless all prior phases are complete.
