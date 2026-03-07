class Evidence:
    def __init__(self,gene_id,evidence_type,normalized_score,confidence_score):
        self.gene_id = gene_id
        self.evidence_type = evidence_type
        self.normalized_score = normalized_score
        self.confidence_score = confidence_score

    def to_dict(self):
        return {
            "gene_id": self.gene_id,
            "evidence_type": self.evidence_type,
            "normalized_score": self.normalized_score,
            "confidence_score": self.confidence_score
        }