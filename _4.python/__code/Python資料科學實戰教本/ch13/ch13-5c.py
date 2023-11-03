import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic_pre.csv")
titanic["Died"] = np.where(titanic["Survived"]==0, 1, 0)
print(titanic.head())
titanic.head().to_html("ch13-5c-01.html")
print("---------------------------")
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
df.to_csv("titanic_train.csv", encoding="utf8")
df.corr().to_html("ch13-5c-02.html")
plt.show()