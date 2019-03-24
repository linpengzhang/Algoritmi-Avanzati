from Graph import Graph
import MyHeap


class Dijkstra:
    """
    il grafo è rappresentato come dizionario (nodi di partenza) di un dizionario (nodi adiacenti, di arrivo) di insiemi (archi tra due nodi)
    - un nodo del grafo rappresenta una stazione
    - un arco del grafo corrisponde ad una tratta tra due stazioni di una certa corsa ad un certo orario
    - il peso dei cammini è dato dall'orario di arrivo presso il nodo (stazione)
    """

    def initsssp(self, s, inizio, g: Graph):
        d = {} # peso dei cammini (il peso corrisponde all'ora di arrivo)
        p = {} # predecessore nel cammino (coppia nodo predecessore e arco utilizzato)
        for v in g.graph.keys():
            d[v] = float("inf")
            p[v] = (None, None)
        d[s] = inizio # il valore iniziale è l'ora dalla quale poter partire
        return d, p

    def relax(self, u, v, edge, d, p):
        d[v] = edge.time_arrival
        p[v] = (u, edge)

    def dijkstrasssp(self, s, inizio, g: Graph):
        d, p = self.initsssp(s, inizio, g) # inizializzazione di: d, p
        # coda di priorità Q (heap binaria)
        # i valori sono coppie (peso, nodo) il cui ordine si basa sul primo valore
        Q = [(d[i],i) for i in g.dict_of_nodes()] # inizializzazione di Q
        MyHeap.heapify(Q) # rende Q una heap binaria
        # iterazione per ciascun elemento di Q
        while len(Q) > 0:
            u = MyHeap.heappop(Q)[1]  # estraggo nodo con tempo di arrivo minimo
            # considero ciascun nodo adiacente al nodo di partenza u
            for v in g.graph[u].keys():
                # cerco l'arco che mi permette di arrivare prima possibile al successivo nodo v
                min_element = float("inf")
                for edge in g.graph[u][v]:
                    # MA considero solo gli archi ammissibili: l'orario di partenza non deve essere
                    # antecedente all'orario di arrivo alla stazione di partenza u
                    if d[u] <= edge.time_departure:
                        if edge.time_arrival < min_element:
                            min_element = edge.time_arrival
                            best_edge = edge
                # se (min_element == float("inf")) => non c'è un arco ammissibile tra i due nodi
                if min_element < float("inf") and best_edge.time_arrival < d[v]:
                    # trovato un arco teso
                    self.relax(u, v, best_edge, d, p)

                    for i in range(len(Q)):  # equivalente a decreasekey(Q,v,d[v]) da implementare meglio
                        if Q[i][1] == v:
                            Q[i] = (d[v], v)
                    MyHeap.heapify(Q)

        return d, p
