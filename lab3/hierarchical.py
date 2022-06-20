from data import data
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# hierarchical on euclidian distance
# Agglomerative (bottom up) variant
data_linkage = linkage(data, method='ward')
data_dendrogram = dendrogram(data_linkage)
plt.show()
