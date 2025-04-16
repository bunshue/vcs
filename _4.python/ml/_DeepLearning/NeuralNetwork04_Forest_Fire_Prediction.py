"""
真實問題
Forest_Fire_Prediction

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

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Forrest Fire (Protugal) prediction using SVR, Random Forest, and Deep NN
"""
forestfires.csv 517筆資料 13欄位

X,Y,month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain,area

    X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
    Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
    month - month of the year: "jan" to "dec"
    day - day of the week: "mon" to "sun"
    FFMC - FFMC index from the FWI system: 18.7 to 96.20
    DMC - DMC index from the FWI system: 1.1 to 291.3
    DC - DC index from the FWI system: 7.9 to 860.6
    ISI - ISI index from the FWI system: 0.0 to 56.10
    temp - temperature in Celsius degrees: 2.2 to 33.30
    RH - relative humidity in %: 15.0 to 100
    wind - wind speed in km/h: 0.40 to 9.40
    rain - outside rain in mm/m2 : 0.0 to 6.4
    area - the burned area of the forest (in ha): 0.00 to 1090.84
"""

df = pd.read_csv("data/forestfires.csv")
print(df.shape)
cc = df.head()
print(cc)

# Basic statistics and visualization of the dataset

cc = df.describe()
print(cc)

# Plot scatterplots and distributions of numerical features to see how they may affect the output 'area'

df["Log-area"] = np.log10(df["area"] + 1)
"""
for i in df.describe().columns[:-2]:
    df.plot.scatter(i, "Log-area",grid=True)
    show()
    
# Plot boxplots of how the categorical features (month and day) affect the outcome

df.boxplot(column="Log-area",by="day")

show()

df.boxplot(column="Log-area",by="month")

