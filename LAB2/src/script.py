# creo grafo orientato e pesato
from collections import defaultdict
from time import sleep
import heapq
import glob
import sys
#suddividerlo e renderlo più carino
#fare decreasekey in modo decente
#ricostruire il percorso sfruttando p
#grafico
#heap binaria anche sugli archi paralleli anziché set
#general improvements
def relax(u,v, edge, d, p):
    d[v] = edge.time_arrival
    p[v] = (u,edge)
class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(set))

    def number_of_nodes(self):
        """
        :return: Return the number of nodes in the graph
        """
        return len(self.graph)

    def initsssp(self, s, inizio):
        d={}
        p={}
        for v in self.graph.keys():
            d[v]=100000
            p[v]=(-1,-1)
        d[s] = inizio
        return d,p
    def nodes(self):
        return self.graph.keys()
    def dijkstrasssp(self, s, inizio):
        d, p = self.initsssp(s, inizio)
        Q=[]
        for i in self.nodes():
            heapq.heappush(Q, (d[i], i))
        while len(Q)>0:
            u=heapq.heappop(Q)[1] #estraggo nodo con tempo di arrivo minimo
            for v in self.graph[u].keys() :
                min = 100000
                for edge in self.graph[u][v] :
                    if d[u]<=edge.time_departure:
                        if edge.time_arrival<min:
                            min=edge.time_arrival
                            bestEdge = edge
                if min<100000 and bestEdge.time_arrival<d[v]:
                    relax(u,v,bestEdge,d,p)

                    for i in range(len(Q)): #equivalente a decreasekey(Q,v,d[v]) da implementare meglio
                        if Q[i][1] == v:
                            Q[i] = (d[v],v)
                    heapq.heapify(Q)

        print(d["300000044"])
        return d
        
class Route: 
  def __init__(self, time_departure=0, time_arrival=0, route_uid=""): 
    self.time_departure = time_departure
    self.time_arrival = time_arrival
    self.route_uid = route_uid
  def __str__(self): 
    return '(' + str(self.time_departure) + ', ' + str(self.time_arrival) + ', '+str(self.route_uid)+')'
  def __repr__(self): 
    return '(' + str(self.time_departure) + ', ' + str(self.time_arrival) + ', '+str(self.route_uid)+')'

dir = './src/*.LIN'
g = Graph()
q = heapq
for filename in glob.glob(dir):
    with open(filename, 'r', encoding='latin-1') as file:
        lines = file.readlines()
        for i in range(0, len(lines)-1):
            if lines[i].startswith('*Z'):
                corsa, linea = lines[i].split()[1:3]
                corsa_uid = corsa + " " + linea
            if not(lines[i].startswith('*') or lines[i+1].startswith('*')):
                row = lines[i]
                nextrow = lines[i+1]
                oraPartenza = row[39:44]
                oraArrivo = nextrow[32:37]
                g.graph[row[0:9]][nextrow[0:9]].add(Route(int(oraPartenza), int(oraArrivo), corsa_uid))
                if nextrow[39:44].isspace() and not (nextrow[0:9] in g.graph.keys()):
                    g.graph[nextrow[0:9]] = defaultdict(set)
d = g.dijkstrasssp("500000079", 1300)
# algoritmo cammini minimi
