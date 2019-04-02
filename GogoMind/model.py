from factory import SimpleNodeFactory

class MindMapModel():
    serial_num = 0
    mind_map = []

    def create_node(self, desc, is_root):
        node = SimpleNodeFactory.create_node(is_root)
        node.description = desc
        node.id = self.serial_num
        self.mind_map.append(node)
        self.serial_num += 1
        return node
    
    def insert_node(self, parent_id, node):
        for parent_node in self.mind_map:
            if int(parent_node.id) == int(parent_id):
                node.x = parent_node.x + 300
                node.y = len(parent_node.child_list) * 150
                parent_node.add_child(node)
        print(node.x)
        print(node.y)
        return node

    def create_mind_map(self, desc):
        pass

    def save_mind_map(self):
        pass