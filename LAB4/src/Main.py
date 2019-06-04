from county import Dataset
from clustering import kmeans_clustering
from clustering import hierarchical_clustering
from clustering import hierarchical_clustering_distortion_list
from plotter import draw_clustering
from plotter import draw_distortion


def domanda_1():
    print("Computing: hierchical clustering on dataset_full...")
    C, t, d = hierarchical_clustering(dataset_full, 15, weighted)
    print("Drawing...")
    draw_clustering(C, "Clustering gerarchico sull'intero dataset" + (" (v. pesata)" if weighted else ""))


def domanda_2():
    print("Computing: kmeans clustering on dataset_full...")
    C, t, d = kmeans_clustering(dataset_full, 15, 5, weighted)
    print("Drawing...")
    draw_clustering(C, "Clustering k-means sull'intero dataset" + (" (v. pesata)" if weighted else ""))


def domanda_4():
    print("Computing: hierchical clustering on dataset_212...")
    C, t, d = hierarchical_clustering(dataset_212, 9, weighted)
    print("Drawing...")
    draw_clustering(C, "Clustering gerarchico su 212 contee" + (" (v. pesata)" if weighted else ""))


def domanda_5():
    print("Computing: kmeans clustering on dataset_212...")
    C, t, d = kmeans_clustering(dataset_212, 9, 5, weighted)
    print("Drawing...")
    draw_clustering(C, "Clustering k-means su 212 contee" + (" (v. pesata)" if weighted else ""))


def domanda_6():
    print("Computing: hierchical clustering on dataset_212...")
    C1, t1, d1 = hierarchical_clustering(dataset_212, 9, weighted)
    print("Distortion for hierchical clustering:", d1)
    print("Computing: kmeans clustering on dataset_212...")
    C2, t2, d2 = kmeans_clustering(dataset_212, 9, 5, weighted)
    print("Distortion for kmeans clustering:", d2)


def domanda_9():
    print("Computing...")
    datasets = {"dataset con 212 contee": dataset_212,
                "dataset con 562 contee": dataset_562,
                "dataset con 1041 contee": dataset_1041}
    min_c, max_c = 6, 21
    interval = range(min_c, max_c)
    for name, dataset in datasets.items():
        h_distortion_list = hierarchical_clustering_distortion_list(dataset, min_c, weighted)[min_c:max_c]
        k_distortion_list = [kmeans_clustering(dataset, i, 5, weighted)[2] for i in interval]
        draw_distortion(list(interval), h_distortion_list, k_distortion_list, name + (" (v. pesata)" if weighted else ""))


print("Script start...")

print("Reading dataset...")
dataset_full = Dataset.read_from_file("inputFiles/unifiedCancerData_3108.csv")
dataset_212 = Dataset.read_from_file("inputFiles/unifiedCancerData_212.csv")
dataset_562 = Dataset.read_from_file("inputFiles/unifiedCancerData_562.csv")
dataset_1041 = Dataset.read_from_file("inputFiles/unifiedCancerData_1041.csv")

# indica se il calcolo dei centroidi è pesato o meno
weighted = False

"""
# EFFICIENZA
domanda_1()
domanda_2()
# AUTOMAZIONE
domanda_4()
domanda_5()
domanda_6()
# QUALITA'
domanda_9()
"""

print("Script end")
