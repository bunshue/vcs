# ch5_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]                                
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares)           
plt.axis([0, 8, 0, 70])     # 繪製線條
x = 2
y = 30
plt.plot(x, y, 'bo')        # 輸出位智繪製藍色的點
plt.text(x, y, '深智數位')  # 輸出字串
plt.grid()
plt.show()











