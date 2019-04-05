from Graph_FromFile import GraphFromFile
import Dijkstra
import PlotMap
import Printer

print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/kroD100.tsp")
print("Graph created.")

