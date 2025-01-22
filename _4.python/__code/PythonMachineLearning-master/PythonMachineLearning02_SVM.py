"""
PythonMachineLearning-master 01

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
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

cc = cancer.keys()
print(cc)

print(cancer["DESCR"])

cc = cancer["feature_names"]
print(cc)

# Set up the DataFrame

df = pd.DataFrame(cancer["data"], columns=cancer["feature_names"])
cc = df.info()
print(cc)

cc = df.describe()
print(cc)

# Is there any missing data?

cc = np.sum(
    pd.isnull(df).sum()
)  # Sum of the count of null objects in all columns of data frame
print(cc)

# What are the 'target' data in the data set?

cc = cancer["target"]
print(cc)

# ** Adding the target data to the DataFrame**

df["Cancer"] = pd.DataFrame(cancer["target"])
cc = df.head()
print(cc)

# Exploratory Data Analysis

sns.set_style("whitegrid")
sns.countplot(x="Cancer", data=df, palette="RdBu_r")
plt.show()

# Run a 'for' loop to draw boxlots of all the mean features (first 10 columns) for '0' and '1' CANCER OUTCOME

l = list(df.columns[0:10])
for i in range(len(l) - 1):
    sns.boxplot(x="Cancer", y=l[i], data=df, palette="winter")
    plt.figure()

plt.show()

# Not all the features seperate out the cancer predictions equally clearly

# For example, from the following two plots it is clear that smaller area generally is indicative of positive cancer detection, while nothing concrete can be said from the plot of mean smoothness

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12, 6))
ax1.scatter(df["mean area"], df["Cancer"])
ax1.set_title("Cancer cases as a function of mean area", fontsize=15)
ax2.scatter(df["mean smoothness"], df["Cancer"])
ax2.set_title("Cancer cases as a function of mean smoothness", fontsize=15)

plt.show()

# Training and prediction
# Train Test Split

df_feat = df.drop("Cancer", axis=1)  # Define a dataframe with only features
cc = df_feat.head()
print(cc)

df_target = df[
    "Cancer"
]  # Define a dataframe with only target results i.e. cancer detections
cc = df_target.head()
print(cc)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df_feat, df_target, test_size=0.30, random_state=101
)

cc = y_train.head()
print(cc)

# Train the Support Vector Classifier

from sklearn.svm import SVC

model = SVC()

model.fit(X_train, y_train)
"""
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
"""
# Predictions and Evaluations

predictions = model.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, predictions))

print(classification_report(y_test, predictions))

# Gridsearch

param_grid = {
    "C": [0.1, 1, 10, 100, 1000],
    "gamma": [1, 0.1, 0.01, 0.001, 0.0001],
    "kernel": ["rbf"],
}

from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=1)

# 久
grid.fit(X_train, y_train)

"""
GridSearchCV(cv=None, error_score='raise',
       estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False),
       fit_params={}, iid=True, n_jobs=1,
       param_grid={'C': [0.1, 1, 10, 100, 1000], 'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 'kernel': ['rbf']},
       pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
       scoring=None, verbose=1)
"""
cc = grid.best_params_
print(cc)

cc = grid.best_estimator_
print(cc)

"""
SVC(C=10, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.0001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
"""

# Then you can re-run predictions on this grid object just like you would with a normal model

grid_predictions = grid.predict(X_test)

# Now print the confusion matrix to see improved predictions

print(confusion_matrix(y_test, grid_predictions))

# Classification report shows improved F1-score

print(classification_report(y_test, grid_predictions))

# Another set of parameters for GridSearch

param_grid = {
    "C": [50, 75, 100, 125, 150],
    "gamma": [1e-2, 1e-3, 1e-4, 1e-5, 1e-6],
    "kernel": ["rbf"],
}
grid = GridSearchCV(SVC(tol=1e-5), param_grid, refit=True, verbose=1)
grid.fit(X_train, y_train)
"""
GridSearchCV(cv=None, error_score='raise',
       estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=1e-05, verbose=False),
       fit_params={}, iid=True, n_jobs=1,
       param_grid={'C': [50, 75, 100, 125, 150], 'gamma': [0.01, 0.001, 0.0001, 1e-05, 1e-06], 'kernel': ['rbf']},
       pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
       scoring=None, verbose=1)
"""
cc = grid.best_estimator_
print(cc)
"""
SVC(C=125, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=1e-05, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=1e-05, verbose=False)
"""
grid_predictions = grid.predict(X_test)
print(confusion_matrix(y_test, grid_predictions))


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
