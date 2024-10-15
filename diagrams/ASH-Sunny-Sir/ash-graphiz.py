import graphviz

# Create a new directed graph
dot = graphviz.Digraph(comment='ASH - CI Execution Viability')
dot.attr(rankdir='TB', size='8,8')

# Define node styles
dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='10')

# Custom node colors
START_COLOR = '#FDFD96'
DECISION_COLOR = '#FFF9B1'
ACTION_COLOR = '#B19CD9'
END_COLOR = '#77DD77'
ERROR_COLOR = '#FF6961'

# Add nodes
dot.node('start', 'Start', shape='oval', fillcolor=START_COLOR)
dot.node('ci_platform', 'Is your CI platform a SaaS\nsolution such as gitlab.com or\ndo you self-host your CI\nplatform?', shape='diamond', fillcolor=DECISION_COLOR)
dot.node('self_hosted', 'Can your self-hosted CI\nagents run Linux containers?\nThis can either be directly as a\nrunner image or via `docker run`\nin a script', shape='diamond', fillcolor=DECISION_COLOR)
dot.node('saas_agents', 'Are you using the hosted agents\nfrom the SaaS provider or self-\nhosting your own agents?', shape='diamond', fillcolor=DECISION_COLOR)
dot.node('ash_supported', 'You should be able to run ASH\ndirectly in your SaaS CI platform\'s supported\ncontainer job mechanisms, as most\nhosted agents support at least `docker`', fillcolor=ACTION_COLOR)
dot.node('container_registry', 'Do you have a private\ncontainer registry such\nas AWS ECR or GitLab\nContainer Registry that you can\npublish images to?', shape='diamond', fillcolor=DECISION_COLOR)
dot.node('no_registry', 'In order to internalize the ASH image,\nyou need an internally available private registry to\npublish the image to first!\n\nWe recommend Amazon ECR:\nhttps://aws.amazon.com/ecr/', fillcolor=ERROR_COLOR)
dot.node('ash_requires', 'ASH requires the ability to run Linux\ncontainers in order to use it for code\nscanning.', fillcolor=ERROR_COLOR)
dot.node('internal_process', 'At this point, you will need to\nfollow your internal processes to publish the\nASH image to your private registry.\nOnce the image has been published, proceed.', fillcolor=ACTION_COLOR)
dot.node('congratulations', 'Congratulations! You should be able to support\nexecution of ASH scans as part of your CI pipeline. You\nwill need to use the internal private image and desired\ntag when configuring your ASH scan job in your CI.', fillcolor=END_COLOR)

# Add edges
dot.edge('start', 'ci_platform')
dot.edge('ci_platform', 'self_hosted', 'Self-hosted')
dot.edge('ci_platform', 'saas_agents', 'SaaS')
dot.edge('saas_agents', 'ash_supported', 'Using SaaS Hosted Agents')
dot.edge('saas_agents', 'self_hosted', 'Using self-hosted\nagents with SaaS CI')
dot.edge('self_hosted', 'container_registry', 'Yes, we can run Linux containers\nin our self-hosted CI agents')
dot.edge('self_hosted', 'ash_requires', 'No, we cannot use\nLinux containers\nin our self-hosted\nCI agents')
dot.edge('container_registry', 'no_registry', 'No, we do not\nhave a private\nregistry available')
dot.edge('container_registry', 'internal_process', 'Yes we have an internal\nprivate registry for\nLinux container images.')
dot.edge('internal_process', 'congratulations', 'ASH container image\nhas been published to\nyour internal private registry')
dot.edge('ash_supported', 'container_registry')

# Render the graph
dot.render('ash_ci_execution_viability', format='png', cleanup=True)
print("Flowchart has been generated as 'ash_ci_execution_viability.png'")