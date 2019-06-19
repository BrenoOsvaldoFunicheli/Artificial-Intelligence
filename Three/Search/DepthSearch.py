from Three.Search.Search import Search
from queue import Queue


class DepthSearch(Search):

    def __init__(self):
        super().__init__()
        self.s_queue = []

    def search(self, node, objective):
        """
        :param node: This param is node of the tree or graph
        :param objective: Contains an objective node for search
        :return:
        """

        s_current = node

        while (not (s_current == objective)) and (s_current is not None):
            """
            While current state is different from the target 
            State or nonzero then it places the value on the stack.
            """

            for i in s_current.get_successor():
                """"
                Iterate of the list of successors  
                """
                self.s_queue.append(i)
            s_current = self.s_queue.pop()

        if s_current is not None:
            self.way.append(s_current)

            while s_current.father is not None:
                s_current = s_current.father
                self.way.append(s_current)

        for i in self.way:
            print(i.value)
