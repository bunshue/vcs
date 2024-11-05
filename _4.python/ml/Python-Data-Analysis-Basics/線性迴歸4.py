print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個


from sklearn.linear_model import LinearRegression

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
print("迴歸係數:", lm.coef_)
print("截距:", lm.intercept_ )
# 預測氣溫26, 30度的業績
new_temperatures = pd.DataFrame(np.array([26, 30]),
                                columns=["氣溫"])
predicted_sales = lm.predict(new_temperatures)
print(predicted_sales)

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression

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

plt.scatter(temperatures, drink_sales)  # 繪點
regression_sales = lm.predict(X)

plt.plot(temperatures, regression_sales, color="blue")
plt.plot(new_temperatures["氣溫"], predicted_sales, 
         color="red", marker="o", markersize=10)
plt.title("使用當日氣溫來預測當日的業積")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression

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

plt.scatter(heights, weights)  # 繪點
regression_weights = lm.predict(X)
plt.plot(heights, regression_weights, color="blue")
plt.plot(new_heights["身高"], predicted_weights, 
         color="red", marker="o", markersize=10)
plt.title("使用學生的身高來預測體重")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression

waist_heights = np.array([[67,160], [68,165], [70,167], 
                          [65,170], [80,165], [85,167],
                          [78,178], [79,182], [95,175],
                          [89,172]])
weights = np.array([50, 60, 65, 65,
                    70, 75, 80, 85,
                    90, 81])
X = pd.DataFrame(waist_heights, columns=["腰圍", "身高"])
target = pd.DataFrame(weights, columns=["體重"])
y = target["體重"]
lm = LinearRegression()
lm.fit(X, y)
print("迴歸係數:", lm.coef_)
print("截距:", lm.intercept_ )

# 預測腰圍和身高[66,164],[82,172]的體重
new_waist_heights = pd.DataFrame(np.array([[66, 164],
                                           [82, 172]]),
                                 columns=["腰圍", "身高"])
predicted_weights = lm.predict(new_waist_heights)
print(predicted_weights)

print("------------------------------------------------------------")  # 60個

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







print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


