from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Users
from diagrams.generic.network import Firewall

def create_wazuh_diagram():
    with Diagram("Wazuh Architecture", show=False, direction="TB"):
        
        # Define nodes
        master = Server("Master node")
        worker = Server("Worker node")
        pool = Server("Process pool")
        integrity = Server("Local Integrity")
        agent_db = RDS("Agent-info DB")
        agent_sync = Server("Agent-info Sync")
        integrity_sync = Server("Integrity Sync")
        response = Server("Response")

        # Define relationships
        pool >> integrity
        integrity >> agent_db
        master >> agent_sync
        agent_db >> agent_sync
        agent_sync >> response
        master >> integrity_sync
        integrity_sync >> response
        worker >> agent_sync
        worker >> integrity_sync

# Generate and save the diagram
create_wazuh_diagram()
