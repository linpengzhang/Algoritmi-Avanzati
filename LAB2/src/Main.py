from Graph_FromFile import GraphFromFile
from Dijkstra import Dijkstra

print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/*.LIN")
print("Graph created.")

print("Starting Dijksta algorithm...")
partenza="500000079"
arrivo="300000044"
d, p = Dijkstra().dijkstrasssp(partenza, 1300, real_graph)
Dijkstra().printResult(p, d, partenza, arrivo)
arrivo="004240102"
Dijkstra().printResult(p, d, partenza, arrivo)
