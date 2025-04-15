"""
隨機森林

RandomForestClassifier

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from common1 import *
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # Cross Validation
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier  # 隨機森林分類函數學習機
from sklearn.ensemble import RandomForestRegressor  # 隨機森林函數學習機
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("決策樹Decision Trees")

plt.figure(figsize=(16, 10))

# 使用 make_blobs 資料
N = 300  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 4  # centers, 分群數
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(n_samples=N, centers=GROUPS, cluster_std=1.0)

plt.subplot(231)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="rainbow")
plt.title("原始資料分佈(make_blobs)")

tree = DecisionTreeClassifier()  # 決策樹函數學習機
tree.fit(X, y)  # 學習訓練.fit


def visualize_classifier(model, X, y, ax=None, cmap="rainbow"):
    print("使用模型 :", model)
    ax = ax or plt.gca()

    # Plot the training points
    ax.scatter(
        X[:, 0], X[:, 1], c=y, s=30, cmap=cmap, clim=(y.min(), y.max()), zorder=3
    )
    ax.axis("tight")
    # ax.axis("off")
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    print(X.min())
    print(X.max())
    print(y.min())
    print(y.max())
    print(xlim)
    print(ylim)

    # fit the estimator
    model.fit(X, y)  # 學習訓練.fit
    xx, yy = np.meshgrid(np.linspace(*xlim, num=200), np.linspace(*ylim, num=200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)  # 預測.predict

    # Create a color plot with the results
    n_classes = len(np.unique(y))
    contours = ax.contourf(
        xx,
        yy,
        Z,
        alpha=0.3,
        levels=np.arange(n_classes + 1) - 0.5,
        cmap=cmap,
        # clim=(y.min(), y.max()),
        zorder=1,
    )
    ax.set(xlim=xlim, ylim=ylim)


print("------------------------------")  # 30個

print("決策樹")
model = DecisionTreeClassifier()  # 決策樹函數學習機
plt.subplot(232)
plt.title("決策樹")
visualize_classifier(model, X, y)

print("------------------------------")  # 30個

print("引導聚集分類(Bagging Classifier)")
tree = DecisionTreeClassifier()  # 決策樹函數學習機
# 通過每個估計器擬合80％的訓練點  BaggingClassifier利用平行估計器的集合
bag = BaggingClassifier(tree, n_estimators=100, max_samples=0.8, random_state=9487)
bag.fit(X, y)  # 學習訓練.fit
plt.subplot(233)
plt.title("引導聚集分類(Bagging Classifier)")
visualize_classifier(bag, X, y)

print("------------------------------")  # 30個

print("隨機森林 Random Forests")
model = RandomForestClassifier(n_estimators=100, random_state=9487)  # 隨機森林分類函數學習機
plt.subplot(234)
plt.title("隨機森林Random Forests")
visualize_classifier(model, X, y)

print("------------------------------")  # 30個

print("隨機森林迴歸 Random Forests Regression")

# Random Forest Regression
# 將隨機森林結合之前講解的線性迴歸，將資料迴歸至一條線上，並進行預測。
# 使用sin()正弦函數，可以看到輸出結果的圖形，符合正弦函數的圖型。

rng = np.random.RandomState(42)
x = 10 * rng.rand(200)


def model(x, sigma=0.3):
    fast_oscillation = np.sin(5 * x)
    slow_oscillation = np.sin(0.5 * x)
    noise = sigma * rng.randn(len(x))

    return slow_oscillation + fast_oscillation + noise


y = model(x)
plt.subplot(235)
plt.errorbar(x, y, 0.3, fmt="o")
# fmt(數據點標記樣式) :   'o' ',' '.' 'x' '+' 'v' '^' '<' '>' 's' 'd' 'p'
plt.title("原始資料分佈")

print("------------------------------")  # 30個

# 再來直接利用SKlearn中的RandomForestRegressor，來繪製出迴歸線
forest = RandomForestRegressor(200)
forest.fit(x[:, None], y)  # 學習訓練.fit

xfit = np.linspace(0, 10, 1000)
yfit = forest.predict(xfit[:, None])  # 預測.predict
ytrue = model(xfit, sigma=0)

plt.subplot(236)
plt.errorbar(x, y, 0.3, fmt="o", alpha=0.5)
plt.plot(xfit, yfit, "-r")
plt.plot(xfit, ytrue, "-k", alpha=0.5)
plt.title("隨機森林迴歸 Random Forests Regression")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用 make_blobs 資料
N = 300  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 4  # centers, 分群數

print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y = make_blobs(n_samples=N, centers=GROUPS, n_features=M)

clf = RandomForestClassifier(n_estimators=100)  # 隨機森林分類函數學習機

scores = cross_val_score(clf, X, y, cv=5)
print("看一下五次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])
Y = np.array(["man", "man", "man", "woman", "woman", "woman"])

RForest = RandomForestClassifier(
    n_estimators=100, max_depth=10, random_state=9487
)  # 隨機森林分類函數學習機

RForest.fit(X, Y)  # 學習訓練.fit

print(RForest.predict([[180, 85]]))  # 預測.predict

X, Y = make_classification(
    n_samples=10,
    n_features=3,
    n_informative=2,
    n_redundant=0,
    random_state=9487,
    shuffle=True,
)

model = RandomForestClassifier(
    n_estimators=100, max_depth=10, random_state=9487
)  # 隨機森林分類函數學習機

model.fit(X, Y)  # 學習訓練.fit

print(model.feature_importances_)
print(model.predict([[0, 0, 0]]))  # 預測.predict
estimator = model.estimators_[5]

from sklearn.tree import export_graphviz

# 決策樹可視化存檔
export_graphviz(
    estimator,
    out_file="tmp_tree.dot",
    feature_names=["A", "B", "C"],
    class_names=["0", "1"],
    rounded=True,
    proportion=False,
    precision=2,
    filled=True,
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
dx_train, dx_test, label_train, label_test = train_test_split(X, y, test_size=0.2)

forest_model = RandomForestClassifier()  # 隨機森林分類函數學習機

forest_model.fit(dx_train, label_train)  # 學習訓練.fit

# 對測試數據做預測
y_pred = forest_model.predict(dx_test)  # 預測.predict

# 輸出準確性
print(f"訓練資料的準確性 = {forest_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {forest_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("隨機森林_空氣盒子")

"""
15178筆資料 13欄位

