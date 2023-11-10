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


#10-1 機器學習前準備
#1. 資料取得

import pandas as pd

filename = 'Iris.csv'
df=pd.read_csv(filename)

df=df.drop('Id', axis=1)

print(df.head())

#2. 資料處理

print(df.info())

df = df.drop_duplicates() #刪除重複列

df.reset_index(drop=True) #將列索引重新編號

s = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2 }

df['Species']=df['Species'].map(s)

print(df.info())

#3. 探索性資料分析
print(df.head())

#4. 機器學習做資料分析
#10-2 機器學習實作
#挑選模型：匯入 K- 平均法模型

from sklearn.cluster import KMeans
#學習訓練：建立並訓練 K-平均法模型

df_X = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
k = 1
km = KMeans(n_clusters = k)   
km.fit(df_X)         

#測試評估

print('分群準確性:',km.inertia_)

#分群準確性: 663.895238095238

s = []
for k in range(1,15):
    km = KMeans(n_clusters=k)
    km.fit(df_X)
    s.append(km.inertia_)

print(s)

#[663.895238095238, 151.77145833333336, 77.91989035087718, 56.64237065018315, 45.816421929824564, 38.380978808131445, 34.1150969785575, 29.771330051212402, 27.730401211361738, 25.771261585636587, 24.236889472455648, 22.68941452991453, 21.258278047116285, 19.7686452991453]

# 看視覺化圖表決定參數K值
df_kmeans = pd.DataFrame()
df_kmeans['inertia_'] = s
df_kmeans.index = list(range(1,15))   
df_kmeans.plot(grid=True)
plt.show()

k=3                      
km=KMeans(n_clusters=k)  
km.fit(df_X)

print('分群的預測結果：')
pred = km.fit_predict(df_X) 
print(pred)

#決定模型
#進行分群預測

df1 = df_X.copy()
df1['pred'] = pred

c = {0:'r', 1:'g', 2:'b'}

df1['colors'] = df1['pred'].map(c)
df1.plot(kind='scatter', x='SepalLengthCm',y='SepalWidthCm',c=df1['colors'])

plt.show()

#給一朵鳶尾花的4個特徵值：「花萼長度 6.6公分、花萼寬度 3.1公分、花瓣長度 5.2公分、花寬度 2.4公分」

new = [[6.6,3.1,5.2,2.4]]

v=km.predict(new)

print('預測結果為：', v)

#預測結果為： [0]


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


