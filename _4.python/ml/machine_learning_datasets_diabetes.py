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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

# 載入資料集

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


from sklearn import datasets
from matplotlib import pyplot as plt

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
plt.show()


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

# 讀取資料

from sklearn.datasets import load_diabetes  # 匯入Sklearn內建資料集

diabetes_sklearn = load_diabetes()  # 將數據匯入

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

from sklearn.datasets import load_diabetes  # 匯入Sklearn內建資料集

data = load_diabetes()  # 將數據匯入

# 觀察資料

df = pd.DataFrame(data.data, columns=data.feature_names)
# 透過data.data來呼叫數據　回傳numpy.ndarray型態
# 透過data.feature_names來呼叫特徵名稱
# 將原先的data由numpy.ndarray變更為pandas.DataFrame型態
# 將特徵名稱與資料放入對應的行(columns)

cc = df.head()
print(cc)

print("------------------------------------------------------------")  # 60個

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from sklearn.datasets import load_diabetes
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso

diabetes_sklearn = load_diabetes()
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

plt.show()


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

plt.show()


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

plt.show()

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

plt.show()

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

"""
/opt/conda/lib/python3.7/site-packages/sklearn/utils/deprecation.py:143: FutureWarning: The sklearn.metrics.classification module is  deprecated in version 0.22 and will be removed in version 0.24. The corresponding classes / functions should instead be imported from sklearn.metrics. Anything that cannot be imported from sklearn.metrics is now part of the private API.
  warnings.warn(message, FutureWarning)
"""

from sklearn.linear_model import RidgeCV

alphas = np.arange(0.01, 10, 0.01)
# ridgeCV_reg = RidgeCV(alphas=alphas)
# ridgeCV_reg.fit(X_train, y_train)
visualizer = AlphaSelection(RidgeCV(alphas=alphas))

visualizer.fit(X_train, y_train)
g = visualizer.poof()

ridgeCV_pred = visualizer.predict(X_test)
print("R-squared:", round(r2_score(y_test, ridgeCV_pred), 4))

# R-squared: 0.476

print("------------------------------------------------------------")  # 60個

"""
# 不知道在演什麼

#MLflow 測試
#載入相關套件

from sklearn import datasets
import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

# 將數據匯入 讀取資料集多了 Y
#sklearn.datasets.load_diabetes(*, return_X_y=False, as_frame=False, scaled=True)
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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


