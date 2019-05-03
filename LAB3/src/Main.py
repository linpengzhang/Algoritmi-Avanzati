from Graph_FromFile import GraphFromFile
from held_karp import hk_tsp
from tsp_constructive_heuristics import random_insertion
from tsp_mst import mst_approx

import sys

# Increase the default recursion limit to not crash the script with the attack
sys.setrecursionlimit(10000)

# import dashtable

files_names = ['burma14.tsp', 'ulysses22.tsp', 'eil51.tsp', 'kroD100.tsp', 'gr229.tsp', 'd493.tsp', 'dsj1000.tsp']
files_descriptions = ['Birmania (Myanmar)', 'Mediterraneo', 'Sintetico', 'Random', 'Asia/Australia',
                      'Foratura di circuiti stampati', 'Random.tsp']
optimal_solutions = [3323, 7013, 426, 21294, 134602, 35002, 18659688]

spans = [
    [[0, 1], [0, 2], [0, 3]],
    [[0, 4], [0, 5], [0, 6]],
    [[0, 7], [0, 8], [0, 9]],
    [[0, 0], [1, 0]]
]
table = [
    ["Istanza", "Held-Karp", "", "", "Euristica costruttiva", "", "", "2-approssimato", "", ""],
    ["", "Soluzione", "Tempo (s)", "Errore", "Soluzione", "Tempo (s)", "Errore", "Soluzione", "Tempo (s)", "Errore"],
    ["burma14", "0", "0", "0", "0", "0", "0", "0", "0", "0", ],
    ["ulysses22", "0", "0", "0", "0", "0", "0", "0", "0", "0", ],
    ["eil51", "0", "0", "0", "0", "0", "0", "0", "0", "0", ],
    ["kroD100", "0", "0", "0", "0", "0", "0", "0", "0", "0", ],
    ["gr229", "0", "0", "0", "0", "0", "0", "0", "0", "0", ],
    ["d493", "0", "0", "0", "0", "0", "0", "0", "0", "0", ],
    ["dsj1000", "0", "0", "0", "0", "0", "0", "0", "0", "0", ],
]
# print(dashtable.data2rst(table, spans, use_headers=True, center_cells=True, center_headers=True))

print("Script start")

# index from 0 to 6
for index in range(len(files_names)):
	print("--------------------------------")
	print("Running for index:" + str(index))

	# Read file and create main graph
	print("Reading graph from file(s)...")
	real_graph = GraphFromFile("./inputFiles/" + files_names[index])
	print("Nodes:" + str(real_graph.number_of_nodes()))
	print("Graph ready")

	# Print some info
	print(files_descriptions[index])
	print("The optimal solution is: ", optimal_solutions[index])

	# Run exact algorithm (Held-Karp)
	print("Running: Held-Karp...")
	held_karp_sol = hk_tsp(real_graph)
	table[index+2][1] = held_karp_sol
	print("Solution:", held_karp_sol)

	# Run constructive heuristic algorithm
	print("Running: Random Insertion...")
	random_insertion_sol = random_insertion(real_graph)
	table[index+2][4] = random_insertion_sol
	print("Solution:", random_insertion_sol)

	# Run 2-approx algorithm
	print("Running: MST Approx...")
	mst_approx_sol = mst_approx(real_graph)
	table[index+2][7] = mst_approx_sol
	print("Solution:", mst_approx_sol)

	
