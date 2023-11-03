import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

raw_df = pd.read_csv("boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
target = pd.DataFrame(target, columns=["MEDV"])
y = target["MEDV"]

lm = LinearRegression()
lm.fit(X, y)

predicted_price = lm.predict(X)
print(predicted_price[0:5])
print("---------------------------")
MSE = np.mean((y-predicted_price)**2)
print("MSE:", MSE)
print("---------------------------")
print("R-squared:", lm.score(X, y))

