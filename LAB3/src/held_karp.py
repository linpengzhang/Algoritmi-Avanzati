from Graph_FromFile import GraphFromFile
from collections import defaultdict


def hk_visit(g: GraphFromFile, v, S, d, p):
    """
    restituisce il peso del cammino minimo da 0 a v che visita tutti i vertici in S
    """
    if S == frozenset([v]):
        return g.graph[v][0]
    elif d[(v, S)] is not None:
        return d[(v, S)]
    else:
        mindist = float("inf")
        minprec = None
        for u in S.difference({v}):
            dist = hk_visit(g, u, S.difference({v}), d, p)
            if dist + g.graph[u][v] < mindist:
                mindist = dist + g.graph[u][v]
                minprec = u
        d[(v, S)] = mindist
        p[(v, S)] = minprec
        return mindist


def hk_tsp(g: GraphFromFile):
    d = defaultdict(lambda: None)
    p = defaultdict()
    return hk_visit(g, 0, g.set_of_nodes(), d, p)
