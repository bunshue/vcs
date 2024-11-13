"""
20190405-空氣盒子數據時間序列預測(全高雄198211-201811)-使用多種不同統計模型

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

#自回归模型AR（Autoregressive model/AR）

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm  # 导入模型

df = pd.read_excel('./data/TimeSeries_198211-201811b.xlsx')

data = df['PM25']  # 选择关闭交易时的数据
temp = np.array(data)  # 转换成数组
model =sm.tsa.AutoReg(temp,lags = 1)  # 训练模型 
results_AR = model.fit() # 训练模型

plt.figure(figsize=(20,10)) 
plt.plot(temp,'b',label='PM25')
plt.plot (results_AR.fittedvalues,'r',label='AR model')  # results_AR.fittedvalues是模型拟合后的结果
plt.legend()


#滑动平均模型（moving average model/MA）

#滑动平均（moving average model/MA）模型也称移动平均模型，
#是用过去各个时期的随机干扰或预测误差的线性组合来表达当前预测值。

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_excel('./data/TimeSeries_198211-201811b.xlsx')

data = df['PM25']
temp = np.array(data)

model = sm.tsa.ARIMA(temp, order=(0, 0, 10))
results_MA = model.fit()

plt.figure(figsize=(20, 10))
plt.plot(temp, 'b', label='PM25')
plt.plot(results_MA.fittedvalues,color = 'red',label ='MA')
plt.legend(fontsize = 15)
plt.show()


#自回归滑动平均（Autoregressive moving average model/ARMA）模型

#ARMA模型就是AR模型和MA模型混合

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_excel('./data/TimeSeries_198211-201811b.xlsx')

data = df['PM25']
temp =np.array(data)
p = 3
q = 10
model = sm.tsa.ARIMA (temp,order=(p,0,q))
results_ARMA = model.fit()

plt.figure(figsize=(20,4*5))
plt.plot(temp,'b',label='PM25')
plt.plot(results_ARMA.fittedvalues,'r',label='ARMA model')
plt.legend()
plt.show()


#自回归差分滑动平均（Autoregressive Integrated Moving Average model/ARIMA）模型

#ARIMA模型在ARMA模型基础上考虑了时间序列的差分，ARIMA模型有三个参数ARIMA(p,d,q)，
#p为自回归AR项数，q为滑动平均MA项数，d为使序列平稳所做的差分次数（阶数）。

# 输出ARIMA模型的拟合效果图
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_excel('./data/TimeSeries_198211-201811b.xlsx')
df = df.set_index(df['Date'])

df['colseDiff_1']=df['PM25'].diff(1)#1阶差分处理
df['closeDiff_2']=df['colseDiff_1'].diff(1)#2阶差分处理
df.plot(subplots=True,figsize=(20,15))

data = df['closeDiff_2']
temp = np.array (data)
p=2;d = 2;q=10
model = sm.tsa.ARIMA(temp,order = (p,d,q))
results_ARIMA = model.fit()
plt.figure (figsize=(20,10))
plt.plot (temp,'b',label='closeDiff_2')
plt.plot (results_ARIMA.fittedvalues,'r',label='ARIMA model')
plt.legend()

plt.show()

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 以每月平均資料進行分析
# +12代表未來12個月的數值

# Autoregression (AR)

import statsmodels.api as sm  # 导入模型

df_pm25 = pd.read_excel("data/TimeSeries_198211-201811b.xlsx").PM25

# fit model
model = sm.tsa.AutoReg(df_pm25, lags = 1)  # 训练模型 

model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(df_pm25), len(df_pm25) + 12)
print(yhat)
plt.plot(yhat)
plt.yticks([30, 40])

plt.show()

print("------------------------------------------------------------")  # 60個

# Moving Average (MA)

from random import random

df_pm25 = pd.read_excel("data/TimeSeries_198211-201811.xlsx").PM25

model = sm.tsa.ARIMA(df_pm25, order=(0, 0, 10))

model_fit = model.fit()

# make prediction
yhat = model_fit.predict(len(df_pm25), len(df_pm25) + 12)

print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個

# Autoregressive Moving Average (ARMA)

from random import random

df_pm25 = pd.read_excel("data/TimeSeries_198211-201811.xlsx").PM25

model = sm.tsa.ARIMA(df_pm25, order=(0, 0, 10))

model_fit = model.fit()

# make prediction
yhat = model_fit.predict(len(df_pm25), len(df_pm25) + 12)
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個

# Autoregressive Integrated Moving Average (ARIMA)

from random import random

df_pm25 = pd.read_excel("data/TimeSeries_198211-201811.xlsx").PM25

# fit model
model = sm.tsa.ARIMA(df_pm25, order=(1, 1, 1))

model_fit = model.fit()

# make prediction
yhat = model_fit.predict(len(df_pm25), len(df_pm25) + 12, typ="levels")
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個

# Seasonal Autoregressive Integrated Moving-Average with Exogenous Regressors (SARIMAX)

# SARIMA example
from statsmodels.tsa.statespace.sarimax import SARIMAX
from random import random

df_pm25 = pd.read_excel("data/TimeSeries_198211-201811.xlsx").PM25
""" NG
# fit model
model = SARIMAX(df_pm25, order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(df_pm25), len(df_pm25) + 12)
print(yhat)
plt.plot(yhat)

plt.show()
"""
print("------------------------------------------------------------")  # 60個

# Simple Exponential Smoothing (SES)

# SES example
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from random import random

df_pm25 = pd.read_excel("data/TimeSeries_198211-201811.xlsx").PM25

# fit model
model = SimpleExpSmoothing(df_pm25)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(df_pm25), len(df_pm25) + 12)
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
