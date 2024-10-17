"""
Python資料科學實戰教本



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
'''
hours_phone_used = [0,0,0,1,1.3,1.5,2,2.2,2.6,3.2,4.1,4.4,4.4,5]
work_performance = [87,89,91,90,82,80,78,81,76,85,80,75,73,72]

x = np.array(hours_phone_used)
y = np.array(work_performance)
n = len(x)
x_mean = x.mean()
y_mean = y.mean()
print("資料數:", n)
print("x平均:", x_mean)
print("y平均:", y_mean)

diff = (x-x_mean)*(y-y_mean)
print("x偏差*y編差和:", diff.sum())
covar = diff.sum()/n
print("共變異數:", covar)

corr = covar/(x.std()*y.std())
print("相關係數:", corr)

print("------------------------------")  # 30個

df = pd.DataFrame({"手機使用時間(小時)":hours_phone_used,
                   "工作效率":work_performance})

print('用pd算相關係數')
print("相關係數:", df.corr())

df.plot(kind="scatter", x="手機使用時間(小時)", y="工作效率")
plt.title("手機使用時數與工作效率")
plt.show()

import seaborn as sns  # 海生, 自動把圖畫得比較好看

sns.heatmap(df.corr(),linewidths=0.1,vmax=1.0, square=True,linecolor='white', annot=True)
plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data2/test.csv")
print(df)

cc = df.info()
print(cc)

df.corr().to_html("test_csv_corr2html.html")

df.to_html("test_csv2html.html")

# 刪除所有 NaN 的記錄
df1 = df.dropna()
print(df1)

print("------------------------------")  # 30個

df2 = df.dropna(how="any")
print(df2)

print("------------------------------")  # 30個

df3 = df.dropna(how="all")
print(df3)

print("------------------------------")  # 30個

df4 = df.dropna(subset=["B", "C"])
print(df4)

print("------------------------------")  # 30個

# 填補遺失資料
df5 = df.fillna(value=1)
print(df5)

print("------------------------------")  # 30個

# 建立布林遮罩
df6 = pd.isnull(df)
print(df6)

print("------------------------------")  # 30個


df["B"] = df["B"].fillna(df["B"].mean())
print(df)

print("------------------------------")  # 30個

df["C"] = df["C"].fillna(df["C"].median())
print(df)

sys.exit()
5
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data2/test2.csv")
print(df)

print(df.duplicated())

df1 = df.drop_duplicates()
print(df1)

print(df.duplicated("B"))

df1 = df.drop_duplicates("B")
print(df1)

df2 = df.drop_duplicates("B", keep="last")
print(df2)

df3 = df.drop_duplicates("B", keep=False)
print(df3)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data2/test3.csv")
print(df)

print("------------------------------")  # 30個

size_mapping = {"XXL": 5,
                "XL": 4,
                "L": 3,
                "M": 2,
                "S": 1,
                "XS": 0}

df["尺寸"] = df["尺寸"].map(size_mapping)
print(df)

print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("data2/titanic_data.csv")
# 顯示資料集的形狀
print(titanic.shape)

# 顯示前5筆
print(titanic.head())

# 顯示統計摘要資訊
print(titanic.describe())

# 顯示資料集資訊
print(titanic.info())

print("---檢查PassengerId欄位是否是唯一值---")
# 檢查PassengerId欄位是否是唯一值
print(np.unique(titanic["PassengerId"].values).size)
print("---指定DataFrame物件的索引欄位---")
# 指定DataFrame物件的索引欄位
titanic.set_index(["PassengerId"], inplace=True)
print(titanic.head())

print("---新增SexCode欄位---")
# 新增SexCode欄位
titanic["SexCode"] = np.where(titanic["Sex"]=="female", 1, 0)
print(titanic.head())

print("---PCass欄位轉換成數值資料---")
# PCass欄位轉換成數值資料
class_mapping = {"1st": 1,
                 "2nd": 2,
                 "3rd": 3}
titanic["PClass"] = titanic["PClass"].map(class_mapping)
print(titanic.head())

print("---檢查Age欄位的遺漏值有多少---")
# 檢查Age欄位的遺漏值有多少
print(titanic.isnull().sum())
print(sum(titanic["Age"].isnull()))
print("---補值成平均值---")
# 補值成平均值
avg_age = titanic["Age"].mean()
titanic["Age"].fillna(avg_age, inplace=True)
print(sum(titanic["Age"].isnull()))
print("---顯示性別人數和計算平均年齡---")
# 顯示性別人數和計算平均年齡
print("性別人數:")
print(titanic["Sex"].groupby(titanic["Sex"]).size())
print(titanic.groupby("Sex")["Age"].mean())
print("---處理姓名欄位---")
# 處理姓名欄位
import re
patt = re.compile(r"\,\s(\S+\s)") 
titles = []
for index, row in titanic.iterrows():
    m = re.search(patt, row["Name"])
    if m is None:
        title = "Mrs" if row["SexCode"] == 1 else "Mr"
    else:
        title = m.group(0)
        title = re.sub(r",", "", title).strip()
        if title[0] != "M":
            title = "Mrs" if row["SexCode"] == 1 else "Mr"
        else:
           if title[0] == "M" and title[1] == "a":
            title = "Mrs" if row["SexCode"] == 1 else "Mr"
    titles.append(title)
titanic["Title"] = titles

print("Title類別:")
print(np.unique(titles).shape[0], np.unique(titles))
print("---修正類別錯誤顯示Titel人數---")
# 修正類別錯誤
titanic["Title"] = titanic["Title"].replace("Mlle","Miss")
titanic["Title"] = titanic["Title"].replace("Ms","Miss")  
titanic.to_csv("tmp_titanic_pre.csv", encoding="utf8")
print("Title人數:")
print(titanic["Title"].groupby(titanic["Title"]).size())
print("---顯示平均生存率---")
""" NG
print("平均生存率:")
print(titanic[["Title","Survived"]].groupby(titanic["Title"]).mean())
"""
print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("data2/titanic_pre.csv")
titanic["Died"] = np.where(titanic["Survived"]==0, 1, 0)
print(titanic.head())

print("------------------------------")  # 30個

# 繪出直方圖的年齡分佈, 生存或死亡
titanic["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 0]
df["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 1]
df["Age"].plot(kind="hist", bins=15)
# 分類顯示Title欄位的生存和死亡數
fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived","Died"]].groupby(titanic["Title"]).sum()
df.plot(kind="bar", ax=axes[0])
df = titanic[["Survived","Died"]].groupby(titanic["Title"]).mean()
df.plot(kind="bar", ax=axes[1])
# 分類顯示Sex欄位的生存和死亡數
fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived","Died"]].groupby(titanic["Sex"]).sum()
df.plot(kind="bar", ax=axes[0])
df = titanic[["Survived","Died"]].groupby(titanic["Sex"]).mean()
df.plot(kind="bar", ax=axes[1])
# 分類顯示PClass欄位的生存和死亡數
df = titanic[['Survived',"Died"]].groupby(titanic["PClass"]).sum()
df.plot(kind="bar")
df = titanic[['Survived',"Died"]].groupby(titanic["PClass"]).mean()
df.plot(kind="bar")
# 計算相關係數
df = titanic.drop("PassengerId", axis=1)
df = df.drop("Died", axis=1)
df = df.drop("Title", axis=1)
#print(df.corr()) NG
df.to_csv("tmp_titanic_train.csv", encoding="utf8")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

f_tracking= [110, 1018, 1130, 417, 626,
             957, 90, 951, 946, 797,
             981, 125, 456, 731, 1640,
             486, 1309, 472, 1133, 1773,
             906, 532, 742, 621, 855]
happiness = [0.3, 0.8, 0.5, 0.4, 0.6,
             0.4, 0.7, 0.5, 0.4, 0.3, 
             0.3, 0.6, 0.2, 0.8, 1,
             0.6, 0.2, 0.7, 0.5, 0.7,
             0.1, 0.4, 0.3, 0.6, 0.3]

df = pd.DataFrame({"FB追蹤數" : f_tracking,
                   "快樂程度" : happiness})
print(df.head())

print("------------------------------")  # 30個

df_scaled = pd.DataFrame(preprocessing.scale(df), 
            columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_scaled.head())

df_scaled.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")
plt.show()

print("------------------------------")  # 30個

from sklearn import preprocessing

f_tracking= [110, 1018, 1130, 417, 626,
             957, 90, 951, 946, 797,
             981, 125, 456, 731, 1640,
             486, 1309, 472, 1133, 1773,
             906, 532, 742, 621, 855]
happiness = [0.3, 0.8, 0.5, 0.4, 0.6,
             0.4, 0.7, 0.5, 0.4, 0.3, 
             0.3, 0.6, 0.2, 0.8, 1,
             0.6, 0.2, 0.7, 0.5, 0.7,
             0.1, 0.4, 0.3, 0.6, 0.3]

df = pd.DataFrame({"FB追蹤數" : f_tracking,
                   "快樂程度" : happiness})
print(df.head())

print("------------------------------")  # 30個

scaler = preprocessing.StandardScaler()
np_std = scaler.fit_transform(df)
df_std = pd.DataFrame(np_std,
         columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_std.head())

df_std.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

f_tracking= [110, 1018, 1130, 417, 626,
             957, 90, 951, 946, 797,
             981, 125, 456, 731, 1640,
             486, 1309, 472, 1133, 1773,
             906, 532, 742, 621, 855]
happiness = [0.3, 0.8, 0.5, 0.4, 0.6,
             0.4, 0.7, 0.5, 0.4, 0.3, 
             0.3, 0.6, 0.2, 0.8, 1,
             0.6, 0.2, 0.7, 0.5, 0.7,
             0.1, 0.4, 0.3, 0.6, 0.3]

df = pd.DataFrame({"FB追蹤數" : f_tracking,
                   "快樂程度" : happiness})
print(df.head())
print("------------------------------")  # 30個

df_scaled = pd.DataFrame(preprocessing.scale(df), 
            columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_scaled.head())
df_scaled.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")

print("------------------------------")  # 30個

scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
np_minmax = scaler.fit_transform(df)
df_minmax = pd.DataFrame(np_minmax,
            columns=["最小最大值縮放FB追蹤數", "最小最大值縮放快樂程度"])
print(df_minmax.head())

df_minmax.plot(kind="scatter", x="最小最大值縮放FB追蹤數",
               y="最小最大值縮放快樂程度")
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

df = pd.read_csv("data2/test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)

print("------------------------------------------------------------")  # 60個

"""
数据相关性分析中，经常用到data.corr()函数，data.corr()表示了data中的两个变量之间的相关性，取值范围为[-1,1],取值接近-1，表示反相关，类似反比例函数，取值接近1，表正相关。
DataFrame.corr()函数使用说明如下：

