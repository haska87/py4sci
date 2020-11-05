# k keans clustering algorithm
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# read data from csv
cust_df = pd.read_csv("sklearn\Cust_Segmentation.csv")
print(cust_df.head())

df = cust_df.drop("Address", axis=1)
print(df.head())

# convert to array
X = df.values[:, 1:]
print(X)
X = np.nan_to_num(X)

# kmeans model
model = KMeans(n_clusters=3)
model.fit(X)

labels = model.labels_
print(labels)

df["Cluster"] = labels
print(df.head())

# mean of groups
cluster_mean = df.groupby("Cluster").mean()
print(cluster_mean)

# plot 2D
# plt.scatter(X[:, 0], X[:, 3], c=labels.astype(np.float))
# plt.xlabel("Age")
# plt.ylabel("Income")
# plt.show()

# plot 3D
fig = plt.figure(1, figsize=(8, 6))
plt.clf()

ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=145)

ax.set_xlabel("Education")
ax.set_ylabel("Age")
ax.set_zlabel("Income")

ax.scatter(X[:, 1], X[:, 0], X[:, 3], c=labels.astype(np.float))
plt.show()
