"""




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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個


"""
pip install pytrends

"""


import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

trends = TrendReq()


trends.build_payload(kw_list=["Machine Learning"])

"""
data = trends.interest_by_region()
data = data.sort_values(by="Machine Learning", ascending=False)
data = data.head(10)
print(data)

print("------------------------------------------------------------")  # 60個

data.reset_index().plot(x="geoName", y="Machine Learning", figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()
"""
print("------------------------------------------------------------")  # 60個

data = TrendReq(hl="en-US", tz=360)
data.build_payload(kw_list=["Machine Learning"])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(20, 15))
data["Machine Learning"].plot()
plt.style.use("fivethirtyeight")
plt.title("Total Google Searches for Machine Learning", fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Total Count")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
