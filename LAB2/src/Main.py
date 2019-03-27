from Graph_FromFile import GraphFromFile
from Dijkstra import Dijkstra
import matplotlib.pyplot as plt
print("Script start")
# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/*.LIN")
print("Graph created.")
#lettura coord
print("Reading coords from file...")
file = open("./inputFiles/bfkoord", 'r', encoding="latin-1")
partenza = "500000079"
arrivo = "300000044"
nodeCoords = {}
for row in file:
    if row[0:9].isalnum():
        latitudine = float(row[12:20])
        longitudine = float(row[22:30])
        nodeCoords[row[0:9]] = (latitudine, longitudine)
        plt.plot(latitudine, longitudine, marker='.', color='gray')
plt.xlabel("Latitudine")
plt.ylabel("Longitudine")
plt.title("Soluzione grafica del viaggio da " + partenza + " ad " + arrivo)
plt.legend()
print("Map created.")
print("Starting Dijksta algorithm...")
d, p = Dijkstra().dijkstrasssp(partenza, 1300, real_graph)
print("Viaggio da ", partenza, " a ", arrivo)
if p[arrivo] != (None, None):
    print("Orario di partenza: ", d[partenza])
    print("Orario di arrivo: ", d[arrivo])
    percorso = Dijkstra().getPercorso(p, partenza, arrivo)
    print(percorso)
    route_attuale = None
    back = 0
    next = 1
    while next < len(percorso):
        route_attuale = p[percorso[next]][1].route_uid
        while next < len(percorso)-1 and route_attuale == p[percorso[next+1]][1].route_uid:
            next = next+1
        print(p[percorso[back+1]][1].time_departure, " : corsa ", route_attuale, " da ", percorso[back], " a ", percorso[next])
        back = next
        next = next + 1
    for i in range(len(percorso)-1):
        plt.plot([nodeCoords[percorso[i]][0], nodeCoords[percorso[i+1]][0]], [nodeCoords[percorso[i]][1], nodeCoords[percorso[i+1]][1]], linestyle='-', color='blue')     
else:
    print("Non c'è nessun viaggio che soddisfa i vincoli richiesti")
plt.show()
"""
arrivo="004240102"
Dijkstra().printResult(p, d, partenza, arrivo)
"""
