import graphviz

def create_wazuh_diagram():
    G = graphviz.Digraph('Wazuh Architecture', format='png')

    # Create nodes
    G.node("Master node")
    G.node("Worker node")
    G.node("Process pool")
    G.node("Local integrity")
    G.node("Agent-info DB")
    G.node("Agent-info sync")
    G.node("Integrity sync")
    G.node("Response")

    # Add edges
    G.edge("Process pool", "Local integrity")
    G.edge("Local integrity", "Agent-info DB")
    G.edge("Master node", "Agent-info sync")
    G.edge("Agent-info DB", "Agent-info sync")
    G.edge("Agent-info sync", "Response")
    G.edge("Master node", "Integrity sync")
    G.edge("Integrity sync", "Response")
    G.edge("Worker node", "Agent-info sync")
    G.edge("Worker node", "Integrity sync")

    # Set attributes (optional)
    G.attr(rankdir='TB')  # Top to Bottom layout
    G.attr('node', shape='ellipse')
    G.attr('edge', color='blue')

    return G

# Generate and save the diagram
diagram = create_wazuh_diagram()
diagram.render('wazuh_architecture', cleanup=True)
