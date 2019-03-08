from Graph import Graph
import random


class GraphRandomUPA(Graph):
    """
    Class that randomly generate a UPA graph
    """

    def __init__(self, number_of_nodes: int, m: int):
        Graph.__init__(self)
        self.generate_random_er(number_of_nodes, m)

    def generate_random_er(self, number_of_nodes: int, m: int):
        num_nodes = 0
        node_numbers = []

        def upa_trial(m: int):
            nonlocal num_nodes
            nonlocal node_numbers
            num_nodes = m
            node_numbers = []
            for upa_trial_index in range(m):
                node_numbers = node_numbers + [upa_trial_index for j in range(m)]

        def run_trial(m: int):
            nonlocal num_nodes
            nonlocal node_numbers
            v1 = set()
            for i in range(1, m + 1):
                v1.add(random.choice(node_numbers))
            node_numbers.append(num_nodes)
            node_numbers = node_numbers + [j for j in v1]
            num_nodes += 1
            return v1

        for u in range(0, m):
            self.graph[u] = set()
        for u in range(0, m - 1):
            for v in range(u + 1, m):
                self.graph[u] |= {v}
                self.graph[v] |= {u}
        upa_trial(m)
        for u in range(m, number_of_nodes):
            v1 = run_trial(m)
            self.graph[u] = set(v1)
            for i in v1:
                self.graph[i] |= {u}
