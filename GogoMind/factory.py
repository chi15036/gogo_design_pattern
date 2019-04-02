from root import Root
from node import Node

class SimpleNodeFactory():
    def create_node(is_root):
        node = Node()
        if is_root:
            node = Root()
        return node
