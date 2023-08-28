# ch3_19.py
import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'Old English Text MT',
        'color':'blue',
        'weight':'bold',
        'size':20}
font2 = {'family':'Old English Text MT',
        'color':'green',
        'weight':'normal',
        'size':12}
x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x, y1, color='c')          # 設定青色cyan            
plt.plot(x, y2, color='r')          # 設定紅色red
plt.title('Sin and Cos function',fontdict=font1)
plt.xlabel('x-value',fontdict=font2)
plt.ylabel('y-value',fontdict=font2)
plt.show()




