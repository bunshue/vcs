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

#尋找銀行行銷活動目標客戶

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

#載入資料集

df = pd.read_csv('./data/banking.csv')
cc = df.head()
print(cc)

#2. 資料清理、資料探索與分析

# y 各類別資料筆數統計
import seaborn as sns
sns.countplot(x='y', data=df)
plt.show()

# y 各類別資料筆數統計
cc = df.y.value_counts()
print(cc)

from matplotlib import pyplot as plt

series1 = df.y.value_counts()
series1.plot.pie(figsize=(6,6), autopct='%1.1f%%')
plt.legend()
plt.show()

cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(df[var], prefix=var)
    data1=df.join(cat_list)
    df=data1
    
data_vars=df.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]
data_final=df[to_keep]
cc = data_final.columns.values
print(cc)

df = data_final
print(df)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.drop('y', axis=1).values
y = df.y.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

#((32950, 63), (8238, 63), (32950,), (8238,))

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

# 計算準確率
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#91.53%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#8. 模型評估，暫不進行

#9. 模型佈署，暫不進行


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



