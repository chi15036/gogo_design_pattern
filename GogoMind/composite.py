from component import Component

class Composite(Component):
    id = 0
    description = 'test'
 
    def add_child(self, node):
        pass
 
    def add_sibling(self, node):
        pass

    def get_children(self):
        pass
 
    def get_map(self):
        pass


if __name__ == '__main__':
    a = Composite()
    print(a)