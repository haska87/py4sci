import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import linear_model

import matplotlib.pyplot as plt

data = pd.read_csv('FuelConsumption.csv')
print(data.head())

viz = data[["FUELCONSUMPTION_COMB_MPG", "ENGINESIZE", "CO2EMISSIONS"]]

# viz.hist()
# plt.show()

X = np.asanyarray(viz[['FUELCONSUMPTION_COMB_MPG', 'ENGINESIZE']])
y = np.asanyarray(viz[['CO2EMISSIONS']])

model = linear_model.LinearRegression()
model.fit(X, y)

coef = model.coef_
inter = model.intercept_

print(coef, inter)

# plt.scatter(viz.ENGINESIZE, viz.CO2EMISSIONS)
# plt.plot(X, coef[0][0]*X + inter[0], color='red')
# plt.show()