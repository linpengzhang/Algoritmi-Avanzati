from Graph_FromFile import GraphFromFile
from cheapest_insertion import cheapest_insertion
from held_karp import hk_tsp

files_names = ['burma14.tsp', 'ulysses22.tsp', 'eil51.tsp', 'kroD100.tsp', 'gr229.tsp', 'd493.tsp', 'dsj1000.tsp']
files_descriptions = ['Birmania (Myanmar)', 'Mediterraneo', 'Sintetico', 'Random', 'Asia/Australia', 'Foratura di circuiti stampati', 'Random.tsp']
optimal_solutions = [3323, 7013, 426,21294, 134602, 35002, 18659688]	 

# index from 0 to 6
index = 6

print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/" + files_names[index])
print("Graph read")

# Print some info
print(files_descriptions[index])
print("The optimal solution is: ", optimal_solutions[index])

# Run exact algorithm (Held-Karp)
#print("Running: Held-Karp...")
#print(hk_tsp(real_graph))

# Run constructive heuristic algorithm
print("Running: Cheapest Insertion")
print("Solution:", cheapest_insertion(real_graph))



