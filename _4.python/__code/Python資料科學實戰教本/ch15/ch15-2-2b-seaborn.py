import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

heights = np.array([147.9, 163.5, 159.8, 155.1,
                    163.3, 158.7, 172.0, 161.2,
                    153.9, 161.6])
weights = np.array([41.7, 60.2, 47.0, 53.2,
                    48.3, 55.2, 58.5, 49.0,
                    46.7, 52.5])
X = pd.DataFrame(heights, columns=["身高"])
target = pd.DataFrame(weights, columns=["體重"])
y = target["體重"]
lm = LinearRegression()
lm.fit(X, y)
print("迴歸係數:", lm.coef_)
print("截距:", lm.intercept_ )

# 預測身高150, 160, 170的體重
new_heights = pd.DataFrame(np.array([150, 160, 170]),
                           columns=["身高"])
predicted_weights = lm.predict(new_heights)
print(predicted_weights)

regression_weights = lm.predict(X)

plt.rcParams["axes.unicode_minus"] = False
sns.set_style("darkgrid", {"axes.axisbelow": False,
                       "font.sans-serif":['Microsoft JhengHei']})

df = pd.DataFrame({"身高": heights,
                   "體重": weights})
sns.regplot(x="身高", y="體重", data=df)
plt.plot(heights, regression_weights, color="pink")
plt.plot(new_heights["身高"], predicted_weights, 
         color="red", marker="o", markersize=10)
plt.title("使用學生的身高來預測體重")
plt.show()