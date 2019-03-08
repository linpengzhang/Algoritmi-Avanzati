from Graph import Graph
import random


class GraphRandomER(Graph):
    """
    Class that randomly generate a ER graph
    """

    def __init__(self, number_of_nodes: int, p: float):
        Graph.__init__(self)
        self.generate_random_er(number_of_nodes, p)

    def generate_random_er(self, number_of_nodes: int, p: float):
        for u in range(0, number_of_nodes):
            self.graph[u] = set()
        for u in range(0, number_of_nodes - 1):
            for v in range(u + 1, number_of_nodes):
                a = random.random()
                if a < p:
                    self.graph[u] |= {v}
                    self.graph[v] |= {u}
