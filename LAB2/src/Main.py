from Graph_FromFile import GraphFromFile
import Dijkstra
import PlotMap

def int_to_time(value: int):
    if value>2359:
        return str(value%2400).rjust(4, "0")[0:2] + ":" + str(value%2400).rjust(4, "0")[2:] + " di " + str(int(value/2400)) + " giorni dopo"
    else:
        return str(value).rjust(4,"0")[0:2]+":"+str(value).rjust(4,"0")[2:]
def print_solution():
    print(" *** SOLUZIONE TROVATA: *** ")
    print("Viaggio da ", partenza, " a ", arrivo)

    # path: lista di tuple (stazione, possible corsa) che compone il percorso
    if len(path) > 0:
        print("Orario di partenza: ", int_to_time(d[partenza]))
        print("Orario di arrivo: ", int_to_time(d[arrivo]))
        idx_from = 0  # indice del percorso della partenza di una corsa
        idx_to = 1  # indice del percorso dell'arrivo di una corsa
        while idx_to < len(path):
            current_route = path[idx_from][1].route_uid  # uid corsa dell'arco attualmente considerato
            # finché nel percorso continuo con la stessa corsa, ignoro le stazioni intermedie
            while idx_to < len(path) - 1 and current_route == path[idx_to][1].route_uid:
                idx_to += 1
            # stampo le informazioni di una corsa che compone il percorso
            print(int_to_time(path[idx_from][1].time_departure), " : corsa ", current_route, " da ", path[idx_from][0], " a ",
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
partenzaList = ["500000079", "200415016", "300000032", "210602003", "200417051", "200417051"]
arrivoList = ["300000044", "200405005", "400000122", "300000030", "140701016", "140701016"]
orarioPartenzaList = [1300, 930, 530, 630, 1200, 2355]
i=0
partenza = partenzaList[i]
arrivo = arrivoList[i]
orarioPartenza = orarioPartenzaList[i]

# Run Dijkstra
print("Starting Dijksta algorithm...")
d, p = Dijkstra.dijkstrasssp(partenza, orarioPartenza, real_graph)
print("Dijksta finished.")

# Stampa la soluzione trovata
path = Dijkstra.get_path(p, partenza, arrivo)
print_solution()

# Mostra il percorso trovato in una mappa
PlotMap.draw_map(path, partenza, arrivo, int_to_time(orarioPartenza))

print("Script end")
