import abc
 
class Component(metaclass=abc.ABCMeta):

    @property
    def id(self):
        return NotImplemented

    @property
    def description(self):
        return NotImplemented
 
    @abc.abstractmethod
    def add_child(self, node):
        return NotImplemented
 
    @abc.abstractmethod
    def add_sibling(self, node):
        return NotImplemented

    @abc.abstractmethod
    def get_children(self):
        return NotImplemented