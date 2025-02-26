"""
Chapter 18-2 Prophet

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

# pip install pandas matplotlib numpy cython
# pip install pystan

# 先安装：http://landinghub.visualstudio.com/visual-cpp-build-tools
# pip install fbprophet

from fbprophet import Prophet

df = pd.read_csv('AirPassengers.csv')
df['DATE'] = pd.to_datetime(df['DATE'])
df.head(2)

df.dtypes

df['DATE'] = pd.DatetimeIndex(df['DATE'])
df.dtypes

df = df.rename(columns={'DATE': 'ds',
                        'AIR': 'y'})
df.head(2)

ax = df.set_index('ds').plot(figsize=(12, 8))
ax.set_ylabel('Monthly Number of Airline Passengers')
ax.set_xlabel('Date')
plt.show()

# 设置趋势的形式和预测值的置信区间为95% 
my_model = Prophet(growth='linear',interval_width=0.95)
my_model.fit(df)

future_dates = my_model.make_future_dataframe(periods=36, freq='MS')
forecast = my_model.predict(future_dates)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(2)

my_model.plot(forecast,uncertainty=True)
plt.show()

my_model.plot_components(forecast)
plt.show()


#乘法模型的实现

df['y'] = np.log(df['y'])
my_model = Prophet(growth='linear',interval_width=0.95)
my_model.fit(df)
future_dates = my_model.make_future_dataframe(periods=36, freq='MS')
forecast = my_model.predict(future_dates)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(2)
my_model.plot(forecast,uncertainty=True)

#INFO:fbprophet.forecaster:Disabling weekly seasonality. Run prophet with weekly_seasonality=True to override this.
#INFO:fbprophet.forecaster:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.

my_model = Prophet(growth='linear',interval_width=0.95)
my_model.fit(df)
future_dates = my_model.make_future_dataframe(periods=36, freq='MS')
forecast = my_model.predict(future_dates)
forecast['yhat']=np.power(math.e, forecast['yhat'])
forecast['yhat_lower']=np.power(math.e, forecast['yhat_lower'])
forecast['yhat_upper']=np.power(math.e, forecast['yhat_upper'])
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(2)
my_model.plot(forecast,uncertainty=True)

#INFO:fbprophet.forecaster:Disabling weekly seasonality. Run prophet with weekly_seasonality=True to override this.
#INFO:fbprophet.forecaster:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.

#forecast.tail(2)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

