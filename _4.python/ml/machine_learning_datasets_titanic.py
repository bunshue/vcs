"""
titanic

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

# 鐵達尼號資料清理

# 載入鐵達尼號資料集

df = sns.load_dataset("titanic")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

cc = df.info()
print(cc)

cc = df.describe()
print(cc)

cc = df.describe(include="O")
print(cc)

cc = df.describe(include="all")
print(cc)

# 遺失值(Missing value)處理

cc = df.isnull().sum()
print(cc)

# 年齡(age)遺失值(Missing value)以中位數取代

df.age.fillna(df.age.median(), inplace=True)
cc = df.isnull().sum()
print(cc)

# 上船港口(embark_town)遺失值(Missing value)以前一筆取代

# 取得遺失值的列數
cc = df[pd.isna(df.embark_town)]
print(cc)

# 以前一筆取代
df.embark_town.fillna(method="ffill", inplace=True)
cc = df.loc[[61, 829]]
print(cc)

# 驗證
cc = df.loc[[61 - 1, 829 - 1]]
print(cc)

# 上船港口(embarked)遺失值(Missing value)以後一筆取代

# 取得遺失值的列數
cc = df[pd.isna(df.embarked)]
print(cc)

# 以後一筆取代
df.embarked.fillna(method="bfill", inplace=True)
cc = df.loc[[61, 829]]
print(cc)

# 驗證
cc = df.loc[[61 + 1, 829 + 1]]
print(cc)

# 甲板(deck)遺失值過多，刪除該欄位

df.drop("deck", axis=1, inplace=True)
cc = df.info()
print(cc)

# 離群值(Outlier) 處理

plt.boxplot(df.age)
plt.show()


def get_box_plot_data(labels, bp):
    rows_list = []

    for i in range(len(labels)):
        dict1 = {}
        dict1["label"] = labels[i]
        dict1["最小值"] = bp["whiskers"][i * 2].get_ydata()[1]
        dict1["箱子下緣"] = bp["boxes"][i].get_ydata()[1]
        dict1["中位數"] = bp["medians"][i].get_ydata()[1]
        dict1["箱子上緣"] = bp["boxes"][i].get_ydata()[2]
        dict1["最大值"] = bp["whiskers"][(i * 2) + 1].get_ydata()[1]
        rows_list.append(dict1)

    return pd.DataFrame(rows_list)


bp = plt.boxplot(df.age)
get_box_plot_data(["age"], bp)
plt.show()

"""
	label 	最小值 	箱子下緣 	中位數 	箱子上緣 	最大值
