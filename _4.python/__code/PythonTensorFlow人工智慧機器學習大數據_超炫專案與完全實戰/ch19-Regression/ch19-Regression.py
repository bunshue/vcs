
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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

plt.plot([1, 2, 3, 4], [0, 0.3, 0.6, 0.9], 'gx')  # 在x=1,y=0 四個位置繪製(g)色x 標記
plt.plot([1, 2, 3, 4], [0, 0.3, 0.6, 0.9], 'r--') # 繪製(r)紅色- 標記也就是線（趨勢線）
plt.axis([0, 5, 0, 1])  # 圖表大小範圍，寬度由0到5 ,高度由0到1
plt.ylabel('Y')  # 設定顯示Y 文字
plt.xlabel('X')  # 設定顯示X 文字
plt.legend(('price','passenger'),loc='upper right')
plt.show()   # 繪製圖表

print("------------------------------------------------------------")  # 60個

#03_plot_dots_not_onTheLine.py

plt.plot([1,2,3,4], [0,0.3,0.6,0.9], 'gx')
plt.plot([1,2,3,4], [0,0.3,0.6,0.9], 'r--')


X = 1+np.arange(30)/10
delta = np.random.uniform(low=-0.1,high=0.1, size=(30,))
Y=0.3*X- 0.3  + delta
plt.plot(X, Y, 'bo')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()

print("------------------------------------------------------------")  # 60個

#04_rsidual.py

plt.plot([1,2,3,4], [0,0.3,0.6,0.9], 'gx')
plt.plot([1,2,3,4], [0,0.3,0.6,0.9], 'r--')

X = 1+np.arange(30)/10
delta = np.random.uniform(low=-0.1,high=0.1, size=(30,))
Y=0.3*X- 0.3  + delta
plt.plot(X, Y, 'bo')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
sum1=0.0
i=0
for X1 in X:
    Y1 = 0.3 * X1 - 0.3
    Y2 = 0.3 * X1 - 0.3 + delta[i]
    sum1=sum1+abs(Y1-Y2)
    i=i+1

print("誤差值",sum1/30)

print("------------------------------------------------------------")  # 60個

#05-Regression.py

from sklearn import linear_model

x_values =pd.DataFrame([1,2,3,4])
y_values =pd.DataFrame([0,0.3,0.6,0.9])
x_test =pd.DataFrame([1.5,3,5])

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)


y_test_predict= body_reg.predict(x_test)
print(" body_reg.predict(x_text)",y_test_predict)

#visualize results
plt.scatter(x_values, y_values)
plt.scatter(x_test, y_test_predict, color='red')
plt.plot(x_test,y_test_predict, color='blue')
plt.show()

print("------------------------------------------------------------")  # 60個

#06_BrainBody.py

from sklearn import linear_model

#read data
dataframe = pd.read_fwf('data/brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#訓練
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#預測
pre=body_reg.predict(x_values)

#圖形化
plt.scatter(x_values, y_values)
plt.plot(x_values,pre )
plt.show()

print("------------------------------------------------------------")  # 60個

#06_BrainBody-Exam.py

from sklearn import linear_model

#read data
dataframe = pd.read_fwf('data/brain_body.txt')
x_values = dataframe[['Body']]
y_values = dataframe[['Brain']]

#訓練
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#預測
pre=body_reg.predict(x_values)


print(body_reg.predict( pd.DataFrame(data=[[170]])))

#圖形化
plt.scatter(x_values, y_values)
plt.plot(x_values,pre )
plt.show()

print("------------------------------------------------------------")  # 60個

#07-diabets.py

from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')

plt.show()

print("------------------------------------------------------------")  # 60個

#08-RegressionDiabetesLoad.py

from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
print("diabetes.data.shape=",diabetes.data.shape)
print("dir(diabetes)",dir(diabetes))
print("diabetes.target.shape=",diabetes.target.shape)

try:
  print("diabetes.feature_names=",diabetes.feature_names)
except:
  print("No diabetes.feature_names=")

import xlsxwriter

try:
  df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
except:
  df = pd.DataFrame(diabetes.data, columns= ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6'])

df['target'] = diabetes.target


print(df.head())
df.to_csv("tmp_diabetes.csv", sep='\t')

writer = pd.ExcelWriter('tmp_diabetes.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')

plt.show()

print("------------------------------------------------------------")  # 60個

#09-LinearRegression-diabetes.py

from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

print("------------------------------------------------------------")  # 60個

#09-LinearRegression-diabetes-exam.py

from sklearn import datasets, linear_model

# Load the diabetes dataset
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:,:]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20,:]
diabetes_X_test = diabetes_X[-20:,:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

print("------------------------------------------------------------")  # 60個


