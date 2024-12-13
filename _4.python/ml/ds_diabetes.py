"""
糖尿病資料集

Sklearn Diabetes Dataset : Scikit-learn Toy Datasets in Python

datasets.load_diabetes是一个Python库中的函数，用于加载糖尿病数据集。
该数据集包含442个病人的10个生理特征和一年后的疾病进展情况。

資料筆數 : 442
資料欄位 : 10
資料目標 : 1年後的疾病進展情況

資料欄位:
    age: Age in years
    sex: Gender of the patient
    bmi: Body mass index
    bp: Average blood pressure
    s1: Total serum cholesterol (tc)
    s2: Low-density lipoproteins (ldl)
    s3: High-density lipoproteins (hdl)
    s4: Total cholesterol / HDL (tch)
    s5: Possibly log of serum triglycerides level (ltg)
    s6: Blood sugar level (glu)

讀取資料
sklearn.datasets.load_diabetes(*, return_X_y=False, as_frame=False, scaled=True)
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
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsClassifier  # K近鄰演算法（K Nearest Neighbor, KNN）
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.datasets import make_hastie_10_2


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("糖尿病資料集 基本數據")

data = datasets.load_diabetes()

# 觀察資料

df = pd.DataFrame(data.data, columns=data.feature_names)
# 透過data.data來呼叫數據　回傳numpy.ndarray型態
# 透過data.feature_names來呼叫特徵名稱
# 將原先的data由numpy.ndarray變更為pandas.DataFrame型態
# 將特徵名稱與資料放入對應的行(columns)

cc = df.head()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
datasets.load_diabetes()
參數 return_X_y :

False(預設) :
True : 返回 (data, target)

參數 as_frame :
False(預設) :
True : 返回資料為df
"""

# 預設 as_frame = False
diabetes_sklearn = datasets.load_diabetes()  # 將數據匯入
print(type(diabetes_sklearn.data))

diabetes_sklearn = datasets.load_diabetes(as_frame=False)  # 將數據匯入
print(type(diabetes_sklearn.data))

# 讀取資料為df格式
diabetes_sklearn = datasets.load_diabetes(as_frame=True)  # 將數據匯入
print(type(diabetes_sklearn.data))

"""
print(diabetes_sklearn.data)
print(diabetes_sklearn.data.shape)
print(diabetes_sklearn.target)
print('数据集列的名称')
print(diabetes_sklearn.feature_names)
print(diabetes_sklearn.frame)
print('数据集的完整描述')
#print(diabetes_sklearn.DESCR)
print('数据位置的路径。')
print(diabetes_sklearn.data_filename)
print('target位置的路径')
print(diabetes_sklearn.target_filename)
"""

print("数据集的完整描述")
# print(diabetes_sklearn.DESCR)

print("feature_names")
print(diabetes_sklearn.feature_names)

print("data")
print(diabetes_sklearn.data)

print("target")
print(diabetes_sklearn.target)

# Load the dataset
diabetes = datasets.load_diabetes(as_frame=True)

# Don't plot the sex data
features = diabetes["feature_names"]
features.remove("sex")

# Plot
fig, axs = plt.subplots(3, 3)
fig.suptitle("Diabetes Dataset")
for i in range(3):
    for j in range(3):
        n = j + i * 3
        feature = features[n]
        axs[i, j].scatter(diabetes["data"][feature], diabetes["target"], s=1)
        axs[i, j].set_xlabel(feature)
        axs[i, j].set_ylabel("target")
plt.tight_layout()
show()

