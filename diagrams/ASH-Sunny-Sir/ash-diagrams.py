from diagrams import Diagram, Edge
from diagrams.custom import Custom
from diagrams.programming.flowchart import Decision

# Custom node colors
PURPLE = "#B19CD9"
RED = "#FF6961"
GREEN = "#77DD77"
YELLOW = "#FDFD96"

# Custom shape for start/end nodes
def custom_shape(name, fill_color):
    return Custom(name, "./custom_node.py", fill_color=fill_color)

with Diagram("ASH - CI Execution Viability", show=False, direction="TB"):
    start = custom_shape("Start", YELLOW)
    
    ci_platform = Decision("Is your CI platform a SaaS\nsolution such as gitlab.com or\ndo you self-host your CI\nplatform?")
    
    self_hosted = Decision("Can your self-hosted CI\nagents run Linux containers?\nThis can either be directly as a\nrunner image or via `docker run`\nin a script")
    
    saas_agents = Decision("Are you using the hosted agents\nfrom the SaaS provider or self-\nhosting your own agents?")
    
    ash_supported = custom_shape("You\nshould be\nable to run ASH\ndirectly in your\nSaaS CI platform's supported\ncontainer job mechanisms, as most\nhosted agents support at least `docker`", PURPLE)
    
    container_registry = Decision("Do you have a private\ncontainer registry such\nas AWS ECR or GitLab\nContainer Registry that you can\npublish\nimages to?")
    
    no_registry = custom_shape("In order to internalize the ASH image,\nyou need an internally available private registry to\npublish the image to first!\n\nWe recommend Amazon ECR:\nhttps://aws.amazon.com/ecr/", RED)
    
    ash_requires = custom_shape("ASH requires the ability to run Linux\ncontainers in order to use it for code\nscanning.", RED)
    
    internal_process = custom_shape("At\nthis point,\nyou will need to\nfollow your internal\nprocesses to publish the\nASH image to your private\nregistry. Once the image has been\npublished, proceed.", PURPLE)
    
    congratulations = custom_shape("Congratulations! You should be able to support\nexecution of ASH scans as part of your CI pipeline. You\nwill need to use the internal private image and desired\ntag when configuring your ASH scan job in your CI.", GREEN)
    
    # Connect nodes
    start >> ci_platform
    ci_platform >> Edge(label="Self-hosted") >> self_hosted
    ci_platform >> Edge(label="SaaS") >> saas_agents
    saas_agents >> Edge(label="Using SaaS Hosted Agents") >> ash_supported
    saas_agents >> Edge(label="Using self-hosted\nagents with SaaS CI") >> self_hosted
    self_hosted >> Edge(label="Yes, we can run Linux containers\nin our self-hosted CI agents") >> container_registry
    self_hosted >> Edge(label="No, we cannot use\nLinux containers\nin our self-hosted\nCI agents") >> ash_requires
    container_registry >> Edge(label="No, we do not\nhave a private\nregistry available") >> no_registry
    container_registry >> Edge(label="Yes we have an internal\nprivate registry for\nLinux container images.") >> internal_process
    internal_process >> Edge(label="ASH container image\nhas been published to\nyour internal private registry") >> congratulations
    ash_supported >> container_registry