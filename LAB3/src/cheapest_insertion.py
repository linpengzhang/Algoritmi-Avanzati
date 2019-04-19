from Graph_FromFile import GraphFromFile
def cheapest_insertion(G):
    C = [0]
    #min_w = min(x for x in G.graph[0] if x>1)
    min_w = min(G.graph[0])
    min_index = G.graph[0].index(min_w)
    C.append(min_index)
    C.append(0)
    result = 2*min_w
    V = {i for i in range(1, G.number_of_nodes())}
    V.remove(min_index)
    for _ in range(2, G.number_of_nodes()):
        min_w = float("inf")
        for k in V:
            for i in range(len(C)-1):
                j=i+1
                actual_w = G.graph[C[i]][k] + G.graph[k][C[j]] - G.graph[C[i]][C[j]]
                if actual_w<min_w:
                    min_w = actual_w
                    ii = C[i]
                    jj = C[j]
                    kk = k
        result = result + min_w
        V.remove(kk)
        C.insert(C.index(jj),kk)
    return result