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
df.head().to_html("ch13-2-1a-01.html")
print("---------------------------")
scaler = preprocessing.StandardScaler()
np_std = scaler.fit_transform(df)
df_std = pd.DataFrame(np_std,
         columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_std.head())
df_std.head().to_html("ch13-2-1a-02.html")

df_std.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")
plt.show()