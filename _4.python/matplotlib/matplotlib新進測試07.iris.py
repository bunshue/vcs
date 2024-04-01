# 新進測試04

"""

iris 鳶尾花

"""

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

filename = "_data/iris_sample.csv"

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

# print('全部資料')
# print(iris)

print("資料.shape :", iris.shape)
print("資料.type :", type(iris))
print("資料.長度 :", len(iris))
print("資料.head()")
print(iris.head())

print("花萼長度資料 :")
print(iris["花萼長度"])
print()
print("花萼長度資料長度 :", len(iris["花萼長度"]))
print("花萼長度資料之第 0 筆資料 :", iris["花萼長度"][0])

print("花萼長度 不同的數字 size :", np.unique(iris["花萼長度"].values).size)
print("花萼寬度 不同的數字 size :", np.unique(iris["花萼寬度"].values).size)
print("花瓣長度 不同的數字 size :", np.unique(iris["花瓣長度"].values).size)
print("花瓣寬度 不同的數字 size :", np.unique(iris["花瓣寬度"].values).size)
print("花萼長度 :")
print(iris["花萼長度"].values)
print("花萼寬度 :")
print(iris["花萼寬度"].values)
print("花瓣長度 :")
print(iris["花瓣長度"].values)
print("花瓣寬度 :")
print(iris["花瓣寬度"].values)

class1 = np.where(iris["類別"] == "setosa", 1, 0)
print("抓出versicolor :", class1)
class2 = np.where(iris["類別"] == "versicolor", 1, 0)
print("抓出versicolor :", class2)
class3 = np.where(iris["類別"] == "virginica", 1, 0)
print("抓出versicolor :", class3)

Setosa = []
Versicolour = []
Virginica = []

# 不同种类保存为不同的列表
for i in range(len(iris)):
    if iris["類別"][i] == "setosa":
        Setosa.append(
            (iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i])
        )
    elif iris["類別"][i] == "versicolor":
        Versicolour.append(
            (iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i])
        )
    elif iris["類別"][i] == "virginica":
        Virginica.append(
            (iris["花萼長度"][i], iris["花萼寬度"][i], iris["花瓣長度"][i], iris["花瓣寬度"][i])
        )

print("Setosa :", Setosa)
print("Versicolour :", Versicolour)
print("Virginica :", Virginica)

plt.scatter(
    x=np.array(Setosa)[:, 0],  # Setosa种类的花瓣的长度
    y=np.array(Setosa)[:, 1],  # Setosa种类的花瓣的宽度
    s=80,
    c="red",
    label="Setosa",
)

plt.scatter(
    x=np.array(Versicolour)[:, 0],  # Versicolour种类的花瓣的长度
    y=np.array(Versicolour)[:, 1],  # Versicolour种类的花瓣的宽度
    s=50,
    c="green",
    label="Versicolour",
)

plt.scatter(
    x=np.array(Virginica)[:, 0],  # Virginica种类的花瓣的长度
    y=np.array(Virginica)[:, 1],  # Virginica种类的花瓣的宽度
    s=20,
    c="blue",
    label="Virginica",
)

# 添加轴标签和标题
plt.title("花瓣长度与宽度的关系", fontsize=20)
plt.xlabel("花瓣的长度", fontsize=15)
plt.ylabel("花瓣的宽度", fontsize=15)
plt.legend(loc="best")  # 添加图例

plt.show()

print("------------------------------------------------------------")  # 60個


"""
import matplotlib as mpl

# 获取图的坐标信息
ax = plt.gca()
# 设置日期的显示格式
date_format = mpl.dates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_format)
# 设置x轴显示多少个日期刻度
# xlocator = mpl.ticker.LinearLocator(10)
# 设置x轴每个刻度的间隔天数
xlocator = mpl.ticker.MultipleLocator(7)
ax.xaxis.set_major_locator(xlocator)
# 为了避免x轴刻度标签的紧凑，将刻度标签旋转45度
plt.xticks(rotation = 45)

# 添加y轴标签
plt.ylabel('人数')
# 添加图形标题
plt.title('每天微信文章阅读人数与人次趋势')
# 添加图例
plt.legend()
# 显示图形
plt.show()
"""


"""
# 读入数据
iris = pd.read_csv(r'F:\\python_Data_analysis_and_mining\\06\\iris.csv')
print(iris.shape)
# 绘制散点图
plt.scatter(x = iris.Petal_Width, # 指定散点图的x轴数据
y = iris.Petal_Length, # 指定散点图的y轴数据
color = 'steelblue' # 指定散点图中点的颜色
)
# 添加x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 添加标题
plt.title('鸢尾花的花瓣宽度与长度关系')
# 显示图形
plt.show()

# Pandas模块绘制散点图
# 绘制散点图
iris.plot(x = 'Petal_Width', y = 'Petal_Length', kind = 'scatter', title = '鸢尾花的花瓣宽度与长度关系')
# 修改x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 显示图形
plt.show()

# seaborn模块绘制分组散点图
sns.lmplot(x = 'Petal_Width', # 指定x轴变量
y = 'Petal_Length', # 指定y轴变量
hue = 'Species', # 指定分组变量
data = iris, # 指定绘图数据集
legend_out = False, # 将图例呈现在图框内
truncate = True # 根据实际的数据范围，对拟合线作截断操作
)
# 修改x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 添加标题
plt.title('鸢尾花的花瓣宽度与长度关系')
# 显示图形
plt.show()
"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
