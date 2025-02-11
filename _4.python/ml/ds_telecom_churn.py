"""
# 客戶流失預警模型

電信客戶流失數據    telecom_churn

telecom_churn.csv 3463筆資料 20欄位
subscriberID,churn,gender,AGE,edu_class,incomeCode,duration,feton,peakMinAv,peakMinDiff,posTrend,negTrend,nrProm,prom,curPlan,avgplan,planChange,posPlanChange,negPlanChange,call_10086
19164958, 1, 0, 20, 2, 12, 16, 0, 113,   -8, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0
39244924, 1, 1, 20, 0, 21,  5, 0, 274, -371, 0, 1, 2, 1, 3, 2, 2, 1, 0, 1
39578413, 1, 0, 11, 1, 47,  3, 0, 392, -784, 0, 1, 0, 0, 3, 3, 0, 0, 0, 1
40992265, 1, 0, 43, 0,  4, 12, 0,  31,  -76, 0, 1, 2, 1, 3, 3, 0, 0, 0, 1
43061957, 1, 1, 60, 0,  9, 14, 0, 129, -334, 0, 1, 0, 0, 3, 3, 0, 0, 0, 0
47196850, 0, 0, 20, 2, 24,  9, 1, 281,  309, 1, 0, 0, 0, 2, 2, 0, 0, 0, 1
51236987, 1, 1, 17, 2, 13,  5, 0, 348,  -29, 0, 1, 1, 1, 3, 3, 0, 0, 0, 1
subscriberID 用戶ID
churn 因變量：是否流失（1表示流失，0表示未流失）
gender 性別（男、女）
AGE 年齡
edu_class 教育程度（小學及以下、初中、高中/中專/技校、大專、本科、研究生及以上）
incomeCode 收入水平（1-10分別代表不同的收入區間）
duration 已加入運營商的時長（月）
feton 上月ARPU值（平均每個用戶每月產生的收入）
peakMinAv 月峰值通話時間（分鐘）
peakMinDiff 非月峰值通話時間（分鐘）
posTrend 正向情感傾向得分
negTrend 負向情感傾向得分
nrProm 最近6個月參與的營銷活動次數
prom 是否參與當前的營銷活動（1表示參與，0表示未參與）
curPlan 當前套餐類型（A/B/C三種）
avgplan 歷史平均套餐價格
planChange 套餐變更次數
posPlanChange 套餐升級次數
negPlanChange 套餐降級次數
call_10086 最近3個月撥打10086客服的次數
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

import joblib
import sklearn.linear_model

# import tensorflow as tf
from common1 import *
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression  # 邏輯回歸
from sklearn.svm import SVC  # 支持向量機
from sklearn.model_selection import cross_val_score, KFold  # 交叉驗證
from sklearn.neighbors import KNeighborsClassifier  # kNN
from sklearn.tree import DecisionTreeClassifier  # 決策樹分類(Decision Tree Classifier)
from sklearn.tree import DecisionTreeRegressor  # 迴歸樹
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import roc_curve
from sklearn.manifold import MDS
from sklearn.decomposition import PCA

# 不要顯示一些警告
import warnings

warnings.filterwarnings("ignore")  # 忽視報錯


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import plotly.graph_objects as go
import plotly.express as px

# 數據清洗與格式轉換

# 導入數據並查看
# 加載數據集
df = pd.read_csv("./data/telecom_churn.csv")

# 將所有列展示出來
df_names = df.columns.tolist()
print(df_names)

cc = df.head()
print("前5筆資料 :\n", cc, sep="")

# 查看信息表，清什么，可以看到ID屬于個人信息沒有用。其次要轉換，將str轉換為float

# 查看數據、缺失值、重復值、總體概覽
cc = df.isna().sum()
print(cc)

# 重復值
cc = df.duplicated().sum()
print(cc)

# 總體
cc = df.info()
print(cc)

cc = df.describe()
print(cc)

# describe()可以返回具體的結果，對于每一列
# 數量、平均值、標準差、25%、分位、50%、分位數、最大值、很多時候可以得到NA的數量和比例

# 缺失值處理：連續值--平均數、眾數、中位數 非數值型特征---統計個數用眾數據填充 當然還可以通過隨機森林等算法做預測---同時消耗的代價也比較大

# 數據並沒有什么問題
# 數據集甚至將類型都轉換好了
# 但是我們在這里寫一下一般是怎末轉換的
# 將比如說將數據轉換為數值類型
# 比如標簽轉換

# df = df.replace({'男':1,'女':0,'No Data': -1})
# df = df.replace({'有':1,'無':0,'No Data': -1})

# 歸一化數據

"""
for feature in data:
    df[feature] = pd.Categorical(df[feature]).codes
