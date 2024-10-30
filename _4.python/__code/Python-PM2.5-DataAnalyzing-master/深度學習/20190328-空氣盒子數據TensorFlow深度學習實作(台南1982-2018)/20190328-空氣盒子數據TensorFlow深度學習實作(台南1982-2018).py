"""
20190328-空氣盒子數據TensorFlow深度學習實作(台南1982-2018)

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

#時間序列繪圖

import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams['axes.unicode_minus'] = False

df=pd.read_excel('Tainan_198211-201811.xlsx')

#檢查屬性

cc = df.dtypes
print(cc)

#屬性轉換

df["SO2"] = pd.to_numeric(df.SO2, errors='coerce')
df["CO"] = pd.to_numeric(df.CO, errors='coerce')
df["CO2"] = pd.to_numeric(df.CO2, errors='coerce')
df["O3"] = pd.to_numeric(df.O3, errors='coerce')
df["PM25"] = pd.to_numeric(df.PM25, errors='coerce')
df["Nox"] = pd.to_numeric(df.Nox, errors='coerce')
df["NO"] = pd.to_numeric(df.NO, errors='coerce')
df["NO2"] = pd.to_numeric(df.NO2, errors='coerce')
df["THC"] = pd.to_numeric(df.THC, errors='coerce')
df["NMHC"] = pd.to_numeric(df.NMHC, errors='coerce')
df["CH4"] = pd.to_numeric(df.CH4, errors='coerce')
df["WindSpeed"] = pd.to_numeric(df.WindSpeed, errors='coerce')
df["TEMP"] = pd.to_numeric(df.TEMP, errors='coerce')
df["Humidity"] = pd.to_numeric(df.Humidity, errors='coerce')

cc = df.head(10)
print(cc)

cc = df.dtypes
print(cc)

cc = df.corr()[['PM25']].sort_values('PM25')  
print(cc)

X = df[['SO2', 'CO','CO2', 'O3', 'Nox', 'NO', 'NO2', 'THC', 'NMHC', 'CH4', 'WindSpeed','TEMP','Humidity']]

y = df['PM25']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)

"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)
"""
y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

df1 = df.head(20)

print(df1)

df1.plot(kind='bar',figsize=(8,6))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

from sklearn.metrics import mean_absolute_error, median_absolute_error

print("The Explained Variance: %.2f" % regressor.score(X_test, y_test))  
print("The Mean Absolute Error: %.2f " % mean_absolute_error(y_test, y_pred))  
print("The Median Absolute Error: %.2f " % median_absolute_error(y_test, y_pred))  

#神經網路

import tensorflow as tf
from sklearn.metrics import explained_variance_score,mean_absolute_error,median_absolute_error
from sklearn.model_selection import train_test_split  

df=pd.read_excel('Tainan_198211-201811.xlsx')
# execute the describe() function and transpose the output so that it doesn't overflow the width of the screen
cc = df.describe().T
print(cc)

cc = df.info()
print(cc)

X = df[['SO2', 'CO', 'O3','CO2', 'Nox', 'NO', 'NO2', 'THC', 'NMHC', 'CH4', 'WindSpeed','TEMP','Humidity']]

y = df['PM25']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=23)

X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=23)

X_train.shape, X_test.shape, X_val.shape  
print("Training instances   {}, Training features   {}".format(X_train.shape[0], X_train.shape[1]))  
print("Validation instances {}, Validation features {}".format(X_val.shape[0], X_val.shape[1]))  
print("Testing instances    {}, Testing features    {}".format(X_test.shape[0], X_test.shape[1])) 

feature_cols = [tf.feature_column.numeric_column(col) for col in X.columns]  

regressor = tf.estimator.DNNRegressor(feature_columns=feature_cols,  
                                      hidden_units=[50, 50],
                                      model_dir='tf_wx_model')

def wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400):  
    return tf.estimator.inputs.pandas_input_fn(x=X,
                                               y=y,
                                               num_epochs=num_epochs,
                                               shuffle=shuffle,
                                               batch_size=batch_size)

wx_input_fn(X, y=None, num_epochs=None, shuffle=True, batch_size=400)

evaluations = []  
STEPS = 400  
for i in range(100):  
    regressor.train(input_fn=wx_input_fn(X_train, y=y_train), steps=STEPS)
    evaluations.append(regressor.evaluate(input_fn=wx_input_fn(X_val,
                                                               y_val,
                                                               num_epochs=1,
                                                               shuffle=False)))

cc = evaluations[0]
print(cc)

# manually set the parameters of the figure to and appropriate size
plt.rcParams['figure.figsize'] = [14, 10]

loss_values = [ev['loss'] for ev in evaluations]  
training_steps = [ev['global_step'] for ev in evaluations]

plt.scatter(x=training_steps, y=loss_values)  
plt.xlabel('Training steps (Epochs = steps / 2)')  
plt.ylabel('Loss (SSE)')  
plt.show()  

pred = regressor.predict(input_fn=wx_input_fn(X_test,  
                                              num_epochs=1,
                                              shuffle=False))
predictions = np.array([p['predictions'][0] for p in pred])

print("The Explained Variance: %.2f" % explained_variance_score(  
                                            y_test, predictions))  
print("The Mean Absolute Error: %.2f " % mean_absolute_error(  
                                            y_test, predictions))  
print("The Median Absolute Error: %.2f " % median_absolute_error(  
                                            y_test, predictions))


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
