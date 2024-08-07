"""
無 scikit-learn(sklearn)的

"""

import keras

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

#迭代次數
ITERATIONS = 50

print('------------------------------------------------------------')	#60個

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

# y = x
xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
ys = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype = float)
print(type(xs))
print(xs)
print(type(ys))
print(ys)

model.fit(xs, ys, epochs = ITERATIONS)

print('keras 預測')
xx = np.linspace(0.0, 10.0, 21)
yy = model.predict(xx)

"""
print(model.predict([2.5]))
print(model.predict([4.5]))
print(model.predict([6.0]))
print(model.predict([10.0]))
print(xx)
print(yy)
"""

x = np.linspace(0, 10, 100)
plt.plot(x, x, 'b', lw = 2, label = 'y = x')
plt.plot(xs, ys, 'g-o', lw = 1, ms = 10, label = '實驗點')
plt.scatter(xx, yy, c = 'red', marker = 'o', lw = 4, label = '預測點')

xmin, xmax, ymin, ymax = -1, 11, -1, 11
plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

#統率, 武力, 智力, 政治, 魅力
main_features = [87, 86, 82, 78, 100]             # 劉備 特徵值
people_names = [                     # 比較人物人名
    '諸葛亮',
    '關羽',
    '張飛',
    '趙雲',
    '曹操',
    '司馬懿',
    '孫權',
    '周瑜',
    '呂布',
]

people_features = [                   # 比較人物特徵值
    [99, 42, 100, 100, 92],
    [92, 100, 74, 51, 83],
    [86, 99, 78, 36, 57],
    [79, 94, 77, 82, 91],
    [100, 85, 93, 96, 95],
    [95, 62, 98, 95, 84],
    [72, 84, 76, 85, 93],
    [93, 71, 94, 81, 92],
    [84, 98, 61, 12, 55],
]

dist = []                           # 儲存人物相似度值
for feature in people_features:
    distances = 0
    for i in range(len(feature)):
        distances += (main_features[i] - feature[i]) ** 2
    dist.append(math.sqrt(distances))
    
min_ = min(dist)                    # 求最小值
min_index = dist.index(min_)        # 最小值的索引

print(f"與 劉備 最相似的人物 : {people_names[min_index]}")
print(f"相似度值 : {dist[min_index]}")
for i in range(len(dist)):
    print(f"人物 : {people_names[i]}, 相似度 : {dist[i]:6.2f}")

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




