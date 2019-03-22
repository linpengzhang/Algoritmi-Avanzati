from Graph import Graph
import random


class AttackGraphs:
    """
    Class that contains the attack functions used against the Graph
    """

    def remove_node(self, g: Graph, node: int):
        """
        Removes the specified node from the graph g
        """
        for v in g.graph[node]:
            g.graph[v].discard(node)
        del g.graph[node]

    def casual_attack(self, g: Graph):
        """
        :return: Values of resilience of the graph g after disabling each node in a casual order
        """
        res_values = [g.max_size_connected_component()]
        for _ in range(g.number_of_nodes()):
            r = random.choice(list(g.graph.keys()))
            self.remove_node(g, r)
            res_values.append(g.max_size_connected_component())
        return res_values

    def ordered_attack(self, g: Graph):
        """
        :return: Values of resilience of the graph g after disabling each node in an ordered way
        """
        res_values = [g.max_size_connected_component()]
        num_nodes = g.number_of_nodes()
        deg_sets = [set() for _ in range(num_nodes)]
        # deg_sets è indicizzata per grado: deg_sets[a] contiene i nodi che hanno grado pari ad a
        for v in g.graph.keys():
            deg = len(g.graph[v])
            deg_sets[deg].add(v)
        for deg in range(num_nodes - 1, -1, -1):
            # ad ogni iterazione del ciclo for si rimuovono tutti i nodi di grado deg
            # partendo dal grado maggiore e rimuovendo nodi non potranno esserci nuovi nodi di grado più alto,
            # quindi alla fine tutti verranno rimossi
            while len(deg_sets[deg]) != 0:
                highest_node = deg_sets[deg].pop()  # ritorna un nodo tra quelli di grado deg
                for v in g.graph[highest_node]:
                    # ogni nodo v adiacente a highestNode viene spostato in deg_sets nella posizione
                    # con il suo grado diminuito di 1 (per riflettere la successiva eliminazione del nodo highestNode)
                    deg_sets[len(g.graph[v])].remove(v)  # tolgo v da deg_sets
                    deg_sets[len(g.graph[v]) - 1].add(v)  # metto v nel giusto indice di deg_sets
                self.remove_node(g, highest_node)
                res_values.append(g.max_size_connected_component())
        return res_values
