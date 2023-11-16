import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#訓練
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#預測
pre=body_reg.predict(x_values)

#圖形化
plt.scatter(x_values, y_values)
plt.plot(x_values,pre )
plt.show()
