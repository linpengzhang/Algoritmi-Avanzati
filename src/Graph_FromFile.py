from Graph import Graph


class GraphFromFile(Graph):
    """
    Class that read the Graph informations from a text file
    """

    def __init__(self, filename: str):
        Graph.__init__(self)
        self.read_graph_from_file(filename)

    def read_graph_from_file(self, filename: str):
        lines = open(filename, 'r').readlines()
        for row in lines:
            if not row.startswith('#'):
                u, v = [int(val) for val in row.split()]
                if u != v:
                    if u in self.graph:
                        self.graph[u] |= {v}
                    else:
                        self.graph[u] = {v}
                    if v in self.graph:
                        self.graph[v] |= {u}
                    else:
                        self.graph[v] = {u}
