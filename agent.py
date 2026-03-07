import random
from evidence_schema import Evidence

def literature_agent(gene_id):
    score = random.uniform(0.6, 0.9)
    confidence = random.uniform(0.7, 0.95)

    return Evidence(gene_id, "literature", score, confidence)


def expression_agent(gene_id):
    score = random.uniform(0.5, 0.85)
    confidence = random.uniform(0.6, 0.9)

    return Evidence(gene_id, "expression", score, confidence)


def interaction_agent(gene_id):
    score = random.uniform(0.55, 0.88)
    confidence = random.uniform(0.65, 0.9)

    return Evidence(gene_id, "protein_interaction", score, confidence)