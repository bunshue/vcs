'''
#numpy製作資料 修改資料 用matplotlib顯示

#numpy的操作 用matplotlib顯示

'''

import sys
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個
'''
import pandas as pd

df=pd.read_csv('data/年度銷售金額.csv')

df.index = df['AREA']

df=df.drop('AREA',axis=1)

print(df)

df['1st'].plot(kind='pie', autopct='%.2f%%')

plt.show()


print('------------------------------------------------------------')	#60個


df['1st'].plot(kind='pie', autopct='%.2f%%')

plt.show()

print('------------------------------------------------------------')	#60個

df.plot(kind='bar', rot=0)

plt.show()

print('------------------------------------------------------------')	#60個

#(圖)-圓餅圖比直條圖更能呈現各項資料所佔的比例

import pandas as pd

n=['Tom','Allen','Cathy','Jacky']

v=[1324,2514,5586,657]

df=pd.DataFrame()

df['name'] = n

df['vote'] = v

print(df)

df.index = df['name']

df['vote'].plot(kind='pie', autopct='%.0f%%')

plt.show()

print('------------------------------------------------------------')	#60個

df.plot(kind='bar', rot=0)

plt.show()

print('------------------------------------------------------------')	#60個

#5-2 常見的資料視覺化圖表
#5-2-1 愛看趨勢的折線圖
#(圖)-折線圖：不同月份參觀人數的統計趨勢圖

import pandas as pd

df=pd.read_csv('data/觀光人數統計.csv')

df.index = df['Month'] 

print(df[['Green Island', 'Guguan']].head())

df[['Green Island', 'Guguan']].plot()

plt.show()

print('------------------------------------------------------------')	#60個

#實作-繪製折線圖【EX5-2.1a.ipynb】
#Step 01

import pandas as pd

a = ['E','W','S','N']

m =[4522,3101,5211,4613]

s = pd.Series(m, index=a)

print(s)

#Step 02

s.plot()

plt.show()

print('------------------------------------------------------------')	#60個

#Step 03

import pandas as pd

df=pd.read_csv('data/觀光人數統計.csv')

df.index = df['Month'] #自定列索引為Month內容

df=df.drop('Month',axis=1) #刪除原本的月份行資料

print(df.head())

#Step 04

df.plot()

plt.show()

print('------------------------------------------------------------')	#60個

#(圖)-圖表各元件名稱

df.plot(linewidth=2, linestyle=':', title='Number of visitors')

plt.show()

print('------------------------------------------------------------')	#60個

print(df.head())

#加廣知識：自定列索引

import pandas as pd

a = ['E','W','S','N']

m =[4522,3101,5211,4613]

s = pd.Series(m, index=a)

print(s)

s.plot()

plt.show()

print('------------------------------------------------------------')	#60個

s.index = ['EAST','WEST','SOUTH','NORTH']

print(s)

s.plot()

plt.show()

print('------------------------------------------------------------')	#60個

print(df.head())

df_T = df.T

print(df_T.head())

#實作-折線圖(部份資料框)【EX5-2.1b.ipynb】
#Step 01

df1=df['Green Island']

print(df1.head())

#Step 02
df1.plot()
plt.show()

print('------------------------------------------------------------')	#60個

#Step 03

df2=df[['Green Island','Guguan']]

print(df2.head())

#Step 04

df2.plot()

plt.show()

print('------------------------------------------------------------')	#60個

#Step 05

df_T=df.T

print(df_T.head())

#Step 06

df3=df_T[3]

df3.plot()

plt.show()

print('------------------------------------------------------------')	#60個

#5-2-2 最愛比較的長條圖
#(圖)-長條圖：呈現及比較不同區域各季的銷售金額

import pandas as pd

df = pd.read_csv('data/年度銷售金額.csv')

df.index = df['AREA']

df = df.drop('AREA', axis=1)

print(df)

df.plot(kind='bar', rot=0)

plt.show()

print('------------------------------------------------------------')	#60個

#實作-長條圖【EX5-2.2.ipynb】
#Step 01

import pandas as pd

df=pd.read_csv('data/年度銷售金額.csv')

df.index = df['AREA']

df = df.drop('AREA', axis=1)

print(df)


#Step 02

df.plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

#Step 03

df.plot(kind='barh')

plt.show()

print('------------------------------------------------------------')	#60個

#加廣知識：旋轉X軸標籤角度

df.plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

df.plot(kind='bar', rot=0)

plt.show()

print('------------------------------------------------------------')	#60個

#5-2-3 能展現自己重要性的圓餅圖
#(圖)-圓餅圖：顯示不同區域佔第一季總銷售金額的比例

import pandas as pd

df = pd.read_csv('data/年度銷售金額.csv')

df.index = df['AREA']

df = df.drop('AREA', axis=1)

print(df)

df['1st'].plot(kind='pie', autopct='%.2f%%')

plt.show()

print('------------------------------------------------------------')	#60個

#實作-圓餅圖【EX5-2.3.ipynb】
#Step 01

import pandas as pd

df=pd.read_csv('data/年度銷售金額.csv')

df.index = df['AREA']

df = df.drop('AREA', axis=1)

print(df)

#Step 02

df['1st'].plot(kind='pie')

plt.show()

print('------------------------------------------------------------')	#60個

#加深知識-繪製圓餅圖pie

df['1st'].plot(kind='pie', title='Proportion of each area')

plt.show()

print('------------------------------------------------------------')	#60個

df['1st'].plot(kind='pie', colors=['red','#00FF00','blue','yellow'])

plt.show()

print('------------------------------------------------------------')	#60個

df['1st'].plot(kind='pie', fontsize=12)

plt.show()

print('------------------------------------------------------------')	#60個

df['1st'].plot(kind='pie', fontsize=24)

plt.show()

print('------------------------------------------------------------')	#60個

df['1st'].plot(kind='pie', figsize=(1,1))

plt.show()
print('------------------------------------------------------------')	#60個


df['1st'].plot(kind='pie', figsize=(4,4))

plt.show()

print('------------------------------------------------------------')	#60個

df['1st'].plot(kind='pie', autopct='%.2f')

plt.show()
print('------------------------------------------------------------')	#60個


df['1st'].plot(kind='pie', autopct='%.0f%%')

plt.show()

print('------------------------------------------------------------')	#60個

#5-2-4 掌握分佈局勢的直方圖
#(圖)-直方圖：顯示成績分布的情形

import pandas as pd

df=pd.read_csv('data/第一次期中考.csv')

print(df)

df['第1次期中考'].plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

df['第1次期中考'].plot(kind='hist', bins=10)

plt.show()

print('------------------------------------------------------------')	#60個

#實作-直方圖【EX5-2.4.ipynb】
#Step 01

import pandas as pd

df=pd.read_csv('data/學生成績檔.csv')

print(df.head())

#Step 02

df['第1次平時考'].plot(kind='hist')

plt.show()
print('------------------------------------------------------------')	#60個

#加深知識：繪製直方圖hist

df['第1次平時考'].plot(kind='hist', bins=20)

plt.show()
print('------------------------------------------------------------')	#60個

df['第1次平時考'].plot(kind='hist', bins=40)

plt.show()
print('------------------------------------------------------------')	#60個

df['第1次平時考'].plot(kind='hist', color='blue', edgecolor='orange')

plt.show()

print('------------------------------------------------------------')	#60個

#5-2-5 愛找模式的散佈圖
#(圖)-散佈圖：氣溫與紅茶銷售量之間的相關性

import pandas as pd

df=pd.read_csv('data/紅茶銷售量.csv')

print(df)

df.plot(kind='scatter', x='temperature', y='sale')

plt.show()
'''

print('------------------------------------------------------------')	#60個

#實作-散佈圖【EX5-2.5.ipynb】
#Step 01

import pandas as pd

df=pd.read_csv('data/sunshine.csv')

print(df)

#Step 02

df.plot(kind='scatter', x='SunShine', y='Temperature')

plt.show()

print('------------------------------------------------------------')	#60個

#加深知識－設定散佈圖X、Y軸的座標值

df.plot(kind='scatter', x='SunShine', y='Temperature')

plt.show()
print('------------------------------------------------------------')	#60個

df.plot(kind='scatter', x='SunShine', y='Temperature',xlim=(0, 200),  ylim=(0, 40))

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


