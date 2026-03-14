from orchestrator import collect_evidence
from aggregator import aggregate_evidence

gene_id = "TP53"

evidences = collect_evidence(gene_id)

final_score, contributions = aggregate_evidence(evidences)

output = {
    "gene_id": gene_id,
    "final_score": round(final_score, 3),
    "contribution_breakdown": contributions,
    "aggregation_version": "v2"
}

print("\nCollected Evidence:\n")

for ev in evidences:
    print(ev.to_dict())

print("\nFinal Output:\n")
print(output)