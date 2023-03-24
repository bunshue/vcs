import matplotlib.pyplot as plt

print("在圖表的指定地方畫圖, 不用subplot")

listx = [1,2,3,4,5]
listy = [15,50,80,40,70]

print("1左下開始(0.1, 0.1), w = 0.3, h = 0.3, 左下圖")
plt.axes([0.1, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'r-s')

print("2左下開始(0.6, 0.1), w = 0.3, h = 0.3, 右下圖")
plt.axes([0.6, 0.1, 0.3, 0.3])
plt.plot(listx, listy, 'g--o')

print("3左下開始(0.1, 0.6), w = 0.3, h = 0.3, 左上圖")
plt.axes([0.1, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'b-s')

print("4左下開始(0.6, 0.6), w = 0.3, h = 0.3, 右上圖")
plt.axes([0.6, 0.6, 0.3, 0.3])
plt.plot(listx, listy, 'y--o')

plt.show()