"""

# 在這里我們需要刪除沒用的標簽比如說id
df_new = df.drop({"subscriberID"}, axis=1)
print(df_new)  # 3463 X 19

print("------------------------------")  # 30個

# 探索性數據分析（EDA）
# 用圖的方式把數據展示出來，告訴大家內些特征對模型有用，那些數據對模型沒用
# 1.特征自己的信息
# 2.特征和特征之間的關系
# 3.特征和標簽之間的關系

# 查看流失比例，以及關于打客服電話的個數分布

plt.subplot(121)
df["churn"].value_counts().plot(kind="bar")  # 將用戶流失分組起來，流失多少人沒用流失多少人
plt.title("流失和未流失比例")
plt.ylabel("數量")

plt.subplot(122)
df["call_10086"].value_counts().plot(kind="bar")
plt.title("打客服電話比例")
plt.ylabel("數量")
plt.suptitle("查看流失比例")
show()

print("------------------------------")  # 30個

# peakMinAv 月峰值通話時間（分鐘） peakMinDiff 非月峰值通話時間（分鐘）

plt.subplot(121)
df["peakMinAv"].plot(kind="kde")  # 峰值通話，圖用的kde的圖例
plt.xlabel("分鐘數")
plt.ylabel("密度")
plt.title("峰值通話")

plt.subplot(122)
df["peakMinDiff"].plot(kind="kde")
plt.xlabel("分鐘數")
plt.ylabel("密度")
plt.title("非峰值通話")
plt.suptitle("峰值通話/非峰值通話")
show()

print("------------------------------")  # 30個

# 數據有大有小有正有負，符合高斯分布，我們在做歸一化的時候將數據作為float類型

# churn 因變量：是否流失（1表示流失，0表示未流失）
# prom 是否參與當前的營銷活動（1表示參與，0表示未參與）

# 查看參與當前營銷和流失的關系
# 查看流失與輸入輸入水平之間的關系
int_yes = df["churn"][df["prom"] == 1].value_counts()
int_no = df["churn"][df["prom"] == 0].value_counts()
# 做圖例
df_int = pd.DataFrame({"參與營銷": int_yes, "未參與營銷": int_no})

df_int.plot(kind="bar", stacked=True)
show()

# 從圖上看來
# 大概有1900未流失的客戶，其中300人參與當月活動0.157 大概有1500流失用戶其中有200人參與當月活動0.133

print("------------------------------")  # 30個

# 特征篩選
# 對于標簽數據需要整合
# ds_result = churn_df['churn']
# shift+tab:condition是布爾類型的數組，每個條件都和x,y對應
# 相當于流失了/true為1，沒有流失/false為0
# Y = np.where(ds_result == 'True',1,0)
# 刪除無用數據
# to_drop = ['stale','Area Code']
# df = ds_tmp.drop(to_drop,axis=1)

cc = df_new.head()
print("前5筆資料 :\n", cc, sep="")

# 特征工程
# 我們需要做一些scala的工作，就是有些屬性的scala太大了
# 對于邏輯回歸和梯度下降來說，各個屬性的scala差距太大，會對收斂速度有很大的影響
# 我們這里對所有的都做，其實可以對一些突出的特征做這種處理

y = df_new["churn"]
x = df_new.drop("churn", axis=1)

# 數量級不一樣，通過scala實現去量綱的影響
# 在訓練模型時之前經常要對數據進行數組轉化，as_matrix()：把所有的特征都轉化為np.float
X = x.astype(np.float32)
print(X)

# 標準化
scaler = StandardScaler()
X = scaler.fit_transform(X)
print(X)
print(X.shape)

print("------------------------------")  # 30個

# 建立多種模型
# 將數據進行拆分

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 初始化模型
models = []
models.append(("KNN", KNeighborsClassifier()))
models.append(("LR", LogisticRegression()))
models.append(("SVM", SVC()))
# 初始化
results = []
names = []
scoring = "accuracy"  # 準確率
for name, model in models:
    print("1111 :", name)
    print("2222 :", model)
    kfold = KFold(5, shuffle=True, random_state=9487)  # 5折
    cv_results = cross_val_score(model, X, y, cv=kfold)
    results.append(cv_results)  # 交叉驗證給的結果分
    names.append(name)
    # 模型的標準差，體現模型的波動值,std越小越穩
    msg = "%s:%f(%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    print("------------------")

fig = plt.figure()
fig.suptitle("")
ax = fig.add_subplot(111)

plt.boxplot(results)
ax.set_xticklabels(names)
show()
"""
KNN:0.773030(0.010844)
------------------
LR:0.835399(0.008645)
------------------
SVM:0.831359(0.001487)
------------------
"""
print("------------------------------")  # 30個

# 如果不進行標準化明顯準確率沒有標準化高
# 初始化
"""
results = []
names = []
scoring = 'accuracy'#準確率
for name,model in models:
    kfold = KFold(5,shuffle=True,random_state=9487)#5折
    cv_results = cross_val_score(model,x,y,cv=kfold)
    results.append(cv_results)#交叉驗證給的結果分
    names.append(name)
    #模型的標準差，體現模型的波動值,std越小越穩
    msg = '%s:%f(%f)'%(name,cv_results.mean(),cv_results.std())
    print(msg)
    print('------------------')

