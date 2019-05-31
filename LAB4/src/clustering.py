import math
import heapq
from numpy import argsort
from county import Dataset, County
import time


class Cluster(Dataset):
    """
    Classe che rappresenta un cluster di contee
    """

    def __init__(self, lista):
        Dataset.__init__(self, lista)
        self._sum_x = sum(map(lambda a: a.x * a.population, lista))
        self._sum_y = sum(map(lambda a: a.y * a.population, lista))
        self._sum_pop = sum(map(lambda a: a.population, lista))

    def append(self, c: County):
        self.data.append(c)
        self._sum_x += c.x * c.population
        self._sum_y += c.y * c.population
        self._sum_pop += c.population

    def extend(self, cl):
        self.data.extend(cl.data)
        self._sum_x += cl._sum_x
        self._sum_y += cl._sum_y
        self._sum_pop += cl._sum_pop

    def get_center(self):
        n = self._sum_pop  # len(self.data)
        return self._sum_x / n, self._sum_y / n

    def get_error(self):
        cent = self.get_center()
        return sum(map(lambda c: c.population * (distance(c.get_coords(), cent) ** 2), self.data))


def hierarchical_clustering(D: Dataset, k):
    start = time.clock()
    # crea inizialmente un cluster per ciascun elemento
    C = [Cluster([c]) for c in D.data]
    while len(C) > k:
        # trova gli indici dei due cluster più vicini
        P = [(i, C[i].get_center()) for i in range(len(C))]
        # P[i][0] è l'indice del cluster
        # P[i][1] sono le coordinate del centro del cluster i-esimo
        P.sort(key=lambda x: x[1][0])  # ordina per coordinata x
        S = argsort(list(map(lambda x: x[1][1], P))).tolist()  # indici su P dei punti ordinati per coordinata y
        d, i, j = fast_closest_pair(P, S, 0, len(P))
        C[i].extend(C[j])
        del C[j]
    end = time.clock()
    return [C, end - start, distortion(C)]


def hierarchical_clustering_distortion_list(D: Dataset, k):
    # crea inizialmente un cluster per ciascun elemento
    C = [Cluster([c]) for c in D.data]
    distortion = [0 for _ in range(len(C) + 1)]
    while len(C) > k:
        # trova gli indici dei due cluster più vicini
        P = [(i, C[i].get_center()) for i in range(len(C))]
        # P[i][0] è l'indice del cluster
        # P[i][1] sono le coordinate del centro del cluster i-esimo
        P.sort(key=lambda x: x[1][0])  # ordina per coordinata x
        S = argsort(list(map(lambda x: x[1][1], P))).tolist()  # indici su P dei punti ordinati per coordinata y
        d, i, j = fast_closest_pair(P, S, 0, len(P))
        distortion[len(C) - 1] = distortion[len(C)] - C[j].get_error() - C[i].get_error()
        C[i].extend(C[j])
        distortion[len(C) - 1] = distortion[len(C) - 1] + C[i].get_error()
        del C[j]
    return distortion


def slow_closest_pair(P: list, start, stop):
    """
    :param P: lista di punti (tuple: (indice, coordinate))
    :param start: indice iniziale della porzione di P da considerare
    :param stop: indice finale (escluso) della porzione di P da considerare
    :return: (d,i,j), d è la minima distanza tra due punti in P, i e j sono gli indici (associati) di questi due punti
    """
    # start, stop: indici della porzione di lista da considerare
    d, i, j = float("inf"), -1, -1
    for u in range(start, stop):
        for v in range(u + 1, stop):
            d, i, j = min((d, i, j), (distance(P[u][1], P[v][1]), P[u][0], P[v][0]), key=lambda a: a[0])
    return d, i, j


def fast_closest_pair(P: list, S: list, p_start, p_stop):
    """
    :param P: lista di punti (tuple: (indice, coordinate)) ordinati per coordinata x
    :param S: lista di indici su P di un sottoinsieme di punti P' di P ordinati per coordinata y
    :param p_start: indice iniziale della porzione P' di P da considerare
    :param p_stop: indice finale (escluso) della porzione P' di P da considerare
    :return: (d,i,j), d è la minima distanza tra due punti in P', i e j sono gli indici (associati) di questi due punti
    """
    n = p_stop - p_start
    if n <= 3:
        return slow_closest_pair(P, p_start, p_stop)
    else:
        m = p_start + math.floor(n / 2)
        P_L = {P[i] for i in range(p_start, m)}
        S_L, S_R = split(P, S, P_L)
        d, i, j = min(fast_closest_pair(P, S_L, p_start, m), fast_closest_pair(P, S_R, m, p_stop), key=lambda a: a[0])
        mid = 0.5 * (P[m - 1][1][0] + P[m][1][0])
        return min((d, i, j), closest_pair_strip(P, S, mid, d), key=lambda a: a[0])


def split(P: list, S: list, P_L: set):
    """
    :param P: lista di punti
    :param S: lista ordinata di indici di un sottoinsieme P' di P
    :param P_L: partizione di P' (P_R = P'\P_L)
    :return: S_L, S_R liste ordinate che contengono gli indici di S degli elementi risp. in P_L, P_R
    """
    S_L = list()
    S_R = list()
    for i in S:
        S_L.append(i) if P[i] in P_L else S_R.append(i)
    return S_L, S_R


def closest_pair_strip(P: list, S: list, mid, d):
    """
    :param P: lista di punti (tuple: (indice, coordinate))
    :param S: lista ordinata di indici su P di un sottoinsieme P' di P
    :param mid: valore reale
    :param d: valore reale positivo
    :return: (d,i,j), d è la minima distanza tra due punti in P', i e j sono gli indici (associati) di questi due punti
    """
    SS = list()
    for idx in S:
        if abs(P[idx][1][0] - mid) < d:
            SS.append(idx)
    d, i, j = float("inf"), -1, -1
    k = len(SS)
    for u in range(k - 1):
        for v in range(u + 1, min(u + 5, k)):
            # confronto ogni punto in SS con i 5 successivi
            d, i, j = min((d, i, j), (distance(P[SS[u]][1], P[SS[v]][1]), P[SS[u]][0], P[SS[v]][0]), key=lambda a: a[0])
    return d, i, j


def kmeans_clustering(P: Dataset, k, q):
    start = time.clock()
    n = len(P.data)
    # inizializza i primi k centroidi come le k contee più popolose
    centroids = list(map(lambda c: c.get_coords(), heapq.nlargest(k, P.data, lambda c: c.population)))
    for _ in range(q):
        # crea k cluster vuoti
        C = [Cluster([]) for _ in range(k)]
        # assegna ciascuna contea al cluster relativo al centroide più vicino
        for j in range(n):
            # trova l'indice l del centroide più vicino
            min_val = float('inf')
            for f in range(k):
                cur_val = distance(P.data[j].get_coords(), centroids[f])
                if cur_val < min_val:
                    min_val = cur_val
                    l = f
            C[l].append(P.data[j])
        # aggiorna i nuovi centroidi in base ai cluster ottenuti
        for f in range(k):
            centroids[f] = C[f].get_center()
    end = time.clock()
    return [C, end - start, distortion(C)]


def distance(a, b):
    """
    Return the euclidean distance between two bidimensional points a and b
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def distortion(L: list):
    """
    Restituisce la distorsione del clustering dato dalla lista di cluster L
    """
    return sum(map(lambda c: c.get_error(), L))
