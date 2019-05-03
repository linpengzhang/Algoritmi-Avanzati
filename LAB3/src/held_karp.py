from threading import Timer
import time

from Graph_FromFile import GraphFromFile
from collections import defaultdict

stop_searching = False


def timeout():
    global stop_searching
    stop_searching = True
    print("Held karp exceeded time, stopping and returning...")


def hk_visit(g: GraphFromFile, v, S, d, p):
    """
    restituisce il peso del cammino minimo da 0 a v che visita tutti i vertici in S
    """
    global stop_searching
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
            if stop_searching:
                break;
        d[(v, S)] = mindist
        p[(v, S)] = minprec
        return mindist


def hk_tsp(g: GraphFromFile):
    start = time.time()
    global stop_searching
    stop_searching = False
    t = Timer(60.0, timeout)
    t.start()
    d = defaultdict(lambda: None)
    p = defaultdict()
    result = hk_visit(g, 0, g.set_of_nodes(), d, p)
    t.cancel()
    end = time.time()
    return [result, end - start]
