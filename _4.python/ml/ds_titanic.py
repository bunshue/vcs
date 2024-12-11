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

df.info()  # 這樣就已經把資料集彙總資訊印出來

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

df.info()  # 這樣就已經把資料集彙總資訊印出來

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


# 6-1 探索性資料分析──以Titanic(鐵達尼號)之生還預測為例
# 資料科學 0. 問個感興趣的問題

# 資料科學 1. 資料取得
# 資料科學1.1 自建資料或下載資料後上傳到雲端硬碟

# train.csv行資料說明.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/titanic.csv"
df = pd.read_csv(filename)
"""
print(df)
print(df.info())
print(df.describe())
"""

# 資料科學2.3 資料清理
# 缺失值的補值或刪除

print(df.isnull())

print(df.isnull().sum())

print(df.isnull().count())

print(df.isnull().sum() / df.isnull().count() * 100)

df[df["Age"].isnull() == True]

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

df[df["Embarked"].isnull()]

df["Embarked"].value_counts()

df["Embarked"] = df["Embarked"].fillna("S")

df.loc[[61, 829], :]  # 顯示列索引61,829的資料

print(df.info())

df = df.drop("Cabin", axis=1)

print(df.info())

# 刪除重複值或異常值
df[df.duplicated()]

# 資料轉換
print(df.head())

s = {"female": 0, "male": 1}
df["Sex"] = df["Sex"].map(s)
e = {"S": 0, "C": 1, "Q": 2}
df["Embarked"] = df["Embarked"].map(e)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)

print(df.head())

# 資料科學3.2 資料視覺化
# 1.全體乘客生還、死亡的比例

print(df["Survived"].value_counts())

df["Survived"].value_counts().plot(kind="pie", autopct="%1.2f%%")
show()

print("------------------------------")  # 30個

# 2.男性、女性乘客的比例

print(df["Sex"].value_counts())

df["Sex"].value_counts().plot(kind="pie", autopct="%1.2f%%")
show()

print("------------------------------")  # 30個

# 3.搭1等艙、2等艙、3等艙的乘客比例

print(df["Pclass"].value_counts())

df["Pclass"].value_counts().plot(kind="pie", autopct="%1.2f%%")
show()

print("------------------------------")  # 30個

# 4.進一步探討性別與生還的關係

# 女、男乘客的人數

print(df.groupby(["Sex"])["PassengerId"].count())

# 不同性別的生還和死亡人數

print(df.groupby(["Sex", "Survived"])["PassengerId"].count())

df.groupby(["Sex", "Survived"])["PassengerId"].count().plot(kind="bar", rot=1)
show()

print("------------------------------")  # 30個

# 不同性別生還人數/不同性別人數

ss = (
    df.groupby(["Sex", "Survived"])["PassengerId"].count()
    / df.groupby(["Sex"])["PassengerId"].count()
    * 100
)
print(ss)

ss.plot(kind="bar", color=["r", "g"], rot=0)
show()

print("------------------------------")  # 30個

# 5.進一步探討艙等與生還的關係

# 三種艙等的生還和死亡人數

print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())

df.groupby(["Pclass", "Survived"])["PassengerId"].count().plot(kind="bar", rot=0)
show()

print("------------------------------")  # 30個

# 不同艙等生還人數/不同艙等人數

ps = (
    df.groupby(["Pclass", "Survived"])["PassengerId"].count()
    / df.groupby(["Pclass"])["PassengerId"].count()
    * 100
)
print(ps)

ps.plot(kind="bar", rot=0)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def read_dataset(fname):
    # 指定第一列作為行索引
    data = pd.read_csv(fname, index_col=0)
    # 丟棄無用的數據
    data.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)
    # 處理性別數據
    data["Sex"] = (data["Sex"] == "male").astype("int")
    # 處理登船港口數據
    labels = data["Embarked"].unique().tolist()
    data["Embarked"] = data["Embarked"].apply(lambda n: labels.index(n))
    # 處理缺失數據
    data = data.fillna(0)
    return data


train = read_dataset("datasets/titanic/train.csv") # 共891筆資料, 8欄位
print(train.head())

# 把 "Survived"欄位拿出來當訓練目標 => y
y = train["Survived"].values

# 把 "Survived"欄位從原訓練資料移除 => X
X = train.drop(["Survived"], axis=1).values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)

print("train_score :", train_score)
print("test_score :", test_score)

print("------------------------------")  # 30個

from sklearn.tree import export_graphviz