KNN:0.698228(0.015081)
------------------
LR:0.825869(0.007094)
------------------
SVM:0.762914(0.012649)
------------------
"""
# "\nresults = []\nnames = []\nscoring = 'accuracy'#準確率\nfor name,model in models:\n    kfold = KFold(5,shuffle=True,random_state=9487)#5折\n    cv_results = cross_val_score(model,x,y,cv=kfold)\n    results.append(cv_results)#交叉驗證給的結果分\n    names.append(name)\n    #模型的標準差，體現模型的波動值,std越小越穩\n    msg = '%s:%f(%f)'%(name,cv_results.mean(),cv_results.std())\n    print(msg)\n    print('------------------')\n\nKNN:0.698228(0.015081)\n------------------\nLR:0.825869(0.007094)\n------------------\nSVM:0.762914(0.012649)\n------------------\n"

print("------------------------------")  # 30個

# 模型優化調參
# 不會調優 這里還是覺得準確率不高,我們試一下決策樹，隨機森林看看

clf = DecisionTreeClassifier(criterion="entropy")  # 實例化模型，添加criterion參數
clf = clf.fit(X_train, y_train)  # 使用實例化好的模型進行擬合操作
score = clf.score(X_test, y_test)  # 返回預測的準確度
score
# 0.7907647907647908

# 隨機森林看一下
# 初始化隨機森林
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=9487)
# 訓練模型
rf_classifier.fit(X_train, y_train)
score2 = rf_classifier.score(X_test, y_test)
score2
# 0.847041847041847

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用決策樹做客戶流失預警模型

churn = pd.read_csv("data/telecom_churn.csv", skipinitialspace=True)

# churn.iloc[3, 2] = np.nan#假設第3Row第2欄資料缺失(從0算起)

# 刪除所有 NaN 的記錄, 本例並無NaN資料
churn = churn.dropna(axis=0, how="any")  # dropna()刪除含有NaN的列
cc = churn.head()
# print("前5筆資料 :\n", cc, sep="")

print("取出資料欄位X, 後18欄位")
X = churn.loc[:, "gender":"call_10086"]
print(X.shape)
cc = X.head()
# print("前5筆資料 :\n", cc, sep="")

print("取出目標欄位y, 是否流失 0:未流失, 1:流失")
y = churn["churn"]

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

"""
分類與回歸樹（classification and regression tree，CART）是決策樹算法中的一種，
與其他決策樹算法相同，同樣由特征選擇，樹的生成與剪枝組成。
CART被廣泛應用，且被用于樹的集成模型，例如，GBDT、RF等集成算法的基學習器都是CART樹。
決策樹是典型的非線性模型，GBDT和RF因此也是非線性模型。
"""

# CART算法(分類樹)

# 建立CART模型

clf = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=100,
    min_samples_leaf=100,
    random_state=9487,
)  # 決策樹函數學習機  # 當前支持計算信息增益和GINI

clf.fit(x_train, y_train)

# 使用graphviz將樹結構輸出，在python中嵌入graphviz可參考：pygraphviz
# 存檔 sklearn.tree.export_graphviz(clf, out_file="tmp_cart1.dot") #存檔

# cart預測

# 預測 訓練資料
train_pred = clf.predict(x_train)  # 預測.predict  # 用模型預測訓練集的結果
train_pred_p = clf.predict_proba(x_train)[:, 1]  # 用模型預測訓練集的概率

# 預測 測試資料
test_pred = clf.predict(x_test)  # 預測.predict  # 用模型預測測試集的結果
test_pred_p = clf.predict_proba(x_test)[:, 1]  # 用模型預測測試集的概率

# 混淆矩陣
cm = confusion_matrix(y_test, test_pred, labels=[0, 1])
print("混淆矩陣 :\n", cm, sep="")

# 計算評估指標, 分類報告
cc = classification_report(y_test, test_pred)
print("分類報告 :\n", cc, sep="")

print("變量重要性指標 :")
print(
    pd.DataFrame(
        zip(X.columns, clf.feature_importances_), columns=["feature", "importance"]
    )
)  # 變量重要性指標

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# DT_churn_classification_model

churn = pd.read_csv("data/telecom_churn.csv")  # 讀取已經整理好的數據
cc = churn.head()
print("前5筆資料 :\n", cc, sep="")

sns.barplot(x="edu_class", y="churn", data=churn)
plt.title("教育程度 與 是否流失 的關係")
show()

sns.boxplot(x="churn", y="peakMinDiff", hue=None, data=churn)
plt.title("是否流失 與 非月峰值通話時間（分鐘） 的關係")
show()

sns.boxplot(x="churn", y="duration", hue="edu_class", data=churn)
plt.title("是否流失 與 已加入運營商的時長（月） 的關係")
show()

# 篩選變量
# 篩選變量時可以應用專業知識，選取與目標字段相關性較高的字段用于建模，也可通過分析現有數據，用統計量輔助選擇
# 為了增強模型穩定性，自變量之間最好相互獨立，可運用統計方法選擇要排除的變量或進行變量聚類

corrmatrix = churn.corr(
    method="spearman"
)  # spearman相關系數矩陣，可選pearson相關系數，目前僅支持這兩種,函數自動排除category類型

corrmatrix_new = corrmatrix[np.abs(corrmatrix) > 0.5]  # 選取相關系數絕對值大于0.5的變量，僅為了方便查看
#  為了增強模型穩定，根據上述相關性矩陣，可排除'posTrend','planChange','nrProm','curPlan'幾個變量

# 連續型變量往往是模型不穩定的原因;
# 如果所有的連續變量都分箱了,可以統一使用卡方檢驗進行變量重要性檢驗
churn["duration_bins"] = pd.qcut(churn.duration, 5)  #  將duration字段切分為數量（大致）相等的5段
churn["churn"].astype("int64").groupby(churn["duration_bins"]).agg(["count", "mean"])

bins = [0, 4, 8, 12, 22, 73]
churn["duration_bins"] = pd.cut(churn["duration"], bins, labels=False)
churn["churn"].astype("int64").groupby(churn["duration_bins"]).agg(["mean", "count"])

# 根據卡方值選擇與目標關聯較大的分類變量
# 計算卡方值需要應用到sklearn模塊，但該模塊當前版本不支持pandas的category類型變量，
# 會出現警告信息，可忽略該警告或將變量轉換為int類型

import sklearn.feature_selection as feature_selection

churn["gender"] = churn["gender"].astype("int")
churn["edu_class"] = churn["edu_class"].astype("int")
churn["feton"] = churn["feton"].astype("int")
feature_selection.chi2(
    churn[
        [
            "gender",
            "edu_class",
            "feton",
            "prom",
            "posPlanChange",
            "duration_bins",
            "curPlan",
            "call_10086",
        ]
    ],
    churn["churn"],
)  # 選取部分字段進行卡方檢驗
# 根據結果顯示，'prom'、'posPlanChange'、'curPlan'字段可以考慮排除

# 建模
# 根據數據分析結果選取建模所需字段，同時抽取一定數量的記錄作為建模數據
# 將建模數據劃分為訓練集和測試集
# 選擇模型進行建模

# 根據模型不同，對自變量類型的要求也不同，為了示例，本模型僅引入'AGE'這一個連續型變量
# model_data = churn[['subscriberID','churn','gender','edu_class','feton','duration_bins']]
model_data = churn[
    [
        "subscriberID",
        "churn",
        "gender",
        "edu_class",
        "feton",
        "duration_bins",
        "call_10086",
        "AGE",
    ]
]  # 第二可選方案

cc = model_data.head()
print("前5筆資料 :\n", cc, sep="")

y = model_data["churn"]  # 選取目標變量
X = model_data.loc[:, "gender":]  # 選取自變量

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 選擇決策樹進行建模

clf = DecisionTreeClassifier(
    criterion="entropy", max_depth=8, min_samples_split=5
)  # 決策樹函數學習機  # 當前支持計算信息增益和GINI

clf.fit(x_train, y_train)  #  使用訓練數據建模

# 預測 訓練資料
train_pred = clf.predict(x_train)  # 預測.predict  #  用模型預測訓練集的結果
train_pred_p = clf.predict_proba(x_train)[:, 1]  # 用模型預測訓練集的概率

# 預測 測試資料
test_pred = clf.predict(x_test)  # 預測.predict  #  用模型預測測試集的結果
test_pred_p = clf.predict_proba(x_test)[:, 1]  #  用模型預測測試集的概率

pd.DataFrame(
    {"y_test": y_test, "test_pred": test_pred, "test_pred_p": test_pred_p}
).T  # 查看測試集預測結果與真實結果對比

# 模型評估
# 混淆矩陣
cm = confusion_matrix(y_test, test_pred, labels=[0, 1])
print("混淆矩陣 :\n", cm, sep="")

# 計算評估指標, 分類報告
cc = classification_report(y_test, test_pred)
print("分類報告 :\n", cc, sep="")

print("變量重要性指標 :")
print(pd.DataFrame(list(zip(X.columns, clf.feature_importances_))))  # 變量重要性指標

# 察看預測值的分布情況
red, blue = sns.color_palette("Set1", 2)

sns.histplot(test_pred_p[y_test == 1], kde=False, bins=15, color=red)
plt.title("1111")
show()

sns.histplot(test_pred_p[y_test == 0], kde=False, bins=15, color=blue)
plt.title("2222")
show()

fpr_test, tpr_test, th_test = roc_curve(y_test, test_pred_p)
fpr_train, tpr_train, th_train = roc_curve(y_train, train_pred_p)
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, tpr_test, color=blue)
plt.plot(fpr_train, tpr_train, color=red)
plt.title("ROC curve 1")

show()

# 這里表現出了過渡擬合的情況
# 參數調優

param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [2, 3, 4, 5, 6, 7, 8],
    "min_samples_split": [4, 8, 12, 16, 20, 24, 28],
}
clf = DecisionTreeClassifier()  # 決策樹函數學習機

clfcv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring="roc_auc", cv=4)
clfcv.fit(x_train, y_train)

# 查看模型預測結果
train_pred = clfcv.predict(x_train)  # 預測.predict  #  用模型預測訓練集的結果
train_pred_p = clfcv.predict_proba(x_train)[:, 1]  # 用模型預測訓練集的概率
test_pred = clfcv.predict(x_test)  # 預測.predict  #  用模型預測測試集的結果
test_pred_p = clfcv.predict_proba(x_test)[:, 1]  #  用模型預測測試集的概率

fpr_test, tpr_test, th_test = roc_curve(y_test, test_pred_p)
fpr_train, tpr_train, th_train = roc_curve(y_train, train_pred_p)
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, tpr_test, color=blue)
plt.plot(fpr_train, tpr_train, color=red)
plt.title("ROC curve 2")
show()

cc = clfcv.best_params_
print(cc)

clf = DecisionTreeClassifier(
    criterion="entropy", max_depth=5, min_samples_split=24
)  # 決策樹函數學習機  # 當前支持計算信息增益和GINI

clf.fit(x_train, y_train)  #  使用訓練數據建模

# 可視化
# 使用dot文件進行決策樹可視化需要安裝一些工具：
# - 第一步是安裝[graphviz](http://www.graphviz.org/)。
#   如果是windows，就在官網下載msi文件安裝。
#   無論是linux還是windows，裝完后都要設置環境變量，將graphviz的bin目錄加到PATH，
#   比如windows，將C:/Program Files (x86)/Graphviz2.38/bin/加入了PATH
# - 第二步是安裝python插件graphviz： pip install graphviz
# - 第三步是安裝python插件pydotplus: pip install pydotplus

import pydotplus
from IPython.display import Image  # 用IPython

dot_data = sklearn.tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=x_train.columns,
    max_depth=5,
    class_names=["0", "1"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())   # 用IPython顯示圖片 skip

"""
# 模型保存/讀取
import pickle
model_file = open(r'clf.model', 'wb')
pickle.pickle.dump(clf, model_file)
model_file.close()