"""
#Bunch 类字典

- data{ndarray, dataframe} of shape (442, 10)
数据矩阵。 如果as_frame = True，则data为pandas DataFrame。
- target: {ndarray, Series} of shape (442,)
回归target。如果as_frame = True，target将是pandas系列。

- frame: DataFrame of shape (442, 11)
仅在as_frame = True时存在。具有data和target的DataFrame。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

diabetes_sklearn = datasets.load_diabetes()

# Convert the dataset to a DataFrame
diabetes_df = pd.DataFrame(
    data=diabetes_sklearn.data, columns=diabetes_sklearn.feature_names
)

# Add target variable to the DataFrame
diabetes_df["target"] = diabetes_sklearn.target

print(diabetes_df.head())

# Print the shape of the feature matrix and target vector
print("Shape of Sklearn Diabetes Data:", diabetes_df.shape)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib.ticker as ticker
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV

diabetes_sklearn = datasets.load_diabetes()

df = pd.DataFrame(diabetes_sklearn.data, columns=diabetes_sklearn.feature_names)
df["TEMP"] = diabetes_sklearn.target
cc = df.head(10)
print(cc)

# standardize and train/test split
diabetes_sklearn.data = preprocessing.scale(diabetes_sklearn.data)
X_train, X_test, y_train, y_test = train_test_split(
    diabetes_sklearn.data, diabetes_sklearn.target, test_size=0.3, random_state=10
)

ols_reg = LinearRegression()
ols_reg.fit(X_train, y_train)
ols_pred = ols_reg.predict(X_test)

cc = pd.DataFrame(
    {"variable": diabetes_sklearn.feature_names, "estimate": ols_reg.coef_}
)

print(cc)

cc = diabetes_sklearn.feature_names
print(cc)

# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

# initialize
ridge_reg = Ridge(alpha=0)
ridge_reg.fit(X_train, y_train)
ridge_df = pd.DataFrame(
    {"variable": diabetes_sklearn.feature_names, "estimate": ridge_reg.coef_}
)
ridge_train_pred = []
ridge_test_pred = []

alphas = np.arange(0, 200, 1)

for alpha in alphas:
    ridge_reg = Ridge(alpha=alpha)
    ridge_reg.fit(X_train, y_train)
    var_name = "estimate" + str(alpha)
    ridge_df[var_name] = ridge_reg.coef_
    # prediction
    ridge_train_pred.append(ridge_reg.predict(X_train))
    ridge_test_pred.append(ridge_reg.predict(X_test))

ridge_df = (
    ridge_df.set_index("variable").T.rename_axis("estimate").reset_index()
)  # .rename_axis(None, 1).reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    ridge_df.bmi,
    "r",
    ridge_df.s1,
    "g",
    ridge_df.age,
    "b",
    ridge_df.sex,
    "c",
    ridge_df.bp,
    "y",
)
ax.axhline(y=0, color="black", linestyle="--")
ax.set_xlabel("Lambda")
ax.set_ylabel("Beta Estimate")
ax.set_title("Ridge Regression Trace", fontsize=16)
ax.legend(labels=["bmi", "s1", "age", "sex", "bp"])
ax.grid(True)

show()

# initialize
lasso_reg = Lasso(alpha=1)
lasso_reg.fit(X_train, y_train)
lasso_df = pd.DataFrame(
    {"variable": diabetes_sklearn.feature_names, "estimate": lasso_reg.coef_}
)
lasso_train_pred = []
lasso_test_pred = []

alphas = np.arange(0.01, 8.01, 0.04)

for alpha in alphas:
    lasso_reg = Lasso(alpha=alpha)
    lasso_reg.fit(X_train, y_train)
    var_name = "estimate" + str(alpha)
    lasso_df[var_name] = lasso_reg.coef_
    # prediction
    lasso_train_pred.append(lasso_reg.predict(X_train))
    lasso_test_pred.append(lasso_reg.predict(X_test))

lasso_df = lasso_df.set_index("variable").T.rename_axis("estimate").reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    ridge_df.bmi,
    "r",
    ridge_df.s1,
    "g",
    ridge_df.age,
    "b",
    ridge_df.sex,
    "c",
    ridge_df.bp,
    "y",
)
ax.set_xlabel("Lambda")
ax.set_xticklabels(np.arange(-1, 10, 1))
ax.set_ylabel("Beta Estimate")
ax.set_title("Lasso Regression Trace", fontsize=16)
ax.legend(labels=["bmi", "s1", "age", "sex", "bp"])
ax.grid(True)

show()

# R-squared of training set
ridge_r_squared_train = [r2_score(y_train, p) for p in ridge_train_pred]
lasso_r_squared_train = [r2_score(y_train, p) for p in lasso_train_pred]

# R-squared of test set
ridge_r_squared_test = [r2_score(y_test, p) for p in ridge_test_pred]
lasso_r_squared_test = [r2_score(y_test, p) for p in lasso_test_pred]

# ols for benchmark
ols_r_squared = r2_score(y_test, ols_pred)

# plot R-squared of training and test
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
plt.rcParams["axes.grid"] = True

# training set and test set together
axes[0, 0].plot(ridge_r_squared_train, "b", ridge_r_squared_test, "r")
axes[0, 0].set_title("Ridge Regression R-squared", fontsize=16)
axes[0, 0].set_ylabel("R-squared")

axes[0, 1].plot(lasso_r_squared_train, "b", lasso_r_squared_test, "r")
axes[0, 1].set_title("Lasso Regression R-squared", fontsize=16)

# test set curve
axes[1, 0].plot(ridge_r_squared_test[:25], "ro")
axes[1, 0].axhline(y=ols_r_squared, color="g", linestyle="--")
axes[1, 0].set_title("Ridge Test Set Zoom-in", fontsize=16)
axes[1, 0].set_xlabel("Model Simplicity$\longrightarrow$")
axes[1, 0].set_ylabel("R-squared")

axes[1, 1].plot(lasso_r_squared_test[:25], "ro")
axes[1, 1].axhline(y=ols_r_squared, color="g", linestyle="--")
axes[1, 1].set_title("Lasso Test Set Zoom-in", fontsize=16)
axes[1, 1].set_xlabel("Model Simplicity$\longrightarrow$")

show()

# Text(0.5, 0, 'Model Simplicity$\\longrightarrow$')

# MSE of training set
ridge_mse_train = [mean_squared_error(y_train, p) for p in ridge_train_pred]
lasso_mse_train = [mean_squared_error(y_train, p) for p in lasso_train_pred]

# MSE of test set
ridge_mse_test = [mean_squared_error(y_test, p) for p in ridge_test_pred]
lasso_mse_test = [mean_squared_error(y_test, p) for p in lasso_test_pred]

# ols mse for benchmark
ols_mse = mean_squared_error(y_test, ols_pred)

# plot MSE of training and test
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
plt.rcParams["axes.grid"] = True

# training set and test set together
axes[0, 0].plot(ridge_mse_train, "b", ridge_mse_test, "r")
axes[0, 0].set_title("Ridge Regression MSE", fontsize=16)
axes[0, 0].set_ylabel("MSE")

axes[0, 1].plot(lasso_mse_train, "b", lasso_mse_test, "r")
axes[0, 1].set_title("Lasso Regression MSE", fontsize=16)

# test set curve
axes[1, 0].plot(ridge_mse_test[:25], "ro")
axes[1, 0].axhline(y=ols_mse, color="g", linestyle="--")
axes[1, 0].set_title("Ridge Test Set MSE", fontsize=16)
axes[1, 0].set_xlabel("Model Simplicity$\longrightarrow$")
axes[1, 0].set_ylabel("MSE")

axes[1, 1].plot(lasso_mse_test[:25], "ro")
axes[1, 1].axhline(y=ols_mse, color="g", linestyle="--")
axes[1, 1].set_title("Lasso Test Set MSE", fontsize=16)
axes[1, 1].set_xlabel("Model Simplicity$\longrightarrow$")

show()

# Text(0.5, 0, 'Model Simplicity$\\longrightarrow$')

from sklearn.model_selection import GridSearchCV

# ols for comparison
print("OLS R-squared:", round(ols_r_squared, 4))
print("OLS MSE:", round(ols_mse, 4))
# OLS R-squared: 0.4747
# OLS MSE: 3324.2175

# parameter setup
param = {"alpha": np.arange(0.01, 10, 0.01)}

ridge_reg_grid = GridSearchCV(Ridge(), param)
ridge_reg_grid.fit(X_train, y_train)
ridge_grid_pred = ridge_reg_grid.predict(X_test)

print(ridge_reg_grid.best_estimator_)
print("\nR-Squared:", round(r2_score(y_test, ridge_grid_pred), 4))
print("MSE:", round(mean_squared_error(y_test, ridge_grid_pred), 4))

"""
Ridge(alpha=9.99)

