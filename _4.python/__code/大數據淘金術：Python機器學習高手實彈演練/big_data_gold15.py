import sys

import pandas as pd

print('------------------------------------------------------------')	#60個

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
# 做時序圖觀察基本的趨勢和週期
data = pd.read_csv('AirPassengers.csv')
ts = data['#Passengers']
plt.plot(ts)

plt.show()

print('------------------------------------------------------------')	#60個

# 分析平穩性，正態性，週期性；並對數據進行轉換
ts_log = np.log(ts)
ts_diff = ts_log.diff(1) 
ts_diff = ts_diff.dropna() 
plt.plot(ts_diff)

plt.show()

print('------------------------------------------------------------')	#60個


# 做自相關和偏自相關圖，確定模型階次
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

f = plot_acf(ts_diff)
plt.show()

f = plot_pacf(ts_diff, method='ols')
plt.show()

print('------------------------------------------------------------')	#60個

""" fail
# 訓練模型
from statsmodels.tsa.arima_model import ARIMA

model = ARIMA(ts_log, order=(2, 1, 2))  
results_ARIMA = model.fit(disp=-1)  
plt.plot(ts_diff, color='#ffff00')
plt.plot(results_ARIMA.fittedvalues, color='#0000ff')

plt.show()
"""

print('------------------------------------------------------------')	#60個

""" fail
# 轉換回原始波形
pred_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
pred_diff_cumsum = pred_diff.cumsum()
pred_log = pd.Series(ts_log.ix[0], index=ts_log.index)
pred_log = pred_log.add(pred_diff_cumsum,fill_value=0)
pred = np.exp(pred_log)
plt.plot(ts)
plt.plot(pred)

plt.show()
"""

'''
print('------------------------------------------------------------')	#60個

print('傅里葉變換')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 將頻域數據轉換成時序數據
# bins爲頻域數據，n設置使用前多少個頻域數據，loop設置生成數據的長度
def fft_combine(bins, n, loops=1):
    length = int(len(bins) * loops)
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(bins[:n]):
        if k != 0 : p *= 2 # 除去直流成分之外, 其餘的係數都乘2
        data += np.real(p) * np.cos(k*index) # 餘弦成分的係數爲實數部分
        data -= np.imag(p) * np.sin(k*index) # 正弦成分的係數爲負的虛數部分
    return index, data

if __name__ == '__main__':
    data = pd.read_csv('AirPassengers.csv')
    ts = data['#Passengers']

    # 平穩化
    ts_log = np.log(ts)
    ts_diff = ts_log.diff(1) # 差分
    ts_diff = ts_diff.dropna() # 去除空數據
    fy = np.fft.fft(ts_diff)
    print(fy[:10]) # 顯示前10個頻域數據
    conv1 = np.real(np.fft.ifft(fy)) # 逆變換
    index, conv2 = fft_combine(fy / len(ts_diff), int(len(fy)/2-1), 1.3) # 只關心一半數據
    plt.plot(ts_diff)
    plt.plot(conv1 - 0.5) # 爲看清楚，將顯示區域下拉0.5
    plt.plot(conv2 - 1)
    plt.show()

print('------------------------------------------------------------')	#60個

print('小波變換')

import pywt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('AirPassengers.csv')
ts = data['#Passengers']
ts_log = np.log(ts)
ts_diff = ts_log.diff(1) 
ts_diff = ts_diff.dropna() 

cA,cD = pywt.dwt(ts_diff, 'db2')
cD = np.zeros(len(cD))
new_data = pywt.idwt(cA, cD, 'db2')

plt.plot(ts_diff)
plt.plot(new_data - 0.5) 
plt.show()


print('------------------------------------------------------------')	#60個

""" pip 失敗
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import tushare as ts
from fbprophet import Prophet
import matplotlib.pyplot as plt
import datetime

# 數據準備
base = ts.get_hist_data('000002')
df = pd.DataFrame()
df['y'] = base['volume']
df['ds'] = base.index

# 日期插補
ds = df['ds'].min()
arr = []
while ds < df['ds'].max():
    ds = str(pd.to_datetime(ds) + datetime.timedelta(days=1))[:10]
    if ds not in np.array(df['ds']):
        arr.append({'ds':ds, 'y':0}) # 以字典方式加入數組
tmp = pd.DataFrame(arr)
df = pd.concat([tmp, df])
df = df.reset_index(drop=True)
df = df.sort_values(['ds'])


holidays = pd.read_csv('holiday.csv')

prophet = Prophet(holidays=holidays) 
prophet.fit(df)  
future = prophet.make_future_dataframe(freq='D',periods=30)  # 測試之後三十天
forecasts = prophet.predict(future)  

prophet.plot(forecasts).show() 
prophet.plot_components(forecasts).show() 
plt.show()
"""

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



import os
import sys

import numpy as np
import pandas as pd

print('------------------------------------------------------------')	#60個

import warnings
warnings.filterwarnings('ignore')


import cv2
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
cv_img = cv2.imread(filename)
width=cv_img.shape[1]
height=cv_img.shape[0]
print(width)
print(height)

from PIL import Image

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

img = Image.open(filename)

mask = np.zeros([10, 5, 3], dtype=np.uint8)
#print(mask)
occlusion = np.logical_not(mask[:, :, -1]).astype(np.uint8)

#print(mask)

#mask[:, :, i] = mask[:, :, i] * occlusion
#occlusion = np.logical_and(occlusion, np.logical_not(mask[:, :, i]))

print('------------------------------------------------------------')	#60個

sys.path.append(os.path.dirname(os.getcwd()))
import skimage.io

ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
image = skimage.io.imread(filename)

print('------------------------------------------------------------')	#60個


