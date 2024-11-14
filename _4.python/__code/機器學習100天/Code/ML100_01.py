#數據預處理（Data Preprocessing）

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

#第三步：處理丟失數據

#我們得到的數據很少是完整的。
#數據可能因為各種原因丟失，為了不降低機器學習模型的性能，需要處理數據。
#我們可以用整列的平均值或中間值替換丟失的數據。
#我們用sklearn.preprocessing庫中的Imputer類完成這項任務。

#Step 3: Handling the missing data
# If you use the newest version of sklearn, use the lines of code commented out
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
#from sklearn.preprocessing import Imputer
# axis=0表示按列進行
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
第3步：處理丟失數據

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : , 1:3] = imputer.transform(X[ : , 1:3])
"""


#Step 4: Encoding categorical data
#第四步：解析分類數據
#分類數據指的是含有標簽值而不是數字值的變量。取值范圍通常是固定的。
#例如"Yes"和"No"不能用于模型的數學計算，所以需要解析成數字。
#為實現這一功能，我們從sklearn.preprocessing庫導入LabelEncoder類。

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
創建虛擬變量

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
"""

#Step 5: Splitting the datasets into training sets and Test sets
#第五步：拆分數據集為測試集合和訓練集合
#把數據集拆分成兩個：一個是用來訓練模型的訓練集合，另一個是用來驗證模型的測試集合。
#兩者比例一般是80:20。
#我們導入sklearn.model_selection庫中的train_test_split()方法。

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

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
#大部分模型算法使用兩點間的歐氏距離表示，
#但此特征在幅度、單位和范圍姿態問題上變化很大。
#在距離計算中，高幅度的特征比低幅度特征權重更大。
#可用特征標準化或Z值歸一化解決。
#導入sklearn.preprocessing庫的StandardScalar類。

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""

#機器學習100天——第二天：


"""

import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print("------------------------------------------------------------")  # 60個

print('簡單線性回歸')

'''
#讀取資料
dataset = pd.read_csv('data/studentscores.csv')
print(dataset)
df = dataset.sort_values("Scores",ascending=False)
print(df)
dataset.head(30)

print(dataset.head(30))

#這里我們需要使用pandas的iloc(區分于loc根據index來索引，iloc利用行號來索引)方法來對數據進行處理，第一個參數為行號，:表示全部行，第二個參數 ：1表示截到第1列(也就是取第0列)

#X = dataset.iloc[ : ,   : 1 ].values
#Y = dataset.iloc[ : , 1 ].values

X = dataset.iloc[ 0: 25,   : 1 ].values
Y = dataset.iloc[ 0: 25, -1: ].values
print("X:",X)
print("Y:",Y)

#導入sklearn庫的cross_validation類來對數據進行訓練集、測試集劃分



from sklearn.model_selection import train_test_split
#拆分數據，0.25作為測試集
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 
print(X_train,X_test)
print(Y_train,Y_test)


#訓練線性回歸
# Fitting Simple Linear Regression Model to the training set
from sklearn.linear_model import LinearRegression
#使用訓練集對模型進行訓練
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#預測結果

Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

# 畫出來
#散點圖
plt.scatter(X_train , Y_train, color = 'red')
#線圖
plt.plot(X_train , regressor.predict(X_train), 'bo-')
#plt.plot(X_train , regressor.predict(X_train), color ='blue')

plt.show()

#散點圖
plt.scatter(X_test , Y_test, color = 'red')
#線圖
plt.plot(X_test ,Y_pred, 'bo-')
#plt.plot(X_test , regressor.predict(X_test), color ='blue')

plt.show()

print(X_test,Y_test)

'''

print("------------------------------------------------------------")  # 60個

print('簡單線性回歸')

#another

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#讀取資料
dataset = pd.read_csv('data/studentscores.csv')
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 

#第二步：訓練集使用簡單線性回歸模型來訓練

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#第三步：預測結果

Y_pred = regressor.predict(X_test)

#第四步：可視化
#訓練集結果可視化

plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')
plt.show()

#測試集結果可視化

plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print('多元线性回归（Multiple Linear Regression）')

'''
import pandas as pd
import numpy as np

#讀取資料
dataset = pd.read_csv('data/50_Startups.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : ,  4 ].values
Z = dataset.iloc[ : ,  0 ].values
print("X:")
print(X[:10])
print("Y:")
print(Y)
dataset.head(5)


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=0.0, strategy="mean")
imputer = imputer.fit(X[ : , 0:3])
X[ : , 0:3] = imputer.transform(X[ : , 0:3])
print(X)

#将类别数据数字化

# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer 
labelencoder = LabelEncoder()
print("original:")
print(X[:10])
#print(X[: , 3])
X[: , 3] = labelencoder.fit_transform(X[ : , 3])
#print(X[: , 3])
print("labelencoder:")
print(X[:10])
ct = ColumnTransformer([( "encoder", OneHotEncoder(), [3])], remainder = 'passthrough')
X = ct.fit_transform(X)
#onehotencoder = OneHotEncoder(categorical_features = [3])
#X = onehotencoder.fit_transform(X).toarray()
print("onehot:")
print(X[:10])

"""


