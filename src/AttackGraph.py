from Graph import Graph
import random


class AttackGraphs:
    """
    Class that contains the attack functions used against the Graph
    """

    def remove_node(self, g: Graph, node: int):
        for v in g.graph[node]:
            g.graph[v].discard(node)
        del g.graph[node]

    def casual_attack(self, g: Graph):
        res_values = [self.calc_resilience(g)]
        for _ in range(g.number_of_nodes()):
            r = random.choice(list(g.graph.keys()))
            self.remove_node(g, r)
            res_values.append(self.calc_resilience(g))
        return res_values

    def ordered_attack(self, g: Graph):
        order = [k for k, _ in sorted(g.graph.items(), key=lambda k_v: len(k_v[1]), reverse=True)]
        res_values = [self.calc_resilience(g)]
        for i in order:
            self.remove_node(g, i)
            res_values.append(self.calc_resilience(g))
        return res_values

    def calc_resilience(self, g: Graph):
        return max(list(map(len, g.connected_components())), default=0)
