from Graph_FromFile import GraphFromFile
import numpy as np
import random

def random_insertion(G):
    # C memorizza il circuito
    # parto dal circuito parziale composto dal solo nodo 0
    C = [0]
    # V contiene i vertici non ancora presenti nel circuito parziale
    V = {i for i in range(1, G.number_of_nodes())}
    # trovo un vertice j che minimizza la distanza w(0,j)
    j = np.argmin(G.graph[0][1:])+1
    V.remove(j)
    # costruisco il circuito parziale (0,j,0)
    C.append(j)
    C.append(0) 
    # itero per tutti gli altri nodi rimanenti
    for _ in range(2, G.number_of_nodes()):
        # scelgo un casuale vertice k non presente nel circuito parziale
        k = random.sample(V,1)[0]
        min_w = float("inf")
        # cerco un arco {i,j} del circuito parziale che minimizza la distanza
        # w(i,k)+w(k,j)-w(i,j)
        for ii in range(len(C)-1):
            i = C[ii]
            j = C[ii+1]
            actual_w = G.graph[i][k] + G.graph[k][j] - G.graph[i][j]
            if actual_w < min_w:
                min_w = actual_w
                idx_j = ii+1 # indice al quale inserire k in C
        # inserisco k tra i e j
        C.insert(idx_j,k)
        V.remove(k)
    # calcola il peso del circuito trovato
    result = 0
    for i in range(len(C)-1):
        result += G.graph[C[i]][C[i+1]]
    return result