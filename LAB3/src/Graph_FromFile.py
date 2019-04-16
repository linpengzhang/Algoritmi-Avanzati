from collections import defaultdict
import glob
from Graph import Graph
import math

class GraphFromFile(Graph):
    """
    Class that read the Graph informations from all the files specified
    """
    def euclide_weight(self, x, y):
        return round(math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2))
    def geo_weight(self, x, y):
        xlat = math.pi * (math.trunc(x[0]) + 5.0 * (x[0]-math.trunc(x[0]))/ 3.0) / 180.0
        xlon = math.pi * (math.trunc(x[1]) + 5.0 * (x[1]-math.trunc(x[1]))/ 3.0) / 180.0
        ylat = math.pi * (math.trunc(y[0]) + 5.0 * (y[0]-math.trunc(y[0]))/ 3.0) / 180.0
        ylon = math.pi * (math.trunc(y[1]) + 5.0 * (y[1]-math.trunc(y[1]))/ 3.0) / 180.0
        q1 = math.cos( xlon - ylon )
        q2 = math.cos( xlat - ylat )
        q3 = math.cos( xlat + ylat )
        return math.trunc( self.RRR * math.acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0)
    def __init__(self, directory_files: str):
        Graph.__init__(self)
        self.RRR = 6378.388
        self.read_graph_from_file(directory_files)
    def read_graph_from_file(self, path: str):
        file = open(path, 'r')
        lines = file.readlines()
        """
        self.name = lines[0][6:]
        self.number_of_nodes = lines.index("DIMENSION : ")
        self.edge_weight_type = lines[4][:]
        """
        init = lines.index("NODE_COORD_SECTION\n")
        finish = lines.index("EOF\n")
        for i in range(0, init):
            if lines[i].startswith("NAME"):
                self.name = lines[i][5:].strip()
            if lines[i].startswith("DIMENSION"):
                self.number_of_nodes = int(lines[i][11:].strip())
            if lines[i].startswith("EDGE_WEIGHT_TYPE"):
                self.edge_weight_type = lines[i][17:].strip()
        print(self.edge_weight_type)
        nodeCoords = []
        for i in range(init+1, finish):
            dati = lines[i].split()
            nodeCoords.append((float(dati[1]), float(dati[2])))
        if self.edge_weight_type == "GEO":
            self.graph = [ [ self.geo_weight(nodeCoords[i],nodeCoords[j]) for j in range(self.number_of_nodes)] for i in range(self.number_of_nodes)]
        else:
            self.graph = [ [ self.euclide_weight(nodeCoords[i],nodeCoords[j]) for j in range(self.number_of_nodes)] for i in range(self.number_of_nodes)]
        print(self.graph)