SO2, CO, O3, PM25, Nox, NO, NO2, THC, NMHC, CH4, WindSpeed, TEMP, Humidity
"""

df = pd.read_excel("data/20160101-20190101(Daily)隨機森林.xlsx")
"""
cc = df.head(10)
print(cc)

#資料長度
print(df.shape)
print(len(df))
print(len(df["PM25"]))
df.info()  # 這樣就已經把資料集彙總資訊印出來
cc = df.describe()
print(cc)
"""

# One-Hot Encoding, 看不出差別
# One-hot encode the data using pandas get_dummies
df = pd.get_dummies(df)
cc = df.head(10)
print(cc)

# 從第5欄開始到最後欄
cc = df.iloc[:, 5:].head(10)
print(cc)

# 特徵轉換

# Labels are the values we want to predict
y = np.array(df["PM25"])
# y 要預測的項目

# 把這欄砍掉
# axis 1 refers to the columns
df = df.drop("PM25", axis=1)
print(df.shape)

# Saving feature names for later use
feature_list = list(df.columns)
print(feature_list)

# Convert to numpy array
print("df 轉 np.array")
X = np.array(df)

# 資料分割
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

"""
print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
"""

print("Training Features Shape:", X_train.shape)
print("Training Labels Shape:", y_train.shape)
print("Testing Features Shape:", X_test.shape)
print("Testing Labels Shape:", y_test.shape)

# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 1000棵 決策樹
random_forest_regressor = RandomForestRegressor(
    n_estimators=60, random_state=9487
)  # 隨機森林函數學習機

random_forest_regressor.fit(X_train, y_train)  # 學習訓練.fit

y_pred = random_forest_regressor.predict(X_test)  # 預測.predict

# 計算誤差
errors = abs(y_pred - y_test)

print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")

# Get numerical feature importances
importances = list(random_forest_regressor.feature_importances_)

# List of tuples with variable and importance
feature_importances = [
    (feature, round(importance, 2))
    for feature, importance in zip(feature_list, importances)
]

# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key=lambda x: x[1], reverse=True)

# Print out the feature and importances
[print("Variable: {:20} Importance: {}".format(*pair)) for pair in feature_importances]

# 視覺化變數特徵的重要程度

# Set the style
plt.style.use("fivethirtyeight")

# list of x locations for plotting
x_values = list(range(len(importances)))

# Make a bar chart
plt.bar(x_values, importances, orientation="vertical")

# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation="vertical")

plt.xlabel("Variable")
plt.ylabel("Importance")
plt.title("Variable Importances")

show()

# 計算MAE

# New random forest with only the two most important variables
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 1000棵 決策樹
rf_most_important = RandomForestRegressor(
    n_estimators=1000, random_state=9487
)  # 隨機森林函數學習機

# Extract the two most important df
important_indices = [feature_list.index("O3"), feature_list.index("TEMP")]
train_important = X_train[:, important_indices]
test_important = X_test[:, important_indices]

# Train the random forest
rf_most_important.fit(train_important, y_train)  # 學習訓練.fit

y_pred = rf_most_important.predict(test_important)  # 預測.predict

# 計算誤差
errors = abs(y_pred - y_test)

# Display the performance metrics
print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")

# 建立小棵的決測樹
from sklearn.tree import export_graphviz
import pydot

# Limit depth of tree to 3 levels
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 10棵 決策樹, 最多3層
rf_small = RandomForestRegressor(n_estimators=20, max_depth=3)  # 隨機森林函數學習機

rf_small.fit(X_train, y_train)  # 學習訓練.fit

# Extract the small tree
tree_small = rf_small.estimators_[5]

# Save the tree as a png image
# 決策樹可視化存檔
export_graphviz(
    tree_small,
    out_file="tmp_small_tree111.dot",
    feature_names=feature_list,
    rounded=True,
    precision=1,
)

(graph,) = pydot.graph_from_dot_file("tmp_small_tree111.dot")

# NG 無法寫入檔案
# graph.write_png('tmp_small_tree111.png');

# Use datetime for creating date objects for plotting
# import datetime

print(feature_list)

""" NG
print('這個df資料裡面根本沒有年月日資料可取出')
# Dates of training values
months = df[:, feature_list.index("month")]
days = df[:, feature_list.index("day")]
years = df[:, feature_list.index("year")]