R-Squared: 0.479
MSE: 3296.5222
"""

lasso_reg_grid = GridSearchCV(Lasso(), param)
lasso_reg_grid.fit(X_train, y_train)
lasso_grid_pred = lasso_reg_grid.predict(X_test)

print(lasso_reg_grid.best_estimator_)
print("\nR-Squared:", round(r2_score(y_test, lasso_grid_pred), 4))
print("MSE:", round(mean_squared_error(y_test, lasso_grid_pred), 4))

"""
Lasso(alpha=0.36000000000000004)

R-Squared: 0.4806
MSE: 3286.5164
"""

#!pip install yellowbrick
# from sklearn.linear_model import RidgeCV
from yellowbrick.regressor import AlphaSelection  # visualization

from sklearn.linear_model import RidgeCV

alphas = np.arange(0.01, 10, 0.01)
# ridgeCV_reg = RidgeCV(alphas=alphas)
# ridgeCV_reg.fit(X_train, y_train)
visualizer = AlphaSelection(RidgeCV(alphas=alphas))

visualizer.fit(X_train, y_train)

""" 有畫圖
g = visualizer.poof()

ridgeCV_pred = visualizer.predict(X_test)
print("R-squared:", round(r2_score(y_test, ridgeCV_pred), 4))
# R-squared: 0.476
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# 不知道在演什麼