躲避虚拟变量陷阱

在回归预测中我们需要所有的数据都是numeric的，但是会有一些非numeric的数据，比如国家，省，部门，性别。这时候我们需要设置虚拟变量（Dummy variable）。做法是将此变量中的每一个值，衍生成为新的变量，是设为1，否设为0.举个例子，“性别”这个变量,我们可以虚拟出“男”和”女”两虚拟变量，男性的话“男”值为1，”女”值为0；女性的话“男”值为0，”女”值为1。

但是要注意，这时候虚拟变量陷阱就出现了。就拿性别来说，其实一个虚拟变量就够了，比如 1 的时候是“男”， 0 的时候是”非男”，即为女。如果设置两个虚拟变量“男”和“女”，语义上来说没有问题，可以理解，但是在回归预测中会多出一个变量，多出的这个变量将会对回归预测结果产生影响。一般来说，如果虚拟变量要比实际变量的种类少一个。

在多重线性回归中，变量不是越多越好，而是选择适合的变量。这样才会对结果准确预测。如果category类的特征都放进去，拟合的时候，所有权重的计算，都可以有两种方法实现，一种是提高某个category的w，一种是降低其他category的w，这两种效果是等效的，也就是发生了共线性,虚拟变量系数相加和为1，出现完全共线陷阱。

但是下面测试尽然和想法不一致。。。

"""

# Avoiding Dummy Variable Trap
X1 = X[: , 1:]

print(X1)
print(X)

#拆分数据集为训练集和测试集
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y, test_size = 0.2, random_state = 0)
print(X_test)
print(Y_test)
print(X1_test)
print(Y1_test)


#第2步：在训练集上训练多元线性回归模型
# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
regressor1 = LinearRegression()
regressor1.fit(X1_train, Y1_train)


LinearRegression()

#第3步：在测试集上预测结果

# Predicting the Test set results
y_pred = regressor.predict(X_test)
y1_pred = regressor1.predict(X1_test)

print(y_pred)
print(y1_pred)







# regression evaluation
from sklearn.metrics import r2_score
print(r2_score(Y_test, y_pred))
'''


print("------------------------------------------------------------")  # 60個

#another

import pandas as pd
import numpy as np

#讀取資料
dataset = pd.read_csv('data/50_Startups.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : ,  4 ].values

#将类别数据数字化

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()
X[: , 3] = labelencoder.fit_transform(X[ : , 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#躲避虚拟变量陷阱

X = X[: , 1:]

#拆分数据集为训练集和测试集

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#第2步： 在训练集上训练多元线性回归模型

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#Step 3: 在测试集上预测结果

y_pred = regressor.predict(X_test)
print(y_pred)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

