from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.azure.compute import AutomanagedVM
from diagrams.azure.compute import VMLinux
from diagrams.azure.migration import RecoveryServicesVaults
from diagrams.azure.storage import StorsimpleDeviceManagers
from diagrams.alibabacloud.compute import ElasticComputeService, ECS
from diagrams.azure.identity import Groups 

def custom_icon(name):
    return Custom(name, "./path_to_custom_icons/" + name + ".png")

with Diagram("Invinsense Central Components", show=False):
    with Cluster("Endpoints"):
        with Cluster("Invinsense agent"):
            endpoints = [
            ElasticComputeService("Server"),
            AutomanagedVM("Desktop"),
            VMLinux("Laptop"),
            RecoveryServicesVaults("Cloud instance"),
            StorsimpleDeviceManagers("virtual machine"),
        ]
    # nlb = custom_icon("Inv.indexer")
    with Cluster("Invinsense Central Components"):
            
        with Cluster("I. Server Cluster"):
            nlb = custom_icon("Network load balancer")
            with Cluster("Master node"):
             master = Server("Master node")
            with Cluster("Worker node"):
             worker = Server("Worker_node")
                
            nlb >> master
            nlb >> worker
     
       # Adding I.Dashboard and a new icon next to it
        dashboard = custom_icon("i_Dashboard")  
        indexer = custom_icon("i_indexer")
        master >> dashboard
        worker >> indexer  
    
    # Users cluster and connections
    users = Groups("Invinsense users")
    endpoints >> nlb
    dashboard >> users
    indexer >> dashboard
   
print("Diagram generated successfully.")
