from Graph_FromFile import GraphFromFile
from Dijkstra import Dijkstra

print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/*.LIN")
print("Graph created.")

print("Starting Dijksta algorithm...")
d, p = Dijkstra().dijkstrasssp("500000079", 1300, real_graph)

print(d["300000044"])
print(d["004240102"]) # nodo non raggiungibile dalla partenza indicata (forse il giorno dopo?)
