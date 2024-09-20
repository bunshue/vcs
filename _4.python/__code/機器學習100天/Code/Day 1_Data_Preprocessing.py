# 機器學習100天——第1天：數據預處理（Data Preprocessing）

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
