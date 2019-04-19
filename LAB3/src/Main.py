from Graph_FromFile import GraphFromFile
from cheapest_insertion import *
from held_karp import *

print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/gr229.tsp")
print("ciao")
print("cheapest_insertion")
print(cheapest_insertion(real_graph))
print("hk")
#print(hk_tsp(real_graph))
print("Graph created.")

