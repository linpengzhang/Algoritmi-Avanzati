from threading import Timer
import time

from Graph_FromFile import GraphFromFile
from collections import defaultdict

stop_searching = False


def timeout():
    global stop_searching
    stop_searching = True
    print("Held karp exceeded time, stopping and returning...")


def hk_visit(g: GraphFromFile, v, S, d):
    """
    restituisce il peso del cammino minimo da 0 a v che visita tutti i vertici in S
    """
    global stop_searching
    if S == frozenset([v]):
        return g.graph[v][0]
    elif d[(v, S)] is not None:
        return d[(v, S)]
    else:
        min_dist = float("inf")
        for u in S.difference({v}):
            dist = hk_visit(g, u, S.difference({v}), d)
            if dist + g.graph[u][v] < min_dist:
                min_dist = dist + g.graph[u][v]
            if stop_searching:
                break
        d[(v, S)] = min_dist
        return min_dist


def hk_tsp(g: GraphFromFile):
    start = time.time()
    global stop_searching
    stop_searching = False
    t = Timer(60.0, timeout)
    t.start()
    d = defaultdict(lambda: None)
    result = hk_visit(g, 0, g.set_of_nodes(), d)
    t.cancel()
    end = time.time()
    return [result, end - start]
