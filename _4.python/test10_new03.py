import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

import pandas as pd

idx = ['1','2','3','4','5','6','7','8','9','10','11','12']

column = ['中文名','英文名','體重','全名']

s = [['鼠', 'mouse', 3, '米老鼠'],
     ['牛', 'ox', 48, '班尼牛'],
     ['虎', 'tiger', 33, '跳跳虎'],
     ['兔', 'rabbit', 8, '彼得兔'],
     ['龍', 'dragon', 38, '逗逗龍'],
     ['蛇', 'snake', 16, '貪吃蛇'],
     ['馬', 'horse', 36, '草泥馬'],
     ['羊', 'goat', 29, '喜羊羊'],
     ['猴', 'monkey', 22, '山道猴'],
     ['雞', 'chicken', 6, '肯德雞'],
     ['狗', 'dog', 12, '貴賓狗'],
     ['豬', 'pig', 42, '佩佩豬']]

df = pd.DataFrame(s, index = idx, columns = column )

print(df)

print('df的方法')
print(df.shape)
print(df.columns)
print(df.index)
print(df.head())
print(df.describe())
print(df.info())
print(df.duplicated())

filename = '動物資料0.csv'
df.to_csv(filename)  #預設為 儲存index行

filename = '動物資料1.csv'
df.to_csv(filename, index = False)  #不儲存index行

filename = '動物資料2.csv'
df.to_csv(filename, index = True)   #儲存index行

for i in range(12):
    print('index :', i, end = '\t')
    print('中文名 :', df.iloc[i, 0], end = '\t')
    print('體重 :', df.iloc[i, 2], end = '\n')

print('全名(第3欄)')
print(df.iloc[0:12, 3])

print('全名(部分)')
print(df.iloc[[3, 6, 9, 11], 3])

print('排序')
df1 = df.sort_values('體重')
print(df1.head())

print('最重 :', df['體重'].max())
print('最輕 :', df['體重'].min())
print('總重 :', df['體重'].sum())
print('平均 :', df['體重'].mean())


'''


#由網址讀取資料檔

import pandas as pd
url='https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
df = pd.read_html(url)
print(df)

'''



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


