import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

temperatures = np.array([29, 28, 34, 31,
                         25, 29, 32, 31,
                         24, 33, 25, 31,
                         26, 30])
drink_sales = np.array([7.7, 6.2, 9.3, 8.4,
                        5.9, 6.4, 8.0, 7.5,
                        5.8, 9.1, 5.1, 7.3,
                        6.5, 8.4])
X = pd.DataFrame(temperatures, columns=["氣溫"])
target = pd.DataFrame(drink_sales, columns=["營業額"])
y = target["營業額"]
lm = LinearRegression()
lm.fit(X, y)
# 預測氣溫26, 30度的業績
new_temperatures = pd.DataFrame(np.array([26, 30]),
                                columns=["氣溫"])
predicted_sales = lm.predict(new_temperatures)
print(predicted_sales)

regression_sales = lm.predict(X)

plt.rcParams["axes.unicode_minus"] = False
sns.set_style("darkgrid", {"axes.axisbelow": False,
                       "font.sans-serif":['Microsoft JhengHei']})

df = pd.DataFrame({"氣溫": temperatures,
                   "營業額": drink_sales})
sns.regplot(x="氣溫", y="營業額", data=df)
plt.plot(temperatures, regression_sales, color="pink")
plt.plot(new_temperatures["氣溫"], predicted_sales, 
         color="red", marker="o", markersize=10)
plt.title("使用當日氣溫來預測當日的業積")
plt.show()