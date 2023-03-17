

# plot 畫兩條線

import matplotlib.pyplot as plt
import numpy as np

degree = np.linspace(0, 2*np.pi, 36)    #共 36 個點
 
#print(degree)
x = degree
y1 = np.sin(degree)
#y1 = np.exp(-degree)   #指數
y2 = np.cos(degree)
y3 = np.tan(degree)
#plt.plot(x, y1)    #無其他參數
plt.plot(x, y1, color='red', lw=2)
plt.plot(x, y2, color='green', lw=2)
plt.plot(x, y3, color='blue', lw=2)
plt.plot(x, y3, 'ro')


'''
x1 = [1, 2, 3, 4, 5, 6]
y1 = [20, 30, 14, 67, 42, 12]
plt.plot(x1, y1, lw=2, label='Mary')

x2 = [1, 3, 4, 5, 9, 11]
y2 = [12, 33, 43, 22, 34, 20]
plt.plot(x2, y2, lw=2, label='Tom')
'''

plt.xlim(-0.1, 6.4)
plt.ylim(-1.1, 1.1)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.xlabel('角度(弧度)')
plt.ylabel('sin cos tan')
#plt.legend()
plt.title('三角函數')

plt.show()





