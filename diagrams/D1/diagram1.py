from graphviz import Digraph

def create_node(graph, name, color='lightblue', style='filled', shape='box'):
    """Creates a node in the Graphviz graph."""
    graph.node(name, name, color=color, style=style, shape=shape)

def create_wazuh_diagram():
    """Creates a Graphviz diagram representing the Wazuh architecture."""
    dot = Digraph(comment='Wazuh Architecture')
    dot.attr(rankdir='TB', ranksep='0.5')

    # Create nodes
    create_node(dot, "Invinsense.core.cluster.client.AbstractClientManager", color='lightblue')
    create_node(dot, "Invinsense.core.cluster.local_client.LocalClient", color='lightgreen')
    create_node(dot, "Invinsense.core.cluster.worker.Worker", color='lightcoral')

    # Create edges
    dot.edge("Invinsense.core.cluster.client.AbstractClientManager", 
             "Invinsense.core.cluster.local_client.LocalClient", label="Local Client")
    dot.edge("Invinsense.core.cluster.client.AbstractClientManager", 
             "Invinsense.core.cluster.worker.Worker", label="Worker")

    # Set edge styles (optional)
    dot.attr('edge', arrowhead='vee', arrowsize='1.2')

    return dot

# Generate and save the diagram
diagram = create_wazuh_diagram()
diagram.render('Invinsense_architecture', format='png', cleanup=True)
print("Diagram saved as 'Invinsense_architecture.png'")
