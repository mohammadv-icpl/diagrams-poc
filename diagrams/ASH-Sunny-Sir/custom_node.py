from diagrams import Node

class CustomNode(Node):
    def __init__(self, label, **kwargs):
        super().__init__(label, **kwargs)

    def _load_icon(self):
        pass