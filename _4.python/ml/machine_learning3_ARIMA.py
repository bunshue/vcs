"""
各種自迴歸模型 Autoregressive model/AR

http://www.statsmodels.org/stable/tsa.html
http://ucanalytics.com/blogs/wp-content/uploads/2017/08/ARIMA-TimeSeries-Analysis-of-Tractor-Sales.html

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import datetime
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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# 忽略ARIMA模型无法估计出结果时的报警信息
# import warnings
# warnings.filterwarnings("ignore")

import statsmodels.api as sm

print("------------------------------------------------------------")  # 60個

"""
TimeSeries_data.csv 14筆資料 7個欄位
Date,Open,High,Low,Close,Adj Close,Volume

日期(Date)、開盤價(Open)、最高價(High)、最低價(Low)、
收盤價(Close)、調整後的收盤價(Adj Close)以及成交量(Volume)。

5/18/2019,7266.080078,8281.660156,7257.259766,8193.139648,8193.139648,723011166
5/19/2019,8193.139648,8193.139648,7591.850098,7998.290039,7998.290039,637617163
5/20/2019,7998.290039,8102.319824,7807.77002,7947.930176,7947.930176,357803946
5/21/2019,7947.930176,8033.759766,7533.660156,7626.890137,7626.890137,424501866
5/22/2019,7626.890137,7971.259766,7478.740234,7876.5,7876.5,386766321
5/23/2019,7876.5,8165.450195,7801.569824,7996.399902,7996.399902,413162746
5/24/2019,7996.399902,8140.819824,7948.680176,8059.129883,8059.129883,179206342
5/25/2019,8059.129883,8779,7894.529785,8726.230469,8726.230469,483663699
5/26/2019,8726.230469,8931.530273,8668.459961,8785.169922,8785.169922,507164714
5/27/2019,8785.169922,8818.709961,8562.200195,8718.849609,8718.849609,360752199
5/28/2019,8718.849609,8760.480469,8444.099609,8664.55957,8664.55957,380343928
5/29/2019,8664.55957,9065.889648,8027.209961,8276.25,8276.25,815525590
5/30/2019,8276.25,8570.780273,8116,8560.080078,8560.080078,500141087
5/31/2019,8550.629883,8576.339844,8459.650391,8504.980469,8504.980469,69915456
"""
print("自回归模型AR（Autoregressive model/AR）")
# 通俗一点讲，就是用过去时间点的数据预测未来时间点的数据

IndexData = pd.read_csv("./data/TimeSeries_data.csv")

print(IndexData)
print(IndexData.shape)

print("取出 收盤價(Close) 欄資料")
data = IndexData["Close"]  # 选择关闭交易时的数据
temp = np.array(data)  # 转换成数组

model = sm.tsa.AutoReg(temp, lags=1)  # 训练模型

results_AR = model.fit()  # 训练模型

plt.figure(figsize=(10, 6))
plt.plot(temp, "r", label="Close")
# results_AR.fittedvalues是模型拟合后的结果
plt.plot(results_AR.fittedvalues, "g", label="AR model")
plt.title("自回归模型AR（Autoregressive model/AR）")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個

print("滑动平均模型（moving average model/MA）")

# 滑动平均（moving average model/MA）模型也称移动平均模型，是用过去各个时期的随机干扰或预测误差的线性组合来表达当前预测值。
"""
python实现
报错记录：AttributeError: module ‘statsmodels.tsa.api’ has no attribute ‘ARMA’
从版本 0.12 开始，statsmodels 库不再具有单独的 ARMA 类。应该使用 ARIMA 类，该类可以处理自回归 （AR） 和移动平均 （MA） 分量。
"""
IndexData = pd.read_csv("./data/TimeSeries_data.csv")
data = IndexData["Close"]
temp = np.array(data)

model = sm.tsa.ARIMA(temp, order=(0, 0, 10))
results_MA = model.fit()

plt.figure(figsize=(10, 6))
plt.plot(temp, "b", label="Close")
plt.plot(results_MA.fittedvalues, color="red", label="MA")
plt.legend(fontsize=15)
plt.title("滑动平均模型（moving average model/MA）")

show()

print("------------------------------------------------------------")  # 60個

print("自回归滑动平均（Autoregressive moving average model/ARMA）模型")
# ARMA模型就是AR模型和MA模型混合

# ARMA(p pp,0) 模型就是 AR(p pp) 模型
# ARMA(0,q qq) 模型就是 MA(q qq) 模型

IndexData = pd.read_csv("./data/TimeSeries_data.csv")
data = IndexData["Close"]
temp = np.array(data)
p = 3
q = 10
model = sm.tsa.ARIMA(temp, order=(p, 0, q))
results_ARMA = model.fit()

plt.figure(figsize=(10, 6))
plt.plot(temp, "b", label="Close")
plt.plot(results_ARMA.fittedvalues, "r", label="ARMA model")
plt.legend()
plt.title("自回归滑动平均（Autoregressive moving average model/ARMA）模型")

show()

print("------------------------------------------------------------")  # 60個

print("自回归差分滑动平均（Autoregressive Integrated Moving Average model/ARIMA）模型")
"""
ARIMA模型在ARMA模型基础上考虑了时间序列的差分，ARIMA模型有三个参数ARIMA(p,d,q)，p为自回归AR项数，q为滑动平均MA项数，d为使序列平稳所做的差分次数（阶数）。
差分后是对序列的差分的结果建立模型而不是真正的序列
"""

# 输出ARIMA模型的拟合效果图

IndexData = pd.read_csv("./data/TimeSeries_data.csv")
IndexData = IndexData.set_index(IndexData["Date"])

IndexData["colseDiff_1"] = IndexData["Close"].diff(1)  # 1阶差分处理
IndexData["closeDiff_2"] = IndexData["colseDiff_1"].diff(1)  # 2阶差分处理
IndexData.plot(subplots=True, figsize=(10, 6))

data = IndexData["closeDiff_2"]
temp = np.array(data)
p = 2
d = 2
q = 10
model = sm.tsa.ARIMA(temp, order=(p, d, q))
results_ARIMA = model.fit()
plt.figure(figsize=(10, 6))
plt.plot(temp, "b", label="closeDiff_2")
plt.plot(results_ARIMA.fittedvalues, "r", label="ARIMA model")
plt.legend()
plt.title("自回归差分滑动平均（Autoregressive Integrated Moving Average model/ARIMA）模型")

show()

print("------------------------------------------------------------")  # 60個

# Autoregressive Moving Average (ARMA) Model

from statsmodels.tsa.arima_process import arma_generate_sample

np.random.seed(12345)

# Generate some data from an ARMA process:

arparams = np.array([0.75, -0.25])
maparams = np.array([0.65, 0.35])

arparams = np.r_[1, -arparams]
maparam = np.r_[1, maparams]
nobs = 250
y = arma_generate_sample(arparams, maparams, nobs)

dates = sm.tsa.datetools.dates_from_range("1980m1", length=nobs)
y = pd.Series(y, index=dates)
print(len(y))
print(y)

"""
arma_mod = sm.tsa.ARMA(y, freq='M')
arma_res = arma_mod.fit(order=(2,2), trend='nc', disp=-1)
"""

print("------------------------------------------------------------")  # 60個

# 1.平稳时间序列分析-ARMA模型 Autoregressive Moving Average (ARMA) Model
# 1.1 AR

from scipy import stats
from statsmodels.graphics.api import qqplot

# dta=AR
ts_simu200 = pd.read_csv("data/ts_simu200.csv", index_col="t")
dates = pd.date_range(start="2017/01/01", periods=200)
ts_simu200.set_index(dates, inplace=True)
dta = ts_simu200["AR1_a"]

dta.plot(figsize=(12, 8))

show()

# 自相关和偏自相关
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.tsa.plot_acf(dta, lags=20)  # lags 表示滞后的阶数
fig = sm.graphics.tsa.plot_pacf(dta, lags=20)

show()

"""
ar10 = sm.tsa.ARMA(dta,(1,0)).fit()

