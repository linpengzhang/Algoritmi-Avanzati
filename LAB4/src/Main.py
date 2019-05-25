from county import Dataset
from clustering import kmeans_clustering
from clustering import hierarchical_clustering
from clustering import hierarchical_clustering_distortion_list
from plotter import draw_clustering
from plotter import draw_distortion

print("Script start...")

print("Reading dataset...")
dataset_full = Dataset.read_from_file("inputFiles/unifiedCancerData_3108.csv")
dataset_212 = Dataset.read_from_file("inputFiles/unifiedCancerData_212.csv")
dataset_562 = Dataset.read_from_file("inputFiles/unifiedCancerData_562.csv")
dataset_1041 = Dataset.read_from_file("inputFiles/unifiedCancerData_1041.csv")
print("Computing...")
"""
C1, t1, d1 = kmeans_clustering(dataset_212, 9, 5)
print("Time spent for kmeans clustering:", t1)
print("Distortion for kmeans clustering:", d1)
print("Drawing...")
draw_clustering(C1)


print("Computing...")
C2, t2, d2 = hierarchical_clustering(dataset_212, 9)
print("Time spent for hierchical clustering:", t2)
print("Distortion for hierchical clustering:", d2)
print("Drawing...")
draw_clustering(C2)
"""
datasets = {"dataset_212": dataset_212,
            "dataset_562": dataset_562,
            "dataset_1041": dataset_1041}
interval = range(6, 21)
for dataset in datasets.keys():
    h_distortion_list = [hierarchical_clustering_distortion_list(datasets[dataset], interval[0])[i] for i in interval]
    k_distortion_list = [kmeans_clustering(datasets[dataset], i, 5)[2] for i in interval]
    """
    print(k_distortion_list)
    print(h_distortion_list)
    """
    draw_distortion(list(interval),h_distortion_list,k_distortion_list, dataset)
print("Script end")
