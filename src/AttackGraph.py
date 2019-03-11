from Graph import Graph
import random
import collections

class AttackGraphs:
    """
    Class that contains the attack functions used against the Graph
    """

    def casual_remove(self, g: Graph):
        r = random.choice(list(g.graph.keys()))
        for v in g.graph[r]:
            g.graph[v].discard(r)
        del g.graph[r]

    def casual_attack(self, g: Graph):
        n = len(g.graph)
        y = collections.deque()
        y.append(self.calc_resilience(g))
        for _ in range(n):
            self.casual_remove(g)
            y.append(self.calc_resilience(g))
        return y

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

    # def dfs_visited(g, u, n, visited):
    #     visited[u] = True
    #     n = n+1
    #     for v in g[u]:
    #         if not visited[v]:
    #             n = dfs_visited(g, v, n, visited)
    #     return n

    def ordered_attack(self, g: Graph):
        order = [k for k, _ in sorted(g.graph.items(), key=lambda k_v: len(k_v[1]), reverse=True)]
        y = collections.deque()
        y.append(self.calc_resilience(g))

        for i in order:
            for v in g.graph[i]:
                g.graph[v].discard(i)
            del g.graph[i]

            y.append(self.calc_resilience(g))
        return y
