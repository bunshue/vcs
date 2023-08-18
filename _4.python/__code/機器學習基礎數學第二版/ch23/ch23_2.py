# ch23_2.py
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,88,75,60,50,55,55,56,58,58,61,63,68,71,71,75,76,88,93,97,97,100]

coef = np.polyfit(x, y, 3)                              # 迴歸直線係數
model = np.poly1d(coef)                                 # 線性迴歸方程式
reg = np.linspace(1,24,100)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(x,y)
plt.title('網路購物調查')
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)
plt.plot(reg,model(reg),color='red')
         
plt.show()














