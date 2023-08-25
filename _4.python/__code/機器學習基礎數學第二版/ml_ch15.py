import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch15\ch15_1.py

# ch15_1.py
base = 10000
rate = 0.03
year = 10
for i in range(1, year+1):
    base = base + base*rate
    print('經過 {0:2d} 年後累積金額 {1:6.2f}'.format(i,base))













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch15\ch15_2.py

# ch15_2.py
base = 100
rate = 1
hour = 10
for i in range(1, hour+1):
    base = base + base*rate
    print('經過 {0:2d} 小時後累積病毒量 {1}'.format(i,base))













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch15\ch15_3.py

# ch15_3.py
base = 100
rate = 0.1
year = 3
for i in range(1, year+1):
    base = base - base*rate
    print('經過 {} 年後車輛殘值 {}'.format(i,base))













print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch15\ch15_4.py

# ch15_4.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 5, 5)                  # 建立含10個元素的陣列
ypt1 = xpt / xpt                            # 時間複雜度是 O(1)
ypt2 = np.log2(xpt)                         # 時間複雜度是 O(logn)               
ypt3 = xpt                                  # 時間複雜度是 O(n)
ypt4 = xpt * np.log2(xpt)                   # 時間複雜度是 O(nlogn)
ypt5 = xpt * xpt                            # 時間複雜度是 O(n*n)
plt.plot(xpt, ypt1, '-o', label="O(1)")                  
plt.plot(xpt, ypt2, '-o', label="O(logn)")                  
plt.plot(xpt, ypt3, '-o', label="O(n)")
plt.plot(xpt, ypt4, '-o', label="O(nlogn)")
plt.plot(xpt, ypt5, '-o', label="O(n*n)")
plt.legend(loc="best")                      # 建立圖例
plt.axis('equal')
plt.show()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch15\ch15_5.py

# ch15_5.py
import matplotlib.pyplot as plt
import numpy as np

x2 = np.linspace(-3, 3, 30)                 # 建立含30個元素的陣列
x4 = np.linspace(-3, 3, 30)                 # 建立含30個元素的陣列
y2 = 2**x2
y4 = 4**x4
plt.plot(x2, y2, label="2**x")
plt.plot(x4, y4, label="4**x")
plt.plot(0, 1, '-o')                        # 標記指數為0位置
plt.legend(loc="best")                      # 建立圖例
plt.axis([-3, 3, 0, 30])
plt.grid()
plt.show()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch15\ch15_6.py

# ch15_6.py
import matplotlib.pyplot as plt
import numpy as np

x2 = np.linspace(-3, 3, 30)                 # 建立含30個元素的陣列
x4 = np.linspace(-3, 3, 30)                 # 建立含30個元素的陣列
y2 = 0.5**x2
y4 = 0.25**x4
plt.plot(x2, y2, label="0.5**x")
plt.plot(x4, y4, label="0.25**x")
plt.plot(0, 1, '-o')                        # 標記指數為0位置
plt.legend(loc="best")                      # 建立圖例
plt.axis([-3, 3, 0, 30])
plt.grid()
plt.show()





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

