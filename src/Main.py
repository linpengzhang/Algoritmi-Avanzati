from Graph_FromFile import GraphFromFile
from Graph_RandomER import GraphRandomER
from Graph_RandomUPA import GraphRandomUPA
from AttackGraph import AttackGraphs
import matplotlib.pyplot as plt
import copy
import sys
sys.setrecursionlimit(10000)

# Read file and create main graph
real_graph = GraphFromFile("networkFiles/teacherNetwork.txt")

# Calculate data to generate other graphs
nodes = real_graph.number_of_nodes()
edges = real_graph.number_of_edges()
m = round(real_graph.average_nodes_degree() / 2)
p = 0 if nodes == 1 else 2 * edges / (nodes * (nodes - 1))

# Generate other graphs
graphEr = GraphRandomER(nodes, p)
graphUPA = GraphRandomUPA(nodes, m)

# Print the generated data to check how similar it is
print("Edges in graph from text file:", real_graph.number_of_edges())
print("Edges in ER graph randomly generated:", graphEr.number_of_edges())
print("Edges in UPA graph randomly generated:", graphUPA.number_of_edges())

# Prepare the data and plot the data
x = list(range(0, nodes + 1))
att = AttackGraphs()

# First attack
print("Starting first attack(casual_attack)...")
plt.plot(x, att.casual_attack(copy.deepcopy(real_graph)), label="Grafo reale")
plt.plot(x, att.casual_attack(copy.deepcopy(graphEr)), label="Grafo ER")
plt.plot(x, att.casual_attack(copy.deepcopy(graphUPA)), label="Grafo UPA")
plt.xlabel("Nodi rimossi in ordine casuale")
plt.ylabel("Dimensione componente connessa massima")
plt.legend()
print("Ended first attack(casual_attack)...")

# Show first plot
plt.show()

# Second attack
print("Starting second attack(ordered_attack)...")
plt.plot(x, att.ordered_attack(real_graph), label="Grafo reale")
plt.plot(x, att.ordered_attack(graphEr), label="Grafo ER")
plt.plot(x, att.ordered_attack(graphUPA), label="Grafo UPA")
plt.xlabel("Nodi rimossi in ordine decrescente di grado")
plt.ylabel("Dimensione componente connessa massima")
plt.legend()
print("Ended second attack(ordered_attack)...")

# Show second plot
plt.show()

print("Script end")
