import matplotlib.pyplot as plt


print("在圖表的指定地方畫圖")

listx = [1,2,3,4,5]

listy1 = [15,50,80,40,70]
plt.axes([0.1, 0.1, 0.3, 0.3])
plt.ylim(0, 100)
plt.plot(listx, listy1, 'r-s')

listy2 = [80,20,60,50,20]
plt.axes([0.6, 0.1, 0.3, 0.3])
plt.ylim(0, 100)
plt.plot(listx, listy2, 'g--o')

plt.axes([0.1, 0.6, 0.3, 0.3])
plt.ylim(0, 100)
plt.plot(listx, listy1, 'r-s')

plt.axes([0.6, 0.6, 0.3, 0.3])
plt.ylim(0, 100)
plt.plot(listx, listy2, 'g--o')

plt.show()
