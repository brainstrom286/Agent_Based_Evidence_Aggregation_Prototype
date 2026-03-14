# Agent Based Evidence Aggregation Prototype

This is a minimal prototype exploring an agent based approach for aggregating heterogeneous biological evidence for drug target identification.

Components:
- Evidence schema for standardized evidence representation
- Simulated evidence agents (literature, expression, interaction)
- Aggregation module using confidence-weighted scoring
- Representation of heterogeneous evidence sources (DepMap, OpenTargets, literature)
- A richer evidence schema supporting different evidence types
- An orchestration layer that deterministically coordinates agents

Run demo:

python demo.py