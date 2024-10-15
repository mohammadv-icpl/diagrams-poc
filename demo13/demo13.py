from graphviz import Digraph

def create_node(graph, name, color='lightgrey', style='filled', shape='box'):
    graph.node(name, name, color=color, style=style, shape=shape)

def create_wazuh_diagram():
    dot = Digraph(comment='Wazuh Architecture')
    dot.attr(rankdir='TB', ranksep='0.5')

    # Create nodes
   #create_node(dot, 'Invinsense.core.cluster.client.AbstractClientManager')
   # create_node(dot, 'Invinsense.core.cluster.client.AbstractClientManager', color='white')
   # create_node(dot, 'wazuh.core.cluster.common.Handler')
    
  #  create_node(dot, 'wazuh.core.cluster.server.AbstractServerHandler', color='#4285F4')
  #  create_node(dot, 'wazuh.core.cluster.common.WazuhCommon', color='#4285F4')
  # create_node(dot, 'wazuh.core.cluster.client.AbstractClient', color='#4285F4')
    
    create_node(dot, 'Invinsense.core.cluster.client.AbstractClientManager')
   # create_node(dot, 'wazuh.core.cluster.worker.WorkerHandler')
    
   # create_node(dot, 'wazuh.core.cluster.local_server.LocalServerHandler')
   # create_node(dot, 'wazuh.core.cluster.local_client.LocalClientHandler')
    
  #  create_node(dot, 'wazuh.core.cluster.local_server.LocalServerHandlerWorker', color='#4285F4')
  #  create_node(dot, 'wazuh.core.cluster.local_server.LocalServerHandlerMaster', color='#4285F4')

    # Create edges
   # dot.edge('Invinsense.core.cluster.local_client.localClient', 'Invinsense.core.cluster.local_client.localClient', color='#4285F4')
    
   # dot.edge('asyncio.protocols.Protocol', 'wazuh.core.cluster.common.Handler')
    
    #dot.edge('wazuh.core.cluster.common.Handler', 'wazuh.core.cluster.server.AbstractServerHandler')
   # dot.edge('wazuh.core.cluster.common.Handler', 'wazuh.core.cluster.common.WazuhCommon')
   # dot.edge('wazuh.core.cluster.common.Handler', 'wazuh.core.cluster.client.AbstractClient')
    
   # dot.edge('wazuh.core.cluster.server.AbstractServerHandler', 'wazuh.core.cluster.master.MasterHandler')
   # dot.edge('wazuh.core.cluster.server.AbstractServerHandler', 'wazuh.core.cluster.local_server.LocalServerHandler')
    
   # dot.edge('wazuh.core.cluster.common.WazuhCommon', 'wazuh.core.cluster.master.MasterHandler')
   # dot.edge('wazuh.core.cluster.common.WazuhCommon', 'wazuh.core.cluster.worker.WorkerHandler')
    
   # dot.edge('wazuh.core.cluster.client.AbstractClient', 'wazuh.core.cluster.worker.WorkerHandler')
   # dot.edge('wazuh.core.cluster.client.AbstractClient', 'wazuh.core.cluster.local_client.LocalClientHandler')
    
    #dot.edge('Invinsense.core.cluster.local_server.LocalServerHandler', 'wazuh.core.cluster.local_server.LocalServerHandlerWorker')
    #dot.edge('Invinsense.core.cluster.Client.AbstractClientManager' , 'wazuh.core.cluster.local_server.LocalServerHandlerMaster')

    # Set edge color
    dot.attr('edge', color='#4285F4')

    return dot

# Generate and save the diagram
diagram = create_wazuh_diagram()
diagram.render('wazuh_architecture', format='png', cleanup=True)
print("Diagram saved as 'wazuh_architecture.png'")

#To create Diagrams Step by step
# 1 from graphviz import Digraph
# 2 def create_node(graph, name, color='lightgrey', style='filled', shape='box'):
#   graph.node(name, name, color=color, style=style, shape=shape)

# 3 def create_wazuh_diagram():
#  dot = Digraph(comment='Wazuh Architecture')
#   dot.attr(rankdir='TB', ranksep='0.5')
# 4 create_node(dot, 'Invinsense.core.cluster.client.AbstractClientManager')
# 5 dot.edge('Invinsense.core.cluster.local_client.localClient', 'Invinsense.core.cluster.local_client.localClient', color='#4285F4')
# 6 dot.attr('edge', color='#4285F4') To cahnge color
# 7 diagram = create_wazuh_diagram()
#diagram.render('wazuh_architecture', format='png', cleanup=True)
#print("Diagram saved as 'wazuh_architecture.png'")




