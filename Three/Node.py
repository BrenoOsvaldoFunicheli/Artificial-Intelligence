class Node:

    def __init__(self, value, successor=[], father=None, cost=None):
        self.value = value
        self.successor = successor
        self.father = father

    def __eq__(self, other):
        return self.value == other.value

    def set_successor(self, value=None, l_list=None):
        if l_list is not None:
            self.insert_list(l_list)
        elif value is not None:
            self.insert_successor(value)
        else:
            raise Exception("You don't setting successor")

    def insert_successor(self, value):
        value.father = self
        self.successor.append(value)

    def insert_list(self, l_successor):
        for v in l_successor:
            self.insert_successor(v)

    def get_successor(self):
        return self.successor
