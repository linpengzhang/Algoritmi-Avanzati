from Graph_FromFile import GraphFromFile
from collections import defaultdict

def hk_visit(G, v, S, d, p):
    """
    restituisce il peso del cammino minimo da 0 a v che visita tutti i vertici in S
    """
    if S == frozenset([v]):
        return G.graph[v][0]
    elif (v, S) in d.keys():
        return d[(v,S)]
    else:
        mindist = float("inf")
        minprec = None
        for u in S.difference({v}):
            dist = hk_visit(G,u,S.difference({v}),d,p)
            if dist + G.graph[u][v] < mindist:
                mindist = dist + G.graph[u][v]
                minprec = u
        d[(v,S)] = mindist
        p[(v,S)] = minprec
        return mindist

def hk_tsp(G: GraphFromFile):
    d = defaultdict()
    p = defaultdict()
    return hk_visit(G, 0, G.set_of_nodes(), d, p)