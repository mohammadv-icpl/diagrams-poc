from diagrams import Diagram
from diagrams.generic.compute import Rack
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server

def create_node(name, label=None, color='lightblue', shape='box'):
    """Creates a node object with specific attributes."""
    return Server(label or name)

def create_wazuh_diagram():
    """Creates a Wazuh architecture diagram using the diagrams library."""
    with Diagram("Invinsense Architecture", show=False, direction="TB"):
        # Create nodes
        manager = create_node("AbstractClientManager", color='lightblue')
        local_client = create_node("LocalClient", color='red')
        worker = create_node("Worker", color='lightcoral')

        # Add edges to represent relationships
        manager >> local_client
        manager >> worker

# Generate and save the diagram
create_wazuh_diagram()
print("Diagram saved as 'Invinsense_Architecture.png'")