#检验下残差序列：
resid = ar10.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)

show()

#残差的ACF和PACF图，可以看到序列残差基本为白噪声
#进一步进行D-W检验，是目前检验自相关性最常用的方法，但它只使用于检验一阶自相关性。
#DW＝４＜＝＞ρ＝－１　即存在负自相关性
#DW＝２＜＝＞ρ＝０　　即不存在（一阶）自相关性
#因此，当DW值显著的接近于O或４时，则存在自相关性，而接近于２时，则不存在（一阶）自相关性。

print(sm.stats.durbin_watson(ar10.resid.values))
#观察是否符合正态分布,这里使用QQ图，它用于直观验证一组数据是否来自某个分布，或者验证某两组数据是否来自同一（族）分布。
print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
fig = qqplot(resid, line='q', fit=True)

show()

#结果表明基本符合正态分布

predict_dta = ar10.forecast(steps=5)
fig = ar10.plot_predict(pd.to_datetime('2017-01-01')+datetime.timedelta(days=190),
                        pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), dynamic=False, plot_insample=True)

show()
"""
print("------------------------------------------------------------")  # 60個

# 1.2 MA

# from __future__ import print_function

from scipy import stats
from statsmodels.graphics.api import qqplot

# dta=MA
ts_simu200 = pd.read_csv("data/ts_simu200.csv", index_col="t")
dates = pd.date_range(start="2017/01/01", periods=200)
ts_simu200.set_index(dates, inplace=True)
dta = ts_simu200["MA1_a"]

# 自相关和偏自相关
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.tsa.plot_acf(dta, lags=20)  # lags 表示滞后的阶数
fig = sm.graphics.tsa.plot_pacf(dta, lags=20)

show()

"""
ma01 = sm.tsa.ARMA(dta,(0,1)).fit()