#MLflow 測試
#載入相關套件

import mlflow
import mlflow.sklearn

# 將數據匯入 讀取資料集多了 Y
# datasets.load_diabetes(*, return_X_y=False, as_frame=False, scaled=True)
X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
# 訓練資料, 測試資料, 訓練目標, 測試目標
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 8成訓練 2成測試

#模型訓練與評估

# 定義模型參數
alpha = 1
l1_ratio = 1

print('3')
with mlflow.start_run():
    # 模型訓練
    model = ElasticNet(alpha = alpha,
                       l1_ratio = l1_ratio)
    model.fit(X_train,y_train)
    
    # 模型評估
    pred = model.predict(X_test)
    rmse = mean_squared_error(pred, y_test)
    abs_error = mean_absolute_error(pred, y_test)
    r2 = r2_score(pred, y_test)
    print('4')
    
    # MLflow 記錄
    mlflow.log_param('alpha', alpha)
    mlflow.log_param('l1_ratio', l1_ratio)
    mlflow.log_metric('rmse', rmse)
    mlflow.log_metric('abs_error', abs_error)
    mlflow.log_metric('r2', r2)
    
    # MLflow 記錄模型
    mlflow.sklearn.log_model(model, "model")

print('5')

#模型評估

mlflow.sklearn.log_model(model, "model")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = pd.read_csv("datasets/pima-indians-diabetes/diabetes.csv")
print("dataset shape {}".format(data.shape))

print(data.head())

print(data.groupby("Outcome").size())

X = data.iloc[:, 0:8]
Y = data.iloc[:, 8]
print("shape of X {}; shape of Y {}".format(X.shape, Y.shape))

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
# 訓練組8成, 測試組2成

from sklearn.neighbors import RadiusNeighborsClassifier

