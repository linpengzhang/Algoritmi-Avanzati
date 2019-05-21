from county import *
from clustering import kmeans_clustering
from clustering import hierarchical_clustering
from plotter import draw_clustering

print("Script start...")

print("Reading dataset...")
dataset_full = Dataset.read_from_file("inputFiles/unifiedCancerData_3108.csv")
dataset_212 = Dataset.read_from_file("inputFiles/unifiedCancerData_212.csv")
dataset_562 = Dataset.read_from_file("inputFiles/unifiedCancerData_562.csv")
dataset_1041 = Dataset.read_from_file("inputFiles/unifiedCancerData_1041.csv")


# print("Computing...")
# C1 = kmeans_clustering(dataset_full, 15, 5)
# print("Drawing...")
# draw_clustering(C1)

print("Computing...")
C2 = hierarchical_clustering(dataset_562, 16)
print("Drawing...")
draw_clustering(C2)


print("Script end")
