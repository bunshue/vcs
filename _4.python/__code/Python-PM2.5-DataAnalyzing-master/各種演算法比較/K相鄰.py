"""
K相鄰

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

df = pd.read_excel("20160101-20190101(Daily)K相鄰.xlsx")
cc = df.head()
print(cc)
# Danger分類點說明
# 對敏感族群不健康為PM2.5數值在35.5以上

cc = df.isnull().any()
print(cc)

from sklearn.preprocessing import StandardScaler

# 將Danger中特徵中移除，作為要預測的對象
scaler = StandardScaler()
scaler.fit(df.drop("Danger", axis=1))
scaled_features = scaler.transform(df.drop("Danger", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
cc = df_feat.head()
print(cc)

from sklearn.model_selection import train_test_split

X = df_feat
y = df["Danger"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=101
)

from sklearn.neighbors import KNeighborsClassifier

# 從k值=1開始測試
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

error_rate = []

for i in range(1, 60):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))


# 將k=1~60的錯誤率製圖畫出。k=7之後，錯誤率就往上跑，
plt.figure(figsize=(10, 6))
plt.plot(
    range(1, 60),
    error_rate,
    color="blue",
    linestyle="dashed",
    marker="o",
    markerfacecolor="red",
    markersize=10,
)
plt.title("Error Rate vs. K Value")
plt.xlabel("K")
plt.ylabel("Error Rate")

plt.show()


knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)
pred = knn.predict(X_test)

print("WITH K=1")
print("\n")
print(confusion_matrix(y_test, pred))
print("\n")
print(classification_report(y_test, pred))


knn = KNeighborsClassifier(n_neighbors=10)

knn.fit(X_train, y_train)
pred = knn.predict(X_test)

print("WITH K=10")
print("\n")
print(confusion_matrix(y_test, pred))
print("\n")
print(classification_report(y_test, pred))


cc = df.head(1)
print(cc)


# 0:Safe   對一般人無害
# 1:Danger 對敏感族群有害
classes = {0: "Safe", 1: "Danger"}

# 建立一筆新資料並進行預測
x_new = [[4, 0.3, 25, 10, 15, 22, 2.2, 20, 2.3, 0.3, 2.3, 2, 20, 60]]
y_predict = knn.predict(x_new)
print(classes[y_predict[0]])

# Danger

classes = {0: "Safe", 1: "Danger"}

x_new = [[1, 0.3, 1, 1, 1, 2, 1, 1, 1, 0.1, 1, 0.5, 30, 50]]
y_predict = knn.predict(x_new)
print(classes[y_predict[0]])

# Safe

cc = knn.score(X_test, y_test)
print(cc)

"""
0.9675010979358806

與前次相比，KNN的準確率 從0.9287356321839081變成0.9675010979358806

前次資料1448筆 本次資料15179筆
"""


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