NEIGHBOARS = 2
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
models = []
models.append(("KNN", KNeighborsClassifier(n_neighbors=NEIGHBOARS)))
models.append(
    (
        "KNN with weights",
        KNeighborsClassifier(n_neighbors=NEIGHBOARS, weights="distance"),
    )
)
models.append(
    (
        "Radius Neighbors",
        RadiusNeighborsClassifier(
            #    n_neighbors=2, radius=500.0)))
            radius=500.0
        ),
    )
)

results = []
for name, model in models:
    model.fit(X_train, Y_train)
    results.append((name, model.score(X_test, Y_test)))
for i in range(len(results)):
    print("name: {}; score: {}".format(results[i][0], results[i][1]))

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

results = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model, X, Y, cv=kfold)
    results.append((name, cv_result))
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(results[i][0], results[i][1].mean()))

print("------------------------------")  # 30個

NEIGHBOARS = 2
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, Y_train)

train_score = knn.score(X_train, Y_train)
test_score = knn.score(X_test, Y_test)
print("train score: {}".format(train_score))
print("test score: {}".format(test_score))

from sklearn.model_selection import ShuffleSplit
from common.utils import plot_learning_curve

NEIGHBOARS = 2
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=9487)

plt.figure(figsize=(10, 6))
plot_learning_curve(
    plt, knn, "Learn Curve for KNN Diabetes", X, Y, ylim=(0.0, 1.01), cv=cv
)
show()

print("------------------------------")  # 30個

# 數據可視化

from sklearn.feature_selection import SelectKBest

selector = SelectKBest(k=2)
X_new = selector.fit_transform(X, Y)
print(X_new[0:5])

results = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model, X_new, Y, cv=kfold)
    results.append((name, cv_result))
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(results[i][0], results[i][1].mean()))

plt.figure(figsize=(10, 6))
plt.ylabel("BMI")
plt.xlabel("Glucose")
plt.scatter(X_new[Y == 0][:, 0], X_new[Y == 0][:, 1], c="r", s=20, marker="o")  # 畫出樣本
plt.scatter(X_new[Y == 1][:, 0], X_new[Y == 1][:, 1], c="g", s=20, marker="^")  # 畫出樣本

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 1. Rescale Data
# 將資料比例縮放到0與1之間# Rescale data (between 0 and 1)

import scipy
from sklearn.preprocessing import MinMaxScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(rescaledX[0:5, :])

print("------------------------------------------------------------")  # 60個

# 2. Standardize Data
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = StandardScaler().fit(X)  # 學習訓練.fit
rescaledX = scaler.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(rescaledX[0:5, :])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 3. Normalize Data
# 最大值變為1，最小值變為0

from sklearn.preprocessing import Normalizer

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = Normalizer().fit(X)  # 學習訓練.fit
normalizedX = scaler.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(normalizedX[0:5, :])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 4. Binarize Data (Make Binary)
# 資料二元化(0或者1)

from sklearn.preprocessing import Binarizer

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
binarizer = Binarizer(threshold=0.0).fit(X)  # 學習訓練.fit
binaryX = binarizer.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(binaryX[0:5, :])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# k_fold_cross_validation  K折交叉驗證法

from sklearn.preprocessing import StandardScaler

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型評分
print(f"R2={linear_regression.score(X_test_std, y_test)}")
# R2=0.41738354865811345

# K折測試
from sklearn.model_selection import KFold

