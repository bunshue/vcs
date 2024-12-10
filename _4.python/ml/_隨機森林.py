"""
隨機森林

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
from sklearn.datasets import make_blobs
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score  # Cross Validation

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 500
GROUPS = 3
X, y = make_blobs(n_samples=N, centers=GROUPS, n_features=2)

print("使用 Random Forest")

clf = RandomForestClassifier(n_estimators=100)

scores = cross_val_score(clf, X, y, cv=5)
print("看一下五次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
機器學習_隨機森林_空氣盒子
"""

df = pd.read_excel("data/20160101-20190101(Daily)隨機森林.xlsx")

"""
cc = df.head(10)
print(cc)

#資料長度
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

# 將資料分成訓練組及測試組
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)# 訓練組8成, 測試組2成
X_train, X_test, y_train, y_test = train_test_split(
    df, labels, test_size=0.25, random_state=42
)  # 訓練組7.5成, 測試組2.5成

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
random_forest_regressor = RandomForestRegressor(n_estimators=60, random_state=42)

random_forest_regressor.fit(X_train, y_train)  # 學習訓練.fit
# 預測
predictions = random_forest_regressor.predict(X_test)  # 預測.predict

# 計算誤差
errors = abs(predictions - y_test)

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

# Axis labels and title
plt.ylabel("Importance")
plt.xlabel("Variable")
plt.title("Variable Importances")

plt.show()

# 計算MAE

# New random forest with only the two most important variables
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 1000棵 決策樹
rf_most_important = RandomForestRegressor(n_estimators=1000, random_state=42)

# Extract the two most important df
important_indices = [feature_list.index("O3"), feature_list.index("TEMP")]
train_important = X_train[:, important_indices]
test_important = X_test[:, important_indices]

# Train the random forest
rf_most_important.fit(train_important, y_train)

# 預測
predictions = rf_most_important.predict(test_important)  # 預測.predict

# 計算誤差
errors = abs(predictions - y_test)

# Display the performance metrics
print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")

# 建立小棵的決測樹
from sklearn.tree import export_graphviz
import pydot

# Limit depth of tree to 3 levels
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 10棵 決策樹, 最多3層
rf_small = RandomForestRegressor(n_estimators=20, max_depth=3)
rf_small.fit(X_train, y_train)

# Extract the small tree
tree_small = rf_small.estimators_[5]

# Save the tree as a png image
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
import datetime

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

plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
20190314-空氣盒子數據Scikit-Learn隨機森林實作
"""
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/200811-201811.csv")  # 共有 687 筆資料, 13欄位

"""
cc = df.head(10)
print(cc)

#資料長度
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

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
train_features, test_features, train_labels, test_labels = train_test_split(
    df, labels, test_size=0.2
)
# 訓練組8成, 測試組2成

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
random_forest_regressor = RandomForestRegressor(n_estimators=1000, random_state=42)

random_forest_regressor.fit(train_features, train_labels)  # 學習訓練.fit

# 預測
predictions = random_forest_regressor.predict(test_features)  # 預測.predict

# 計算誤差
errors = abs(predictions - test_labels)

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

# Export the image to a dot file
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

plt.show()


# 計算MAE

# New random forest with only the two most important variables
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 1000棵 決策樹
rf_most_important = RandomForestRegressor(n_estimators=1000, random_state=42)

# Extract the two most important features
important_indices = [feature_list.index("NO2"), feature_list.index("TEMP")]
train_important = train_features[:, important_indices]
test_important = test_features[:, important_indices]

rf_most_important.fit(train_important, train_labels)  # 學習訓練.fit

# 預測
predictions = rf_most_important.predict(test_important)  # 預測.predict

# 計算誤差
errors = abs(predictions - test_labels)

# Display the performance metrics
print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")

# 建立小棵的決測樹
from sklearn.tree import export_graphviz
import pydot

# Limit depth of tree to 3 levels
# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 10棵 決策樹, 最多3層
rf_small = RandomForestRegressor(n_estimators=10, max_depth=3)

rf_small.fit(train_features, train_labels)  # 學習訓練.fit

# Extract the small tree
tree_small = rf_small.estimators_[5]

# Save the tree as a png image
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

X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])
Y = np.array(["man", "man", "man", "woman", "woman", "woman"])

RForest = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=2)
RForest.fit(X, Y)
print(RForest.predict([[180, 85]]))

X, Y = make_classification(
    n_samples=10,
    n_features=3,
    n_informative=2,
    n_redundant=0,
    random_state=0,
    shuffle=True,
)

model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=2)
model.fit(X, Y)
print(model.feature_importances_)
print(model.predict([[0, 0, 0]]))
estimator = model.estimators_[5]

from sklearn.tree import export_graphviz

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

data, label = datasets.load_iris(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    data, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
forest_model = RandomForestClassifier()

# 建立訓練數據模型
forest_model.fit(dx_train, label_train)

# 對測試數據做預測
pred = forest_model.predict(dx_test)

# 輸出準確性
print(f"訓練資料的準確性 = {forest_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {forest_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
