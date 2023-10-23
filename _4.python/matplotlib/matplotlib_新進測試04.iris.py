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
#sepal_length, sepal_width, petal_length, petal_width, species
共有五個欄位：
1. 花萼長度(Sepal Length)：計算單位是公分。
2. 花萼寬度(Sepal Width)：計算單位是公分。
3. 花瓣長度(Petal Length) ：計算單位是公分。
4. 花瓣寬度(Petal Width)：計算單位是公分。
5. 類別(Class)：可分為Setosa，Versicolor和Virginica三個品種。
"""

#print('全部資料')
#print(iris)

print('資料.shape :', iris.shape)
print('資料.type :', type(iris))
print('資料.長度 :', len(iris))
print('資料.head()')
print(iris.head())

print('花萼長度資料 :')
print(iris["花萼長度"])
print()
print('花萼長度資料長度 :', len(iris["花萼長度"]))
print('花萼長度資料之第 0 筆資料 :', iris["花萼長度"][0])

print('花萼長度 不同的數字 size :', np.unique(iris["花萼長度"].values).size)
print('花萼寬度 不同的數字 size :', np.unique(iris["花萼寬度"].values).size)
print('花瓣長度 不同的數字 size :', np.unique(iris["花瓣長度"].values).size)
print('花瓣寬度 不同的數字 size :', np.unique(iris["花瓣寬度"].values).size)
print('花萼長度 :')
print(iris['花萼長度'].values)
print('花萼寬度 :')
print(iris['花萼寬度'].values)
print('花瓣長度 :')
print(iris['花瓣長度'].values)
print('花瓣寬度 :')
print(iris['花瓣寬度'].values)

class1 = np.where(iris["類別"] == "setosa", 1, 0)
print('抓出versicolor :', class1)
class2 = np.where(iris["類別"] == "versicolor", 1, 0)
print('抓出versicolor :', class2)
class3 = np.where(iris["類別"] == "virginica", 1, 0)
print('抓出versicolor :', class3)

Setosa = []
Versicolour = []
Virginica = []

# 不同种类保存为不同的列表
for i in range(len(iris)):
    if iris["類別"][i] == 'setosa':
        Setosa.append((iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i]))
    elif iris["類別"][i] == 'versicolor':
        Versicolour.append((iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i]))
    elif iris["類別"][i] == 'virginica':
        Virginica.append((iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i]))

print('Setosa :', Setosa)
print('Versicolour :', Versicolour)
print('Virginica :', Virginica)

plt.scatter(x = np.array(Setosa)[:, 0], # Setosa种类的花瓣的长度
            y = np.array(Setosa)[:, 1], # Setosa种类的花瓣的宽度
            s = 80,
            c = 'red',
            label = 'Setosa')

plt.scatter(x = np.array(Versicolour)[:, 0],    # Versicolour种类的花瓣的长度
            y = np.array(Versicolour)[:, 1],    # Versicolour种类的花瓣的宽度
            s = 50,
            c = 'green',
            label = 'Versicolour')

plt.scatter(x = np.array(Virginica)[:, 0],  # Virginica种类的花瓣的长度
            y = np.array(Virginica)[:, 1],  # Virginica种类的花瓣的宽度
            s = 20,
            c = 'blue',
            label = 'Virginica')

# 添加轴标签和标题
plt.title('花瓣长度与宽度的关系', fontsize = 20)
plt.xlabel('花瓣的长度', fontsize = 15)
plt.ylabel('花瓣的宽度', fontsize = 15)
plt.legend(loc = 'best') # 添加图例

plt.show()

print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個