show()
"""
# Data pre-processing, test/train split, REC function

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

# Label encoder for the categorical feature (day and month)

enc = LabelEncoder()
enc.fit(df["month"])

# LabelEncoder()

print(enc.classes_)


df["month_encoded"] = enc.transform(df["month"])
cc = df.head()
print(cc)

enc.fit(df["day"])

# LabelEncoder()

print(enc.classes_)


df["day_encoded"] = enc.transform(df["day"])
cc = df.head(15)
print(cc)

# Test set fraction

test_size = 0.4

# Test/train split

X_data = df.drop(["area", "Log-area", "month", "day"], axis=1)
y_data = df["Log-area"]

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=test_size)

y_train = np.array(y_train)

y_train = y_train.reshape(y_train.size, 1)

# Regression Error Characteristic (REC) estimation

# Receiver Operating Characteristic (ROC) curves provide a powerful tool for visualizing and comparing classification results.
# Regression Error Characteristic (REC) curves generalize ROC curves to regression.
# REC curves plot the error tolerance on the
# The area-over-the-curve (AOC) is a biased estimate of the expected error.


def rec(m, n, tol):
    if type(m) != "numpy.ndarray":
        m = np.array(m)
    if type(n) != "numpy.ndarray":
        n = np.array(n)
    l = m.size
    percent = 0
    for i in range(l):
        if np.abs(10 ** m[i] - 10 ** n[i]) <= tol:
            percent += 1
    return 100 * (percent / l)


# Define the max tolerance limit for REC curve x-axis
# For this problem this represents the absolute value of error in the prediction of the outcome i.e. area burned
tol_max = 20

# Gridsearch

# Finding the right parameters for machine learning models is a tricky task! But luckily, Scikit-learn has the functionality of trying a bunch of combinations and see what works best, built in with GridSearchCV! The CV stands for cross-validation.

# GridSearchCV takes a dictionary that describes the parameters that should be tried and a model to train. The grid of parameters is defined as a dictionary, where the keys are the parameters and the values are the settings to be tested.
# Support Vector Regressor (SVR)

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

scaler = StandardScaler()

# Parameter grid for the Grid Search
param_grid = {
    "C": [0.01, 0.1, 1, 10],
    "epsilon": [10, 1, 0.1, 0.01, 0.001, 0.0001],
    "kernel": ["rbf"],
}

grid_SVR = GridSearchCV(SVR(), param_grid, refit=True, verbose=0, cv=5)

grid_SVR.fit(scaler.fit_transform(X_train), scaler.fit_transform(y_train))

print("Best parameters obtained by Grid Search:", grid_SVR.best_params_)

# Best parameters obtained by Grid Search: {'C': 0.01, 'epsilon': 1, 'kernel': 'rbf'}

a = grid_SVR.predict(X_test)
print("RMSE for Support Vector Regression:", np.sqrt(np.mean((y_test - a) ** 2)))

# RMSE for Support Vector Regression: 0.671031657615

plt.xlabel("Actual area burned")
plt.ylabel("Error")
plt.grid(True)
plt.scatter(10 ** (y_test), 10 ** (a) - 10 ** (y_test))

show()

plt.title("Histogram of prediction errors")
plt.xlabel("Prediction error ($ha$)")
plt.grid(True)
plt.hist(
    10
    ** (
        a.reshape(
            a.size,
        )
    )
    - 10 ** (y_test),
    bins=50,
)

show()

rec_SVR = []
for i in range(tol_max):
    rec_SVR.append(rec(a, y_test, i))

plt.figure(figsize=(5, 5))
plt.title("REC curve for the Support Vector Regressor")
plt.xlabel("Absolute error (tolerance) in prediction ($ha$)")
plt.ylabel("Percentage of correct prediction")
plt.xticks([i * 5 for i in range(tol_max + 1)])
plt.ylim(-10, 100)
plt.yticks([i * 20 for i in range(6)])
plt.grid(True)
plt.plot(range(tol_max), rec_SVR)

show()

# Decision Tree Regressor

from sklearn.tree import DecisionTreeRegressor

# tree_model = DecisionTreeRegressor(max_depth=10,criterion='mae')
tree_model = DecisionTreeRegressor(max_depth=10)
tree_model.fit(scaler.fit_transform(X_train), scaler.fit_transform(y_train))

a = tree_model.predict(X_test)
print("RMSE for Decision Tree:", np.sqrt(np.mean((y_test - a) ** 2)))

# RMSE for Decision Tree: 0.624177314982

plt.xlabel("Actual area burned")
plt.ylabel("Error")
plt.grid(True)
plt.scatter(10 ** (y_test), 10 ** (a) - 10 ** (y_test))

show()

plt.title("Histogram of prediction errors")
plt.xlabel("Prediction error ($ha$)")
plt.grid(True)
plt.hist(
    10
    ** (
        a.reshape(
            a.size,
        )
    )
    - 10 ** (y_test),
    bins=50,
)

show()


rec_DT = []
for i in range(tol_max):
    rec_DT.append(rec(a, y_test, i))

plt.figure(figsize=(5, 5))
plt.title("REC curve for the single Decision Tree")
plt.xlabel("Absolute error (tolerance) in prediction ($ha$)")
plt.ylabel("Percentage of correct prediction")
plt.xticks([i for i in range(0, tol_max + 1, 5)])
plt.ylim(-10, 100)
plt.yticks([i * 20 for i in range(6)])
plt.grid(True)
plt.plot(range(tol_max), rec_DT)

show()

# Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor

param_grid = {
    "max_depth": [5, 10, 15, 20, 50],
    "max_leaf_nodes": [2, 5, 10],
    "min_samples_leaf": [2, 5, 10],
    "min_samples_split": [2, 5, 10],
}
grid_RF = GridSearchCV(RandomForestRegressor(), param_grid, refit=True, verbose=0, cv=5)
grid_RF.fit(X_train, y_train)

print("Best parameters obtained by Grid Search:", grid_RF.best_params_)

# Best parameters obtained by Grid Search: {'max_depth': 20, 'max_leaf_nodes': 2, 'min_samples_leaf': 10, 'min_samples_split': 5}

a = grid_RF.predict(X_test)
rmse_rf = np.sqrt(np.mean((y_test - a) ** 2))
print("RMSE for Random Forest:", rmse_rf)

# RMSE for Random Forest: 0.614885707514

plt.xlabel("Actual area burned")
plt.ylabel("Error")
plt.grid(True)
plt.scatter(10 ** (y_test), 10 ** (a) - 10 ** (y_test))

show()

plt.title("Histogram of prediction errors")
plt.xlabel("Prediction error ($ha$)")
plt.grid(True)
plt.hist(
    10
    ** (
        a.reshape(
            a.size,
        )
    )
    - 10 ** (y_test),
    bins=50,
)

show()

rec_RF = []
for i in range(tol_max):
    rec_RF.append(rec(a, y_test, i))

plt.figure(figsize=(5, 5))
plt.title("REC curve for the Random Forest")
plt.xlabel("Absolute error (tolerance) in prediction ($ha$)")
plt.ylabel("Percentage of correct prediction")
plt.xticks([i for i in range(0, tol_max + 1, 5)])
plt.ylim(-10, 100)
plt.yticks([i * 20 for i in range(6)])
plt.grid(True)
plt.plot(range(tol_max), rec_RF)

show()

# Deep network (using Keras (TensorFlow backend))

from keras.models import Sequential
import keras.optimizers as opti
from keras.layers import Dense, Activation, Dropout

# Layers

model = Sequential()
model.add(Dense(100, input_dim=12))
model.add(Activation("selu"))
model.add(Dropout(0.3))
model.add(Dense(100))
model.add(Dropout(0.3))
model.add(Activation("selu"))
model.add(Dense(50))
model.add(Activation("elu"))
model.add(Dense(1))

print("檢視模型架構")
model.summary()  # 檢視模型架構

# Learning rate and optimizer

learning_rate = 0.001
optimizer = opti.RMSprop(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss="mse")

# Input data and mode fitting

data = X_train
target = y_train
model.fit(data, target, epochs=100, batch_size=10, verbose=0)

# Prediction and RMSE

a = model.predict(X_test)
print(
    "RMSE for Deep Network:",
    np.sqrt(
        np.mean(
            (
                y_test
                - a.reshape(
                    a.size,
                )
            )
            ** 2
        )
    ),
)

# RMSE for Deep Network: 0.610289206294

plt.xlabel("Actual area burned")
plt.ylabel("Error")
plt.grid(True)
plt.scatter(
    10 ** (y_test),
    10
    ** (
        a.reshape(
            a.size,
        )
    )
    - 10 ** (y_test),
)

show()

plt.title("Histogram of prediction errors")
plt.xlabel("Prediction error ($ha$)")
plt.grid(True)
plt.hist(
    10
    ** (
        a.reshape(
            a.size,
        )
    )
    - 10 ** (y_test),
    bins=50,
)

show()

rec_NN = []
for i in range(tol_max):
    rec_NN.append(rec(a, y_test, i))

plt.figure(figsize=(5, 5))
plt.title("REC curve for the Deep Network")
plt.xlabel("Absolute error (tolerance) in prediction ($ha$)")
plt.ylabel("Percentage of correct prediction")
plt.xticks([i for i in range(0, tol_max + 1, 5)])
plt.ylim(-10, 100)
plt.yticks([i * 20 for i in range(6)])
plt.grid(True)
plt.plot(range(tol_max), rec_NN)

show()

# Relative performance of various models (REC curves)

plt.figure(figsize=(10, 8))
plt.title("REC curve for various models")
plt.xlabel("Absolute error (tolerance) in prediction ($ha$)")
plt.ylabel("Percentage of correct prediction")
plt.xticks([i for i in range(0, tol_max + 1, 1)])
plt.ylim(-10, 100)
plt.xlim(-2, tol_max)
plt.yticks([i * 20 for i in range(6)])
plt.grid(True)
plt.plot(range(tol_max), rec_SVR, "--", lw=3)
plt.plot(range(tol_max), rec_DT, "*-", lw=3)
plt.plot(range(tol_max), rec_RF, "o-", lw=3)
plt.plot(range(tol_max), rec_NN, "k-", lw=3)
plt.legend(["SVR", "Decision Tree", "Random Forest", "Deep NN"])

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


print("------------------------------------------------------------")  # 60個
