import abc


class Search(abc.ABC):

    def __init__(self):
        self.way = []

    @abc.abstractmethod
    def search(self,  node, objective):
        pass
    """
    :node: need object node for find in the tree
    :arg: 
    """

