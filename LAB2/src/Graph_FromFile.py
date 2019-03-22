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
                lines = file.readlines()
                for i in range(0, len(lines) - 1):
                    if lines[i].startswith('*Z'):
                        corsa, linea = lines[i].split()[1:3]
                        corsa_uid = corsa + " " + linea
                    if not (lines[i].startswith('*') or lines[i + 1].startswith('*')):
                        row = lines[i]
                        nextrow = lines[i + 1]
                        ora_partenza = row[39:44]
                        ora_arrivo = nextrow[32:37]
                        self.graph[row[0:9]][nextrow[0:9]].add(Route(int(ora_partenza), int(ora_arrivo), corsa_uid))
                        if nextrow[39:44].isspace() and not (nextrow[0:9] in self.graph.keys()):
                            self.graph[nextrow[0:9]] = defaultdict(set)
