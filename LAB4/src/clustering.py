import math
import random
import heapq
from country import *
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

def center(C: Dataset):
    """
    Returns the centroid of the cluster C
    """
    (sum_x, sum_y) = reduce((lambda a, b : (a[0] + b[0], a[1] + b[1])), C.get_list_of_coords(), (0,0))
    m = len(C.dataset)
    return (sum_x/m, sum_y/m)