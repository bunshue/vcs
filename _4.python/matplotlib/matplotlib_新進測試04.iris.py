# 新進測試04

"""

iris 鳶尾花

"""
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

filename = 'data/iris_sample.csv'

iris = pd.read_csv(filename)
"""
共有五個欄位：
1. 花萼長度(Sepal Length)：計算單位是公分。
2. 花萼寬度(Sepal Width)：計算單位是公分。
3. 花瓣長度(Petal Length) ：計算單位是公分。
4. 花瓣寬度(Petal Width)：計算單位是公分。
5. 類別(Class)：可分為Setosa，Versicolor和Virginica三個品種。
"""

print('資料')
#print(iris)

print('資料shape')
print(iris.shape)

print('資料.type')
print(type(iris))

print('資料.head()')
print(iris.head())

print('size')
print(np.unique(iris["花萼長度"].values).size)
print()

cccc = np.where(iris["類別"] == "versicolor", 1, 0)
print('抓出versicolor :', cccc)
print()

color = ['r','y','b']
species = ['Setosa','Versicolour','Virginica']
Setosa = []
Versicolour = []
Virginica = []

print(type(iris))
print(len(iris))
print(iris.shape)

#sepal_length,sepal_width,petal_length,petal_width,species
print(iris["花萼長度"])
print(len(iris["花萼長度"]))
print(iris["花萼長度"][0])

# 不同种类保存为不同的列表
for i in range(len(iris)):
    if iris["類別"][i] == 'setosa':
        Setosa.append((iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i]))
    elif iris["類別"][i] == 'versicolor':
        Versicolour.append((iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i]))
    elif iris["類別"][i] == 'virginica':
        Virginica.append((iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i]))

#print('Setosa :', Setosa)
#print('Versicolour :', Versicolour)
#print('Virginica :', Virginica)

fig = plt.figure()
ax = fig.add_subplot(111)



ax.scatter(x=np.array(Setosa)[:,0], # Setosa种类的花瓣的长度
     y=np.array(Setosa)[:,1], # Setosa种类的花瓣的宽度
     s=35,                    # 散点大小为35
     c=color[0],              # 颜色为红色
     label=species[0])        # 标签为Setosa

ax.scatter(x=np.array(Versicolour)[:,0],    # Versicolour种类的花瓣的长度
     y=np.array(Versicolour)[:,1],    # Versicolour种类的花瓣的宽度
     s=35,                            # 散点大小为35
     c=color[1],                      # 颜色为黄色
     label=species[1])                # 标签为Versicolour

ax.scatter(x=np.array(Virginica)[:,0],  # Virginica种类的花瓣的长度
     y=np.array(Virginica)[:,1],  # Virginica种类的花瓣的宽度
     s=35,                        # 散点大小为35
     c=color[2],                  # 颜色为蓝色
     label=species[2])            # 标签为Virginica

# 添加轴标签和标题
ax.set_title('花瓣长度与宽度的关系',
       fontsize=20)
ax.set_xlabel('花瓣的长度',
        fontsize=15)
ax.set_ylabel('花瓣的宽度',
        fontsize=15)

ax.legend(loc='best') # 添加图例

plt.show()

print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個
