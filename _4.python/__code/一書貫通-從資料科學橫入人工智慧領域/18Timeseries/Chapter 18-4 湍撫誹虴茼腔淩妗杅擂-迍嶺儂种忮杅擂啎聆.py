
# coding: utf-8

# # 15章 3节 拖拉机销售数据预测

# ## 1 数据整理

# In[1]:


import warnings
import itertools

import pandas as pd
import numpy as np

import statsmodels.api as sm
import statsmodels.tsa.api as smt
import statsmodels.formula.api as smf

import matplotlib.pyplot as plt

import os
os.chdir(r"D:\Python_book\18Timeseries")
# In[2]:


sales_data = pd.read_csv('tractor_sales.csv')
sales_data.head(2)


# In[3]:


# since the complete date was not mentioned, we assume that it was the first of every month
dates = pd.date_range(start='2003-01-01', freq='MS', periods=len(sales_data))


# In[4]:


import calendar
sales_data['Month'] = dates.month
sales_data['Month'] = sales_data['Month'].apply(lambda x: calendar.month_abbr[x])
sales_data['Year'] = dates.year


# In[5]:


sales_data.drop(['Month-Year'], axis=1, inplace=True)
sales_data.rename(columns={'Number of Tractor Sold':'Tractor-Sales'}, inplace=True)
sales_data = sales_data[['Month', 'Year', 'Tractor-Sales']]


# In[6]:


# set the dates as the index of the dataframe, so that it can be treated as a time-series dataframe
sales_data.set_index(dates, inplace=True)


# In[7]:


# check out first 5 samples of the data
sales_data.head(5)


# In[8]:


# extract out the time-series
sales_ts = sales_data['Tractor-Sales']


# In[9]:


sales_data = pd.read_csv('tractor_sales.csv')
plt.figure(figsize=(10, 5))
plt.plot(sales_ts)
plt.xlabel('Years')
plt.ylabel('Tractor Sales')


# ## 2 趋势分解

# In[ ]:


#decomposition = sm.tsa.seasonal_decompose(sales_ts, model='multiplicative')
#fig = decomposition.plot()
#fig.set_figwidth(12)
#fig.set_figheight(8)
#fig.suptitle('Decomposition of multiplicative time series')
#plt.show()


# ## 3 构建ARIMA

# - 3.1 进行必要的数值转换

# In[10]:


plt.figure(figsize=(10, 5))
plt.plot(np.log(sales_ts))
plt.xlabel('Years')
plt.ylabel('Log (Tractor Sales)')


# - 3.2 选择合适的差分阶数

# In[11]:


plt.figure(figsize=(10, 5))
plt.plot(np.log(sales_ts).diff(periods=1))
plt.xlabel('Years')
plt.ylabel('Differenced Log (Tractor Sales)')


# In[12]:


sales_ts_log = np.log(sales_ts)
sales_ts_log.dropna(inplace=True)

sales_ts_log_diff = sales_ts_log.diff(periods=1) 
sales_ts_log_diff.dropna(inplace=True)

fig, axes = plt.subplots(1, 2, sharey=False, sharex=False)
fig.set_figwidth(12)
fig.set_figheight(4)
smt.graphics.plot_acf(sales_ts_log_diff, lags=30, ax=axes[0], alpha=0.5)
smt.graphics.plot_pacf(sales_ts_log_diff, lags=30, ax=axes[1], alpha=0.5)
plt.tight_layout()


# - 3.3 确定参数

# In[ ]:


# 设置自相关(AR)、差分(I)、移动平均(MA)的三个参数的取值范围
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
# 设置季节效应的自相关(AR)、差分(I)、移动平均(MA)的三个参数的取值范围
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]


# In[ ]:


import sys
warnings.filterwarnings("ignore") # 忽略ARIMA模型无法估计出结果时的报警信息
best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None

for param in pdq:
    for param_seasonal in seasonal_pdq:        
        try:
            temp_model = sm.tsa.statespace.SARIMAX(sales_ts_log,
                                             order = param,
                                             seasonal_order = param_seasonal,
                                             enforce_stationarity=True,
                                             enforce_invertibility=True)
            results = temp_model.fit()
            if results.aic < best_aic:
                best_aic = results.aic
                best_pdq = param
                best_seasonal_pdq = param_seasonal
        except:
            continue
print("Best SARIMAX{}x{}12 model - AIC:{}".format(best_pdq, best_seasonal_pdq, best_aic))


# In[13]:


best_model = sm.tsa.statespace.SARIMAX(sales_ts_log,
                                      order=(0, 1, 1),
                                      seasonal_order=(1, 0, 1, 12),
                                      enforce_stationarity=True,
                                      enforce_invertibility=True)
best_results = best_model.fit()


# In[ ]:


print(best_results.summary().tables[0])
print(best_results.summary().tables[1])


# - 3.4 对残差进行检验

# In[16]:


best_results.plot_diagnostics(lags=30, figsize=(16,12))
plt.show()


# - 3.5 进行预测


# In[29]:


import math
n_steps = 36
pred_uc_95 = best_results.get_forecast(steps=n_steps, alpha=0.05) 
pred_pr_95=pred_uc_95.predicted_mean
pred_ci_95 = pred_uc_95.conf_int()
idx = pd.date_range(sales_ts.index[-1], periods=n_steps, freq='MS')
fc_95 = pd.DataFrame(np.column_stack([np.power(math.e, pred_pr_95), 
                                      np.power(math.e, pred_ci_95)]), index=idx,
                               columns=['forecast', 'lower_ci_95', 'upper_ci_95'])
fc_95.head(2)


# In[28]:


axis = sales_ts.plot(label='Observed', figsize=(15, 6))
fc_95['forecast'].plot(ax=axis, label='Forecast', alpha=0.7)
axis.fill_between(fc_95.index, fc_95['lower_ci_95'], fc_95['upper_ci_95'], 
                  color='k', alpha=.25)
axis.set_xlabel('Years')
axis.set_ylabel('Tractor Sales')
plt.legend(loc='best')
plt.show()


#%%