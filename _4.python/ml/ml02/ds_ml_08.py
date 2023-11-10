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

import pandas as pd

#氣溫
t = [17, 17, 17, 22, 19, 21, 17, 17, 22, 24, 21, 21, 21, 17, 25, 21, 20, 19, 19, 22]

#飲料銷售量
q = [386, 360, 383, 146, 300, 254, 403, 381, 269, 99, 171, 204, 213, 279, 97, 262, 262, 225, 240, 226]

df = pd.DataFrame()

df['T'] = t         #行資料：氣溫

df['Q'] = q         #行資料：銷售量

print(df.head())

df.plot(kind='scatter', x='T', y='Q')
plt.show()


df_X = df[['T']]    # 雙層的中括號(特徵值)，設定成資料框
df_y = df['Q']      # 單層的中括號(標籤)，設定成序列
print(df_X.head())

print(df_y.head())


#8-2 機器學習實作

#8-2-1 提出具體的假設
#8-2-2 找出機器學習模型
#挑選模型：匯入線性迴歸模型

from sklearn.linear_model import LinearRegression

#學習訓練：建立並訓練線性迴歸模型

lm = LinearRegression()            #建立新模型 lm
lm.fit(df_X, df_y)                 #訓練模型

#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

#測試評估
#決定模型：取出線性迴歸模型的 m、b 參數

print('線性迴歸的模型為 y = f(x) = mx +b')  
print('m 為 ',lm.coef_)           
print('b 為 ', lm.intercept_)     

#線性迴歸的模型為 y = f(x) = mx +b
#m 為  [-33.19704219]
#b 為  920.2809917355372

#進行預測

temp = [[23]]        # 輸入特徵值(氣溫) 
p = lm.predict(temp) # 輸出標籤(預測的銷售量)
print(p) 

#[156.74902131]

temp = [[23],[18],[36]]  
p = lm.predict(temp)     
print(p) 

#[ 156.74902131  322.73423227 -274.81252719]

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


