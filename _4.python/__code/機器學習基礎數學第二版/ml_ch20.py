import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch20\ch20_1.py

# ch20_1.py
from sympy import Symbol, solve

a = Symbol('a')
b = Symbol('b')
eq1 = -a + b -2
eq2 = a + b - 4
ans = solve((eq1, eq2))
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))








print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch20\ch20_2.py

# ch20_2.py
import numpy as np
import math

a = np.array([1, 1])
b = np.array([5, 5])
c = np.array([1, 5])
d = np.array([5, 1])

ab = b - a                              # 向量ab
cd = d - c                              # 向量bc

norm_a = np.linalg.norm(ab)             # 計算向量大小
norm_b = np.linalg.norm(cd)             # 計算向量大小
                    
dot_ab = np.dot(ab, cd)                 # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)              # acos轉成弧度
deg = math.degrees(rad)                 # 轉成角度
print('角度是 = {}'.format(deg))









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch20\ch20_3.py

# ch20_3.py
import numpy as np

def cosine_similarity(va, vb):
    norm_a = np.linalg.norm(va)                 # 計算向量大小
    norm_b = np.linalg.norm(vb)                 # 計算向量大小
    dot_ab = np.dot(va, vb)                     # 計算向量內積
    return (dot_ab / (norm_a * norm_b))         # 回傳相似度

a = np.array([2, 1, 1, 1, 0, 0, 0, 0])
b = np.array([1, 1, 0, 0, 1, 1, 1, 0])
c = np.array([1, 1, 0, 0, 1, 1, 0, 1])
print('a 和 b 相似度 = {0:5.3f}'.format(cosine_similarity(a, b)))
print('a 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(a, c)))
print('b 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(b, c)))







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch20\ch20_4.py

# ch20_4.py
import numpy as np

x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])             
x_mean = np.mean(x)
y_mean = np.mean(y)

xi_x = [v - x_mean  for v in x]
yi_y = [v - y_mean  for v in y]

data1 = [0]*10
data2 = [0]*10
data3 = [0]*10
for i in range(len(x)):
    data1[i] = xi_x[i] * yi_y[i]
    data2[i] = xi_x[i]**2
    data3[i] = yi_y[i]**2

v1 = np.sum(data1)
v2 = np.sum(data2)
v3 = np.sum(data3)
r = v1 / ((v2**0.5)*(v3**0.5))
print('coefficient = {}'.format(r))









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch20\ch20_5.py

# ch20_5.py
import numpy as np
import matplotlib.pyplot as plt

x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])             
x_mean = np.mean(x)
y_mean = np.mean(y)
xpt1 = np.linspace(0, 12, 12)      
ypt1 = [y_mean for xp in xpt1]          # 平均購買次數
ypt2 = np.linspace(0, 20, 20)
xpt2 = [x_mean for yp in ypt2]          # 平均滿意度

plt.scatter(x, y)                       # 滿意度 vs 購買次數
plt.plot(xpt1, ypt1, 'g')               # 平均購買次數
plt.plot(xpt2, ypt2, 'g')               # 平均滿意度
plt.grid()
plt.show()










print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch20\ch20_6.py

# ch20_6.py
import numpy as np
import math

a = np.array([4, 2])
b = np.array([1, 3])

norm_a = np.linalg.norm(a)              # 計算向量大小
norm_b = np.linalg.norm(b)              # 計算向量大小
                    
dot_ab = np.dot(a, b)                   # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)              # acos轉成弧度

area = norm_a * norm_b * math.sin(rad) / 2
print('area = {0:5.2f}'.format(area))









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch20\ch20_7.py

# ch20_7.py
import numpy as np

a = np.array([4, 2])
b = np.array([1, 3])

ab_cross = np.cross(a, b)               # 計算向量外積
area = np.linalg.norm(ab_cross) / 2     # 向量長度除以2
                    
print('area = {0:5.2f}'.format(area))









print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

