from graphviz import Digraph

def create_node(graph, name, color='lightgrey', style='filled', shape='box'):
    graph.node(name, name, color=color, style=style, shape=shape)

def create_wazuh_diagram():
    dashed = Digraph(comment='Wazuh Architecture')
    dashed.attr(rankdir='TB', ranksep='0.5')

    # Create nodes
    #create_node(dot, 'Invinsense.core.cluster.client.AbstractClientManager')
    create_node(dashed ,'asyncio.protocol.BaseProtocol')
    create_node(dashed, 'asyncio.protocol.Protocol', color='#4285F4')
    
    create_node(dashed, 'Invinsense.core.cluster.common.Handler')
    create_node(dashed, 'Invinsense.core.cluster.server.AbstractServerHandler', color='#4285F4')
    create_node(dashed, 'Invinsense.core.cluster.common.InvinsenseCommon', color='#4285F4')
    
    create_node(dashed, 'Invinsense.core.cluster.client.AbstractClient', color='#4285F4')
    create_node(dashed, 'Invinsense.core.cluster.master.MasterHandler')
    create_node(dashed, 'Invinsense.core.cluster.worker.workerHandler')
    
    create_node(dashed, 'Invinsense.core.cluster.local_server.LocalServerHandler')
    create_node(dashed, 'Invinsense.core.cluster.local_client.LocalClientHandler')
    
    create_node(dashed, 'Invinsense.core.cluster.local_server.LocalServerHandlerWorker', color='#4285F4')
    create_node(dashed, 'Invinsense.core.cluster.local_server.LocalServerHandlerMaster', color='#4285F4')

    # Create edges
    dashed.edge('asyncio.protocol.BaseProtocol', 'asyncio.protocol.Protocol', color='#4285F4')
    dashed.edge('asyncio.protocol.Protocol', 'Invinsense.core.cluster.common.Handler', color='#4285F4')  
    dashed.edge('Invinsense.core.cluster.common.Handler', 'Invinsense.core.cluster.server.AbstractServerHandler',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.common.Handler', 'Invinsense.core.cluster.common.InvinsenseCommon',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.common.Handler', 'Invinsense.core.cluster.client.AbstractClient',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.server.AbstractServerHandler', 'Invinsense.core.cluster.master.MasterHandler',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.common.InvinsenseCommon', 'Invinsense.core.cluster.master.MasterHandler',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.common.InvinsenseCommon', 'Invinsense.core.cluster.worker.workerHandler',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.client.AbstractClient', 'Invinsense.core.cluster.worker.workerHandler',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.server.AbstractServerHandler', 'Invinsense.core.cluster.local_server.LocalServerHandler',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.client.AbstractClient', 'Invinsense.core.cluster.local_client.LocalClientHandler',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.local_server.LocalServerHandler', 'Invinsense.core.cluster.local_server.LocalServerHandlerWorker',color='#4285F4')
    dashed.edge('Invinsense.core.cluster.local_server.LocalServerHandler', 'Invinsense.core.cluster.local_server.LocalServerHandlerMaster',color='#4285F4')

    # Set edge color
    dashed.attr('edge', color='#4285F4')

    return dashed

# Generate and save the diagram
diagram = create_wazuh_diagram()
diagram.render('wazuh_architecture', format='png', cleanup=True)
print("Diagram saved as 'wazuh_architecture.png'")