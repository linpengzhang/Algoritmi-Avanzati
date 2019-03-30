from Graph_FromFile import GraphFromFile
import Dijkstra
import PlotMap


def print_solution():
    print(" *** SOLUZIONE TROVATA: *** ")
    print("Viaggio da ", partenza, " a ", arrivo)

    # path: lista di tuple (stazione, possible corsa) che compone il percorso
    if len(path) > 0:
        print("Orario di partenza: ", d[partenza])
        print("Orario di arrivo: ", d[arrivo])
        idx_from = 0  # indice del percorso della partenza di una corsa
        idx_to = 1  # indice del percorso dell'arrivo di una corsa
        while idx_to < len(path):
            current_route = path[idx_from][1].route_uid  # uid corsa dell'arco attualmente considerato
            # finché nel percorso continuo con la stessa corsa, ignoro le stazioni intermedie
            while idx_to < len(path) - 1 and current_route == path[idx_to][1].route_uid:
                idx_to += 1
            # stampo le informazioni di una corsa che compone il percorso
            print(path[idx_from][1].time_departure, " : corsa ", current_route, " da ", path[idx_from][0], " a ",
                  path[idx_to][0])
            # aggiorno gli indici relativi alle stazioni considerate nel percorso
            idx_from = idx_to
            idx_to = idx_from + 1
    else:
        print("Non c'è nessun viaggio che soddisfa i vincoli richiesti")


print("Script start")

# Read file and create main graph
print("Reading graph from file(s)...")
real_graph = GraphFromFile("./inputFiles/*.LIN")
print("Graph created.")

# Imposta stazioni di partenza e arrivo
partenza = "500000079"
arrivo = "300000044"

# Run Dijkstra
print("Starting Dijksta algorithm...")
d, p = Dijkstra.dijkstrasssp(partenza, 1300, real_graph)
print("Dijksta finished.")

# Stampa la soluzione trovata
path = Dijkstra.get_path(p, partenza, arrivo)
print_solution()

# Mostra il percorso trovato in una mappa
PlotMap.draw_map(path, partenza, arrivo)

print("Script end")
