import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

f_tracking= [110, 1018, 1130, 417, 626,
             957, 90, 951, 946, 797,
             981, 125, 456, 731, 1640,
             486, 1309, 472, 1133, 1773,
             906, 532, 742, 621, 855]
happiness = [0.3, 0.8, 0.5, 0.4, 0.6,
             0.4, 0.7, 0.5, 0.4, 0.3, 
             0.3, 0.6, 0.2, 0.8, 1,
             0.6, 0.2, 0.7, 0.5, 0.7,
             0.1, 0.4, 0.3, 0.6, 0.3]

df = pd.DataFrame({"FB追蹤數" : f_tracking,
                   "快樂程度" : happiness})
print(df.head())
print("---------------------------")
df_scaled = pd.DataFrame(preprocessing.scale(df), 
            columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_scaled.head())
df_scaled.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")
print("---------------------------")
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
np_minmax = scaler.fit_transform(df)
df_minmax = pd.DataFrame(np_minmax,
            columns=["最小最大值縮放FB追蹤數", "最小最大值縮放快樂程度"])
print(df_minmax.head())
df_minmax.head().to_html("ch13-2-2.html")

df_minmax.plot(kind="scatter", x="最小最大值縮放FB追蹤數",
               y="最小最大值縮放快樂程度")
plt.show()