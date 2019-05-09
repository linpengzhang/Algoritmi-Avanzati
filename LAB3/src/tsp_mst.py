from Graph_FromFile import GraphFromFile
from collections import defaultdict

import time


def prim_mst_completo(g):
    """
    g: grafo completo non orientato pesato
    g.graph: matrice delle adiacenze di g contenente i pesi di tutti gli archi
    :return: albero di copertura minimo (nodo di partenza: 0)
    """
    # utilizzo l'algoritmo di prim per il problema dell'albero di copertura minimo
    key = {i: float('inf') for i in range(g.number_of_nodes())}
    p = [None for _ in range(g.number_of_nodes())]
    key[0] = 0
    # key: contiene le priorità dei nodi rimanenti
    while len(key) > 0:
        # estraggo il nodo con valore associato minimo
        u = _extract_min(key)
        # essendo il grafo completo, considero tutti i nodi ancora presenti in key
        for v in key.keys():
            if g.graph[u][v] < key[v]:
                key[v] = g.graph[u][v]  # decrease key
                p[v] = u
    # creo l'albero di copertura minimo, rappresentato come lista delle adiacenze
    mst = defaultdict(set)
    for i in range(1, g.number_of_nodes()):
        mst[i].add(p[i])
        mst[p[i]].add(i)
    return mst


def _extract_min(d):
    u = None
    current_min = float("inf")
    for i in d.keys():
        if d[i] < current_min:
            current_min = d[i]
            u = i
    d.pop(u)
    return u


def dfs_visited_tree(tree, visited, u, path):
    visited[u] = True
    path.append(u)
    for v in tree[u]:
        if not visited[v]:
            dfs_visited_tree(tree, visited, v, path)
    return path


def mst_approx(g: GraphFromFile):
    """
    :return: soluzione approssimata di tsp (usando mst)
    """
    # mst: l'albero di copertura minimo
    start = time.time()
    mst = prim_mst_completo(g)
    visited = [False for i in range(g.number_of_nodes())]
    # path: sequenza dei nodi ottenuta da una visita in profondità a mst
    path = dfs_visited_tree(mst, visited, 0, [])
    path.append(0)
    # calcolo la soluzione di tsp dal circuito ottenuto
    tsp_sum = 0
    for i in range(len(path) - 1):
        tsp_sum = tsp_sum + g.graph[path[i]][path[i + 1]]
    end = time.time()
    return [tsp_sum, end - start]
