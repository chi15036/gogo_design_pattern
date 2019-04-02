from component import Component

class Composite(Component):
    id = 0
    description = 'init'
    x = 0
    y = 0
    def __init__(self):
        self.child_list = []

    def add_child(self, node):
        self.child_list.append(node)

    def add_sibling(self, node):
        pass

    def get_children(self):
        return self.child_list


if __name__ == '__main__':
    a = Composite()
    print(a)