#检验下残差序列：
resid = ma01.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)

show()

#进一步进行D-W检验，是目前检验自相关性最常用的方法，但它只使用于检验一阶自相关性。
#DW＝４＜＝＞ρ＝－１　即存在负自相关性
#DW＝２＜＝＞ρ＝０　　即不存在（一阶）自相关性
#因此，当DW值显著的接近于O或４时，则存在自相关性，而接近于２时，则不存在（一阶）自相关性。

print(sm.stats.durbin_watson(ma01.resid.values))
#观察是否符合正态分布,这里使用QQ图，它用于直观验证一组数据是否来自某个分布，或者验证某两组数据是否来自同一（族）分布。
print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
fig = qqplot(resid, line='q', fit=True)

show()

#结果表明基本符合正态分布

fig = ma01.plot_predict(pd.to_datetime('2017-01-01'),
                        pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), 
                        dynamic=False, plot_insample=True)

show()
"""
print("------------------------------------------------------------")  # 60個

# 1.3 ARMA

# from __future__ import print_function

from scipy import stats
from statsmodels.graphics.api import qqplot

# dta=ARMA
ts_simu200 = pd.read_csv("data/ts_simu200.csv", index_col="t")
dates = pd.date_range(start="2017/01/01", periods=200)
ts_simu200.set_index(dates, inplace=True)
dta = ts_simu200["ARMA_11_b"]
dta.head()

# 自相关和偏自相关
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.tsa.plot_acf(dta, lags=20)  # lags 表示滞后的阶数
fig = sm.graphics.tsa.plot_pacf(dta, lags=20)

show()

import itertools

# 设置自相关(AR)、差分(I)、移动平均(MA)的三个参数的取值范围
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))

best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None

for param in pdq:
    try:
        temp_model = sm.tsa.ARIMA(dta, param)
        results = temp_model.fit()
        if results.aic < best_aic:
            best_aic = results.aic
            best_pdq = param
            best_seasonal_pdq = param_seasonal
    except:
        continue

print("Best ARIMA{} model - AIC:{}".format(best_pdq, best_aic))

# Best ARIMA(1, 0, 1) model - AIC:594.4262237292969
"""
arma11 = sm.tsa.ARMA(dta,(1,1)).fit()

#检验下残差序列：
resid = arma11.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)

show()

#残差的ACF和PACF图，可以看到序列残差基本为白噪声

#进一步进行D-W检验，是目前检验自相关性最常用的方法，但它只使用于检验一阶自相关性。
#DW＝４＜＝＞ρ＝－１　即存在负自相关性
#DW＝２＜＝＞ρ＝０　　即不存在（一阶）自相关性
#因此，当DW值显著的接近于O或４时，则存在自相关性，而接近于２时，则不存在（一阶）自相关性。

print(sm.stats.durbin_watson(arma11.resid.values))
#观察是否符合正态分布,这里使用QQ图，它用于直观验证一组数据是否来自某个分布，或者验证某两组数据是否来自同一（族）分布。
print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
fig = qqplot(resid, line='q', fit=True)

show()

fig = arma11.plot_predict(pd.to_datetime('2017-01-01'),
                        pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), 
                          dynamic=False, plot_insample=True)
