import math
import random
from numpy import argsort


def hierarchical_clustering(P: list, k):
    C = [[p_i] for p_i in P]
    while len(C) > k:
        cl = [(i, center(C[i])) for i in range(len(C))]
        #cl[i][0] è l'indice del cluster, cl[i][1] le coordinate del centro del cluster i-esimo. Meglio di una mappa nel caso pessimo!
        (d, i, j) = fast_closest_pair(sorted(cl, key=lambda coppia:coppia[1][0]), sorted(cl, key=lambda coppia:coppia[1][1]))
        print(d, i, j)
        C.append(C[i]+C[j])
        C.remove(C[i])
        C.remove(C[j])
    return C


def slow_closest_pair(P: list):
    (d, i, j) = (float("inf"), -1, -1)
    for new_i in range(len(P)):
        for new_j in range(new_i+1, len(P)):
            (d, i, j) = min((d,i,j), (distance(P[new_i][1], P[new_j][1]), P[new_i][0], P[new_j][0]), key=lambda a:a[0])
    return (d, i, j)


def fast_closest_pair(P: list, S: list):
    """
    P vettore di punti ordinato per x crescente
    S vettore di punti ordinato per y crescente
    :return: (d,i,j), d è la minima distanza tra due punti in P, i e j sono gli indici di questi due punti
    """
    n = len(P)
    if n <= 3:
        return slow_closest_pair(P)
    else:
        m = math.floor(n/2)
        P_L = P[:m]
        P_R = P[m:]
        S_L, S_R = split(S, P_L, P_R)
        (d,i,j) = min(fast_closest_pair(P_L, S_L), fast_closest_pair(P_R, S_R), key=lambda a: a[0])
        mid = 0.5*(P[m-1][1][0]+P[m][1][0])
        return min((d,i,j), closest_pair_strip(S, mid, d), key=lambda a:a[0])


def split(S: list, P_L: list, P_R: list):
    """
    S vettore ordinato
    P_L, P_R partizione di S
    :return: S_L, S_R vettori ordinati che contengono rispettivamente gli elementi in P_L, P_R
    """
    n = len(S)
    S_L = list()
    S_R = list()
    list(map(lambda i: S_L.append(i) if i in P_L else S_R.append(i), S))
    return S_L, S_R


def closest_pair_strip(S: list, mid, d):
    """
    S vettore ordinato per y crescente
    mid valore reale
    d valore reale positivo
    :return: (d,i,j) con d minima distanza tra i punti in S, i e j gli indici dei punti
    """
    n = len(S)
    SS = list()
    for i in range(n):
        if abs(S[i][1][0]-mid) < d:
            SS.append(S[i])
    (d, i, j) = (float("inf"), -1, -1)
    k = len(SS)
    for u in range(k-1):
        for v in range(u+1, min(u+5, k)):
            #confronto ogni punto in SS con i 5 successivi
            (d, i, j) = min((d, i, j), (distance(SS[u][1], SS[v][1]), SS[u][0], SS[v][0]), key=lambda a:a[0])
    return (d, i, j)


def kmeans_clustering(P: list, k, q):
    n = len(P)
    # crea k centroidi con valori arbitrari
    centroids = [(random.random(), random.random()) for _ in range(k)]
import heapq
from county import *
from functools import reduce

def kmeans_clustering(P: Dataset, k, q):
    n = len(P.dataset)
    # inizializza i primi k centroidi come le k contee più popolose
    centroids = list(map(lambda c : c.get_coords(), heapq.nlargest(k, P.dataset, lambda c : c.population)))
    for _ in range(q):
        # crea k cluster vuoti
        C = [Dataset() for _ in range(k)]
        # assegna ciascuna contea al cluster relativo al centroide più vicino
        for j in range(n):
            # trova l'indice l del centroide più vicino
            min_val = float('inf')
            for f in range(k):
                cur_val = distance(P.dataset[j].get_coords(),centroids[f])
                if cur_val < min_val:
                    min_val = cur_val
                    l = f
            C[l].append(P.dataset[j])
        # aggiorna i nuovi centroidi in base ai cluster ottenuti
        for f in range(k):
            centroids[f] = center(C[f])
    return C


def distance(a, b):
    """
    Return the euclidean distance between two bidimensional points a and b
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1]- b[1]) ** 2)


def center(C: list):
    x = 0
    y = 0
    for p in C:
        x += p[0]
        y += p[1]
    if (len(C) > 0):
        x /= len(C)
        y /= len(C)
    return (x, y)
"""
def center(C: set):
    x = 0
    y = 0
    for p in C:
        x += p[0]
        y += p[1]
    if (len(C) > 0):
        x /= len(C)
        y /= len(C)
    return (x,y)
"""
