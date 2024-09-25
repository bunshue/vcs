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

#計程車小費資料集EDA

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import seaborn as sns
import numpy as np

#載入資料集

df = sns.load_dataset('tips')
cc = df.head()
print(cc)

#2. 資料清理、資料探索與分析

# 對小費繪製直方圖
sns.histplot(x='tip', data=df)
plt.show()

df['log_tip'] = np.log(df['tip'])
sns.kdeplot(x='log_tip', data=df)
plt.show()

# 散佈圖
sns.scatterplot(x="total_bill", y="tip", data=df);
plt.show()

# 三維散佈圖
sns.scatterplot(x="total_bill", y="tip", hue='sex', data=df);
plt.show()

# joint plot
sns.jointplot(data=df, x="total_bill", y="tip", hue="day")
plt.show()

df.day.unique()

#['Sun', 'Sat', 'Thur', 'Fri']
#Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']

#觀察週間對小費的影響

sns.barplot(x='day', y='tip', data=df)
plt.show()

# 箱型圖
sns.boxplot(x='day', y='tip', data=df)
plt.show()

# 類別變數轉換為數值
df.sex = df.sex.map({'Female':0, 'Male':1}).astype(int)
df.smoker = df.smoker.map({'No':0, 'Yes':1}).astype(int)
df.day = df.day.map({'Thur':1, 'Fri':2, 'Sat':3, 'Sun':4}).astype(int)
df.time = df.time.map({'Lunch':0, 'Dinner':1}).astype(int)

cc = df.info()
print(cc)

# 繪製pair plot
sns.pairplot(data=df, height=1)
plt.show()

# 熱力圖
sns.heatmap(data=df.corr(), annot=True, fmt=".2f", linewidths=.5)
plt.show()

cc = df.isna().sum()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.drop('tip', axis=1).values
y = df.tip.values
print(y)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

#((195, 7), (49, 7), (195,), (49,))

#特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#6. 模型訓練

lr.fit(X_train_std, y_train)

"""
LinearRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

#7. 模型計分

y_pred = lr.predict(X_test_std)

# 計算 r2、MSE
print(f'R2:{r2_score(y_test, y_pred):.2f}, MSE:{mean_squared_error(y_test, y_pred):.2f}') 

#R2:0.91, MSE:0.26

#8. 模型評估，暫不進行

#9. 模型佈署，暫不進行

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



