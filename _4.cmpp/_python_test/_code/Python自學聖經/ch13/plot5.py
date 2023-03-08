import matplotlib.pyplot as plt

#在同一張圖 畫 兩條曲線

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1, listy1, 'r-.s')

listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2, listy2, 'y-s')

plt.show()
