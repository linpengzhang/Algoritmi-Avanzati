from Graph import Graph
from MyHeap import MyHeap
from collections import deque

"""
il grafo è rappresentato come dizionario (nodi di partenza) di un dizionario (nodi adiacenti, di arrivo) di insiemi (archi tra due nodi)
- un nodo del grafo rappresenta una stazione
- un arco del grafo corrisponde ad una tratta tra due stazioni di una certa corsa ad un certo orario
- il peso dei cammini è dato dall'orario di arrivo presso il nodo (stazione)
"""

def initsssp(s, inizio, g: Graph):
    d = {} # peso dei cammini (il peso corrisponde all'ora di arrivo)
    p = {} # predecessore nel cammino (coppia nodo predecessore e arco utilizzato)
    for v in g.graph.keys():
        d[v] = float("inf")
        p[v] = (None, None)
    d[s] = inizio # il valore iniziale è l'ora dalla quale poter partire
    return d, p

def relax(u, v, edge, d, p):
    d[v] = edge.time_arrival
    p[v] = (u, edge)

def dijkstrasssp(s, inizio, g: Graph):
    d, p = initsssp(s, inizio, g) # inizializzazione di: d, p
    # coda di priorità Q (heap binaria)
    # i valori sono coppie (peso, nodo) il cui ordine si basa sul primo valore
    Q = MyHeap(d,g.dict_of_nodes())
    # iterazione per ciascun elemento di Q
    while len(Q) > 0:
        u = Q.extract_min() # estraggo nodo con tempo di arrivo minimo
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
                # caso in cui si prenda una corsa che PARTE il giorno successivo - da controllare
                # elif d[u] <= edge.time_departure + 2400:
                #     if edge.time_arrival + 2400 < min_element:
                #         min_element = edge.time_arrival + 2400
                #         best_edge = edge
            # se (min_element == float("inf")) => non c'è un arco ammissibile tra i due nodi
            if min_element < float("inf") and best_edge.time_arrival < d[v]:
                # trovato un arco teso
                relax(u, v, best_edge, d, p)
                Q.decrease_key(v,d[v])
    return d, p

"""
def getPercorso(p, partenza, arrivo):
    # p[arrivo] != (None, None)
    if partenza == arrivo:
        return [partenza]
    percorso = getPercorso(p, partenza, p[arrivo][0])
    percorso.append(arrivo)
    return percorso
"""

def get_path(p, origin, destination):
    """
    :return: List of tuples (node, possible edge) composing the path from origin to destination
    """
    # input: dict p: predecessore di ciascun nodo nel cammino (coppia nodo predecessore e arco utilizzato)
    path = deque()
    # verifico che la destinazione sia raggiungibile
    if p[destination] != (None, None):
        # aggiungo l'ultimo nodo (stazione) del cammino che non ha archi successivi
        path.append((destination,None))
        current_station = destination
        # procedo a ritroso fino ad arrivare alla stazione di origine
        while current_station != origin:
            previous_station = p[current_station][0]
            previous_route = p[current_station][1]
            # aggiungo il nodo (stazione) precedente e l'arco (tratta) precedenti nel percorso
            path.appendleft((previous_station, previous_route))
            # aggiorno la stazione corrente
            current_station = previous_station
    return path
        