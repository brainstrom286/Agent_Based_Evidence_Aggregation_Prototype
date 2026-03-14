from agent import depmap_agent, opentargets_agent, literature_agent

def collect_evidence(gene_id):

    agents = [
        depmap_agent,
        opentargets_agent,
        literature_agent
    ]

    evidences = []

    for agent in agents:
        evidence = agent(gene_id)
        evidences.append(evidence)

    return evidences