DataFrame.corr(method='pearson', min_periods=1)

参数说明：
method：可选值为{‘pearson’, ‘kendall’, ‘spearman’}
pearson：Pearson相关系数来衡量两个数据集合是否在一条线上面，即针对线性数据的相关系数计算，针对非线性                                           数据便会有误差。
kendall：用于反映分类变量相关性的指标，即针对无序序列的相关系数，非正太分布的数据
spearman：非线性的，非正太分析的数据的相关系数
min_periods：样本最少的数据量
返回值：各类型之间的相关系数DataFrame表格。
"""
import seaborn as sns  # 海生, 自動把圖畫得比較好看
import numpy as np

df = pd.DataFrame([[1,6,7,5,1],[2,10,8,3,4],[3,4,0,10,2]],columns=['val1','val2','val3','val4','val5'])
print(df)


#5个变量的数据如表所示
#各变量数据相关性的热力图

sns.heatmap(df.corr(),linewidths=0.1,vmax=1.0, square=True,linecolor='white', annot=True)
plt.show()

#从图中可以看出，val2和val3的相关性最高为0.83，其次是val2和val5。
'''
print("------------------------------------------------------------")  # 60個

"""
pandas相关系数-DataFrame.corr()参数详解

DataFrame.corr(method='pearson', min_periods=1)

