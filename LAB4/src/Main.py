from county import Dataset
from clustering import kmeans_clustering
from clustering import hierarchical_clustering
from plotter import draw_clustering


print("Script start...")

dataset_full = Dataset("inputFiles/unifiedCancerData_3108.csv")
dataset_212 = Dataset("inputFiles/unifiedCancerData_212.csv")
dataset_562 = Dataset("inputFiles/unifiedCancerData_562.csv")
dataset_1041 = Dataset("inputFiles/unifiedCancerData_1041.csv")

C1 = kmeans_clustering(dataset_full, 15, 5)
C2 = hierarchical_clustering(dataset_full, 15)
draw_clustering(C1)


print("Script end")