0 	age 	3.0 	22.0 	28.0 	35.0 	54.0
"""

df = df[(3.0 <= df.age) & (df.age <= 54.0)]
plt.hist(df.age)
plt.show()


# 類別變數轉換為數值

df.sex = df.sex.map({"male": 1, "female": 0})
cc = df.head()
print(cc)

df.embark_town = df.embark_town.map({"Southampton": 0, "Cherbourg": 1, "Queenstown": 2})
cc = df.head()
print(cc)

# 欄位分組(bin)

bins = [0, 12, 18, 25, 35, 60, 100]
cats = pd.cut(df.age, bins)
print(cats)

print(cats.cat.categories)

cc = cats.cat.categories.to_list()[1].left, cats.cat.categories.to_list()[1].right
print(cc)

df.age = pd.cut(df.age, bins, labels=range(len(bins) - 1))
cc = df.head()
print(cc)

# 移除重複資料

# 增加一筆重複資料
print(df.shape)

df.drop_duplicates()

y = df.survived
X = df.drop(["survived", "alive", "embarked", "who", "alone", "class"], axis=1)
cc = X.head()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

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

from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test_std)
# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 82.42%

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, "tmp_titanic_model.joblib")
joblib.dump(scaler, "tmp_titanic_scaler.joblib")

print("------------------------------------------------------------")  # 60個

# Scikit-learn 前置處理
# 遺失值(Missing value)處理

from sklearn.impute import SimpleImputer

# 以平均數填補
imp = SimpleImputer(missing_values=np.nan, strategy="mean")
# 訓練
imp.fit([[1, 2], [np.nan, 3], [7, 6]])

# 轉換
X = [[np.nan, 2], [6, np.nan], [7, 6]]
print(imp.transform(X))

df = sns.load_dataset("titanic")

imp = SimpleImputer(missing_values=pd.NA, strategy="median")
# 訓練並轉換，SimpleImputer 輸入必須是二維
imp.fit_transform(df.age.values.reshape(-1, 1))

# 多變數(Multivariate)

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# 訓練
imp = IterativeImputer(max_iter=10, random_state=0)
imp.fit([[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]])

# 轉換
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
print(np.round(imp.transform(X_test)))

# 必須為數值欄位
df = sns.load_dataset("titanic")
df.sex = df.sex.map({"male": 1, "female": 0})
df2 = df[["pclass", "sex", "age", "sibsp", "parch", "fare"]]

imp = IterativeImputer(max_iter=10, random_state=0)

# 訓練並轉換
df2 = imp.fit_transform(df2.values)
df_new = pd.DataFrame(df2, columns=["pclass", "sex", "age", "sibsp", "parch", "fare"])
print(df_new)

cc = df_new.isnull().sum()
print(cc)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing, linear_model

titanic = pd.read_csv("data/titanic_ds.csv")
print(titanic.info())
print("---------------------------")
# 將年齡的空值填入年齡的中位數
age_median = np.nanmedian(titanic["Age"])
print("年齡中位數", age_median)
print("---------------------------")
new_age = np.where(titanic["Age"].isnull(), age_median, titanic["Age"])
titanic["Age"] = new_age
print(titanic)
print("---------------------------")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, titanic["SexCode"], titanic["Age"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)
print("迴歸係數:", logistic.coef_)
print("截距:", logistic.intercept_)

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing, linear_model

titanic = pd.read_csv("data/titanic_ds.csv")
print(titanic.info())
print("---------------------------")
# 將年齡的空值填入年齡的中位數
age_median = np.nanmedian(titanic["Age"])
new_age = np.where(titanic["Age"].isnull(), age_median, titanic["Age"])
titanic["Age"] = new_age
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, titanic["SexCode"], titanic["Age"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)

preds = logistic.predict(X)
print(pd.crosstab(preds, titanic["Survived"]))

print("---------------------------")
print((805 + 265) / (805 + 185 + 58 + 265))
print(logistic.score(X, y))

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing, linear_model

titanic = pd.read_csv("data/titanic_ds.csv")
print(titanic.info())
print("---------------------------")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, titanic["SexCode"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)
print("迴歸係數:", logistic.coef_)
print("截距:", logistic.intercept_)
print("---------------------------")
preds = logistic.predict(X)
print(pd.crosstab(preds, titanic["Survived"]))

print("---------------------------")
print((840 + 222) / (840 + 222 + 23 + 228))
print(logistic.score(X, y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import datasets

import pandas as pd
from sklearn import preprocessing, tree
from sklearn.model_selection import train_test_split

titanic = pd.read_csv("data/titanic_ds.csv")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([titanic["SexCode"], encoded_class]).T
X.columns = ["SexCode", "PClass"]
y = titanic["Survived"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25, random_state=1)

dtree = tree.DecisionTreeClassifier()
dtree.fit(XTrain, yTrain)

print("準確率:", dtree.score(XTest, yTest))
print("---------------------------")
preds = dtree.predict_proba(X=XTest)
print(pd.crosstab(preds[:, 0], columns=[XTest["PClass"], XTest["SexCode"]]))
pd.crosstab(preds[:, 0], columns=[XTest["PClass"], XTest["SexCode"]]).to_html(
    "tmp_ch16-1-2.html"
)

print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import preprocessing, tree
from sklearn.model_selection import train_test_split

titanic = pd.read_csv("data/titanic_ds.csv")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([titanic["SexCode"], encoded_class]).T
X.columns = ["SexCode", "PClass"]
y = titanic["Survived"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25, random_state=1)

dtree = tree.DecisionTreeClassifier()
dtree.fit(XTrain, yTrain)

with open("tmp_tree.dot", "w") as f:
    f = tree.export_graphviz(dtree, feature_names=["Sex", "Class"], out_file=f)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
