from data import data
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

nn_classifier = NearestNeighbors(n_neighbors=2)
nn_classifier = nn_classifier.fit(data)


def get_clusters(nearest):
    clusters = [[i] for i in range(len(nearest))]
    for i in range(len(nearest)):
        merge_clusters = []
        for val in nearest[i]:
            for j in range(len(clusters)):
                if val in clusters[j]:
                    merge_clusters.append(j)
        if len(merge_clusters) == 0:
            clusters.append([i])
        elif len(merge_clusters) == 1:
            continue
        else:
            new_clusters = [[], ]
            for j in range(len(clusters)):
                if j in merge_clusters:
                    new_clusters[0].extend(clusters[j])
                else:
                    new_clusters.append(clusters[j])
            clusters = new_clusters
    return clusters


# getting neighbours
result = nn_classifier.kneighbors(data, return_distance=False)
print(result)

# merging and getting clusters
clusters = get_clusters(result)

res_color = list(range(len(data)))
for i in range(len(clusters)):
    for val in clusters[i]:
        res_color[val] = i


fig, ax = plt.subplots(figsize=(8, 6))
customcmap = ListedColormap(["crimson", "mediumblue", "darkmagenta"])
plt.scatter(data[:, 0], data[:, 1], marker='o',
            c=res_color,
            cmap=customcmap, s=80, alpha=0.5)
ax.set_xlabel(r'x', fontsize=14)
ax.set_ylabel(r'y', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
