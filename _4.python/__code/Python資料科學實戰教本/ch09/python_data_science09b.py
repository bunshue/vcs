"""
Python資料科學實戰教本



"""


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-1a.py

import matplotlib.pyplot as plt
import pandas as pd

data = [100, 110, 150, 170, 190, 200, 220]
s = pd.Series(data)
s.plot()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

data = [100, 110, 150, 170, 190, 200, 220]
weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
s = pd.Series(data, index=weekday)
s.plot()
plt.show()

'''
weight = [3, 48,33,8,38,16,36,29,22,6,12,42]
animals = ["鼠牛虎兔龍蛇馬羊猴雞狗豬"]
'''



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-2.py

import matplotlib.pyplot as plt
import pandas as pd

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}
df = pd.DataFrame(dists)
print(df) 
#df.to_html("ch9-4-2-01.html")  #df轉html
df.plot()

df2 = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df2)
#df2.to_html("ch9-4-2-02.html")  #df轉html
df2.plot()
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-2a.py

import matplotlib.pyplot as plt
import pandas as pd

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}

df = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df)
df.plot(xticks=range(len(df.index)),
        use_index=True)

df.plot(xticks=range(len(df.index)),
        use_index=True,
        rot=90)

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-3.py

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

dists = {"區名": ["中正區", "板橋區", "桃園區", "北屯區", 
                  "安南區", "三民區", "大安區", "永和區", 
                  "八德區", "前鎮區", "鳳山區", 
                  "信義區", "新店區"],
         "人口": [159598, 551452, 441287, 275207,
                  192327, 343203, 309835, 222531,
                  198473, 189623, 359125, 
                  225561, 302070],
         "面積": [7.6071, 23.1373, 34.8046, 62.7034, 
                  107.2016, 19.7866, 11.3614, 5.7138, 
                  33.7111, 19.1207, 26.7590, 
                  11.2077, 120.2255]}

df = pd.DataFrame(dists, 
                  columns=["人口", "面積"],
                  index=dists["區名"])
print(df)
#df.to_html("ch9-4-3.html")  #df轉html
df["面積"] *= 1000
df.plot(xticks=range(len(df.index)),
        use_index=True,
        rot=45)

plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-3a.py

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

dists = {"區名": ["中正區", "板橋區", "桃園區", "北屯區", 
                  "安南區", "三民區", "大安區", "永和區", 
                  "八德區", "前鎮區", "鳳山區", 
                  "信義區", "新店區"],
         "人口": [159598, 551452, 441287, 275207,
                  192327, 343203, 309835, 222531,
                  198473, 189623, 359125, 
                  225561, 302070],
         "面積": [7.6071, 23.1373, 34.8046, 62.7034, 
                  107.2016, 19.7866, 11.3614, 5.7138, 
                  33.7111, 19.1207, 26.7590, 
                  11.2077, 120.2255]}

df = pd.DataFrame(dists, 
                  columns=["人口", "面積"],
                  index=dists["區名"])
print(df)
fig, ax = plt.subplots()
fig.suptitle("分區統計")
ax.set_ylabel("人口")
ax.set_xlabel("分區")
ax2 = ax.twinx()
ax2.set_ylabel("面積")
df["人口"].plot( ax=ax, 
                 style="b--o",
                 use_index=True,
                 rot=90)
df["面積"].plot( ax=ax2, 
                 style="g-s",
                 use_index=True,
                 rot=90)
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-4.py

import matplotlib.pyplot as plt
import pandas as pd

data = [100, 110, 150, 170, 190, 200, 220]
s = pd.Series(data)
s.plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-4a.py

import matplotlib.pyplot as plt
import pandas as pd

usage = {"os": ["Windows","Mac OS","Linux","Chrome OS","BSD"],
         "percentage": [88.78, 8.21, 2.32, 0.34, 0.02]}

df = pd.DataFrame(usage, 
                  columns=["percentage"],
                  index=usage["os"])
print(df)
df.to_html("ch9-4-4.html")
df.plot(kind="bar")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-5.py

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

fruits = ["蘋果","梨子","香蕉","橙子"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="水果")
print(s)
s.plot(kind="pie")
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-5a.py

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

fruits = ["蘋果","梨子","香蕉","橙子"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="水果")
print(s)
explode = [0.1, 0.3, 0.1, 0.3]
s.plot(kind="pie",
       figsize=(6, 6),
       explode=explode)
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-6.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
df = pd.DataFrame({"x":x, "y":y})
df.plot(kind="scatter", x="x", y="y", 
        title="Sin(x)")
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch09\ch9-4-6a.py

import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("iris.csv")

iris.boxplot(column="sepal_length",
             by="target",
             figsize=(6,5))
plt.show()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




