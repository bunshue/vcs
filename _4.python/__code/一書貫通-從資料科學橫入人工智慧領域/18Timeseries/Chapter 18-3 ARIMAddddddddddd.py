"""
Chapter 15-2 ARIMA

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


#1.平稳时间序列分析-ARMA模型
#1.1 AR

import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

#不要顯示一些警告
import warnings
warnings.filterwarnings("ignore")


#dta=AR
ts_simu200= pd.read_csv('ts_simu200.csv',index_col='t')
dates=pd.date_range(start='2017/01/01', periods=200)
ts_simu200.set_index(dates, inplace=True)
dta=ts_simu200['AR1_a']

dta.plot(figsize=(12,8))
plt.show()

#自相关和偏自相关
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(dta,lags=20)#lags 表示滞后的阶数
fig = sm.graphics.tsa.plot_pacf(dta,lags=20)
plt.show()

ar10 = sm.tsa.ARMA(dta,(1,0)).fit()


# In[ ]:


#检验下残差序列：
resid = ar10.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)
plt.show()

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
plt.show()
#结果表明基本符合正态分布

predict_dta = ar10.forecast(steps=5)
import datetime
fig = ar10.plot_predict(pd.to_datetime('2017-01-01')+datetime.timedelta(days=190),
                        pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), dynamic=False, plot_insample=True)
plt.show()

#1.2 MA

from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

#dta=MA
ts_simu200= pd.read_csv('ts_simu200.csv',index_col='t')
dates=pd.date_range(start='2017/01/01', periods=200)
ts_simu200.set_index(dates, inplace=True)
dta=ts_simu200['MA1_a']

#自相关和偏自相关
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(dta,lags=20)#lags 表示滞后的阶数
fig = sm.graphics.tsa.plot_pacf(dta,lags=20)

plt.show()

ma01 = sm.tsa.ARMA(dta,(0,1)).fit()

#检验下残差序列：
resid = ma01.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)
plt.show()

#进一步进行D-W检验，是目前检验自相关性最常用的方法，但它只使用于检验一阶自相关性。
#DW＝４＜＝＞ρ＝－１　即存在负自相关性
#DW＝２＜＝＞ρ＝０　　即不存在（一阶）自相关性
#因此，当DW值显著的接近于O或４时，则存在自相关性，而接近于２时，则不存在（一阶）自相关性。

print(sm.stats.durbin_watson(ma01.resid.values))
#观察是否符合正态分布,这里使用QQ图，它用于直观验证一组数据是否来自某个分布，或者验证某两组数据是否来自同一（族）分布。
print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
fig = qqplot(resid, line='q', fit=True)
plt.show()
#结果表明基本符合正态分布

import datetime
fig = ma01.plot_predict(pd.to_datetime('2017-01-01'),
                        pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), 
                        dynamic=False, plot_insample=True)
plt.show()

#1.3 ARMA

from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

#dta=ARMA
ts_simu200= pd.read_csv('ts_simu200.csv',index_col='t')
dates=pd.date_range(start='2017/01/01', periods=200)
ts_simu200.set_index(dates, inplace=True)
dta=ts_simu200['ARMA_11_b']
dta.head()

#自相关和偏自相关
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(dta,lags=20)#lags 表示滞后的阶数
fig = sm.graphics.tsa.plot_pacf(dta,lags=20)
plt.show()

import warnings
import itertools
# 设置自相关(AR)、差分(I)、移动平均(MA)的三个参数的取值范围
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
# 忽略ARIMA模型无法估计出结果时的报警信息
import sys
warnings.filterwarnings("ignore")

best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None

for param in pdq:
    try:
        temp_model = sm.tsa.ARIMA(dta,param)
        results = temp_model.fit()
        if results.aic < best_aic:
            best_aic = results.aic
            best_pdq = param
            best_seasonal_pdq = param_seasonal
    except:
        continue
        
print("Best ARIMA{} model - AIC:{}".format(best_pdq, best_aic))

# Best ARIMA(1, 0, 1) model - AIC:594.4262237292969

arma11 = sm.tsa.ARMA(dta,(1,1)).fit()

#检验下残差序列：
resid = arma11.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)
plt.show()

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
plt.show()

import datetime
fig = arma11.plot_predict(pd.to_datetime('2017-01-01'),
                        pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), 
                          dynamic=False, plot_insample=True)
plt.show()

# 2.非平稳时间序列分析-ARIMA模型

from __future__ import print_function
import pandas as pd
import pandas as Series
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#dta=ARIMA_11_b
ts_simu200= pd.read_csv('ts_simu200.csv',index_col='t')
dates=pd.date_range(start='2017/01/01', periods=200)
ts_simu200.set_index(dates, inplace=True)
dta=ts_simu200['ARIMA_110']

#平稳性检验
result = adfuller(dta)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])

#ADF Statistic: -1.897349
#p-value: 0.333309

#原序列的自相关和偏自相关
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(dta,lags=20)
fig = sm.graphics.tsa.plot_pacf(dta,lags=20)
plt.show()
#print(dta)

#差分序列的时序图
diff1= dta.diff(1)
diff1.plot(figsize=(12,8))
plt.show()

#差分序列的自相关和偏自相关图
ddta = diff1
ddta.dropna(inplace=True)
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(ddta,lags=20)
fig = sm.graphics.tsa.plot_pacf(ddta,lags=20)
plt.show()

arima110 = sm.tsa.ARIMA(dta,(1,1,0)).fit()

#检验下残差序列：
resid = arima110.resid
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=20)
fig = sm.graphics.tsa.plot_pacf(resid, lags=20)
plt.show()

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
plt.show()

import datetime
fig = arima110.plot_predict(pd.to_datetime('2017-01-01'),
                            pd.to_datetime('2017-01-01')+datetime.timedelta(days=220), 
                            dynamic=False, plot_insample=True)
plt.show()

#3.自动寻找ARIMA参数


#dta=ARIMA_11_b
ts_simu200= pd.read_csv('ts_simu200.csv',index_col='t')
dates=pd.date_range(start='2017/01/01', periods=200)
ts_simu200.set_index(dates, inplace=True)
dta=ts_simu200['ARIMA_110']
cc = dta.head()
print(cc)

import warnings
import itertools
# 设置自相关(AR)、差分(I)、移动平均(MA)的三个参数的取值范围
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
# 忽略ARIMA模型无法估计出结果时的报警信息
import sys
warnings.filterwarnings("ignore")

best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None

for param in pdq:
    try:
        temp_model = sm.tsa.ARIMA(dta,param)
        results = temp_model.fit()
        if results.aic < best_aic:
            best_aic = results.aic
            best_pdq = param
    except:
        continue
        
print("Best ARIMA{} model - AIC:{}".format(best_pdq, best_aic))

#Best ARIMA(1, 1, 0) model - AIC:545.9023842214676


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

