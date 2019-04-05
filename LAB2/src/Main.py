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
partenzaList = ["500000079", "200415016", "300000032", "210602003", "200417051", "200417051", "400000035", "221106005", "170601004"]
arrivoList = ["300000044", "200405005", "400000122", "300000030", "140701016", "140701016", "200415005", "220902016", "170501010"]
orarioPartenzaList = [1300, 930, 530, 630, 1200, 2355, 1102, 1301, 408]
i = 8
partenza = partenzaList[i]
arrivo = arrivoList[i]
orarioPartenza = orarioPartenzaList[i]

# Run Dijkstra
print("Starting Dijksta algorithm...")
d, p = Dijkstra.dijkstrasssp(partenza, orarioPartenza, real_graph)
print("Dijksta finished.")

# Stampa la soluzione trovata
path = Dijkstra.get_path(d, p, partenza, arrivo)
Printer.print_solution(partenza, arrivo, path)

# Mostra il percorso trovato in una mappa
PlotMap.draw_map(path, partenza, arrivo, Printer.print_time(orarioPartenza))

print("Script end")
