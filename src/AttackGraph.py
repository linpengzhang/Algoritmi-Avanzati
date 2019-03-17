from Graph import Graph
import random


class AttackGraphs:
    """
    Class that contains the attack functions used against the Graph
    """

    def remove_node(self, g: Graph, node: int):
        """
        Removes the specified node from the graph g
        """
        for v in g.graph[node]:
            g.graph[v].discard(node)
        del g.graph[node]

    def casual_attack(self, g: Graph):
        """
        :return: Values of resilience of the graph g after disabling each node in a casual order
        """
        res_values = [g.max_size_connected_component()]
        for _ in range(g.number_of_nodes()):
            r = random.choice(list(g.graph.keys()))
            self.remove_node(g, r)
            res_values.append(g.max_size_connected_component())
        return res_values

    def ordered_attack(self, g: Graph):
        """
        :return: Values of resilience of the graph g after disabling each node in an ordered way
        """
        order = [k for k, _ in sorted(g.graph.items(), key=lambda k_v: len(k_v[1]), reverse=True)]
        res_values = [g.max_size_connected_component()]
        for i in order:
            self.remove_node(g, i)
            res_values.append(g.max_size_connected_component())
        return res_values
