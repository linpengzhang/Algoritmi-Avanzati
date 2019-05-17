import math
import random

def kmeans_clustering(P: list, k, q):
    n = len(P)
    # crea k centroidi con valori arbitrari
    centroids = [(random.random(),random.random()) for _ in range(k)]
    for _ in range(q):
        # crea k cluster vuoti
        C = [[] for _ in range(k)]
        for j in range(n):
            min_val = float('inf')
            for f in range(k):
                if distance(P[j],centroids[f]) < min_val:
                    min_val = distance(P[j],centroids[f])
                    l = f
            C[l].append(P[j])
        for f in range(k):
            centroids[f] = center(C[f])
    return C


def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def center(C: list):
    x = 0
    y = 0
    for p in C:
        x += p[0]
        y += p[1]
    if (len(C) > 0):
        x /= len(C)
        y /= len(C)
    return (x,y)