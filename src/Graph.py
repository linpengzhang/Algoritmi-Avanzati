from collections import defaultdict


class Graph:
    """
    Class used to represent a undirected graph using a Python Dictionary
    """

    def __init__(self):
        self.graph = defaultdict(set)

    def sum_all_degrees(self):
        """
        :return: Return a sum of all nodes degrees in the graph
        """
        return sum(len(self.graph.get(i)) for i in self.graph)

    def average_nodes_degree(self):
        """
        :return: Return the average degree between the nodes in the graph
        """
        return self.sum_all_degrees() / self.number_of_nodes()

    def number_of_nodes(self):
        """
        :return: Return the number of nodes in the graph
        """
        return len(self.graph)

    def number_of_edges(self):
        """
        :return: Return the number of edges in the graph
        """
        return sum(len(self.graph.get(i)) for i in self.graph.keys()) / 2

    def connected_components(self):
        color = {v: "white" for v in self.graph.keys()}
        cc = []
        for v in self.graph.keys():
            if color[v] == "white":
                comp = self.dfs_visited(color, v, set())
                cc.append(comp)
        return cc

    def dfs_visited(self, color, u, visited):
        color[u] = "gray"
        visited.add(u)
        for v in self.graph[u]:
            if color[v] == "white":
                visited = self.dfs_visited(color, v, visited)
        color[u] = "black"
        return visited
