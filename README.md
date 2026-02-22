MedGemma Impact — RICCI ERS

Governed Clinical Event Reasoning System

Overview

RICCI ERS is a governance-driven clinical reasoning system designed for emergency-response environments.

Instead of focusing on free-form medical text generation, the system enforces structured, auditable clinical event documentation.

It transforms:

Operational Timeline
→ LLM Clinical Reasoning
→ Structured Medical Events (JSON)
→ Governance Validation
→ Audit-Ready Export

The objective is reliability, safety, and structural integrity in AI-assisted emergency documentation.

Problem Context

In emergency systems (EMS / SAMU environments), AI must:

Produce structured outputs

Avoid omission of mandatory documentation

Remain auditable

Degrade safely when model output fails

The primary operational risk is not hallucination — it is omission.

RICCI ERS addresses this through a deterministic governance layer.

System Architecture

Timeline ingestion

LLM reasoning (MedGemma-ready interface)

JSON structure validation

Mandatory event classification (Hard vs Soft)

Deterministic fallback activation (if needed)

Export of structured artifacts (.json + .md)

This ensures minimum clinical safety compliance even under parsing or generation failure.

Safety & Governance Layer

The system enforces:

JSON parsing validation

Hard-required events (must exist)

Soft-required events (recommended but non-blocking)

Deterministic fallback generation

Structured export for auditing

If the LLM output cannot be parsed into valid JSON, a fallback mechanism guarantees mandatory clinical events are generated.

This design prioritizes operational safety over generative flexibility.

Runnable Demonstration

A fully executable Kaggle notebook demonstrates the complete pipeline:

Timeline → LLM → Governance → Export

Generated artifacts are committed in /exports:

ricci_ers_llm_demo_*.md

ricci_ers_llm_demo_*.json

The notebook runs end-to-end and exports audit-ready outputs.

Repository Structure
docs/         → Competition write-up  
notebooks/    → Kaggle submission notebook  
src/          → Core governance and reasoning logic  
exports/      → Generated demonstration artifacts  
Why This Approach

Emergency AI systems must be:

Deterministic under failure

Structurally validated

Auditable

Governance-aware

RICCI ERS proposes a pattern for integrating LLMs into clinical environments where reliability is mandatory.

License

MIT License

Author

Eduardo Ricci
Governed Clinical Event Reasoning System — RICCI ERS
