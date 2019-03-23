from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(set))

    def number_of_nodes(self):
        """
        :return: Return the number of nodes in the graph
        """
        return len(self.graph)

    def dict_of_nodes(self):
        return self.graph.keys()

    def add_edge(self, from_node, to_node, edge):
        self.graph[from_node][to_node].add(edge)
