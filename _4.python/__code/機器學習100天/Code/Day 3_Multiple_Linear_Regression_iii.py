# Importing the libraries
import pandas as pd
import numpy as np


#机器学习100天——第3天：多元线性回归（Multiple Linear Regression）
#第1步：数据预处理


#导入数据集

dataset = pd.read_csv('../datasets/50_Startups.csv')
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
