import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

n = np.linspace(1.1, 10, 90)            # 建立1.1-10的陣列
count = 0                               # 用於計算每5筆輸出換行
for i in n:
    count += 1
    print('{0:2.1f} = {1:4.3f}'.format(i, np.log10(i)), end='    ')
    if count % 5 == 0:                  # 每5筆輸出就換行
        print()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.linspace(0.1, 10, 99)                   # 建立含30個元素的陣列
x2 = np.linspace(0.1, 10, 99)                   # 建立含30個元素的陣列
y1 = [math.log2(x) for x in x1]
y2 = [math.log(x, 0.5) for x in x2]
plt.plot(x1, y1, label="base = 2")
plt.plot(x2, y2, label="base = 0.5")

plt.legend(loc="best")                          # 建立圖例
plt.axis([0, 10, -5, 5])
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個