kf = KFold(n_splits=5)
for i, (train_index, test_index) in enumerate(kf.split(X_train_std)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")

# K折驗證
score = []
for i, (train_index, test_index) in enumerate(kf.split(X_train_std)):
    X_new = X_train_std[train_index]
    y_new = y_train[train_index]
    linear_regression.fit(X_new, y_new)  # 學習訓練.fit
    score_fold = linear_regression.score(X_train_std[test_index], y_train[test_index])
    score.append(score_fold)
    print(f"Fold {i} 分數: {np.mean(score)}")
print(f"平均值: {np.mean(score)}")
print(f"標準差: {np.std(score)}")

# 效能調校

from sklearn.model_selection import GridSearchCV

lasso = Lasso(random_state=9487, max_iter=10000)

# 正則化強度：3種選擇
alphas = np.logspace(-4, -0.5, 30)
# 強迫係數(權重)須為正數
positive = (True, False)
tuned_parameters = [{"alpha": alphas, "positive": positive}]

# 效能調校
clf = GridSearchCV(lasso, tuned_parameters, cv=5, refit=False)

clf.fit(X, y)  # 學習訓練.fit

# cv_results_ : 具體用法模型不同參數下交叉驗證的結果
scores_mean = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]
print("平均分數:\n", scores_mean, "\n標準差:\n", scores_std)

# 取得最高分數
cc = np.max(clf.cv_results_["mean_test_score"])
print(cc)

# 參數組合
cc = clf.param_grid
print(cc)

# 取得最佳參數組合
cc = clf.best_params_
print(cc)

# 驗證
from math import floor

index = np.argmax(clf.cv_results_["mean_test_score"])
cc = index, clf.cv_results_["mean_test_score"][index], alphas[floor((index - 1) / 2)]
print(cc)

cc = clf.best_score_
print(cc)

# 以最佳參數組合重新訓練

clf = Lasso(
    random_state=9487, max_iter=10000, alpha=0.07880462815669913, positive=False
)

clf.fit(X_train_std, y_train)  # 學習訓練.fit

cc = clf.score(X_test_std, y_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# pipeline_cross_validation 管線測試

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 建立管線：特徵縮放、特徵萃取、模型訓練

pipe_lr = make_pipeline(
    StandardScaler(), PCA(n_components=5), Lasso(random_state=9487, max_iter=10000)
)

pipe_lr.fit(X_train, y_train)  # 學習訓練.fit

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('pca', PCA(n_components=5)),
                ('lasso', Lasso(max_iter=10000, random_state=9487))])
