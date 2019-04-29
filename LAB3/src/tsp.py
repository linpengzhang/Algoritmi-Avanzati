from Graph_FromFile import GraphFromFile
from collections import defaultdict


def prim_mst_completo(G):
    """
    G: grafo completo non orientato pesato
    G.graph: matrice delle adiacenze di G
    :return: albero di copertura minimo
    """
    key = defaultdict()
    p = defaultdict()
    for v in range(1, G.number_of_nodes()):
        key[v] = float("inf")
        p[v] = None
    key[0] = 0
    while len(key) > 0:
        current_min = float("inf")
        for i in key.keys():
            if key[i] < current_min:
                u = i
        key.pop(u)
        for v in key.keys():
            if G.graph[u][v] < key[v]:
                key[v] = G.graph[u][v]
                p[v] = u
    Adj = defaultdict(set)
    for i in range(1, G.number_of_nodes()):
        Adj[i].add(p[i])
        Adj[p[i]].add(i)
    return Adj


def dfs_visited_tree(Adj, visited, u, path):
    visited[u] = True
    path.append(u)
    for v in Adj[u]:
        if not visited[v]:
            dfs_visited_tree(Adj, visited, v, path)
    return path


def tsp(g: GraphFromFile):
    Adj = prim_mst_completo(g)
    visited = [False for i in range(g.number_of_nodes())]
    path = dfs_visited_tree(Adj, visited, 0, [])
    path.append(0)
    tsp_sum = 0
    for i in range(len(path) - 1):
        tsp_sum = tsp_sum + g.graph[path[i]][path[i + 1]]
    return tsp_sum
