import pandas as pd
import matplotlib.pyplot as plt

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

'''
#case1
df = pd.read_csv("hours_used_performance.csv")
df.plot(kind="scatter", 
        x="hours_used",
        y="work_performance")
print(df.corr())
'''

'''
#case2
df = pd.read_csv("fb_tracking_happiness.csv")
print(df.head())

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
np_std = scaler.fit_transform(df)
df_std = pd.DataFrame(np_std, 
                      columns=["fb_tracking_s",
                               "happiness_s"])
print(df_std.head())

df_std.plot(kind="scatter",
            x="fb_tracking_s",
            y="happiness_s")

'''
#case3
df = pd.read_csv("fb_tracking_happiness.csv")
print(df.head())

from sklearn import preprocessing

scaler = preprocessing.MinMaxScaler(
                       feature_range=(0, 1))
np_minmax = scaler.fit_transform(df)
df_minmax = pd.DataFrame(np_minmax,
                         columns=["fb_tracking_m",
                                  "happiness_m"])
print(df_minmax.head())

df_minmax.plot(kind="scatter",
               x="fb_tracking_m",
               y="happiness_m")

plt.show()



