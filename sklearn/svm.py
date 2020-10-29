# k nearest neighbors
import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm

# Read data
iris =  datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

model = svm.SVC()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

acc = metrics.accuracy_score(y_test, prediction)
print(acc)