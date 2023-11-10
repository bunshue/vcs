import os
import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#6-1 探索性資料分析──以Titanic(鐵達尼號)之生還預測為例
#資料科學 0. 問個感興趣的問題

#資料科學 1. 資料取得
#資料科學1.1 自建資料或下載資料後上傳到雲端硬碟

#train.csv行資料說明.jpg
#資料科學1.2 讀取Google雲端硬碟中的csv檔
#資料科學1.3 將行列結構的資料建立為Pandas的資料框

import pandas as pd

filename = 'titanic.csv'
df = pd.read_csv(filename)

print(df)

#資料科學2. 資料處理
#資料科學2.1 由列資料了解資料集

print(df.head())

#資料科學2.2 了解行資料的標題與資料型別 ( 整數、浮點數、字串等)
#Step 01

print(df.info())

#Step 02

print(df.describe())

#資料科學2.3 資料清理
#缺失值的補值或刪除
#Step 01

print(df.isnull())

#Step 02

print(df.isnull().sum())

print(df.isnull().count())

print(df.isnull().sum()/df.isnull().count()*100)

#Step 03

df[df['Age'].isnull() == True] 

#Step 04

df['Age']=df['Age'].fillna(df['Age'].mean())

print(df)

#Step 05

df[df['Embarked'].isnull()]

#Step 06

df['Embarked'].value_counts()

#Step 07

df['Embarked']=df['Embarked'].fillna('S')

df.loc[[61,829], :] #顯示列索引61,829的資料

#Step 08

print(df.info())

df=df.drop('Cabin', axis=1)

print(df.info())

#刪除重複值或異常值
df[df.duplicated()]  

#資料轉換
print(df.head()) 

s={'female':0, 'male':1}
df['Sex']=df['Sex'].map(s)
e={'S':0, 'C':1, 'Q':2}
df['Embarked']=df['Embarked'].map(e)
print(df.head())

#資料科學3. 探索性資料分析
#資料科學3.1 觀察資料的分佈(統計)

print(df.head())

#資料科學3.2 資料視覺化
#1.全體乘客生還、死亡的比例

print(df['Survived'].value_counts())

df['Survived'].value_counts().plot(kind='pie',autopct='%1.2f%%')
plt.show()

print('------------------------------------------------------------')	#60個

#2.男性、女性乘客的比例

print(df['Sex'].value_counts())

df['Sex'].value_counts().plot(kind='pie',autopct='%1.2f%%')
plt.show()

print('------------------------------------------------------------')	#60個

#3.搭1等艙、2等艙、3等艙的乘客比例

print(df['Pclass'].value_counts())

df['Pclass'].value_counts().plot(kind='pie',autopct='%1.2f%%')
plt.show()

print('------------------------------------------------------------')	#60個

#4.進一步探討性別與生還的關係

#女、男乘客的人數

print(df.groupby(['Sex'])['PassengerId'].count())

#不同性別的生還和死亡人數

print(df.groupby(['Sex','Survived'])['PassengerId'].count())

df.groupby(['Sex','Survived'])['PassengerId'].count().plot(kind='bar', rot=1)
plt.show()

print('------------------------------------------------------------')	#60個

#不同性別生還人數/不同性別人數

ss = df.groupby(['Sex','Survived'])['PassengerId'].count() / df.groupby(['Sex'])['PassengerId'].count()  * 100 
print(ss)

ss.plot(kind='bar', color=['r','g'], rot=0)
plt.show()

print('------------------------------------------------------------')	#60個

#5.進一步探討艙等與生還的關係

#三種艙等的生還和死亡人數

print(df.groupby(['Pclass','Survived'])['PassengerId'].count())

df.groupby(['Pclass','Survived'])['PassengerId'].count().plot(kind='bar', rot=0)
plt.show()

print('------------------------------------------------------------')	#60個

#不同艙等生還人數/不同艙等人數

ps = df.groupby(['Pclass','Survived'])['PassengerId'].count() / df.groupby(['Pclass'])['PassengerId'].count()  * 100 
print(ps)

ps.plot(kind='bar', rot=0)
plt.show()

print('------------------------------------------------------------')	#60個

#6-2 探索性資料分析──以 Iris 的花種分類為例
#資料科學0. 感興趣的問題

#資料科學1. 資料取得
#資料科學1.1 自建資料或從網路下載資料後上傳到雲端硬碟

#Iris.jpg
#資料科學1.2 讀取Google雲端硬碟中的csv檔
#資料科學1.3 將行列結構的資料建立為Pandas的資料框

import pandas as pd

filename = 'Iris.csv'
df = pd.read_csv(filename)
print(df)

df=df.drop('Id', axis=1)
print(df.head())

#資料科學2. 資料處理
#資料科學2.1 由列資料了解資料集

print(df.head())

#資料科學2.2 了解行資料的標題與資料型別(整數、浮點數、字串等)

print(df.info())

#資料科學2.3 資料清理

#缺失值的補值或刪除

print(df.info())

#刪除重複值或異常值

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df[df.duplicated()])

df.reset_index(drop=True) #將列索引重新編號

#資料轉換

s = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2 }
df['Species']=df['Species'].map(s)
print(df.head())

#資料科學3. 探索性資料分析
#資料科學3.1 觀察資料的分佈(統計)
print(df.head())

#資料科學3.2 資料視覺化
#Step 01

c = {0:'r', 1:'g', 2:'b'}
df['colors'] = df['Species'].map(c)
print(df)

#Step 02
df.plot(kind='scatter', x='SepalLengthCm', y='Species', c=df['colors'])
plt.show()

print('------------------------------------------------------------')	#60個

#(圖)-不同欄位和「類別(Species)」所繪製的散佈圖
#(a)花萼長度
df.plot(kind='scatter', x='SepalLengthCm', y='Species', c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(b)花萼寬度
df.plot(kind='scatter', x='SepalWidthCm', y='Species', c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(c)花瓣長度
df.plot(kind='scatter', x='PetalLengthCm', y='Species', c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(d)花瓣寬度
df.plot(kind='scatter', x='PetalWidthCm', y='Species', c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(圖)-2個欄位組合所繪製的散佈圖
#(a)花萼長度 vs. 花萼寬度
df.plot(kind='scatter', x='SepalLengthCm',y='SepalWidthCm',c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(b)花瓣長度 vs. 花瓣寬度
df.plot(kind='scatter', x='PetalLengthCm',y='PetalWidthCm',c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(c)花萼長度 vs. 花瓣寬度
df.plot(kind='scatter', x='SepalLengthCm',y='PetalWidthCm',c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(d)花瓣長度 vs. 花萼寬度
df.plot(kind='scatter', x='PetalLengthCm',y='SepalWidthCm',c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(e)花萼長度 vs. 花瓣長度
df.plot(kind='scatter', x='SepalLengthCm',y='PetalLengthCm',c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

#(f)花萼寬度 vs. 花瓣寬度
df.plot(kind='scatter', x='SepalWidthCm',y='PetalWidthCm',c=df['colors']) 
plt.show()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('作業完成')

