'''
#numpy製作資料 修改資料 用matplotlib顯示

#numpy的操作 用matplotlib顯示

'''
print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

W, H, D = 5, 5, 3

print('建立 0 ~ 255 的隨機陣列')
image1 = np.random.randint(0, 256, size = [W, H, D], dtype = np.uint8)
print(image1.shape)

image1[:, :, 0] = 0;    #R通道
image1[:, :, 1] = 0;    #G通道
image1[:, :, 2] = 0;    #B通道
print(image1)

plt.imshow(image1)
plt.show()

print('建立 0.0 ~ 1.0 的隨機陣列')
image2 = np.random.random((W, H, D))
print(image2.shape)
#print(image2)

plt.imshow(image2)
plt.show()

print('建立 0 ~ 255 的 16 X 16 陣列')
image3 = np.arange(0, 256).reshape(16, 16)
print(image3.shape)
#print(image3)

plt.imshow(image3)
plt.show()

print('------------------------------------------------------------')	#60個

print('建立一黑圖')

W = 640
H = 480
print('numpy製作一個 %d X %d 的圖 黑色, 2維 3 通道' % (W, H))
image = np.zeros((H, W, 3), dtype = np.uint8)    #預設為0, 黑色, 2維, 3通道
#image = np.zeros((H, W), dtype = np.uint8)    #預設為0, 黑色, 2維, 1通道

print('中間一塊用填成灰色')
for i in range(100, 200):
    for j in range(100, 200):
        image[i,j] = 200

print('中間一塊用填成白色')
#     y_st y_sp  x_st y_st
image[300 : 400, 50 : 200] = 255

#image[:, :, 0] = 255 #將第0通道設為全亮 藍
#image[:, :, 1] = 255 #將第1通道設為全亮 綠
#image[:, :, 2] = 255 #將第0通道設為全亮 紅

image[:,0:50,0]=255      #第0通道, 藍色通道
image[:,50:100,1]=255    #第1通道, 綠色通道
image[:,100:150,2]=255    #第2通道, 紅色通道

y = 75
#                  y   x
print('讀取像素點 (y, 25) =', image[y, 25])
print('讀取像素點 (y, 75) =', image[y, 75])
print('讀取像素點 (y, 125) =', image[y, 125])
print('讀取像素點 (y, 125) 裡面的紅 =', image[y, 125, 2])

#逕行修改
image[:, 75] = 255
image[:, 125, 2] = 0


print('建立一個每點顏色任意顏色之圖')
random_image = np.random.randint(0, 256, size = [100, 100, 3], dtype = np.uint8)

print('將一任意圖貼上來')
#     y_st  y_sp x_st  y_st
image[100 : 200, 400 : 500] = random_image

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

img1 = np.random.randint(0, 256, size = [3, 3], dtype = np.uint8)
print("img1 = \n", img1)
plt.imshow(img1)
plt.show()

img2 = np.random.randint(0, 256, size = [3, 3], dtype = np.uint8)
print("img2 = \n", img2)
plt.imshow(img2)
plt.show()

img3 = img1 + img2
print("img3 = \n", img3)
plt.imshow(img3)
plt.show()

print('------------------------------------------------------------')	#60個

img = np.random.randint(10, 99, size = [5, 5], dtype = np.uint8)
print("img = \n", img)

print("讀取像素點img.item(3, 2) = ", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后img = \n", img)
print("修改后像素點img.item(3, 2) = ", img.item(3, 2))

print('------------------------------------------------------------')	#60個

img = np.random.randint(10, 99, size = [2, 4, 3], dtype = np.uint8)
print("img = \n", img)

print("讀取像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print("讀取像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print("讀取像素點img[1, 0, 2] = ", img.item(1, 0, 2))
img.itemset((1, 2, 0), 255)
img.itemset((0, 2, 1), 255)
img.itemset((1, 0, 2), 255)
print("修改后img = \n", img)
print("修改后像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print("修改后像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print("修改后像素點img[1, 0, 2] = ", img.item(1, 0, 2))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

x = [x for x in range(0, 11)]                   
y = [7.5*y - 3.33 for y in x]
voucher = 25                            # unit = 100
ans_x = (25 + 3.33) / 7.5
print('拜訪次數 = {}'.format(int(ans_x*100)))
plt.axis([0, 4, 0, 30])
plt.plot(x, y)   
plt.plot(1, 5, '-x')
plt.plot(2, 10, '-x')
plt.plot(3, 20, '-x')
plt.plot(ans_x, 25, '-o')
plt.text(ans_x-0.6, 25+0.2, '('+str(int(ans_x*100))+','+str(2500)+')')
plt.xlabel('Times:unit=100')
plt.ylabel('Voucher:unit=100')
plt.grid()                              # 加格線

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 10)                          # 建立 x
y = np.random.random((7, 10))                       # 建立 y 7 X 10 的隨機陣列

print(y.shape)
print(y)

for yy in y:    
    plt.scatter(x, yy, c='r', marker='*')

plt.xticks(np.arange(0,11,step=1.0))

plt.show()



print('------------------------------------------------------------')	#60個

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




print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

