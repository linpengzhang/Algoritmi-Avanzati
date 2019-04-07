from Graph_FromFile import GraphFromFile
from held_karp import *

print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/burma14.tsp")
print("ciao")
print(hk_tsp(real_graph))
print("Graph created.")