with open("tmp_titanic1.dot", "w") as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在電腦上安裝 graphviz
# 2. 運行 `dot -Tpng titanic.dot -o titanic.png`
# 3. 在當前目錄查看生成的決策樹 titanic.png


# 參數選擇 max_depth
def cv_score(d):
    clf = DecisionTreeClassifier(max_depth=d)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)


depths = range(2, 15)
scores = [cv_score(d) for d in depths]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = depths[best_score_index]
print("best param: {0}; best score: {1}".format(best_param, best_score))

plt.figure(figsize=(10, 6))
plt.grid()
plt.xlabel("max depth of decision tree")
plt.ylabel("score")
plt.plot(depths, cv_scores, ".g-", label="cross-validation score")
plt.plot(depths, tr_scores, ".r--", label="training score")
plt.legend()
show()

print("------------------------------")  # 30個

# 訓練模型，并計算評分
def cv_score(val):
    clf = DecisionTreeClassifier(criterion="gini", min_impurity_decrease=val)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)


# 指定參數范圍，分別訓練模型，并計算評分
values = np.linspace(0, 0.005, 50)
scores = [cv_score(v) for v in values]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

# 找出評分最高的模型參數
best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = values[best_score_index]
print("best param: {0}; best score: {1}".format(best_param, best_score))

# 畫出模型參數與模型評分的關系
plt.figure(figsize=(10, 6))
plt.grid()
plt.xlabel("threshold of entropy")
plt.ylabel("score")
plt.plot(values, cv_scores, ".g-", label="cross-validation score")
plt.plot(values, tr_scores, ".r--", label="training score")
plt.legend()
show()

print("------------------------------")  # 30個


def plot_curve(train_sizes, cv_results, xlabel):
    train_scores_mean = cv_results["mean_train_score"]
    train_scores_std = cv_results["std_train_score"]
    test_scores_mean = cv_results["mean_test_score"]
    test_scores_std = cv_results["std_test_score"]
    plt.figure(figsize=(10, 6))
    plt.title("parameters turning")
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel("score")
    plt.fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    plt.fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    plt.plot(train_sizes, train_scores_mean, ".--", color="r", label="Training score")
    plt.plot(
        train_sizes, test_scores_mean, ".-", color="g", label="Cross-validation score"
    )

    plt.legend(loc="best")


from sklearn.model_selection import GridSearchCV

thresholds = np.linspace(0, 0.005, 50)
# Set the parameters by cross-validation
param_grid = {"min_impurity_decrease": thresholds}

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

# cv_results_ : 具體用法模型不同參數下交叉驗證的結果
plot_curve(thresholds, clf.cv_results_, xlabel="gini thresholds")

show()

print("------------------------------")  # 30個

from sklearn.model_selection import GridSearchCV

entropy_thresholds = np.linspace(0, 0.01, 50)
gini_thresholds = np.linspace(0, 0.005, 50)

# Set the parameters by cross-validation
param_grid = [
    {"criterion": ["entropy"], "min_impurity_decrease": entropy_thresholds},
    {"criterion": ["gini"], "min_impurity_decrease": gini_thresholds},
    {"max_depth": range(2, 10)},
    {"min_samples_split": range(2, 30, 2)},
]

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

print("------------------------------")  # 30個

print("生成決策樹圖形")

clf = DecisionTreeClassifier(
    criterion="entropy", min_impurity_decrease=0.002857142857142857
)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

# 導出 titanic.dot 文件
with open("tmp_titanic2.dot", "w") as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在電腦上安裝 graphviz
# 2. 運行 `dot -Tpng titanic.dot -o titanic.png`
# 3. 在當前目錄查看生成的決策樹 titanic.png

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 數據集和數據處理

from pandas import Series, DataFrame

# 繪圖分析
sns.set_style("whitegrid")

# 機器學習
from sklearn.linear_model import LogisticRegression  # 邏輯迴歸
#from sklearn.svm import SVC, LinearSVC  # 支持向量機
from sklearn.ensemble import RandomForestClassifier  # 隨機森林

from sklearn.naive_bayes import GaussianNB  # 數據集和數據處理

print("------------------------------")	#30個

titanic_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")
print(titanic_df.head())
print(titanic_df.info())
print(titanic_df.describe())

facet = sns.FacetGrid(titanic_df, hue="Survived", aspect=4)
facet.map(sns.kdeplot, "Age", shade=True)
facet.set(xlim=(0, titanic_df["Age"].max()))
facet.add_legend()
show()

