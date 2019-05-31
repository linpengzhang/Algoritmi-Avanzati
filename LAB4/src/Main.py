from county import Dataset
from clustering import kmeans_clustering
from clustering import hierarchical_clustering
from clustering import hierarchical_clustering_distortion_list
from plotter import draw_clustering
from plotter import draw_distortion


def domanda_1():
    print("Computing: hierchical clustering on dataset_full...")
    C, t, d = hierarchical_clustering(dataset_full, 15)
    print("Drawing...")
    draw_clustering(C)


def domanda_2():
    print("Computing: kmeans clustering on dataset_full...")
    C, t, d = kmeans_clustering(dataset_full, 15, 5)
    print("Drawing...")
    draw_clustering(C)


def domanda_4():
    print("Computing: hierchical clustering on dataset_212...")
    C, t, d = hierarchical_clustering(dataset_212, 9)
    print("Drawing...")
    draw_clustering(C)


def domanda_5():
    print("Computing: kmeans clustering on dataset_212...")
    C, t, d = kmeans_clustering(dataset_212, 9, 5)
    print("Drawing...")
    draw_clustering(C)


def domanda_6():
    print("Computing: hierchical clustering on dataset_212...")
    C1, t1, d1 = hierarchical_clustering(dataset_212, 9)
    print("Distortion for hierchical clustering:", d1)
    print("Computing: kmeans clustering on dataset_212...")
    C2, t2, d2 = kmeans_clustering(dataset_212, 9, 5)
    print("Distortion for kmeans clustering:", d2)


def domanda_9():
    datasets = {"dataset_212": dataset_212,
                "dataset_562": dataset_562,
                "dataset_1041": dataset_1041}
    min_c, max_c = 6, 21
    interval = range(min_c, max_c)
    for dataset in datasets.keys():
        h_distortion_list = hierarchical_clustering_distortion_list(datasets[dataset], min_c)[min_c:max_c]
        k_distortion_list = [kmeans_clustering(datasets[dataset], i, 5)[2] for i in interval]
        draw_distortion(list(interval), h_distortion_list, k_distortion_list, dataset)


print("Script start...")

print("Reading dataset...")
dataset_full = Dataset.read_from_file("inputFiles/unifiedCancerData_3108.csv")
dataset_212 = Dataset.read_from_file("inputFiles/unifiedCancerData_212.csv")
dataset_562 = Dataset.read_from_file("inputFiles/unifiedCancerData_562.csv")
dataset_1041 = Dataset.read_from_file("inputFiles/unifiedCancerData_1041.csv")
domanda_6()
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