# List and then convert to datetime object
dates = [
    str(int(year)) + "-" + str(int(month)) + "-" + str(int(day))
    for year, month, day in zip(years, months, days)
]
dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]

# Dataframe with true values and dates
true_data = pd.DataFrame(data={"date": dates, "actual": labels})

# Dates of predictions
months = X_test[:, feature_list.index("month")]
days = X_test[:, feature_list.index("day")]
years = X_test[:, feature_list.index("year")]

# Column of dates
test_dates = [
    str(int(year)) + "-" + str(int(month)) + "-" + str(int(day))
    for year, month, day in zip(years, months, days)
]

# Convert to datetime objects
test_dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in test_dates]

# Dataframe with predictions and dates
predictions_data = pd.DataFrame(data={"date": test_dates, "prediction": predictions})

# Plot the actual values
plt.plot(true_data["date"], true_data["actual"], "b-", label="actual")

# Plot the predicted values
plt.plot(
    predictions_data["date"], predictions_data["prediction"], "ro", label="prediction"
)
plt.xticks(rotation="60")
plt.legend()

# Graph labels
plt.xlabel("Date")
plt.ylabel("Maximum Temperature (F)")
plt.title("Actual and Predicted Values")

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("隨機森林_空氣盒子")

"""
687筆資料 13欄位
SO2, CO, O3, PM25, Nox, NO, NO2, THC, NMHC, CH4, WindSpeed, TEMP, Humidity
"""

df = pd.read_csv("data/200811-201811.csv")  # 共有 687 筆資料, 13欄位
"""
cc = df.head(10)
print(cc)

#資料長度
print(df.shape)
print(len(df))
print(len(df["PM25"]))
df.info()  # 這樣就已經把資料集彙總資訊印出來
cc = df.describe()
print(cc)
"""

# One-Hot Encoding, 看不出差別
# One-hot encode the data using pandas get_dummies
df = pd.get_dummies(df)
cc = df.head(10)
print(cc)