model_load_file = open(r'clf.model', 'rb')
model_load = pickle.pickle.load(model_load_file)
model_load_file.close()

test_pred_load = model_load.predict(x_test)  # 預測.predict
pd.crosstab(test_pred_load,test_pred)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 邏輯回歸

# subscriberID="個人客戶的ID"
# churn="是否流失：1=流失";
# Age="年齡"
# incomeCode="用戶居住區域平均收入的代碼"
# peakMinAv="統計期間內最高單月通話時長"
# peakMinDiff="統計期間結束月份與開始月份相比通話時長增加數量"
# posTrend="該用戶通話時長是否呈現出上升態勢：是=1"
# negTrend="該用戶通話時長是否呈現出下降態勢：是=1"
# nrProm="電話公司營銷的數量"
# prom="最近一個月是否被營銷過：是=1"
# curPlan="統計時間開始時套餐類型：1=最高通過200分鐘；2=300分鐘；3=350分鐘；4=500分鐘"
# avPlan="統計期間內平均套餐類型"
# planChange="統計期間是否更換過套餐：1=是"
# posPlanChange="統計期間是否提高套餐：1=是"
# negPlanChange="統計期間是否降低套餐：1=是"

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

# pd.set_option('display.max_columns', None)

# 導入數據和數據清洗

