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


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#9-1 機器學習前準備─以Iris為例

#1. 資料取得

filename = 'Iris.csv'

import pandas as pd

df=pd.read_csv(filename)

df=df.drop('Id', axis=1)

print(df.head())

#2. 資料處理

df.info()

df = df.drop_duplicates() #刪除重複列
df.reset_index(drop=True) #將列索引重新編號
s = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2 }
df['Species']=df['Species'].map(s)
df.info()

#3. 探索性資料分析
print(df.head())
"""
#4. 機器學習做資料分析
9-2 機器學習實作──以Iris為例
9-2-1 提出具體的假設
9-2-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

#學習訓練：建立並訓練 KNN 模型

df_X = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
df_y = df['Species']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size = 0.2)

k = 1
knn=KNeighborsClassifier(n_neighbors=k)  #建立新模型 knn

knn.fit(X_train, y_train)  # 用 training data 去訓練模型

#測試評估

print('----KNN模式訓練後，取test data 進行分類的正確率計算-------')

print('準確率:',knn.score(X_test,y_test))



s = []
for i in range(3,11):
  k=i
  knn=KNeighborsClassifier(n_neighbors=k)  
  knn.fit(X_train, y_train)  # 用 training data 去訓練模型
  print('k =',k,' 準確率:',knn.score(X_test,y_test)) #用 test data 檢測模型的準確率
  s.append(knn.score(X_test,y_test))

k = 8
knn=KNeighborsClassifier(n_neighbors=k)  
knn.fit(X_train, y_train)

#加廣知識：視覺化圖表來顯示準確率

df_knn = pd.DataFrame()
df_knn['s'] = s
df_knn.index = [3,4,5,6,7,8,9,10]  
df_knn.plot(grid=True)

plt.show()

print('分類的預測結果：')
pred = knn.predict(X_test) #產生Test data預測結果
print(pred)

print(y_test.values) #觀察Test data真實數據

#加廣知識：利用values屬性做橫式顯示

print(y_test)

print(y_test.values)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)

#1.0

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, pred)

#加深知識：交叉驗證概念

from sklearn.model_selection import cross_val_score
s = cross_val_score(knn, df_X, df_y, scoring='accuracy', cv=10)
print('交叉驗證每次的準確率：',s)
print('交叉驗證得到的平均準確率：',s.mean())

#決定模型
#進行分類預測

new = [[6.6,3.1,5.2,2.4]]
v=knn.predict(new)
if v==0:
  s='Iris-Setosa'
elif v==1:
  s='Iris-Versicolour'
elif v==2:
  s='Iris-Virginica'
else:
  s='錯誤'
print('預測結果為：', s)    

#預測結果為： 錯誤

#9-3 機器學習前準備─以Titanic為例

#1. 資料取得

import pandas as pd
filename = 'titanic.csv'
df = pd.read_csv(filename)
print(df.head())

#2. 資料處理
df.info()

df['Age']=df['Age'].fillna(df['Age'].mean()) 
df['Embarked']=df['Embarked'].fillna('S') 
df=df.drop('Cabin', axis=1) 
print('重複值：', df[df.duplicated()]) #檢查有無重複值

df['Sex']=df['Sex'].map({'female':0, 'male':1}) 
df['Embarked']=df['Embarked'].map({'S':0, 'C':1, 'Q':2}) 
print(df.head())

#重複值： Empty DataFrame


#3. 探索性資料分析

print(df.head())

"""
4. 機器學習做資料分析
9-4 機器學習實作─以Titanic為例
9-4-1 提出具體的假設
9-4-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

#學習訓練：建立並訓練 KNN 模型

df_X = df[['Sex','Pclass']]
df_y = df['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size = 0.2)

k = 1
knn=KNeighborsClassifier(n_neighbors=k)  

knn.fit(X_train, y_train)  

#測試評估

print('----KNN模式訓練後，取test data 進行分類的準確率計算-------')
print('準確率:',knn.score(X_test,y_test))

s = []
for i in range(3,11):
  k=i
  knn=KNeighborsClassifier(n_neighbors=k)  
  knn.fit(X_train, y_train)  # 用 training data 去訓練模型
  print('k =',k,' 準確率:',knn.score(X_test,y_test))  #用 test data 檢測模型的準確率
  s.append(knn.score(X_test,y_test))

k = 4
knn=KNeighborsClassifier(n_neighbors=k)  
knn.fit(X_train, y_train)

print('分類的預測結果：')
pred = knn.predict(X_test) 
print(pred) #觀察預測結果

print('真實數據：')
print(y_test.values)  #觀察真實數據(Test data)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)

#0.7541899441340782

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, pred)

from sklearn.model_selection import cross_val_score
s = cross_val_score(knn, df_X, df_y, scoring='accuracy', cv=10)
print('準確率：',s)
print('平均準確率：',s.mean())
print('最高：',s.max())
print('最差：',s.min())

#決定模型
#進行分類預測

print('-----------(1)電影中兩位主角的生還推測-------------')

Rose=[[0,1]] #女性 頭等艙 蘿絲（Rose DeWitt Bukater）
Jack=[[1,3]] #男性 三等艙 傑克（Jack Dawson）
v=knn.predict(Rose)
if v==1:
  s='生還'
else:
  s='死亡'
print('Rose能生還嗎 ? ', s)           #Rose為女性,及坐頭等艙

v=knn.predict(Jack)
if v==1:
  s='生還'
else:
  s='死亡'

print('Jack能生還嗎 ? ', s)           #Jack為男性,及坐三等艙


# 真實的伊西多和伊達·斯特勞斯（Isidor and Ida Straus）夫婦 (You stay, I stay)
# http://www.epochtimes.com/b5/17/12/6/n9931745.htm
# Isidor 美國梅西百貨創辦人之一 

print('-----(2)真實的伊西多和伊達·斯特勞斯夫婦的生還推測-------')
Mrs=[[0,1]]    #女性 頭等艙 Straus, Mrs. Isidor (Rosalie Ida Blun)
Mr=[[1,1]] #男性 頭等艙 Straus, Mr. Isidor
v=knn.predict(Mrs)
if v==1:
  s='生還'
else:
  s='死亡'
print('Mrs. Straus能生還嗎 ? ', s)      #Ida為女性,及坐頭等艙，可優先搭乘救生艇存活

v=knn.predict(Mr)                  #Isidor的生存率有多高呢？
if v==1:
  s='生還'
else:
  s='死亡'
print('Mr. Straus能生還嗎 ? ', s) 

# 真實的 Mrs. Brown
# https://hokkfabrica.com/her-story-margaret-brown-from-titanic/
#

print('-----------(3)真實的Mrs. Brown的生還推測-------------')

#女性 頭等艙 Brown, Mrs. James Joseph (Margaret Tobin) 故事中的暴發戶 對Jack很友善
Brown=[[0,1]]    
v=knn.predict(Brown)                     #Mrs. Brown呢？
if v==1:
  s='生還'
else:
  s='死亡'
print('Mrs. Brown能生還嗎 ? ', s)

print('-------------- (5)若你也搭上了鐵達尼號呢？ ----------------')

#s=input('您的性別（0：女，1：男），請輸入代碼？ ')
s = 1
#c=input('搭乘的船艙艙等（1：S艙，2：C艙，3：Q艙），請輸入代碼？ ')
c = 3
you=[[int(s),int(c)]]
v=knn.predict(you)
if v==1:
  print('預測為:幸運生還')
else:
  print('預測為:無法生還')

print('------------------------------------------------------------')	#60個

print('作業完成')

print('------------------------------------------------------------')	#60個


