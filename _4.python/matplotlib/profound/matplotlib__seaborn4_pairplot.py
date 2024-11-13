"""
海生, 自動把圖畫得比較好看
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''

"""
sns.pairplot()

pairplot:pair是成对的意思，即是说这个用来展现变量两两之间的关系，线性、非线性、相关等等
"""


#使用鸢尾花数据画图


#两种导入方式，这次是直接从sklearn.datasets导入
import pandas as pd 
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt

#sns.set_style('white',{'font.sans-serif':['simhei','Arial']})  #解决中文不能显示问题

iris=datasets.load_iris()
iris_data= pd.DataFrame(iris.data,columns=iris.feature_names)
iris_data['species']=iris.target_names[iris.target]
# NG iris_data.head(3).append(iris_data.tail(3))   #前面三条+后面三条
iris_data.rename(columns={"sepal length (cm)":"萼片长",
                     "sepal width (cm)":"萼片宽",
                     "petal length (cm)":"花瓣长",
                     "petal width (cm)":"花瓣宽",
                     "species":"种类"},inplace=True)
kind_dict = {
    "setosa":"山鸢尾",
    "versicolor":"杂色鸢尾",
    "virginica":"维吉尼亚鸢尾"
}
iris_data["种类"] = iris_data["种类"].map(kind_dict)

#画变量之间关系的图

#全部变量都放进去
sns.pairplot(iris_data)
plt.show()

"""
可以看到对角线上是各个属性的直方图（分布图），而非对角线上是两个不同属性之间的相关图，
从图中我们发现，花瓣的长度和宽度之间以及萼片的长短和花瓣的长、宽之间具有比较明显的相关关系
"""
 

#kind:用于控制非对角线上图的类型，可选'scatter'与'reg'
#diag_kind:用于控制对角线上的图分类型，可选'hist'与'kde'

sns.pairplot(iris_data,kind='reg',diag_kind='ked')

plt.show()


sns.pairplot(iris_data,kind='reg',diag_kind='hist')

plt.show()


#hue：针对某一字段进行分类
sns.pairplot(iris_data,hue='种类')
plt.show()

"""
经过hue分类后的pairplot中发现，不论是从对角线上的分布图还是从分类后的散点图，
都可以看出对于不同种类的花，其萼片长、花瓣长、花瓣宽的分布差异较大，换句话说，
这些属性是可以帮助我们去识别不同种类的花的。
比如，对于萼片、花瓣长度较短，花瓣宽度较窄的花，那么它大概率是山鸢尾
"""

#vars：研究某2个或者多个变量之间的关系vars,
#x_vars,y_vars：选择数据中的特定字段，以list形式传入需要注意的是，x_vars和y_vars要同时指定

sns.pairplot(iris_data,vars=["萼片长","花瓣长"])
plt.show()

sns.pairplot(iris_data,x_vars=["萼片长","花瓣宽"],y_vars=["萼片宽","花瓣长"]) 
plt.show()

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = sns.load_dataset("iris")
iris.head()

sns.set()
sns.pairplot(iris, hue="species", height=3)
print(iris)

plt.show()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


