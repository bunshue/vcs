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

# descriptive_statistics

# 鳶尾花(Iris)品種的辨識

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#載入資料集

ds = datasets.load_iris()

#2. 資料清理、資料探索與分析

# 資料集說明
print(ds.DESCR)

import pandas as pd
df = pd.DataFrame(ds.data, columns=ds.feature_names)
print(df)

y = ds.target
print(y)

cc = ds.target_names
print(cc)

# 觀察資料集彙總資訊
cc = df.info()
print(cc)

# 描述統計量
cc = df.describe()
print(cc)

# 集中
cc = df['sepal length (cm)'].mean(), df['sepal length (cm)'].median(), df['sepal length (cm)'].mode()
print(cc)

# 計算變異數(variance)、標準差(standard deviation)、IQR
cc = df['sepal length (cm)'].var(), df['sepal length (cm)'].std(), \
    df['sepal length (cm)'].quantile(.75) - df['sepal length (cm)'].quantile(.25)

print(cc)

#(0.6856935123042505, 0.8280661279778629, 1.3000000000000007)

# 計算偏態(skewness)及峰度(kurtosis)
cc = df['sepal length (cm)'].skew(), df['sepal length (cm)'].kurt()
print(cc)

# 自行計算偏態
mean1 = df['sepal length (cm)'].mean()
std1  = df['sepal length (cm)'].std()
n = len(df['sepal length (cm)'])
skew1  = (((df['sepal length (cm)'] - mean1)/std1)**3).sum() * n / ((n-1) * (n-2))
print(skew1)

#0.31491095663697277

# 自行計算峰度
M2  = (((df['sepal length (cm)'] - mean1)/std1)**2).mean()
M4  = (((df['sepal length (cm)'] - mean1)/std1)**4).mean()
K = (M4 / (M2 ** 2)) 
print(K-3)

#-0.5735679489249756

from scipy.stats import kurtosis
print(kurtosis(df['sepal length (cm)'], axis=0, bias=True))

#-0.5735679489249765

# 直方圖
import seaborn as sns

sns.histplot(x='sepal length (cm)', data=df)
plt.show()

# 直方圖平滑化
sns.kdeplot(x='sepal length (cm)', data=df)
plt.show()

# 右偏
import numpy as np

data1 = np.random.normal(0, 1, 500)
data2 = np.random.normal(5, 1, 100)
data = np.concatenate((data1,data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
plt.show()

# 右偏
import numpy as np

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(5, 1, 500)
data = np.concatenate((data1,data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
plt.show()

#關聯度

df['y'] = y
cc = df.corr()
print(cc)

# 箱型圖
sns.boxplot(data=df)
plt.show()

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

#繪圖

# y 各類別資料筆數統計
import seaborn as sns
sns.countplot(x=y)
plt.show()

# 以Pandas函數統計各類別資料筆數
cc = pd.Series(y).value_counts()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#((120, 4), (30, 4), (120,), (30,))

print(y_train)

#特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()

#6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

#7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred)
                              , display_labels=ds.target_names)
disp.plot()
plt.show()

#8. 模型評估，暫不進行

#9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, 'tmp_model.joblib')
joblib.dump(scaler, 'tmp_scaler.joblib');

#10.模型預測，請參見 01_05_iris_prediction.py

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



