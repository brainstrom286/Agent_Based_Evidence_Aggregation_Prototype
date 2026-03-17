from orchestrator import collect_evidence
from aggregator import aggregate_evidence

genes = ["TP53", "BRCA1", "EGFR", "GENE_X"]

for gene in genes:
    print(f"\n{gene}")

    evidences = collect_evidence(gene)

    print("\nCollected Evidence:")
    for ev in evidences:
        print(ev.to_dict())

    final_score, contributions = aggregate_evidence(evidences)

    print("\nFinal Score:", round(final_score, 3))
    print("Contribution Breakdown:", contributions)