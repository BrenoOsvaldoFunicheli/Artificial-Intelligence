from Three.Search.Search import Search


class BreathSearch(Search):

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
        if s_current == objective:
            return s_current

        while s_current is not None:
            for i in s_current.get_successor():
                if i == objective:
                    return i
                self.s_queue.append(i)

            s_current = self.s_queue.pop()


