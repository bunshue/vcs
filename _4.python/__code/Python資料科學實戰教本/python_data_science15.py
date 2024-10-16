"""
Python資料科學實戰教本



"""

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

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
print(data.shape)

print("------------------------------------------------------------")  # 60個

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
print(X.head())

print("---------------------------")
target = pd.DataFrame(target, columns=["MEDV"])
print(target.head())

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
target = pd.DataFrame(target, columns=["MEDV"])
y = target["MEDV"]

lm = LinearRegression()
lm.fit(X, y)
print("迴歸係數:", lm.coef_)
print("截距:", lm.intercept_ )
print("---------------------------")
coef = pd.DataFrame(feature_names, columns=["features"])
coef["estimatedCoefficients"] = lm.coef_
print(coef)

plt.scatter(X.RM, y)
plt.xlabel("每個住宅的平均房間數(RM)")
plt.ylabel("中位數房價(MEDV)")
plt.title("每個住宅的平均房間數和中位數房價的關聯性")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
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

plt.scatter(y, predicted_price)
plt.xlabel("中位數房價")
plt.ylabel("預測的中位數房價")
plt.title("中位數房價 vs 預測的中位數房價")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
target = pd.DataFrame(target, columns=["MEDV"])
y = target["MEDV"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=5)
lm = LinearRegression()
lm.fit(XTrain, yTrain)

pred_test = lm.predict(XTest)

plt.scatter(yTest, pred_test)
plt.xlabel("中位數房價")
plt.ylabel("預測的中位數房價")
plt.title("中位數房價 vs 預測的中位數房價")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
target = pd.DataFrame(target, columns=["MEDV"])
y = target["MEDV"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=5)
lm = LinearRegression()
lm.fit(XTrain, yTrain)

pred_train = lm.predict(XTrain)
pred_test = lm.predict(XTest)

MSE_train = np.mean((yTrain-pred_train)**2)
MSE_test = np.mean((yTest-pred_test)**2)
print("訓練資料的MSE:", MSE_train)
print("測試資料的MSE:", MSE_test)
print("---------------------------")
print("訓練資料的R-squared:", lm.score(XTrain, yTrain))
print("測試資料的R-squared:", lm.score(XTest, yTest))

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
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

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
target = pd.DataFrame(target, columns=["MEDV"])
y = target["MEDV"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=5)
lm = LinearRegression()
lm.fit(XTrain, yTrain)

pred_train = lm.predict(XTrain)
pred_test = lm.predict(XTest)

plt.scatter(pred_train, yTrain-pred_train,
            c="b", s=40, alpha=0.5, label="訓練資料集")
plt.scatter(pred_test, yTest-pred_test,
            c="r", s=40, label="測試資料集")
plt.hlines(y=0, xmin=0, xmax=50)
plt.title("殘差圖(Residual Plot)")
plt.ylabel("殘差值(Residual Value)")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns

raw_df = pd.read_csv("data/boston.csv", sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
                 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
X = pd.DataFrame(data, columns=feature_names)
target = pd.DataFrame(target, columns=["MEDV"])
y = target["MEDV"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=5)
lm = LinearRegression()
lm.fit(XTrain, yTrain)

pred_train = lm.predict(XTrain)
pred_test = lm.predict(XTest)

sns.set_style("darkgrid", {"axes.axisbelow": False,
                       "font.sans-serif":['Microsoft JhengHei']})

df = pd.DataFrame({"x": pred_train, "y": yTrain})
df2 = pd.DataFrame({"x": pred_test, "y": yTest})
sns.residplot(x="x", y="y", data=df)
sns.residplot(x="x", y="y", data=df2)
plt.title("殘差圖(Residual Plot)")
plt.ylabel("殘差值(Residual Value)")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

t = np.arange(-6, 6, 0.1)
S = 1/(1+(np.e**(-t)))

plt.plot(t, S)
plt.title("sigmoid函數")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing, linear_model

titanic = pd.read_csv("data/titanic.csv")
print(titanic.info())
print("---------------------------")
# 將年齡的空值填入年齡的中位數
age_median = np.nanmedian(titanic["Age"])
print("年齡中位數", age_median)
print("---------------------------")
new_age = np.where(titanic["Age"].isnull(), 
                   age_median, titanic["Age"])
titanic["Age"] = new_age
print(titanic)
print("---------------------------")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, 
                  titanic["SexCode"],
                  titanic["Age"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)
print("迴歸係數:", logistic.coef_)
print("截距:", logistic.intercept_ )

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing, linear_model

titanic = pd.read_csv("data/titanic.csv")
print(titanic.info())
print("---------------------------")
# 將年齡的空值填入年齡的中位數
age_median = np.nanmedian(titanic["Age"])
new_age = np.where(titanic["Age"].isnull(), 
                   age_median, titanic["Age"])
titanic["Age"] = new_age
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, 
                  titanic["SexCode"],
                  titanic["Age"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)

preds = logistic.predict(X)
print(pd.crosstab(preds, titanic["Survived"]))

print("---------------------------")
print((805+265)/(805+185+58+265))
print(logistic.score(X, y))

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing, linear_model

titanic = pd.read_csv("data/titanic.csv")
print(titanic.info())
print("---------------------------")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, 
                  titanic["SexCode"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)
print("迴歸係數:", logistic.coef_)
print("截距:", logistic.intercept_ )
print("---------------------------")
preds = logistic.predict(X)
print(pd.crosstab(preds, titanic["Survived"]))

print("---------------------------")
print((840+222)/(840+222+23+228))
print(logistic.score(X, y))

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

