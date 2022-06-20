from data import data
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

kmeans = KMeans(init="random", n_clusters=3)
kmeans.fit(data)


def get_nearest(cur_arr, centers):
    res = []
    for x, y in cur_arr:
        min_dist = 1e10
        min_id = -1
        for i in range(len(centers)):
            cur_dist = (centers[i][0] - x) ** 2 + (centers[i][1] - y) ** 2
            if cur_dist < min_dist:
                min_id = i
                min_dist = cur_dist
        res.append(min_id)

    return res


fig, ax = plt.subplots(figsize=(8, 6))
customcmap = ListedColormap(["crimson", "mediumblue", "darkmagenta"])
plt.scatter(data[:, 0], data[:, 1], marker='o',
            c=get_nearest(data, kmeans.cluster_centers_),
            cmap=customcmap, s=80, alpha=0.5)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            marker='s', s=200, c=[0, 1, 2],
            cmap=customcmap)
ax.set_xlabel(r'x', fontsize=14)
ax.set_ylabel(r'y', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
