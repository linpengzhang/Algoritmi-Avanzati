from Graph import Graph
import random


class GraphRandomUPA(Graph):
    """
    Class that randomly generate a UPA graph
    """

    def __init__(self, number_of_nodes: int, m: int):
        Graph.__init__(self)
        self.generate_random_upa(number_of_nodes, m)

    def generate_random_upa(self, number_of_nodes: int, upa_m: int):
        num_nodes = 0
        node_numbers = []

        def upa_trial(m: int):
            nonlocal num_nodes
            nonlocal node_numbers
            num_nodes = m
            node_numbers = []
            for upa_trial_index in range(m):
                node_numbers.extend([upa_trial_index for _ in range(m)])

        def run_trial(m: int):
            nonlocal num_nodes
            nonlocal node_numbers
            v1 = set()
            for _ in range(m):
                v1.add(random.choice(node_numbers))
            node_numbers.append(num_nodes)
            node_numbers.extend(v1)
            num_nodes += 1
            return v1

        for u in range(0, upa_m):
            self.graph[u] = {v for v in range(0, upa_m) if v != u}
        upa_trial(upa_m)
        for u in range(upa_m, number_of_nodes):
            v1 = run_trial(upa_m)
            self.graph[u] = v1
            for i in v1:
                self.graph[i].add(u)
