from Graph import Graph
from MyHeap import MyHeap
import matplotlib.pyplot as plt

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
                # se (min_element == float("inf")) => non c'è un arco ammissibile tra i due nodi
                if min_element < float("inf") and best_edge.time_arrival < d[v]:
                    # trovato un arco teso
                    self.relax(u, v, best_edge, d, p)
                    Q.decrease_key(v,d[v])
        return d, p
    def getPercorso(self, p, partenza, arrivo):
        """
    def printResult(self, p, d, partenza, arrivo):
        print("Viaggio da ", partenza, " a ", arrivo)
        if p[arrivo] != (None, None):
            print("Orario di partenza: ", d[partenza])
            print("Orario di arrivo: ", d[arrivo])
            self.printPercorso(p, d, partenza, arrivo, None)
        else:
            print("Non c'è nessun viaggio che soddisfa i vincoli richiesti")
    def printPercorso(self, p, d, partenza, arrivo, actual_route):
        #input: p[arrivo] != (None, None)
        if partenza == arrivo:
            return 
        self.printPercorso(p, d, partenza, p[arrivo][0], p[arrivo][1].route_uid)
        if actual_route != p[arrivo][1].route_uid:
            print(p[arrivo][1].time_departure, " : corsa ", p[arrivo][1].route_uid, " da ", partenza, " a ", arrivo)
"""
        #input: p[arrivo] != (None, None)
        if partenza == arrivo:
            return [partenza]
        percorso = self.getPercorso(p, partenza, p[arrivo][0])
        percorso.append(arrivo)
        return percorso