fig, axis1 = plt.subplots(1, 1, figsize=(18, 4))
average_age = titanic_df[["Age", "Survived"]].groupby(["Age"], as_index=False).mean()
sns.barplot(x="Age", y="Survived", data=average_age)
show()

print("------------------------------")	#30個


def get_person(passenger):  # 小於16歲的分類爲兒童
    age, sex = passenger
    return "child" if age < 16 else sex


def conv(df):
    df["Person"] = df[["Age", "Sex"]].apply(get_person, axis=1)  # 組合特徵
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())  # 缺失值填充爲均值
    df["Embarked"] = df["Embarked"].fillna("S")  # 缺失值填充爲S
    df["Fare"] = df["Fare"].astype(int)  # 類型轉換

    person_dummies = pd.get_dummies(df["Person"])  # onehot編碼
    person_dummies.columns = ["Child", "Female", "Male"]
    df = df.join(person_dummies)  # 連接原數據與onehot數據
    df = df.drop(
        ["PassengerId", "Name", "Ticket", "Person", "Sex", "Embarked", "Cabin", "Age"],
        axis=1,
    )  # 刪除非數據型特徵
    return df


titanic_df = conv(titanic_df)
test_df = conv(test_df)

print("------------------------------")	#30個

# 生成模型所需的訓練集和測試集
X_train = titanic_df.drop("Survived", axis=1)
Y_train = titanic_df["Survived"]
X_test = test_df.copy()

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()  # 初始化模型

logreg.fit(X_train, Y_train)  # 學習訓練.fit

print(logreg.score(X_train, Y_train))  # 模型評分

Y_pred = logreg.predict(X_test)  # 預測

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# How do I use pandas with scikit-learn to create Kaggle submissions? (video)

# 讀取[Kaggle's Titanic competition]資料集至df
# train = pd.read_csv('http://bit.ly/kaggletrain')
filename = "data/titanic_train.csv"
train = pd.read_csv(filename)

print("檢視前幾行")
cc = train.head()
print(cc)

# create a feature matrix 'X' by selecting two DataFrame columns
feature_cols = ["Pclass", "Parch"]
X = train.loc[:, feature_cols]

print("X之大小")
cc = X.shape
print(cc)

# create a response vector 'y' by selecting a Series
y = train.Survived
print("y之大小")
cc = y.shape
print(cc)

# fit a classification model to the training data
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X, y)

# read the testing dataset from Kaggle's Titanic competition into a DataFrame
test = pd.read_csv("http://bit.ly/kaggletest")
print("檢視前幾行")
cc = test.head()
print(cc)

# create a feature matrix from the testing data that matches the training data
X_new = test.loc[:, feature_cols]
print("X_new之大小")
cc = X_new.shape
print(cc)

# use the fitted model to make predictions for the testing set observations
new_pred_class = logreg.predict(X_new)

# create a DataFrame of passenger IDs and testing set predictions
print("檢視前幾行")
cc = pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).head()
print(cc)

# ensure that PassengerID is the first column by setting it as the index
print("檢視前幾行")
cc = (
    pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class})
    .set_index("PassengerId")
    .head()
)
print(cc)

print("df轉csv")
pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).set_index(
    "PassengerId"
).to_csv("tmp_sub.csv")

print("df轉pickle")
train.to_pickle("tmp_train.pkl")

print("pickle轉df")
print("檢視前幾行")
cc = pd.read_pickle("tmp_train.pkl").head()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_13_chaid_three_cat

from seaborn import load_dataset

df = load_dataset("titanic")
cc = df.head()
print(cc)

df.embarked = df.embarked.fillna(method="ffill")
cc = df.head()
print(cc)

from CHAID import Tree

independent_variable_columns = ["sex", "embarked"]
dep_variable = "survived"
tree = Tree.from_pandas_df(
    df,
    dict(zip(independent_variable_columns, ["nominal"] * 3)),
    dep_variable,
    dep_variable_type="categorical",
    max_depth=5,
    min_parent_node_size=2,
    alpha_merge=0.1,
)
tree.print_tree()

from CHAID import Tree

independent_variable_columns = ["fare", "sex", "embarked"]
dep_variable = "survived"
tree = Tree.from_pandas_df(
    df,
    dict(zip(independent_variable_columns, ["ordinal"] + ["nominal"] * 3)),
    dep_variable,
    dep_variable_type="categorical",
    max_depth=5,
    min_parent_node_size=2,
    alpha_merge=0.1,
)
tree.print_tree()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
