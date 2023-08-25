import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch10\ch10_1.py

# ch10_1.py
import matplotlib.pyplot as plt                                  
x = [x for x in range(0, 11)]                   
y = [7.5*y - 3.33 for y in x]
plt.axis([0, 4, 0, 25])
plt.plot(x, y)   
plt.plot(1, 5, '-o')
plt.plot(2, 10, '-o')
plt.plot(3, 20, '-o')
plt.xlabel('Times:unit=100')
plt.ylabel('Voucher:unit=100')
plt.grid()                              # 加格線
plt.show()



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch10\ch10_2.py

# ch10_2.py                               
import numpy as np

x = np.array([1, 2, 3])                 # 拜訪次數, 單位是100
y = np.array([5, 10, 20])               # 銷售考卷數, 單位是100

a, b = np.polyfit(x, y, 1)
print('斜率 a = {0:5.2f}'.format(a))
print('截距 a = {0:5.2f}'.format(b))





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch10\ch10_3.py

# ch10_3.py
import matplotlib.pyplot as plt                                  
import numpy as np

x = np.array([1, 2, 3])                 # 拜訪次數, 單位是100
y = np.array([5, 10, 20])               # 銷售考卷數, 單位是100

a, b = np.polyfit(x, y, 1)              # 迴歸直線
print('斜率 a = {0:5.2f}'.format(a))
print('截距 a = {0:5.2f}'.format(b))

y2 = a*x + b
plt.scatter(x, y)                       # 繪製散佈圖
plt.plot(x, y2)                         # 繪製迴歸直線
plt.show()                      


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch10\ch10_4.py

# ch10_4.py
import matplotlib.pyplot as plt                                  
x = [x for x in range(0, 11)]                   
y = [7.5*y - 3.33 for y in x]
voucher = 25                            # unit = 100
ans_x = (25 + 3.33) / 7.5
print('拜訪次數 = {}'.format(int(ans_x*100)))
plt.axis([0, 4, 0, 30])
plt.plot(x, y)   
plt.plot(1, 5, '-x')
plt.plot(2, 10, '-x')
plt.plot(3, 20, '-x')
plt.plot(ans_x, 25, '-o')
plt.text(ans_x-0.6, 25+0.2, '('+str(int(ans_x*100))+','+str(2500)+')')
plt.xlabel('Times:unit=100')
plt.ylabel('Voucher:unit=100')
plt.grid()                              # 加格線
plt.show()



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\機器學習基礎數學第二版\ch10\ch10_5.py

# ch10_5.py
import matplotlib.pyplot as plt                                  
import numpy as np

x = np.array([22, 26, 23, 28, 27, 32, 30])      # 溫度
y = np.array([15, 35, 21, 62, 48, 101, 86])     # 飲料銷售數量

a, b = np.polyfit(x, y, 1)                      # 迴歸直線
print(f'斜率 a = {a:5.2f}')
print(f'截距 b = {b:5.2f}')

y2 = a*x + b
plt.scatter(x, y)                               # 繪製散佈圖
plt.plot(x, y2)                                 # 繪製迴歸直線

sold = a*31 + b
print('氣溫31度時的銷量 = {}'.format(int(sold)))
plt.plot(31, int(sold), '-o') 
plt.show()                      


print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

