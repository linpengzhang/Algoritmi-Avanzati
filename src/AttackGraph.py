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
        res_values = []
        res_values.append(self.calc_resilience(g))
        for _ in range(g.number_of_nodes()):
            r = random.choice(list(g.graph.keys()))
            self.remove_node(g, r)
            res_values.append(self.calc_resilience(g))
        return res_values

    def ordered_attack(self, g: Graph):
        order = [k for k, _ in sorted(g.graph.items(), key=lambda k_v: len(k_v[1]), reverse=True)]
        res_values = []
        res_values.append(self.calc_resilience(g))
        for i in order:
            self.remove_node(g, i)
            res_values.append(self.calc_resilience(g))
        return res_values

    def calc_resilience(self, g:Graph):
        return max(list(map(len,g.connected_components())), default=0)

    # def calc_resilience(self, g: Graph):
    #     visited = {i: False for i in g.graph.keys()}
    #     max_res = 0
    #     for i in g.graph.keys():
    #         if not visited[i]:
    #             t_res = self.dfs_visited(g, i, 0, visited)
    #             if t_res > max_res:
    #                 max_res = t_res
    #     return max_res

    # def dfs_visited(self, g, u, n, visited):
    #     visited[u] = True
    #     n = n+1
    #     for v in g.graph[u]:
    #         if not visited[v]:
    #             n = self.dfs_visited(g, v, n, visited)
    #     return n