show()
"""
print("------------------------------------------------------------")  # 60個

# 2.非平稳时间序列分析-ARIMA模型

from scipy import stats
from statsmodels.graphics.api import qqplot
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

# dta=ARIMA_11_b
ts_simu200 = pd.read_csv("data/ts_simu200.csv", index_col="t")
dates = pd.date_range(start="2017/01/01", periods=200)
ts_simu200.set_index(dates, inplace=True)
dta = ts_simu200["ARIMA_110"]

# 平稳性检验
result = adfuller(dta)
print("ADF Statistic: %f" % result[0])
print("p-value: %f" % result[1])

# ADF Statistic: -1.897349
# p-value: 0.333309

# 原序列的自相关和偏自相关
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.tsa.plot_acf(dta, lags=20)
fig = sm.graphics.tsa.plot_pacf(dta, lags=20)

show()

# print(dta)

# 差分序列的时序图
diff1 = dta.diff(1)
diff1.plot(figsize=(12, 8))

show()

# 差分序列的自相关和偏自相关图
ddta = diff1
ddta.dropna(inplace=True)
fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.tsa.plot_acf(ddta, lags=20)
fig = sm.graphics.tsa.plot_pacf(ddta, lags=20)

show()

""" NG
arima110 = sm.tsa.ARIMA(dta,(1,1,0)).fit()

#检验下残差序列：
resid = arima110.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)

show()

#残差的ACF和PACF图，可以看到序列残差基本为白噪声

#进一步进行D-W检验，是目前检验自相关性最常用的方法，但它只使用于检验一阶自相关性。
#DW＝４＜＝＞ρ＝－１　即存在负自相关性
#DW＝２＜＝＞ρ＝０　　即不存在（一阶）自相关性
#因此，当DW值显著的接近于O或４时，则存在自相关性，而接近于２时，则不存在（一阶）自相关性。

print(sm.stats.durbin_watson(arima110.resid.values))
#观察是否符合正态分布,这里使用QQ图，它用于直观验证一组数据是否来自某个分布，或者验证某两组数据是否来自同一（族）分布。
print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
fig = qqplot(resid, line='q', fit=True)

show()

fig = arima110.plot_predict(pd.to_datetime('2017-01-01'),
                        pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), 
                            dynamic=False, plot_insample=True)
show()
"""
print("------------------------------------------------------------")  # 60個

# 3.自动寻找ARIMA参数

# dta=ARIMA_11_b
ts_simu200 = pd.read_csv("data/ts_simu200.csv", index_col="t")
dates = pd.date_range(start="2017/01/01", periods=200)
ts_simu200.set_index(dates, inplace=True)
dta = ts_simu200["ARIMA_110"]
cc = dta.head()
print(cc)

import itertools

# 设置自相关(AR)、差分(I)、移动平均(MA)的三个参数的取值范围
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))

best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None

for param in pdq:
    try:
        temp_model = sm.tsa.ARIMA(dta, param)
        results = temp_model.fit()
        if results.aic < best_aic:
            best_aic = results.aic
            best_pdq = param
            best_seasonal_pdq = param_seasonal
    except:
        continue

print("Best ARIMA{} model - AIC:{}".format(best_pdq, best_aic))

# Best ARIMA(1, 1, 0) model - AIC:545.9023842214676

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 做時序圖觀察基本的趨勢和週期
data = pd.read_csv("data/AirPassengers.csv")
ts = data["#Passengers"]

plt.plot(ts)
plt.title("旅客人數")
show()

print("------------------------------")  # 30個

# 分析平穩性，正態性，週期性；並對數據進行轉換
ts_log = np.log(ts)
ts_diff = ts_log.diff(1)
ts_diff = ts_diff.dropna()

plt.plot(ts_diff)
plt.title("旅客人數 => log => diff")
show()

print("------------------------------")  # 30個

# 做自相關和偏自相關圖，確定模型階次
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

f = plot_acf(ts_diff)
plt.title("plot_acf 自相關圖")
show()

f = plot_pacf(ts_diff, method="ols")
plt.title("plot_pacf 偏自相關圖")
show()

print("------------------------------")  # 30個

# 訓練模型
import statsmodels.api as smapi

model = smapi.tsa.arima.ARIMA(ts_log, order=(2, 1, 2))

results_ARIMA = model.fit()

plt.plot(ts_diff, color="r")
plt.plot(results_ARIMA.fittedvalues, color="g")

plt.title("ARIMA")
show()

cc = sum((results_ARIMA.fittedvalues - ts_log) ** 2)
print("RSS: %.4f" % cc)

print("------------------------------")  # 30個

# 轉換回原始波形
pred_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
pred_diff_cumsum = pred_diff.cumsum()
pred_log = pd.Series(ts_log, index=ts_log.index)
pred_log = pred_log.add(pred_diff_cumsum, fill_value=0)
pred = np.exp(pred_log)
plt.plot(ts)
plt.plot(pred)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
