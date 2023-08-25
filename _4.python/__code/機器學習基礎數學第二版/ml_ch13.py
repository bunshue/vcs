import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_1.py

# ch13_1.py
import random           # 導入模組random

min = 1
max = 6
target = 5
n = 10000
counter = 0
for i in range(n):
    if target == random.randint(min, max):
        counter += 1
print('經過 {} 次, 得到 {} 次 {}'.format(n, counter, target))
P = counter / n
print('機率 P = {}'.format(P))






        


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_2.py

# ch13_2.py
import matplotlib.pyplot as plt
from random import randint

min = 1
max = 6                                         # 骰子有幾面
times = 10000                                   # 擲骰子次數

dice = [0] * 7                                  # 建立擲骰子的串列
for i in range(times):
    data = randint(min, max)
    dice[data] += 1
    
del dice[0]                                     # 刪除索引0資料
    
for i, c in enumerate(dice, 1):
    print('{} = {} 次'.format(i, c))
    
x = [i for i in range(1, max+1)]                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, dice, width, color='g')              # 繪製長條圖
plt.ylabel('Frequency')
plt.title('Test 10000 times')
plt.show()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_3.py

# ch13_3.py
from fractions import Fraction

x = Fraction(2, 7) * Fraction(1, 6)
y = Fraction(5, 7) * Fraction(2, 6)
p = x + y
print('第 1 位抽籤的中獎機率 {}'.format(Fraction(2, 7)))
print('第 2 位抽籤的中獎機率 {}'.format(p))







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_4.py

# ch13_4.py
from fractions import Fraction

x = Fraction(5, 6)
p = 1 - (x**3)
print('連擲骰子不出現 5 的機率 {}'.format(p))
print('連擲骰子不出現 5 的機率 {}'.format(float(p)))







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_5.py

# ch13_15.py
import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_6.py

# ch13_6.py
import random
import math
import matplotlib.pyplot as plt

trials = 5000
Hits = 0
radius = 50
for i in range(trials):
    x = random.randint(1, 100)                      # x軸座標
    y = random.randint(1, 100)                      # y軸座標
    if math.sqrt((x-50)**2 + (y-50)**2) < radius:   # 在圓內
        plt.scatter(x, y, marker='.', c='y')
        Hits += 1
    else:
        plt.scatter(x, y, marker='.', c='g')    
plt.axis('equal')
plt.show()












print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_7.py

# ch13_7.py
import numpy as np

# 建立 1 個隨機數
x = np.random.rand()
print(x)

# 建立 3 個隨機數
x = np.random.rand(3)
print(x)
    
# 建立 3x2 個隨機數
x = np.random.rand(3,2)
print(x)





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_8.py

# ch13_8.py
import numpy as np

# 建立 1 個 0-4(含) 的整數隨機數
x = np.random.randint(5)
print(x)

# 建立 3 個 0-9(含) 的整數隨機數 
x = np.random.randint(10,size=3)
print(x)
    
# 建立 3x2 個0-9(含) 的整數隨機數
x = np.random.randint(0, 10, size=(3,2))
print(x)
    






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_9.py

# ch13_9.py
import matplotlib.pyplot as plt
import numpy as np

sides = 6
# 建立 10000 個 1-6(含) 的整數隨機數 
dice = np.random.randint(1,sides+1,size=10000)  # 建立隨機數
    
h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('Frequency')
plt.title('Test 10000 times')
plt.show()
    






print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_10.py

# ch13_10.py
import numpy as np

x = np.random.randint(10,size=10)
print(x)

    






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_11.py

# ch13_11.py
import numpy as np
np.random.seed(5)
x = np.random.randint(10,size=10)
print(x)

    






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_12.py

# ch13_12.py
import numpy as np

# 一維陣列
arr1 = np.arange(9)
print("一維陣列")
print(arr1)
np.random.shuffle(arr1)         # 重新排列
print("重新排列")
print(arr1)

# 二維陣列
arr2 = np.arange(9).reshape((3,3))
print("二維陣列")
print(arr2)
np.random.shuffle(arr2)         # 重新排列
print("重新排列")
print(arr2)
    






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_13.py

# ch13_13.py
import numpy as np

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits,3)
print("隨機挑選 3 種水果")
print(fruit1)

fruit2 = np.random.choice(fruits,5)
print("隨機挑選 5 種水果 -- 可以重複")
print(fruit2)
    
fruit3 = np.random.choice(fruits,5,replace=False)
print("隨機挑選 5 種水果 -- 不可以重複")
print(fruit3)





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_14.py

# ch13_14.py
import numpy as np

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits,5,p=[0.8,0.05,0.05,0.05,0.05])
print("依權重挑選 5 種水果")
print(fruit1)

fruit2 = np.random.choice(fruits,5,p=[0.05,0.05,0.05,0.05,0.8])
print("依權重挑選 5 種水果")
print(fruit2)





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch13\ch13_15.py

# ch13_15.py
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10000)
y = np.random.rand(10000)
plt.scatter(x, y, c=y, cmap='hsv')  # 色彩依 y 軸值變化
plt.colorbar()
plt.show()






print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

