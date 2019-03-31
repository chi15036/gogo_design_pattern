import abc
 
class Component(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def id(self):
        return NotImplemented

    @property
    @abc.abstractmethod
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
 
    @abc.abstractmethod
    def get_map(self):
        return NotImplemented