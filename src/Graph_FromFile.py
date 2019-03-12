from Graph import Graph


class GraphFromFile(Graph):
    """
    Class that read the Graph informations from a text file
    """

    def __init__(self, filename: str):
        Graph.__init__(self)
        self.read_graph_from_file(filename)

    def read_graph_from_file(self, filename: str):
        file = open(filename, 'r')
        for row in file:
            if not row.startswith('#'):
                u, v = [int(val) for val in row.split()]
                if u != v:
                    self.graph[u].add(v)
                    self.graph[v].add(u)
        file.close()