参数说明：
method：可选值为{‘pearson’, ‘kendall’, ‘spearman’}
               pearson：Pearson相关系数来衡量两个数据集合是否在一条线上面，即针对线性数据的相关系数计算，针对非线性数据便会有误差。
                kendall：用于反映分类变量相关性的指标，即针对无序序列的相关系数，非正太分布的数据
                spearman：非线性的，非正太分布的数据的相关系数
min_periods：样本最少的数据量

返回值：各类型之间的相关系数DataFrame表格。
"""

import seaborn as sns  # 海生, 自動把圖畫得比較好看

x = [a for a in range(11)]


def y1_x(x):
    return x * 2


def y2_x(x):
    return x**2 // 4


def y3_x(x):
    return (x - 5) ** 2


def y4_x(x):
    return 10 - x


y1 = [y1_x(i) for i in x]
y2 = [y2_x(i) for i in x]
y3 = [y3_x(i) for i in x]
y4 = [y4_x(i) for i in x]

print("x :", x)
print("y1 :", y1)
print("y2 :", y2)
print("y3 :", y3)
print("y4 :", y4)

df = pd.DataFrame({"x": x, "y1": y1, "y2": y2, "y3": y3, "y4": y4})
print(df)
print(df.columns)

columns = ["x", "2倍", "平方除4", "(減5)平方", "10-x"]
df.columns = columns

df.plot(kind="line", legend=True, title="線圖", figsize=[10, 5])

cc = df.head()
print(cc)

cc = df.corr()
print(cc)

plt.figure(figsize=(12, 8))
plt.subplot(221)
sns.heatmap(cc, annot=True, cmap="coolwarm")

cc = df.corr(method="spearman")
print(cc)
plt.subplot(222)
sns.heatmap(cc, annot=True, cmap="coolwarm")

cc = df.corr(method="kendall")
print(cc)
plt.subplot(223)
sns.heatmap(cc, annot=True, cmap="coolwarm")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