"""

# 模型評估

# y_pred = pipe_lr.predict(X_test)
print(f"R2={pipe_lr.score(X_test, y_test)}")

# 管線結合K折交叉驗證

from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=pipe_lr, X=X_test, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.3f}, 標準差: {np.std(scores):.3f}")

# 管線結合K折交叉驗證、效能調校

from sklearn.model_selection import GridSearchCV

# 正則化強度：3種選擇
alphas = np.logspace(-4, -0.5, 30)
# 強迫係數(權重)須為正數
positive = (True, False)
tuned_parameters = [{"lasso__alpha": alphas, "lasso__positive": positive}]

# 效能調校
clf = GridSearchCV(pipe_lr, tuned_parameters, cv=5, refit=False)

clf.fit(X, y)  # 學習訓練.fit

# cv_results_ : 具體用法模型不同參數下交叉驗證的結果
scores_mean = clf.cv_results_["mean_test_score"]
scores_std = clf.cv_results_["std_test_score"]
print("平均分數:\n", scores_mean, "\n標準差:\n", scores_std)

# 取得最佳參數組合
cc = clf.best_params_
print(cc)

# 驗證
from math import floor

index = np.argmax(clf.cv_results_["mean_test_score"])
cc = index, clf.cv_results_["mean_test_score"][index], clf.best_score_
print(cc)

# 以最佳參數組合重新訓練

pipe_lr = make_pipeline(
    StandardScaler(),
    PCA(n_components=5),
    Lasso(
        random_state=9487,
        max_iter=10000,
        alpha=clf.best_params_["lasso__alpha"],
        positive=clf.best_params_["lasso__positive"],
    ),
)

pipe_lr.fit(X_train, y_train)  # 學習訓練.fit

cc = pipe_lr.score(X_test, y_test)
print(cc)

from sklearn.pipeline import Pipeline

pipe_lr = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=5)),
        (
            "lasso",
            Lasso(
                random_state=9487,
                max_iter=10000,
                alpha=clf.best_params_["lasso__alpha"],
                positive=clf.best_params_["lasso__positive"],
            ),
        ),
    ]
)

pipe_lr.fit(X_train, y_train)  # 學習訓練.fit

cc = pipe_lr.score(X_test, y_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# gradient_boost
# 自行開發『梯度提升決策樹』(Gradient Boosting Decision Tree)

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 建立Gradient Boost模型
from sklearn.tree import DecisionTreeRegressor


class GradientBooster:
    # 初始化
    def __init__(
        self,
        max_depth=8,
        min_samples_split=5,
        min_samples_leaf=5,
        max_features=3,
        lr=0.1,
        num_iter=1000,
    ):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.lr = lr
        self.num_iter = num_iter
        self.y_mean = 0

    # 計算 MSE
    def __calculate_loss(self, y, y_pred):
        loss = (1 / len(y)) * 0.5 * np.sum(np.square(y - y_pred))
        return loss

    # 計算梯度
    def __take_gradient(self, y, y_pred):
        grad = -(y - y_pred)
        return grad

    # 單一模型訓練
    def __create_base_model(self, X, y):
        base = DecisionTreeRegressor(
            criterion="squared_error",
            max_depth=self.max_depth,
            min_samples_split=self.min_samples_split,
            min_samples_leaf=self.min_samples_leaf,
            max_features=self.max_features,
        )
        base.fit(X, y)  # 學習訓練.fit
        return base

    # 預測
    def predict(self, models, X):
        pred_0 = np.array([self.y_mean] * X.shape[0])
        pred = pred_0  # .reshape(len(pred_0),1)

        # 加法模型預測
        for i in range(len(models)):
            temp = models[i].predict(X)
            pred -= self.lr * temp

        return pred

    # 模型訓練
    def train(self, X, y):
        models = []
        losses = []
        self.y_mean = np.mean(y)
        pred = np.array([np.mean(y)] * len(y))

        # 加法模型訓練
        for epoch in range(self.num_iter):
            loss = self.__calculate_loss(y, pred)
            losses.append(loss)
            grads = self.__take_gradient(y, pred)
            base = self.__create_base_model(X, grads)
            r = base.predict(X)
            pred -= self.lr * r
            models.append(base)

        return models, losses, pred


# 模型訓練
G = GradientBooster()
models, losses, pred = G.train(X_train, y_train)

# 繪製損失函數
sns.set_style("darkgrid")
ax = sns.lineplot(x=range(1000), y=losses)
ax.set(xlabel="Epoch", ylabel="Loss", title="Loss vs Epoch")
show()

# 模型評估
y_pred = G.predict(models, X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
# RMSE: 62.47630199377564

# 個別模型評估
model = DecisionTreeRegressor(
    max_depth=8, min_samples_split=5, min_samples_leaf=5, max_features=3
)

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
# RMSE: 75.54768636162939

# Scikit-learn GradientBoostingRegressor 模型評估

from sklearn.ensemble import GradientBoostingRegressor

model = GradientBoostingRegressor(
    n_estimators=1000,
    criterion="squared_error",
    max_depth=8,
    min_samples_split=5,
    min_samples_leaf=5,
    max_features=3,
)

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# RMSE: 60.69114783838949

# Scikit-learn GradientBoostingClassifier 模型評估

from sklearn.ensemble import GradientBoostingClassifier

X, y = make_hastie_10_2(random_state=9487)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = GradientBoostingClassifier(
    n_estimators=100, learning_rate=1.0, max_depth=1, random_state=9487
).fit(
    X_train, y_train
)  # 學習訓練.fit

cc = clf.score(X_test, y_test)
print(cc)

# 0.9229166666666667

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# XGBoost測試
#!pip install xgboost -U

"""
Requirement already satisfied: xgboost in c:\anaconda3\lib\site-packages (1.6.1)
Collecting xgboost
  Downloading xgboost-1.7.3-py3-none-win_amd64.whl (89.1 MB)
     ---------------------------------------- 89.1/89.1 MB 8.7 MB/s eta 0:00:00
