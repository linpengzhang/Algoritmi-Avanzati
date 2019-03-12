#!/usr/bin/env python3

from Graph_FromFile import GraphFromFile
from Graph_RandomER import GraphRandomER
from Graph_RandomUPA import GraphRandomUPA
from AttackGraph import AttackGraphs
import matplotlib.pyplot as plt
import copy
import sys

print("Script start")

# Increase the default recursion limit to not crash the script with the attack
sys.setrecursionlimit(10000)

# Read file and create main graph
print("Reading graph from file...")
real_graph = GraphFromFile("networkFiles/teacherNetwork.txt")

# Calculate data to generate other graphs
nodes = real_graph.number_of_nodes()
edges = real_graph.number_of_edges()
m = round(real_graph.average_nodes_degree() / 2)
p = 0 if nodes == 1 else 2 * edges / (nodes * (nodes - 1))

# Generate other graphs
print("Generating random ER and UPA...")
graphEr = GraphRandomER(nodes, p)
graphUPA = GraphRandomUPA(nodes, m)

# Print the generated data to check how similar it is
print("Edges in graph from text file:", real_graph.number_of_edges())
print("Edges in ER graph randomly generated:", graphEr.number_of_edges())
print("Edges in UPA graph randomly generated:", graphUPA.number_of_edges())

# Prepare the data and plot the data
x = list(range(0, nodes + 1))
soglia_grafo_resiliente = [0.75 * (nodes - i) for i in x]
att = AttackGraphs()

# First attack
print("Starting first attack(casual_attack)...")
plt.plot(x, att.casual_attack(copy.deepcopy(real_graph)), label="Grafo reale")
plt.plot(x, att.casual_attack(copy.deepcopy(graphEr)), label="Grafo ER")
plt.plot(x, att.casual_attack(copy.deepcopy(graphUPA)), label="Grafo UPA")
plt.plot(x, soglia_grafo_resiliente, color="red", linewidth=1, linestyle="--", label="Soglia grafo resiliente")
plt.axvline(x=nodes * 0.2, color="black", linewidth=1, linestyle="--", label="20% dei nodi eliminati")
plt.xlabel("Nodi rimossi in ordine casuale")
plt.ylabel("Dimensione componente connessa massima")
plt.legend()
plt.title("Attacco casuale (p=" + str(p) + ", m=" + str(m) + ")")
print("Ended first attack(casual_attack)...")

# Show first plot
print("Showing first plot, close it to continue with second attack...")
plt.show()

# Second attack
print("Starting second attack(ordered_attack)...")
plt.plot(x, att.ordered_attack(real_graph), label="Grafo reale")
plt.plot(x, att.ordered_attack(graphEr), label="Grafo ER")
plt.plot(x, att.ordered_attack(graphUPA), label="Grafo UPA")
plt.plot(x, soglia_grafo_resiliente, color="red", linewidth=1, linestyle="--", label="Soglia grafo resiliente")
plt.axvline(x=nodes * 0.2, color="black", linewidth=1, linestyle="--", label="20% dei nodi eliminati")
plt.xlabel("Nodi rimossi in ordine decrescente di grado")
plt.ylabel("Dimensione componente connessa massima")
plt.legend()
plt.title("Attacco ordinato (p=" + str(p) + ", m=" + str(m) + ")")
print("Ended second attack(ordered_attack)...")

# Show second plot
print("Showing second plot...")
plt.show()

print("Script end")
