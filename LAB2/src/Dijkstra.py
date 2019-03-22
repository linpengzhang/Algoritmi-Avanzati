from Graph import Graph
import heapq


class Dijkstra:

    def initsssp(self, s, inizio, g: Graph):
        d = {}
        p = {}
        for v in g.graph.keys():
            d[v] = 100000
            p[v] = (-1, -1)
        d[s] = inizio
        return d, p

    def relax(self, u, v, edge, d, p):
        d[v] = edge.time_arrival
        p[v] = (u, edge)

    def dijkstrasssp(self, s, inizio, g: Graph):
        d, p = self.initsssp(s, inizio, g)
        Q = []
        for i in g.nodes():
            heapq.heappush(Q, (d[i], i))
        while len(Q) > 0:
            u = heapq.heappop(Q)[1]  # estraggo nodo con tempo di arrivo minimo
            for v in g.graph[u].keys():
                min_element = 100000
                for edge in g.graph[u][v]:
                    if d[u] <= edge.time_departure:
                        if edge.time_arrival < min_element:
                            min_element = edge.time_arrival
                            best_edge = edge
                if min_element < 100000 and best_edge.time_arrival < d[v]:
                    self.relax(u, v, best_edge, d, p)

                    for i in range(len(Q)):  # equivalente a decreasekey(Q,v,d[v]) da implementare meglio
                        if Q[i][1] == v:
                            Q[i] = (d[v], v)
                    heapq.heapify(Q)

        print(d["300000044"])
        return d
