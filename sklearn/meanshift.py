import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import MeanShift

# center of blobs
centers = [[1, 1], [5, 5], [5, 10], [10, 5]]

# generate blobs
X, _ = make_blobs(n_samples=1000, centers=centers, cluster_std=1)

# plot blobs

plt.scatter(X[:, 0], X[:, 1])
plt.show()

# mean-shift model
model = MeanShift(max_iter=500)
model.fit(X)

labels = model.labels_
cluster_centers = model.cluster_centers_
print(cluster_centers)

# plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels.astype(np.float32))
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1],
            marker="x", linewidths=4)
plt.show()
