import pandas as pd
import numpy as np

titanic = pd.read_csv("titanic_data.csv")
print("---檢查PassengerId欄位是否是唯一值---")
# 檢查PassengerId欄位是否是唯一值
print(np.unique(titanic["PassengerId"].values).size)
print("---指定DataFrame物件的索引欄位---")
# 指定DataFrame物件的索引欄位
titanic.set_index(["PassengerId"], inplace=True)
print(titanic.head())
titanic.head().to_html("ch13-5b-01.html")
print("---新增SexCode欄位---")
# 新增SexCode欄位
titanic["SexCode"] = np.where(titanic["Sex"]=="female", 1, 0)
print(titanic.head())
titanic.head().to_html("ch13-5b-02.html")
print("---PCass欄位轉換成數值資料---")
# PCass欄位轉換成數值資料
class_mapping = {"1st": 1,
                 "2nd": 2,
                 "3rd": 3}
titanic["PClass"] = titanic["PClass"].map(class_mapping)
print(titanic.head())
titanic.head().to_html("ch13-5b-03.html")
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
titanic.to_csv("titanic_pre.csv", encoding="utf8")
print("Title人數:")
print(titanic["Title"].groupby(titanic["Title"]).size())
print("---顯示平均生存率---")
print("平均生存率:")
print(titanic[["Title","Survived"]].groupby(titanic["Title"]).mean())