Requirement already satisfied: numpy in c:\anaconda3\lib\site-packages (from xgboost) (1.23.5)
Requirement already satisfied: scipy in c:\anaconda3\lib\site-packages (from xgboost) (1.9.3)
Installing collected packages: xgboost
  Attempting uninstall: xgboost
    Found existing installation: xgboost 1.6.1
    Uninstalling xgboost-1.6.1:
      Successfully uninstalled xgboost-1.6.1
Successfully installed xgboost-1.7.3
"""

X, y = datasets.load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練
from xgboost import XGBRegressor

model = XGBRegressor()

model.fit(X_train, y_train)  # 學習訓練.fit

"""
XGBRegressor(base_score=None, booster=None, callbacks=None,
             colsample_bylevel=None, colsample_bynode=None,
             colsample_bytree=None, early_stopping_rounds=None,
             enable_categorical=False, eval_metric=None, feature_types=None,
             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,
             interaction_constraints=None, learning_rate=None, max_bin=None,
             max_cat_threshold=None, max_cat_to_onehot=None,
             max_delta_step=None, max_depth=None, max_leaves=None,
             min_child_weight=None, missing=nan, monotone_constraints=None,
             n_estimators=100, n_jobs=None, num_parallel_tree=None,
             predictor=None, random_state=None, ...)
"""

# 模型評估

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test, y_test, cv=10, scoring="neg_mean_squared_error")
print(scores)

# 平均分數與標準差

print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -5473.1857409034155, 標準差: 3004.388074594913

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用迴歸模型

from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

estimators = [("lr", RidgeCV()), ("svr", LinearSVR(random_state=9487))]

model = StackingRegressor(
    estimators=estimators,
    final_estimator=RandomForestRegressor(n_estimators=10, random_state=9487),
)

model.fit(X_train_std, y_train)  # 學習訓練.fit

scores = cross_val_score(model, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")
# 平均分數: 0.12143159519945441, 標準差: 0.4732757387323812

svc = LinearSVR()

svc.fit(X_train_std, y_train)  # 學習訓練.fit

scores = cross_val_score(svc, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")
# 平均分數: -1.0399780386178537, 標準差: 0.36412901584183494

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MLflow 測試

import mlflow
import mlflow.sklearn

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練與評估

# 定義模型參數
alpha = 1
l1_ratio = 1

with mlflow.start_run():
    # 模型訓練
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)

    model.fit(X_train, y_train)  # 學習訓練.fit

    # 模型評估
    pred = model.predict(X_test)
    rmse = mean_squared_error(pred, y_test)
    abs_error = mean_absolute_error(pred, y_test)
    r2 = r2_score(pred, y_test)

    # MLflow 記錄
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("abs_error", abs_error)
    mlflow.log_metric("r2", r2)

    # MLflow 記錄模型
    mlflow.sklearn.log_model(model, "model")

# 模型評估
""" NG
cc = mlflow.sklearn.log_model(lr, "model")
print(cc)

#平均分數: 0.9303030303030303, 標準差: 0.08393720596645175
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用迴歸模型

from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

estimators = [("lr", RidgeCV()), ("svr", LinearSVR(random_state=9487))]

model = StackingRegressor(
    estimators=estimators,
    final_estimator=RandomForestRegressor(n_estimators=10, random_state=9487),
)
model.fit(X_train_std, y_train)  # 學習訓練.fit

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.12143159519945441, 標準差: 0.4732757387323812

svc = LinearSVR()

svc.fit(X_train_std, y_train)  # 學習訓練.fit
from sklearn.model_selection import cross_val_score

scores = cross_val_score(svc, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -1.0399780386178537, 標準差: 0.36412901584183494

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
