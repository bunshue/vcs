import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

area_dists = np.array([[10,80], [8,0], [8,200], 
                       [5,200], [7,300], [8,230],
                       [7,40], [9,0], [6,330],
                       [9,180]])
sales = np.array([46.9, 36.6, 37.1, 20.8,
                    24.6, 29.7, 36.6, 43.6,
                    19.8, 36.4])
X = pd.DataFrame(area_dists, columns=["店面積", "距捷運"])
target = pd.DataFrame(sales, columns=["月營收"])
y = target["月營收"]
lm = LinearRegression()
lm.fit(X, y)
print("迴歸係數:", lm.coef_)
print("截距:", lm.intercept_ )

# 預測腰面積和距離[10,100]的營業額
new_area_dists = pd.DataFrame(np.array([[10, 100]]),
                              columns=["店面積", "距捷運"])
predicted_sales = lm.predict(new_area_dists)
print(predicted_sales)
