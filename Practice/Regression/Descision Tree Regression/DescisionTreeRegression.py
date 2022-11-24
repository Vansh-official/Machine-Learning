import pandas as pd
import numpy as np

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[: , 1: -1].values
Y = dataset.iloc[:, -1].values

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, Y)

print(regressor.predict([[6.5]]))

import  matplotlib.pyplot as plt
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Desicion Tree regressor')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()