churn = pd.read_csv(r"data/telecom_churn.csv", skipinitialspace=True)
print(churn.shape)

cc = churn.head()
print("前5筆資料 :\n", cc, sep="")

# 分類變量的相關關系

# 交叉表

cross_table = pd.crosstab(churn.posTrend, churn.churn, margins=True)
cross_table

# 列聯表


def percConvert(ser):
    return ser / float(ser[-1])


cross_table.apply(percConvert, axis=1)

cc = stats.chi2_contingency(cross_table.iloc[:2, :2])
print("chisq = %6.4f\np-value = %6.4f\ndof = %i\nexpected_freq = %s" % cc, sep="")

# 邏輯回歸

churn.plot(kind="scatter", x="duration", y="churn")
plt.title("已加入運營商的時長（月） 與 是否流失 的關係")
show()

# •隨機抽樣，建立訓練集與測試集

train = churn.sample(frac=0.7, random_state=9487).copy()
test = churn[~churn.index.isin(train.index)].copy()
print(" 訓練集樣本量: %i \n 測試集樣本量: %i" % (len(train), len(test)))

lg = smf.glm(
    "churn ~ duration",
    data=train,
    family=sm.families.Binomial(sm.families.links.logit()),
).fit()
lg.summary()

# 預測
train["proba"] = lg.predict(train)  # 預測.predict
test["proba"] = lg.predict(test)  # 預測.predict

