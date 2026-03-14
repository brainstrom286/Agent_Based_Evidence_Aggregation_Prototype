import random
from evidence_schema import Evidence

def depmap_agent(gene_id):

    value = random.uniform(-1, 0)
    normalized = abs(value)

    return Evidence(
        gene_id,
        source="DepMap",
        evidence_type="gene_dependency",
        value=value,
        normalized_score=normalized,
        confidence_score=0.9
    )


def opentargets_agent(gene_id):

    score = random.uniform(0.4, 0.9)

    return Evidence(
        gene_id,
        source="OpenTargets",
        evidence_type="gene_disease_association",
        value=score,
        normalized_score=score,
        confidence_score=0.85
    )


def literature_agent(gene_id):

    count = random.randint(10, 200)

    normalized = min(count / 200, 1)

    return Evidence(
        gene_id,
        source="Literature",
        evidence_type="publication_support",
        value=count,
        normalized_score=normalized,
        confidence_score=0.7
    )