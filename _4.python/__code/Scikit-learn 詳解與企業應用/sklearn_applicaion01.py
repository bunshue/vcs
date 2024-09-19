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

#鳶尾花(Iris)品種的辨識

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#1. 載入資料集

ds = datasets.load_iris()

#2. 資料清理、資料探索與分析

print("資料集說明")
print(ds.DESCR)

df = pd.DataFrame(ds.data, columns=ds.feature_names)
print(df)

y = ds.target
print(y)

print(ds.target_names)

#array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

print("觀察資料集彙總資訊")
cc = df.info()
print(cc)

# 描述統計量
cc = df.describe()
print(cc)


# 箱型圖
import seaborn as sns
sns.boxplot(data=df)

plt.show()

print("是否有含遺失值(Missing value)")
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

print("特徵縮放")

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
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
#7. 模型評估

y_pred = clf.predict(X_test_std)
print(y_pred)

"""
array([2, 2, 1, 2, 0, 1, 0, 2, 0, 2, 0, 1, 1, 0, 0, 1, 2, 1, 1, 2, 0, 0,
       0, 1, 2, 0, 0, 0, 1, 0])
"""

print('計算準確率')
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#100.00%

print('混淆矩陣')
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

print('混淆矩陣圖')
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

joblib.dump(clf, 'model.joblib')
joblib.dump(scaler, 'scaler.joblib');

print("------------------------------------------------------------")  # 60個

import streamlit as st
import joblib

#10.模型預測

# 載入模型與標準化轉換模型
clf = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

st.title('鳶尾花（Iris）預測')
sepal_length = st.slider('花萼長度:', min_value=3.0, max_value=8.0, value=5.8)
sepal_width = st.slider('花萼寬度:', min_value=2.0, max_value=5.0, value=3.5)
petal_length = st.slider('花瓣長度:', min_value=1.0, max_value=7.0, value=4.4)
petal_width = st.slider('花瓣寬度:', min_value=0.1, max_value=2.5, value=1.3)

labels = ['setosa', 'versicolor', 'virginica']
if st.button('預測'):
    X_new = [[sepal_length,sepal_width,petal_length,petal_width]]
    X_new = scaler.transform(X_new)
    st.write('### 預測品種是：', labels[clf.predict(X_new)[0]])


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



