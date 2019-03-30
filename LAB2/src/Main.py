from Graph_FromFile import GraphFromFile
import Dijkstra
import PlotMap
import Printer

print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/*.LIN")
print("Graph created.")

# Imposta stazioni di partenza e arrivo
partenza = "500000079"
arrivo = "300000044"
# "004240102"
orario = 1300
# partenza = "200417051"
# arrivo = "140701016"
# orario = 2355

# Run Dijkstra
print("Starting Dijksta algorithm...")
d, p = Dijkstra.dijkstrasssp(partenza, orario, real_graph)
print("Dijksta finished.")

# Stampa la soluzione trovata
path = Dijkstra.get_path(p, partenza, arrivo)
Printer.print_solution(partenza, arrivo, orario, path)

# Mostra il percorso trovato in una mappa
PlotMap.draw_map(path, partenza, arrivo)

print("Script end")
