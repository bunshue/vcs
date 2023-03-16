# 載入所需套件 import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 創造一些隨機資料 create some data with random value
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum() # 計算累積值 cumulative sum
df = pd.DataFrame(np.random.randn(1000, 4),
                  index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure(); # 定義一個圖像窗口 define an image window
df.plot(); # 繪圖 plot



