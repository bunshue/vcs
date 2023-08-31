import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,88,75,60,50,55,55,56,58,58,61,63,68,71,71,75,76,88,93,97,97,100]

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(x,y)
plt.title('網路購物調查')
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,88,75,60,50,55,55,56,58,58,61,63,68,71,71,75,76,88,93,97,97,100]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
reg = np.linspace(1,24,100)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(x,y)
plt.title('網路購物調查')
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)
plt.plot(reg,model(reg),color='red')
         
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,88,75,60,50,55,55,56,58,58,61,63,68,71,71,75,76,88,93,97,97,100]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
print(r2_score(y, model(x)).round(3))

print('------------------------------------------------------------')	#60個

from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,88,75,60,50,55,55,56,58,58,61,63,68,71,71,75,76,88,93,97,97,100]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
print(f"18點購物人數預測 = {model(18).round(2)}")
print(f"20點購物人數預測 = {model(20).round(2)}")

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,21,75,49,15,98,55,31,33,82,61,80,32,71,99,15,66,88,21,97,30,5]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
reg = np.linspace(1,24,100)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(x,y)
plt.title('網路購物調查')
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)
plt.plot(reg,model(reg),color='red')
         
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.metrics import r2_score
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,21,75,49,15,98,55,31,33,82,61,80,32,71,99,15,66,88,21,97,30,5]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
print(r2_score(y, model(x)).round(3))

print('------------------------------------------------------------')	#60個
