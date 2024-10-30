"""
20190314-空氣盒子數據Scikit-Learn邏輯迴歸實作

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

train = pd.read_csv("data/200811-201811c.csv")
cc = train.head()
print(cc)
# Danger分類點說明
# 對敏感族群不健康為PM2.5數值在35.5以上

# 用heatmap(.isnull())來找出缺失的資料在哪些欄位

sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis")

plt.show()

print("------------------------------------------------------------")  # 60個

# 用countplot來看Nox是否影響健康

sns.countplot(x="Danger", hue="Nox", data=train, palette="RdBu_r")

plt.show()

print("------------------------------------------------------------")  # 60個

# 用直方圖看年齡分佈。缺失資料在此不計。

sns.distplot(train["PM25"].dropna(), kde=False, bins=30)

plt.show()

print("------------------------------------------------------------")  # 60個

# 用直方圖看Nox的分佈

train["Nox"].hist(bins=40, figsize=(10, 4))

plt.show()

print("------------------------------------------------------------")  # 60個

X = train.drop("Danger", axis=1)
y = train["Danger"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.75, random_state=42
)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression(solver="liblinear")
logmodel.fit(X_train, y_train)

"""
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='liblinear',
          tol=0.0001, verbose=0, warm_start=False)
"""
predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))


from sklearn.metrics import confusion_matrix

cc = confusion_matrix(y_test, predictions)
print(cc)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
