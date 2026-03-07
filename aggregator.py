#t_s=total_score / t_w=total_weight /c_b=contribution_breakdown
def aggregate_evidence(evidences):

    t_s = 0
    t_w = 0
    c_b = {}

    for ev in evidences:
        weight = ev.confidence_score
        contribution = ev.normalized_score * weight

        t_s += contribution
        t_w += weight

        c_b[ev.evidence_type] = contribution

    final = t_s / t_w if t_w > 0 else 0

    return final, c_b