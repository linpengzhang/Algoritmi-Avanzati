from Graph_FromFile import GraphFromFile
def prim_mst(G, w,r):
    """
    G: grafo connesso non orientato pesato
    w: peso
    r: vertice in V
    """
    for v in G.graph:
        key[v] = float("inf")
        p[v] = None
    key[r] = 0
    Q = G.list_of_nodes()
    while len(Q)>0:
        min_key = min(key)
        for v in G.graph[key.index(min_key)]:
            if v in Q and w[u][v] < key[v]:
                key[v] = w[u][v]
                p[v] = u
