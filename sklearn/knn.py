# k nearest neighbors
import numpy as np
import pandas as pd

from sklearn import neighbors
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Read data
iris =  datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Model
knn = neighbors.KNeighborsClassifier(n_neighbors=10, weights='uniform')

knn.fit(X_train, y_train)

prediction = knn.predict(X_test)

print(prediction)
print(y_test)

acc = metrics.accuracy_score(y_test, prediction)
print(acc)
mae = metrics.mean_absolute_error(y_test, prediction)
print(mae)