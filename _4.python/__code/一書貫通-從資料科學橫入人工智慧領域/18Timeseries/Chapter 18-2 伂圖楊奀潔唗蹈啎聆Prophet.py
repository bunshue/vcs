import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

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

my_model.plot_components(forecast)

# ## 乘法模型的实现

import numpy as np

df['y'] = np.log(df['y'])
my_model = Prophet(growth='linear',interval_width=0.95)
my_model.fit(df)
future_dates = my_model.make_future_dataframe(periods=36, freq='MS')
forecast = my_model.predict(future_dates)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(2)
my_model.plot(forecast,uncertainty=True)


import math

my_model = Prophet(growth='linear',interval_width=0.95)
my_model.fit(df)
future_dates = my_model.make_future_dataframe(periods=36, freq='MS')
forecast = my_model.predict(future_dates)
forecast['yhat']=np.power(math.e, forecast['yhat'])
forecast['yhat_lower']=np.power(math.e, forecast['yhat_lower'])
forecast['yhat_upper']=np.power(math.e, forecast['yhat_upper'])
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(2)
my_model.plot(forecast,uncertainty=True)

forecast.tail(2)

