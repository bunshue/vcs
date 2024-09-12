# 机器学习100天——第1天：数据预处理（Data Preprocessing）

#Day 1: Data Prepocessing

import numpy as np
import pandas as pd


''' 未知
import sklearn
from sklearn.impute import SimpleImputer
#This block is an example used to learn SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]])
X = [[np.nan, 2, 3], [4, np.nan, 6], [10, np.nan, 9]]
print(imp_mean.transform(X))
print("Sklearn verion is {}".format(sklearn.__version__))

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore')
X = [['Male', 1], ['Female', 3], ['Female', 2]]
"""
>>> enc.fit(X)
OneHotEncoder(handle_unknown='ignore')
>>> enc.categories_
[array(['Female', 'Male'], dtype=object), array([1, 2, 3], dtype=object)]
>>> enc.transform([['Female', 1], ['Male', 4]]).toarray()
array([[1., 0., 1., 0., 0.],
       [0., 1., 0., 0., 0.]])
>>> enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
array([['Male', 1],
       [None, 2]], dtype=object)
>>> enc.get_feature_names(['gender', 'group'])
array(['gender_Female', 'gender_Male', 'group_1', 'group_2', 'group_3'],
  dtype=object)
"""
'''


import numpy as np
import pandas as pd

#取得數據
dataset = pd.read_csv('data/Data.csv')
# 不包括最后一列的所有列
X = dataset.iloc[ : , :-1].values # //.iloc[行，列]
                                 
#取最后一列
Y = dataset.iloc[ : , 3].values  # : 全部行 or 列；[a]第a行 or 列
                                 # [a,b,c]第 a,b,c 行 or 列

print("Step 2: Importing dataset")
print("X")
print(X)
print("Y")
print(Y)
print(X[ : , 1:3])

#第三步：处理丢失数据

#我们得到的数据很少是完整的。
#数据可能因为各种原因丢失，为了不降低机器学习模型的性能，需要处理数据。
#我们可以用整列的平均值或中间值替换丢失的数据。
#我们用sklearn.preprocessing库中的Imputer类完成这项任务。

#Step 3: Handling the missing data
# If you use the newest version of sklearn, use the lines of code commented out
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
#from sklearn.preprocessing import Imputer
# axis=0表示按列进行
#imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
#print(imputer)
# print(X[ : , 1:3])
imputer = imputer.fit(X[ : , 1:3]) #put the data we want to process in to this imputer
X[ : , 1:3] = imputer.transform(X[ : , 1:3]) #replace the np.nan with mean
#print(X[ : , 1:3])
print("---------------------")
print("Step 3: Handling the missing data")
print("step2")
print("X")
print(X)

""" another
第3步：处理丢失数据

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
"""


#Step 4: Encoding categorical data
#第四步：解析分类数据
#分类数据指的是含有标签值而不是数字值的变量。取值范围通常是固定的。
#例如"Yes"和"No"不能用于模型的数学计算，所以需要解析成数字。
#为实现这一功能，我们从sklearn.preprocessing库导入LabelEncoder类。

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

""" another
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
"""

#labelencoder_X = LabelEncoder()
#X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
#Creating a dummy variable
#print(X)
ct = ColumnTransformer([("", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)
#onehotencoder = OneHotEncoder(categorical_features = [0])
#X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
print("---------------------")
print("Step 4: Encoding categorical data")
print("X")
print(X)
print("Y")
print(Y)

""" another
创建虚拟变量

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
"""

#Step 5: Splitting the datasets into training sets and Test sets
#第五步：拆分数据集为测试集合和训练集合
#把数据集拆分成两个：一个是用来训练模型的训练集合，另一个是用来验证模型的测试集合。
#两者比例一般是80:20。
#我们导入sklearn.model_selection库中的train_test_split()方法。

from sklearn.model_selection import train_test_split

""" fail ? another
from sklearn.cross_validation import train_test_split
"""

X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)
print("---------------------")
print("Step 5: Splitting the datasets into training sets and Test sets")
print("X_train")
print(X_train)
print("X_test")
print(X_test)
print("Y_train")
print(Y_train)
print("Y_test")
print(Y_test)

#第六步：特征縮放
#第6步：特征量化
#Step 6: Feature Scaling
#大部分模型算法使用两点间的欧氏距离表示，
#但此特征在幅度、单位和范围姿态问题上变化很大。
#在距离计算中，高幅度的特征比低幅度特征权重更大。
#可用特征标准化或Z值归一化解决。
#导入sklearn.preprocessing库的StandardScalar类。

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
print("---------------------")
print("Step 6: Feature Scaling")
print("X_train")
print(X_train)
print("X_test")
print(X_test)

