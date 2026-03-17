from agent import depmap_agent, opentargets_agent, literature_agent

def collect_evidence(gene_id):

    agents = [
        depmap_agent,
        opentargets_agent,
        literature_agent
    ]

    evidences = []

    for agent in agents:
        ev = agent(gene_id)

        if ev is not None:   # handling missing evidence
            evidences.append(ev)

    return evidences