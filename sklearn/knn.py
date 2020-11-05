# k nearest neighbors
from sklearn import neighbors
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Read data
iris = datasets.load_iris()

# features and tagret
X = iris.data
y = iris.target

# split to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
knn = neighbors.KNeighborsClassifier(n_neighbors=10, weights='uniform')
# train
knn.fit(X_train, y_train)

prediction = knn.predict(X_test)

print(prediction)
print(y_test)

# metrics
acc = metrics.accuracy_score(y_test, prediction)
mae = metrics.mean_absolute_error(y_test, prediction)

print(acc)
print(mae)
