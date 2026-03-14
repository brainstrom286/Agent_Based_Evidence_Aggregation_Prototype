class Evidence:
    def __init__(self, gene_id, source, evidence_type, value, normalized_score, confidence_score, metadata=None):
        self.gene_id = gene_id
        self.source = source
        self.evidence_type = evidence_type
        self.value = value
        self.normalized_score = normalized_score
        self.confidence_score = confidence_score
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "gene_id": self.gene_id,
            "source": self.source,
            "evidence_type": self.evidence_type,
            "value": self.value,
            "normalized_score": self.normalized_score,
            "confidence_score": self.confidence_score,
            "metadata": self.metadata
        }