"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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
"""

乳癌診斷預測

"""

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#1. 載入資料集

ds = datasets.load_breast_cancer()
"""
print("資料集說明")
print(ds.DESCR)

print("資料集欄位")
print(ds.feature_names)

print("資料集資料")
print(ds.data)

print("資料集目標名稱")
print(ds.target_names)

print("資料集目標")
print(ds.target)
"""

#2. 資料清理、資料探索與分析

df = pd.DataFrame(ds.data, columns=ds.feature_names)
#print(df)

# 資料集目標
y = ds.target
#print(y)
#資料集目標名稱
#print(ds.target_names)

print("觀察資料集彙總資訊")
cc = df.info()
print(cc)

print("描述統計量")
cc = df.describe()
print(cc)

# 箱型圖
import seaborn as sns
sns.boxplot(data=df)
plt.title('xxxxx箱型圖')
plt.show()


print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
"""
import seaborn as sns
sns.countplot(x=y)
plt.title('y 各類別資料筆數統計')
plt.show()
"""
print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
# 訓練資料, 測試資料, 訓練目標, 測試目標
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 8成訓練 2成測試

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("訓練目標")
#print(y_train)

print("測試目標")
print(y_test)

print("特徵縮放")

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)

#7. 模型評估

y_pred = clf.predict(X_test_std)
print('預測目標')
print(y_pred)

print('計算準確率 測試目標 與 預測目標 接近程度')
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

print('混淆矩陣')
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

print('混淆矩陣圖')
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred)
                              , display_labels=ds.target_names)
disp.plot()
plt.title('混淆矩陣圖')
plt.show()

#8. 模型評估，暫不進行

#9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, 'tmp_cancer_model.joblib')
joblib.dump(scaler, 'tmp_cancer_scaler.joblib');

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



