"""
迴歸分析

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_excel('20160101-20190101(Daily)迴歸分析.xlsx')
#print(df)

cc = df.set_index('Date')
print(cc)

"""
df.dtypes
df.isnull().sum()
df.isnull().any()
"""

X = df[['SO2', 'CO', 'O3','PM10', 'Nox', 'NO', 'NO2', 'THC', 'NMHC', 'CH4', 'WindSpeed','TEMP','Humidity']].values

y = df['PM25'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
         normalize=False)

sns.heatmap(df.corr())

plt.show()

cc = df.corr()
print(cc)

y_pred = regressor.predict(X_test)


df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)
#print(df1)

df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
