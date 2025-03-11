"""
Skewed_LogReg

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

# Use scikit-learn's built-in make_classification method to generate syntehtic classificiation data

from sklearn.datasets import make_classification

# I used two informative features (Temp, Humidity) and one redundant feature 'Crime'

X, y = make_classification(
    n_samples=35040,
    n_classes=2,
    n_features=3,
    n_informative=2,
    n_redundant=1,
    weights=[0.999, 0.001],
    class_sep=1.0,
)

df = pd.DataFrame(data=X, columns=["Temp", "Humidity", "Crime"])

df["y"] = y

df["Temp"] = df["Temp"] - min(df["Temp"])
maxt = max(df["Temp"])
df["Temp"] = 90 * df["Temp"] / maxt

df["Humidity"] = df["Humidity"] - min(df["Humidity"])
maxh = max(df["Humidity"])
df["Humidity"] = 100 * df["Humidity"] / maxh

df["Crime"] = df["Crime"] - min(df["Crime"])
maxc = max(df["Crime"])
df["Crime"] = 10 * df["Crime"] / maxc

df.hist("Temp")
plt.show()
# array([[<matplotlib.axes._subplots.AxesSubplot object at 0x000002A1F3DE1358>]], dtype=object)

df.hist("Humidity")
plt.show()
# array([[<matplotlib.axes._subplots.AxesSubplot object at 0x000002A1F5ECCE10>]], dtype=object)

df.hist("Crime")
plt.show()
# array([[<matplotlib.axes._subplots.AxesSubplot object at 0x000002A1F63B6320>]], dtype=object)

# Take a sum on the Boolean array with df['y']==1 to count the number of positive examples

sum(df["y"] == 1)

# 208

# ** That means only 223 responses out of 35040 samples are positive **

cc = df.head(10)
print(cc)

cc = df.describe()
print(cc)

# Logistic Regression undersampling

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import classification_report

# Under-sampling the negative class to limited number

df0 = df[df["y"] == 0].sample(800)
df1 = df[df["y"] == 1]
df_balanced = pd.concat([df0, df1], axis=0)
df_balanced.describe()

df_balanced.hist("y")
plt.title(
    "Relative frequency of positive and negative classes\n in the balanced (under-sampled) dataset"
)

plt.show()

log_model_balanced = LogisticRegressionCV(cv=5, class_weight="balanced")

X_train, X_test, y_train, y_test = train_test_split(
    df_balanced.drop("y", axis=1), df_balanced["y"], test_size=0.30
)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)

log_model_balanced.fit(X_train, y_train)
"""
LogisticRegressionCV(Cs=10, class_weight='balanced', cv=5, dual=False,
           fit_intercept=True, intercept_scaling=1.0, max_iter=100,
           multi_class='ovr', n_jobs=1, penalty='l2', random_state=None,
           refit=True, scoring=None, solver='lbfgs', tol=0.0001, verbose=0)
"""
print(classification_report(y_test, log_model_balanced.predict(X_test)))

# I did an experiment with how the degree of under-sampling affects F1-score, precision, and recall

from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

n_neg = [i for i in range(200, 4200, 200)]

df1 = df[df["y"] == 1]
F1_scores = []
precision_scores = []
recall_scores = []

for num in n_neg:
    # Create under-sampled data sets
    df0 = df[df["y"] == 0].sample(num)
    df_balanced = pd.concat([df0, df1], axis=0)
    # Create model with 'class_weight=balanced' and 5-fold cross-validation
    log_models = LogisticRegressionCV(cv=5, class_weight="balanced")
    # Create test/train splits
    X_train, X_test, y_train, y_test = train_test_split(
        df_balanced.drop("y", axis=1), df_balanced["y"], test_size=0.30
    )
    # Min-max scale the training data
    X_train = scaler.fit_transform(X_train)

    # Fit the logistic regression model
    log_models.fit(X_train, y_train)

    # Calculate various scores
    F1_scores.append(f1_score(y_test, log_models.predict(X_test)))
    precision_scores.append(precision_score(y_test, log_models.predict(X_test)))
    recall_scores.append(recall_score(y_test, log_models.predict(X_test)))

plt.scatter(n_neg, F1_scores, color="green", edgecolor="black", alpha=0.6, s=100)
plt.title("F1-score as function of negative samples")
plt.grid(True)
plt.ylabel("F1-score")
plt.xlabel("Number of negative samples")

plt.show()

plt.scatter(
    n_neg, precision_scores, color="orange", edgecolor="black", alpha=0.6, s=100
)
plt.title("Precision score as function of negative samples")
plt.grid(True)
plt.ylabel("Precision score")
plt.xlabel("Number of negative samples")

plt.show()

plt.scatter(n_neg, recall_scores, color="blue", edgecolor="black", alpha=0.6, s=100)
plt.title("Recall score as function of negative samples")
plt.grid(True)
plt.ylabel("Recall score")
plt.xlabel("Number of negative samples")

plt.show()

"""
So, precision goes down rapidly with more negative samples and so does F1-score. Recall is largely unaffected by mixing negative samples with the positive ones.
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
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
