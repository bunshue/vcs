'''
使用pandas讀取csv檔, 讀成 DataFrame 格式
'''

import pandas as pd

print('------------------------------------------------------------')	#60個

filename = 'data/missing_data.csv'
df = pd.read_csv(filename)

print('原資料\n', df, '\n')

print('資料結構訊息', df.info(), '\n')

df1 = df.dropna()
print('清除NA\n', df1, '\n')

df2 = df.dropna(how="any")
print(df2)
print()

df3 = df.dropna(subset=["B", "C"])
print(df3)
print()

df4 = df.fillna(value=1)
print(df4)
print()

df["B"] = df["B"].fillna(df["B"].mean())
print(df)
print()

print('------------------------------------------------------------')	#60個

filename = 'data/duplicated_data.csv'
df = pd.read_csv(filename)

print('原資料\n', df, '\n')

print(df.duplicated())
print()

print(df.duplicated("B"))
print()

df1 = df.drop_duplicates()
print(df1)
print()

df2 = df.drop_duplicates("B")
print(df2)
print()

df3 = df.drop_duplicates("B", keep=False)
print(df3)
print()

print('------------------------------------------------------------')	#60個

filename = 'data/labelencoder_data.csv'
df = pd.read_csv(filename)

print('原資料\n', df, '\n')

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
print(df)

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 載入資料集

# 鐵達尼號資料集是一個CSV檔案：titanic_data.csv，我們可以建立DataFrame物件來載入資料集，如下所示：

'''
資料前處理

在檢視資料集的描述資料後，我們知道目前需要處理的工作，如下所示：

    PassengerId欄位是否是流水號，如果是，我們可以將此欄位改為索引欄位。
    Sex欄位需要處理分類資料轉換成數值的0和1（1是女；0是男）。
    PClass欄位需要處理分類資料轉換成數值的1、2和3（1是1st；2是2nd；3是3rd）。
    Age欄位有很多遺漏值，我們準備使用Age欄位的平均值來補值。

'''
filename = 'data/titanic_data.csv'
titanic = pd.read_csv(filename)

print('資料shape')
print(titanic.shape)
print()

print('資料')
print(titanic)
print()

print('資料.head()')
print(titanic.head())
print()


print('size')
print(np.unique(titanic["PassengerId"].values).size)
print()


titanic.set_index(["PassengerId"], inplace=True)
print(titanic.head())
print()

titanic["SexCode"] = np.where(titanic["Sex"]=="female", 1, 0)
print(titanic.head())
print()

print('------------------------------------------------------------')	#60個

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
titanic["PClass"] = label_encoder.fit_transform(titanic["PClass"])
print(titanic.head())

print('isnull().sum()')
print(titanic.isnull().sum())


print('age.isnull()')
print(sum(titanic["Age"].isnull()))

avg_age = titanic["Age"].mean()
print('average age =', avg_age)

titanic["Age"].fillna(avg_age, inplace=True)
print(sum(titanic["Age"].isnull()))

print('1111')
print(titanic["Sex"].groupby(titanic["Sex"]).size())

print('2222')
print(titanic.groupby("Sex")["Age"].mean())

print('------------------------------------------------------------')	#60個

#探索性資料分析

print('3333')
titanic["Died"] = np.where(titanic["Survived"]==0, 1, 0)
print(titanic.head())

titanic["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 0]
df["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 1]
df["Age"].plot(kind="hist", bins=15)

plt.show()

print('------------------------------------------------------------')	#60個

fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived","Died"]].groupby(titanic["Sex"]).sum()
df.plot(kind="bar", ax=axes[0])
df = titanic[["Survived","Died"]].groupby(titanic["Sex"]).mean()
df.plot(kind="bar", ax=axes[1])

plt.show()

print('------------------------------------------------------------')	#60個

df = titanic[['Survived',"Died"]].groupby(titanic["PClass"]).sum()
df.plot(kind="bar")

plt.show()

print('------------------------------------------------------------')	#60個

df = titanic[['Survived',"Died"]].groupby(titanic["PClass"]).mean()
df.plot(kind="bar")

plt.show()

print('------------------------------------------------------------')	#60個

df = titanic.drop("Died", axis=1)
print('係數矩陣 :', df.corr())

plt.show()

print('------------------------------------------------------------')	#60個

'''

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示



plt.show()
'''






