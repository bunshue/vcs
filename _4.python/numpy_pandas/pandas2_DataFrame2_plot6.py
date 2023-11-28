import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from matplotlib import style
style.use("fivethirtyeight")

dictionary1 = {"順序": [1, 2, 3, 4],
              "中文名": ['鼠', '牛', '虎', '兔'],
              "英文名": ['mouse', 'ox', 'tiger', 'rabbit'],
              "體重": [3, 48, 33, 8],
              "代表": ['米老鼠', '班尼牛', '跳跳虎', '彼得兔']
              }
print('字典轉DataFrame')
df1 = pd.DataFrame(dictionary1)
print(df1)

print('-----------------')

dictionary2 = {"順序": [5, 6, 7, 8],
              "中文名": ['龍', '蛇', '馬', '羊'],
              "英文名": ['dragon', 'snake', 'horse', 'goat'],
              "體重": [38, 16, 36, 29],
              "代表": ['逗逗龍', '貪吃蛇', '草泥馬', '喜羊羊']
              }

df2 = pd.DataFrame(dictionary2)

print('合併兩個DataFrame')
df3 = pd.concat([df1, df2])
print(df3)

print('-----------------')

#設定陣列的第一欄
df3.set_index("順序", inplace = True)

#排序, 升冪排序
df3.sort_values(by=['順序'])

print(df3)

df3.plot()

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
