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

hours_phone_used = [0,0,0,1,1.3,1.5,2,2.2,2.6,3.2,4.1,4.4,4.4,5]
work_performance = [87,89,91,90,82,80,78,81,76,85,80,75,73,72]

df = pd.DataFrame({"手機使用時間(小時)":hours_phone_used,
                   "工作效率":work_performance})

df.plot(kind="scatter", x="手機使用時間(小時)", y="工作效率")
plt.title("手機使用時數與工作效率")
plt.show()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

hours_phone_used = [0,0,0,1,1.3,1.5,2,2.2,2.6,3.2,4.1,4.4,4.4,5]
work_performance = [87,89,91,90,82,80,78,81,76,85,80,75,73,72]

x = np.array(hours_phone_used)
y = np.array(work_performance)
n = len(x)
x_mean = x.mean()
y_mean = y.mean()

diff = (x-x_mean)*(y-y_mean)
covar = diff.sum()/n
print("共變異數:", covar)

corr = covar/(x.std()*y.std())
print("相關係數:", corr)
print("------------------------------")  # 30個

df = pd.DataFrame({"手機使用時間(小時)":hours_phone_used,
                   "工作效率":work_performance})
print(df.corr())

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

df = pd.read_csv("test.csv")
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

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test.csv")
# 填補遺失資料
df1 = df.fillna(value=1)
print(df1)

print("------------------------------")  # 30個

df["B"] = df["B"].fillna(df["B"].mean())
print(df)

print("------------------------------")  # 30個

df["C"] = df["C"].fillna(df["C"].median())
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test.csv")
# 建立布林遮罩
df1 = pd.isnull(df)
print(df1)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test2.csv")
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test2.csv")
print(df.duplicated())

print("------------------------------")  # 30個

print(df.duplicated("B"))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test2.csv")

df1 = df.drop_duplicates()
print(df1)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test2.csv")

df1 = df.drop_duplicates("B")
print(df1)

print("------------------------------")  # 30個

df2 = df.drop_duplicates("B", keep="last")
print(df2)

print("------------------------------")  # 30個

df3 = df.drop_duplicates("B", keep=False)
print(df3)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test3.csv")
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

from sklearn import preprocessing

df = pd.read_csv("test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)

print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("titanic_data.csv")
# 顯示資料集的形狀
print(titanic.shape)

print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("titanic_data.csv")
# 顯示前5筆
print(titanic.head())

print("------------------------------")  # 30個

# 顯示統計摘要資訊
print(titanic.describe())

print("------------------------------")  # 30個

# 顯示資料集資訊
print(titanic.info())

print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("titanic_data.csv")
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
print("平均生存率:")
print(titanic[["Title","Survived"]].groupby(titanic["Title"]).mean())

print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("titanic_pre.csv")
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
print(df.corr())
df.to_csv("tmp_titanic_train.csv", encoding="utf8")

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

df = pd.read_csv("test.csv")
print(df)
df.to_html("ch13-3-1.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("test.csv")
print(df)

print("------------------------------")  # 30個

df.info()

print("------------------------------------------------------------")  # 60個



df.corr().to_html("ch13-1-3.html")

