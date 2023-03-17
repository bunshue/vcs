import matplotlib.pyplot as plt
import numpy as np

print("subplot 範例")

plt.figure(figsize=[10,8])  #設定圖表大小

x = np.linspace(0, 6.28, 20)
y = np.sin(x)

#plt.subplot(2, 3, 1)   same
plt.subplot(231)
#plt.title('231')   same
plt.title(label='231')
plt.plot(x, y, 'ro-')

plt.subplot(232)
plt.title(label='232')
plt.plot(x, y, 'g.-')

plt.subplot(233)
plt.title(label='233')
plt.plot(x, y, 'b:o')

plt.subplot(234)
plt.title(label='234')
plt.plot(x, y, 'y--o')

plt.subplot(235)
plt.title(label='235')
plt.plot(x, y, 'm.-')

plt.subplot(236)
plt.title(label='236')
plt.plot(x, y, 'c.-')
#plt.axes([0.2,0.2,0.4,0.4]) #設定顯示位置

plt.show()


