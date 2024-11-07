"""
邏輯迴歸




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
print("------------------------------------------------------------")  # 60個

# 尋找銀行行銷活動目標客戶

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("./data/banking.csv")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# y 各類別資料筆數統計

sns.countplot(x="y", data=df)
plt.show()

# y 各類別資料筆數統計
cc = df.y.value_counts()
print(cc)

from matplotlib import pyplot as plt

series1 = df.y.value_counts()
series1.plot.pie(figsize=(6, 6), autopct="%1.1f%%")
plt.legend()
plt.show()

cat_vars = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "day_of_week",
    "poutcome",
]
for var in cat_vars:
    cat_list = "var" + "_" + var
    cat_list = pd.get_dummies(df[var], prefix=var)
    data1 = df.join(cat_list)
    df = data1

data_vars = df.columns.values.tolist()
to_keep = [i for i in data_vars if i not in cat_vars]
data_final = df[to_keep]
cc = data_final.columns.values
print(cc)

df = data_final
print(df)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.drop("y", axis=1).values
y = df.y.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# ((32950, 63), (8238, 63), (32950,), (8238,))

# 特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 91.53%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# 8. 模型評估，暫不進行

# 9. 模型佈署，暫不進行

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectKBest 單變數特徵選取(Univariate feature selection)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

# (150, 4)

# SelectKBest 特徵選取

clf = SelectKBest(chi2, k=2)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# (150, 2)

# 顯示特徵分數
cc = clf.scores_
print(cc)

# 顯示 p value
print(clf.pvalues_)

# 顯示特徵名稱

ds = datasets.load_iris()
cc = np.array(ds.feature_names)[clf.scores_.argsort()[-2:][::-1]]
print(cc)

X = pd.DataFrame(ds.data, columns=ds.feature_names)
clf = SelectKBest(chi2, k=2)
X_new = clf.fit_transform(X, y)
cc = clf.get_feature_names_out()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X[clf.get_feature_names_out()].values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectPercentile 單變數特徵選取(Univariate feature selection)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectPercentile, chi2

X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# SelectPercentile 特徵選取

clf = SelectPercentile(chi2, percentile=10)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 顯示特徵分數
print(clf.scores_)

# 顯示 p value
print(clf.pvalues_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 71.94%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (1437, 64) (360, 64) (1437,) (360,)
# 98.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
GenericUnivariateSelect 單變數特徵選取(Univariate feature selection)
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import GenericUnivariateSelect, chi2

X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# GenericUnivariateSelect 特徵選取

# 使用 SelectKBest, 20 個特徵
clf = GenericUnivariateSelect(chi2, mode="k_best", param=20)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 顯示特徵分數
print(clf.scores_)

# 顯示 p value
print(clf.pvalues_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (1437, 64) (360, 64) (1437,) (360,)
# 97.22%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
遞迴特徵消去法(Recursive feature elimination)
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import RFE
from sklearn.svm import SVC

X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

# RFE 特徵選取

svc = SVC(kernel="linear", C=1)
clf = RFE(estimator=svc, n_features_to_select=2, step=1)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 特徵重要性排名
print(clf.ranking_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