cc = test["proba"].head()
print("前5筆資料 :\n", cc, sep="")

# 模型評估
# 設定閾值

test["prediction"] = (test["proba"] > 0.3).astype("int")

# 混淆矩陣

pd.crosstab(test.churn, test.prediction, margins=True)

# 計算準確率

acc = sum(test["prediction"] == test["churn"]) / np.float(len(test))
print("The accurancy is %.2f" % acc)

for i in np.arange(0.1, 0.9, 0.1):
    prediction = (test["proba"] > i).astype("int")
    confusion_matrix = pd.crosstab(prediction, test.churn, margins=True)
    precision = confusion_matrix.loc[0, 0] / confusion_matrix.loc["All", 0]
    recall = confusion_matrix.loc[0, 0] / confusion_matrix.loc[0, "All"]
    Specificity = confusion_matrix.loc[1, 1] / confusion_matrix.loc[1, "All"]
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(
        "threshold: %s, precision: %.2f, recall:%.2f ,Specificity:%.2f , f1_score:%.2f"
        % (i, precision, recall, Specificity, f1_score)
    )


# 繪制ROC曲線

fpr_test, tpr_test, th_test = metrics.roc_curve(test.churn, test.proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train.churn, train.proba)

plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC curve")
show()

print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

# 包含分類預測變量的邏輯回歸

