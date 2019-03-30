class MyHeap:
    """
    Class that implements a binary heap of tuples (weight, node) ordered by weight
    """

    def __init__(self, d, nodes):
        self.heap = []
        self.nodes_keys = {}
        for n in nodes:
            self.nodes_keys[n] = len(self.heap)
            self.heap.append((d[n], n))
        # inizializzazione della coda di priorità come heap binaria
        self._build_heap()

    def __len__(self):
        return len(self.heap)

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _parent(self, i):
        return (i - 1) >> 1

    def _bubble_up(self, i):
        p = self._parent(i)
        while i > 0 and self.heap[i][0] < self.heap[p][0]:
            self._swap(i, p)  # swap
            i = p
            p = self._parent(i)

    def _trickle_down(self, i):
        l = self._left(i)
        r = self._right(i)
        n = len(self.heap)
        smallest = i
        if l < n and self.heap[l][0] < self.heap[i][0]:
            smallest = l
        if r < n and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r
        if smallest != i:
            self._swap(i, smallest)  # swap
            self._trickle_down(smallest)

    def _swap(self, i, j):
        node_i = self.heap[i][1]
        node_j = self.heap[j][1]
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.nodes_keys[node_i], self.nodes_keys[node_j] = self.nodes_keys[node_j], self.nodes_keys[node_i]

    def _build_heap(self):
        for i in range((len(self.heap) >> 1) - 1, -1, -1):
            self._trickle_down(i)

    def decrease_key(self, node, new_key):
        """
        :return: Decrease the key related to the specified node and keep the heap structure
        """
        i = self.nodes_keys[node]
        if self.heap[i][0] > new_key:
            self.heap[i] = (new_key, node)
            self._bubble_up(i)

    def extract_min(self):
        """
        :return: Return the node with the lowest weigth and keep the heap structure
        """
        if len(self.heap) == 1:
            self.nodes_keys = {}
            return self.heap.pop()
        else:
            min = self.heap[0][1]
            del self.nodes_keys[min]
            self.heap[0] = self.heap.pop()
            self.nodes_keys[self.heap[0][1]] = 0
            self._trickle_down(0)
            return min
