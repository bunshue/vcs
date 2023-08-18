# ch23_5.py
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21,22,23,24]
y = [100,21,75,49,15,98,55,31,33,82,61,80,32,71,99,15,66,88,21,97,30,5]

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














