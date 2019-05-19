from county import Dataset
from clustering import kmeans_clustering
from clustering import hierarchical_clustering
from plotter import draw_clustering


print("Script start...")

dataset_full = Dataset.read_from_file("inputFiles/unifiedCancerData_3108.csv")
dataset_212 = Dataset.read_from_file("inputFiles/unifiedCancerData_212.csv")
dataset_562 = Dataset.read_from_file("inputFiles/unifiedCancerData_562.csv")
dataset_1041 = Dataset.read_from_file("inputFiles/unifiedCancerData_1041.csv")

#C1 = kmeans_clustering(dataset_212, 15, 5)
#draw_clustering(C1)
C2 = hierarchical_clustering(dataset_562, 15)
somma = 0
for i in C2:
    somma= somma + len(i.dataset)
print(somma)
draw_clustering(C2)
print("Script end")