from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = [[]]
    def number_of_nodes(self):
        """
        :return: Return the number of nodes (stations) in the graph
        """
        return len(self.graph)
    def set_of_nodes(self):
        return frozenset(range(self.number_of_nodes))
    def list_of_nodes(self):
        return list(range(self.number_of_nodes))
