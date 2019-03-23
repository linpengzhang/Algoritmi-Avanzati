from collections import defaultdict
import glob
from Graph import Graph
from Route import Route


class GraphFromFile(Graph):
    """
    Class that read the Graph informations from all the files specified
    """

    def __init__(self, directory_files: str):
        Graph.__init__(self)
        self.read_graph_from_file(directory_files)

    def read_graph_from_file(self, directory_files: str):
        for filename in glob.glob(directory_files):
            with open(filename, 'r', encoding='latin-1') as file:
                # nota.. legge tutte le linee per creare l'intera lista
                lines = file.readlines()
                for i in range(0, len(lines) - 1):
                    if lines[i].startswith('*Z'):
                        # riga con l'identificativo univoco della corsa
                        codice, linea = lines[i].split()[1:3]
                        corsa_uid = codice + " " + linea
                    if not (lines[i].startswith('*') or lines[i + 1].startswith('*')):
                        # righe con informazioni sulla tratta della corsa
                        row = lines[i]
                        nextrow = lines[i + 1]
                        ora_partenza = row[39:44]
                        ora_arrivo = nextrow[32:37]
                        ora_prossima_partenza = nextrow[39:44]
                        stazione_partenza = row[0:9]
                        stazione_arrivo = nextrow[0:9]
                        # aggiunta dell'arco tra le due stazioni
                        self.add_edge(stazione_partenza, stazione_arrivo, Route(int(ora_partenza), int(ora_arrivo), corsa_uid))
                        if ora_prossima_partenza.isspace() and not (stazione_arrivo in self.graph.keys()):
                            # caso in cui una stazione finale di arrivo non sia presente come stazione di partenza per qualche tratta
                            self.graph[stazione_arrivo] = defaultdict(set)