# 從第5欄開始到最後欄
cc = df.iloc[:, 5:].head(10)
print(cc)

# 特徵轉換

# Labels are the values we want to predict
labels = np.array(df["PM25"])
# labels 要預測的項目

print(df.shape)

# 把這欄砍掉
# axis 1 refers to the columns
df = df.drop("PM25", axis=1)
print(df.shape)

# Saving feature names for later use
feature_list = list(df.columns)
print(feature_list)

# Convert to numpy array
print("df 轉 np.array")
df = np.array(df)

# 資料分割
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
train_features, test_features, train_labels, test_labels = train_test_split(
    df, labels, test_size=0.2
)

"""
print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
"""
print("Training Features Shape:", train_features.shape)
print("Training Labels Shape:", train_labels.shape)
print("Testing Features Shape:", test_features.shape)
print("Testing Labels Shape:", test_labels.shape)

# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 1000棵 決策樹
random_forest_regressor = RandomForestRegressor(
    n_estimators=1000, random_state=9487
)  # 隨機森林函數學習機

random_forest_regressor.fit(train_features, train_labels)  # 學習訓練.fit

y_pred = random_forest_regressor.predict(test_features)  # 預測.predict

# 計算誤差
errors = abs(y_pred - test_labels)

print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")

# 繪製決策樹

from sklearn.tree import export_graphviz
import pydot

# Pull out one tree from the forest
tree = random_forest_regressor.estimators_[5]

# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot

# Pull out one tree from the forest
tree = random_forest_regressor.estimators_[5]

# 決策樹可視化存檔
export_graphviz(
    tree, out_file="tmp_tree.dot", feature_names=feature_list, rounded=True, precision=1
)

# Use dot file to create a graph
(graph,) = pydot.graph_from_dot_file("tmp_tree.dot")

# NG 無法寫入檔案
# graph.write_png('tree.png')

# 是否產出 dot file ?

# 變數特徵的重要程度

# Get numerical feature importances
importances = list(random_forest_regressor.feature_importances_)

# List of tuples with variable and importance
feature_importances = [
    (feature, round(importance, 2))
    for feature, importance in zip(feature_list, importances)
]

# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key=lambda x: x[1], reverse=True)

# Print out the feature and importances
[print("Variable: {:20} Importance: {}".format(*pair)) for pair in feature_importances]

# 視覺化變數特徵的重要程度

# Set the style
plt.style.use("fivethirtyeight")

# list of x locations for plotting
x_values = list(range(len(importances)))

# Make a bar chart
plt.bar(x_values, importances, orientation="vertical")

# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation="vertical")

# Axis labels and title
plt.ylabel("Importance")
plt.xlabel("Variable")
plt.title("Variable Importances")

show()

# 計算MAE

# New random forest with only the two most important variables
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 1000棵 決策樹
rf_most_important = RandomForestRegressor(
    n_estimators=1000, random_state=9487
)  # 隨機森林函數學習機

# Extract the two most important features
important_indices = [feature_list.index("NO2"), feature_list.index("TEMP")]
train_important = train_features[:, important_indices]
test_important = test_features[:, important_indices]

rf_most_important.fit(train_important, train_labels)  # 學習訓練.fit

y_pred = rf_most_important.predict(test_important)  # 預測.predict

# 計算誤差
errors = abs(y_pred - test_labels)

# Display the performance metrics
print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")

# 建立小棵的決測樹
from sklearn.tree import export_graphviz
import pydot

# Limit depth of tree to 3 levels
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 10棵 決策樹, 最多3層
rf_small = RandomForestRegressor(n_estimators=10, max_depth=3)  # 隨機森林函數學習機

rf_small.fit(train_features, train_labels)  # 學習訓練.fit

# Extract the small tree
tree_small = rf_small.estimators_[5]

# 決策樹可視化存檔
export_graphviz(
    tree_small,
    out_file="tmp_small_tree222.dot",
    feature_names=feature_list,
    rounded=True,
    precision=1,
)

(graph,) = pydot.graph_from_dot_file("tmp_small_tree222.dot")

# NG 無法寫入檔案
# graph.write_png('tmp_small_tree222.png');

# value為預測之PM2.5的數值

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Random Forest Regression

from sklearn.datasets import make_regression

