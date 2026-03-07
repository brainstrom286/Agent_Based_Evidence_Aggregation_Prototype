from agent import literature_agent, expression_agent, interaction_agent
from aggregator import aggregate_evidence

gene_id = "TP53"

evidences = [
    literature_agent(gene_id),
    expression_agent(gene_id),
    interaction_agent(gene_id)
]

final_score, contributions = aggregate_evidence(evidences)

output = {
    "gene_id": gene_id,
    "final_score": round(final_score, 3),
    "contribution_breakdown": contributions,
    "aggregation_version": "v1"
}

print("\nFinal Output:\n")
print(output)