formula = "churn ~ C(avgplan)"

lg_m = smf.glm(
    formula=formula, data=train, family=sm.families.Binomial(sm.families.links.logit())
).fit()
lg_m.summary()


# 多元邏輯回歸
# 向前法
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float("inf"), float("inf")
    while remaining:
        aic_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response, " + ".join(selected + [candidate]))
            aic = (
                smf.glm(
                    formula=formula,
                    data=data,
                    family=sm.families.Binomial(sm.families.links.logit()),
                )
                .fit()
                .aic
            )
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = aic_with_candidates.pop()
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print("aic is {},continuing!".format(current_score))
        else:
            print("forward selection over!")
            break

    formula = "{} ~ {} ".format(response, " + ".join(selected))
    print("final formula is {}".format(formula))
    model = smf.glm(
        formula=formula,
        data=data,
        family=sm.families.Binomial(sm.families.links.logit()),
    ).fit()
    return model


candidates = [
    "churn",
    "duration",
    "AGE",
    "edu_class",
    "incomeCode",
    "feton",
    "peakMinAv",
    "peakMinDiff",
    "call_10086",
]
data_for_select = train[candidates]

lg_m1 = forward_select(data=data_for_select, response="churn")
lg_m1.summary()

# Seemingly wrong when using 'statsmmodels.stats.outliers_influence.variance_inflation_factor'


def vif(df, col_i):
    from statsmodels.formula.api import ols

    cols = list(df.columns)
    cols.remove(col_i)
    cols_noti = cols
    formula = col_i + "~" + "+".join(cols_noti)
    r2 = ols(formula, df).fit().rsquared
    return 1.0 / (1.0 - r2)


exog = train[candidates].drop(["churn"], axis=1)

for i in exog.columns:
    print(i, "\t", vif(df=exog, col_i=i))

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
