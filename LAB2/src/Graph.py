from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(set))

    def number_of_nodes(self):
        """
        :return: Return the number of nodes (stations) in the graph
        """
        return len(self.graph)

    def dict_of_nodes(self):
        """
        :return: Return keys of the graph (stations)
        """
        return self.graph.keys()

    def add_edge(self, from_node, to_node, edge):
        """
        :return: Add an edge (route) between two nodes (stations)
        """
        self.graph[from_node][to_node].add(edge)

    def add_node(self, node):
        """
        :return: Add a node (station) to the graph
        """
        self.graph[node] = defaultdict(set)