n_samples = 100  # Number of samples
n_features = 6  # Number of features
n_informative = (
    3  # Number of informative features i.e. actual features which influence the output
)

X, y, coef = make_regression(
    n_samples=n_samples,
    n_features=n_features,
    n_informative=n_informative,
    random_state=None,
    shuffle=False,
    noise=20,
    coef=True,
)

df1 = pd.DataFrame(data=X, columns=["X" + str(i) for i in range(1, n_features + 1)])
df2 = pd.DataFrame(data=y, columns=["y"])
df = pd.concat([df1, df2], axis=1)
df.head(10)

# Scatter plots

with plt.style.context(("seaborn-dark")):
    for i, col in enumerate(df.columns[:-1]):
        plt.figure(figsize=(6, 4))
        plt.grid(True)
        plt.xlabel("Feature:" + col, fontsize=12)
        plt.ylabel("Output: y", fontsize=12)
        plt.scatter(df[col], df["y"], c="red", s=50, alpha=0.6)
show()

with plt.style.context(("fivethirtyeight")):
    for i, col in enumerate(df.columns[:-1]):
        plt.figure(figsize=(6, 4))
        plt.grid(True)
        plt.xlabel("Feature:" + col, fontsize=12)
        plt.ylabel("Output: y", fontsize=12)
        plt.hist(df[col], alpha=0.6, facecolor="g")
show()

from sklearn import tree

tree_model = tree.DecisionTreeRegressor(max_depth=5, random_state=None)
tree_model.fit(X, y)

print("Relative importance of the features: ", tree_model.feature_importances_)
with plt.style.context("dark_background"):
    plt.figure(figsize=(10, 7))
    plt.grid(True)
    plt.yticks(range(n_features + 1, 1, -1), df.columns[:-1], fontsize=20)
    plt.xlabel("Relative (normalized) importance of parameters", fontsize=15)
    plt.ylabel("Features\n", fontsize=20)
    plt.barh(
        range(n_features + 1, 1, -1), width=tree_model.feature_importances_, height=0.5
    )
show()

# Print the R2 score of the Decision Tree regression model

print("Regression coefficient:", tree_model.score(X, y))

# Regression coefficient: 0.95695111153

# Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    max_depth=5,
    random_state=None,
    max_features="auto",
    max_leaf_nodes=5,
    n_estimators=100,
)
"""
model.fit(X, y)

#Print the relative importance of the features

print("Relative importance of the features: ",model.feature_importances_)
with plt.style.context('dark_background'):
    plt.figure(figsize=(10,7))
    plt.grid(True)
    plt.yticks(range(n_features+1,1,-1),df.columns[:-1],fontsize=20)
    plt.xlabel("Relative (normalized) importance of parameters",fontsize=15)
    plt.ylabel("Features\n",fontsize=20)
    plt.barh(range(n_features+1,1,-1),width=model.feature_importances_,height=0.5)
show()

#Print the R2 score of the Random Forest regression model

print("Regression coefficient:",model.score(X,y))

#Regression coefficient: 0.811794737752

import statsmodels.api as sm

Xs=sm.add_constant(X)
stat_model = sm.OLS(y,Xs)
stat_result = stat_model.fit()

print(stat_result.summary())

rf_coef=np.array(coef)
stat_coef=np.array(stat_result.params[1:])

df_coef = pd.DataFrame(data=[rf_coef,stat_coef],columns=df.columns[:-1],index=['True Regressors', 'OLS method estimation'])
df_coef

df_importance = pd.DataFrame(data=[model.feature_importances_,stat_result.tvalues[1:]/sum(stat_result.tvalues[1:])],
                             columns=df.columns[:-1],
                             index=['RF Regressor relative importance', 'OLS method normalized t-statistic'])
df_importance
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/Social_Network_Ads.csv")

X = df.iloc[:, [2, 3]].values
y = df.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Feature Scaling 特征縮放
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

clf = RandomForestClassifier(n_estimators=10, criterion="entropy", random_state=0)

clf.fit(X_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

# 生成混淆矩陣(Confusion Matrix)，也稱作誤差矩陣

cm = confusion_matrix(y_test, y_pred)

from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("Random Forest Classification (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

from matplotlib.colors import ListedColormap

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("Random Forest Classification (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個
