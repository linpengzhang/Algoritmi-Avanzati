from Graph_FromFile import GraphFromFile
import numpy as np
import random
import matplotlib.pyplot as plt


def random_insertion(G):
    # C memorizza il circuito
    # parto dal circuito parziale composto dal solo nodo 0
    C = [0]
    # V contiene i vertici non ancora presenti nel circuito parziale
    V = {i for i in range(1, G.number_of_nodes())}
    # trovo un vertice j che minimizza la distanza w(0,j)
    j = np.argmin(G.graph[0][1:]) + 1
    V.remove(j)
    # costruisco il circuito parziale (0,j,0)
    C.append(j)
    C.append(0)
    # itero per tutti gli altri nodi rimanenti
    for _ in range(2, G.number_of_nodes()):
        # scelgo un casuale vertice k non presente nel circuito parziale
        k = random.sample(V, 1)[0]
        min_w = float("inf")
        # cerco un arco {i,j} del circuito parziale che minimizza la distanza
        # w(i,k)+w(k,j)-w(i,j)
        for ii in range(len(C) - 1):
            i = C[ii]
            j = C[ii + 1]
            actual_w = G.graph[i][k] + G.graph[k][j] - G.graph[i][j]
            if actual_w < min_w:
                min_w = actual_w
                idx_j = ii + 1  # indice al quale inserire k in C
        # inserisco k tra i e j
        C.insert(idx_j, k)
        V.remove(k)
    # calcola il peso del circuito trovato
    result = 0
    for v in range(len(C) - 1):
        result += G.graph[C[v]][C[v + 1]]
    # plot_circuit(G, C)
    return result


def cheapest_insertion(G):
    # C memorizza il circuito
    # parto dal circuito parziale composto dal solo nodo 0
    C = [0]
    # V contiene i vertici non ancora presenti nel circuito parziale
    V = {i for i in range(1, G.number_of_nodes())}
    # trovo un vertice j che minimizza la distanza w(0,j)
    j = np.argmin(G.graph[0][1:]) + 1
    V.remove(j)
    # costruisco il circuito parziale (0,j,0)
    C.append(j)
    C.append(0)
    # NOTA: non posso calcolare subito il risultato perche' inserendo nodi nel mezzo del cammino certi archi non li considero piu'!
    # itero per tutti gli altri nodi rimanenti
    for _ in range(2, G.number_of_nodes()):
        # trovo un vertice k non presente nel circuito parziale e un arco {i,j}
        # del circuito parziale che minimizzano la distanza w(i,k)+w(k,j)-w(i,j)
        min_w = float("inf")
        for k in V:
            for ii in range(len(C) - 1):
                i = C[ii]
                j = C[ii + 1]
                actual_w = G.graph[i][k] + G.graph[k][j] - G.graph[i][j]
                if actual_w < min_w:
                    min_w = actual_w
                    idx_j = ii + 1  # indice al quale inserire k in C
                    found_k = k  # vertice k da aggiungere
        # inserisco k tra i e j
        C.insert(idx_j, found_k)
        V.remove(found_k)
    # calcola il peso del circuito trovato
    result = 0
    for v in range(len(C) - 1):
        result += G.graph[C[v]][C[v + 1]]
    # plot_circuit(G, C)
    return result


def nearest_neighbor(G: GraphFromFile):
    # C memorizza il circuito
    # parto dal circuito parziale composto dal solo nodo 0
    C = [0]
    result = 0
    # V contiene i vertici non ancora presenti nel circuito parziale
    V = {i for i in range(1, G.number_of_nodes())}
    # itero per tutti gli altri nodi rimanenti
    for _ in range(1, G.number_of_nodes()):
        # trovo un vertice k non ancora inserito nel circuito a distanza minima dall'ultimo inserito
        min_d = float('inf')
        last = C[len(C) - 1]
        for i in V:
            if G.graph[last][i] < min_d:
                min_d = G.graph[last][i]
                k = i
        # inserisco il vertice trovato
        V.remove(k)
        C.append(k)
        result += G.graph[last][k]
    # creo il collegamento tra l'ultimo vertice inserito e il primo
    C.append(0)
    result += G.graph[last][0]
    # plot_circuit(G, C)
    return result


def plot_circuit(G: GraphFromFile, C):
    x_coord = list(map(lambda v: G.node_coords[v][0], C))
    y_coord = list(map(lambda v: G.node_coords[v][1], C))
    plt.plot(x_coord, y_coord, marker="o")
    plt.show()
