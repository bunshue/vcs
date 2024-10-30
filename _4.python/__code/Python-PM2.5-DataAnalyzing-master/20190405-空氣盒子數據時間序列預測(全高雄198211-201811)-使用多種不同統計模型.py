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

#以每月平均資料進行分析
#+12代表未來12個月的數值

import matplotlib.pyplot as plt

#Autoregression (AR)

# AR example
from statsmodels.tsa.ar_model import AR
import pandas as pd
# contrived dataset
data = pd.read_excel('TimeSeries_198211-201811b.xlsx').PM25
# fit model
model = AR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data)+12)
print(yhat)
plt.plot(yhat)
plt.yticks([30,40])

plt.show()

print("------------------------------------------------------------")  # 60個

#Moving Average (MA)

from statsmodels.tsa.arima_model import ARMA
from random import random

# contrived dataset
data = pd.read_excel('TimeSeries_198211-201811.xlsx').PM25
# fit model
model = ARMA(data, order=(0, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data)+12)
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個

#Autoregressive Moving Average (ARMA)

# ARMA example
from statsmodels.tsa.arima_model import ARMA
from random import random
# contrived dataset
data = pd.read_excel('TimeSeries_198211-201811.xlsx').PM25
# fit model
model = ARMA(data, order=(2, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data)+12)
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個

#Autoregressive Integrated Moving Average (ARIMA)

# ARIMA example
from statsmodels.tsa.arima_model import ARIMA
from random import random
# contrived dataset
data = pd.read_excel('TimeSeries_198211-201811.xlsx').PM25
# fit model
model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data)+12, typ='levels')
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個

#Seasonal Autoregressive Integrated Moving-Average with Exogenous Regressors (SARIMAX)

# SARIMA example
from statsmodels.tsa.statespace.sarimax import SARIMAX
from random import random
# contrived dataset
data = pd.read_excel('TimeSeries_198211-201811.xlsx').PM25
# fit model
model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data)+12)
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個

#Simple Exponential Smoothing (SES)

# SES example
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from random import random
# contrived dataset
data = pd.read_excel('TimeSeries_198211-201811.xlsx').PM25
# fit model
model = SimpleExpSmoothing(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data)+12)
print(yhat)
plt.plot(yhat)

plt.show()

print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
