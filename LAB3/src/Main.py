from Graph_FromFile import GraphFromFile
from held_karp import hk_tsp
from tsp_constructive_heuristics import random_insertion
from tsp_mst import mst_approx
from multiprocessing.pool import ThreadPool

import sys

# Increase the default recursion limit to not crash the script
sys.setrecursionlimit(10000)

import dashtable

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

print("Script start")
pool = ThreadPool(processes=3)

# index from 0 to 6
for index in range(len(files_names)):
    print("--------------------------------")
    print("Running for index:" + str(index))

    # Read file and create main graph
    print("Reading graph from file " + files_names[index] + "...")
    real_graph = GraphFromFile("./inputFiles/" + files_names[index])
    print("Nodes:" + str(real_graph.number_of_nodes()))
    print("Graph ready")

    # Print some info
    print("File description:" + files_descriptions[index])
    print("The optimal solution is: ", optimal_solutions[index])

    # Run exact algorithm (Held-Karp)
    print("Starting thread: Held-Karp...")
    held_karp_thread = pool.apply_async(hk_tsp, [real_graph])

    # Run constructive heuristic algorithm
    print("Starting thread: Random Insertion...")
    random_insertion_thread = pool.apply_async(random_insertion, [real_graph])

    # Run 2-approx algorithm
    print("Starting thread: MST Approx...")
    mst_approx_thread = pool.apply_async(mst_approx, [real_graph])

    print("Threads started, waiting for solution...")
    held_karp_thread.wait()
    random_insertion_thread.wait()
    mst_approx_thread.wait()

    # Get solutions
    [held_karp_sol, held_karp_time] = held_karp_thread.get()
    print("Held-Karp solution:", held_karp_sol)
    [random_insertion_sol, random_insertion_time] = random_insertion_thread.get()
    print("Constructive heuristic solution:", random_insertion_sol)
    [mst_approx_sol, mst_approx_time] = mst_approx_thread.get()
    print("2-approx solution:", mst_approx_sol)

    # Fill table with results
    table[index + 2][1] = held_karp_sol
    table[index + 2][2] = round(held_karp_time, 3)
    table[index + 2][3] = \
        str(round(((held_karp_sol - optimal_solutions[index]) / optimal_solutions[index] * 100), 3)) + "%"

    table[index + 2][4] = random_insertion_sol
    table[index + 2][5] = round(random_insertion_time, 3)
    table[index + 2][6] = \
        str(round(((random_insertion_sol - optimal_solutions[index]) / optimal_solutions[index] * 100), 3)) + "%"

    table[index + 2][7] = mst_approx_sol
    table[index + 2][8] = round(mst_approx_time, 3)
    table[index + 2][9] = \
        str(round(((mst_approx_sol - optimal_solutions[index]) / optimal_solutions[index] * 100), 3)) + "%"

print("--------------------------------")
print(dashtable.data2rst(table, spans, use_headers=True, center_cells=True, center_headers=True))
