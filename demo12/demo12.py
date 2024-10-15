# from diagrams import Diagram, Cluster
# from diagrams.custom import Custom
# from diagrams.onprem.client import Client
# from diagrams.onprem.compute import Server
# from diagrams.onprem.network import Internet
# from diagrams.azure.compute import AutomanagedVM
# from diagrams.azure.compute import VMLinux
# from diagrams.azure.migration import RecoveryServicesVaults
# from diagrams.azure.storage import StorsimpleDeviceManagers
# from diagrams.alibabacloud.compute import ElasticComputeService, ECS 

# def custom_icon(name):
#     return Custom(name, "./path_to_custom_icons/" + name + ".png")

# with Diagram("Wazuh Central Components", show=False):
#     with Cluster("Endpoints"):
#         endpoints = [
#             Client("Server"),
#             Client("Desktop"),
#             Client("Laptop"),
#             custom_icon("Cloud instance"),
#             custom_icon("Virtual machine")
#         ]
    
#     with Cluster("Wazuh central components"):
#         with Cluster("W. server cluster"):
#             nlb = custom_icon("Network load balancer")
            
#             with Cluster("Master node"):
#                 master = Server("Master node")
            
#             with Cluster("Worker node"):
#                 worker = Server("Worker node")
            
#             nlb >> master
#             nlb >> worker
        
#         dashboard = custom_icon("W. dashboard")
#         indexer = custom_icon("W. Indexer")
        
#         master >> dashboard
#         worker >> indexer
    
#     users = Internet("Wazuh users")
    
#     endpoints >> nlb
#     dashboard >> users
#     indexer >> dashboard

# print("Diagram generated successfully.")
from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet
from diagrams.azure.compute import AutomanagedVM, VMLinux
from diagrams.azure.migration import RecoveryServicesVaults
from diagrams.azure.storage import StorsimpleDeviceManagers
from diagrams.alibabacloud.compute import ElasticComputeService
from diagrams.azure.identity import Groups

# Function to load a custom icon
def custom_icon(name):
    return Custom(name, f"./path_to_custom_icons/{name}.png")

# Diagram generation
with Diagram("Invinsense Central Components", show=False):
    
#     અહીં Diagram() ઓબ્જેક્ટ બનાવ્યું છે, જે ડાયાગ્રામનો મુખ્ય કંટેનર છે.
# "show=False"નો અર્થ છે કે આ ડાયાગ્રામ સ્ક્રિપ્ટ રન થતી વખતે તરત જ ન દર્શાવાય.
    # Endpoint Cluster
    
#Endpoints ક્લસ્ટરમાં વિવિધ ડિવાઇસેસ છે જે Invinsense એજન્ટ સાથે જોડાયેલી છે.
    
    with Cluster("Endpoints"):
        with Cluster("Invinsense agent"):
            endpoints = [
                ElasticComputeService("Server"),
                AutomanagedVM("Desktop"),
                VMLinux("Laptop"),
                RecoveryServicesVaults("Cloud instance"),
                StorsimpleDeviceManagers("Virtual Machine"),
            ]
    
    # Custom icon for Inv.indexer
    inv_indexer_icon = custom_icon("inv_indexer_icon")

    # Invinsense Central Components Cluster
    with Cluster("Invinsense Central Components"):
        with Cluster("I. Server Cluster"):
            nlb = custom_icon("Network load balancer")

            with Cluster("Master node"):
                master = Server("Master node")
            with Cluster("Worker node"):
                worker = Server("Worker node")

            # Connections
            nlb >> master
            nlb >> worker

        dashboard = custom_icon("inv_indexer_icon")  
        indexer = inv_indexer_icon  # Use the custom icon here

        # Connections within the cluster
        master >> dashboard
        worker >> indexer  

    # External connections
    users = Groups("Invinsense users")
    endpoints >> nlb
    dashboard >> users
    indexer >> dashboard

print("Diagram generated successfully.")
