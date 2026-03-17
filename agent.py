from evidence_schema import Evidence

# DepMap Agent
def depmap_agent(gene_id):

    data = {
        "TP53": 0.9,
        "BRCA1": 0.7,
        "EGFR": 0.9,   # strong
        "GENE_X": None  # missingevidence
    }

    value = data.get(gene_id, 0.3)

    if value is None:
        return None

    return Evidence(
        gene_id,
        source="DepMap",
        evidence_type="gene_dependency",
        value=value,
        normalized_score=value,
        confidence_score=0.9
    )


# OpenTargets Agent
def opentargets_agent(gene_id):

    data = {
        "TP53": 0.85,
        "BRCA1": 0.9,
        "EGFR": 0.4,   #conflicting
        "GENE_X": 0.3
    }

    value = data.get(gene_id, 0.4)

    return Evidence(
        gene_id,
        source="OpenTargets",
        evidence_type="gene_disease_association",
        value=value,
        normalized_score=value,
        confidence_score=0.85
    )


# Literature Agent
def literature_agent(gene_id):

    data = {
        "TP53": 0.95,
        "BRCA1": 0.9,
        "EGFR": 0.8,
        "GENE_X": 0.2
    }

    value = data.get(gene_id, 0.3)

    return Evidence(
        gene_id,
        source="Literature",
        evidence_type="publication_support",
        value=value,
        normalized_score=value,
        confidence_score=0.7
    )