# ch25_4.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x_pos = [0,0]
y_pos = [0,0]
x_direct = [1,1]
y_direct = [1,-1]
plt.quiver(x_pos,y_pos,x_direct,y_direct,color=['b','g'],
           angles='xy',scale_units='xy', scale=1)
plt.title('繪製藍色和綠色箭頭,箭頭長度單位與座標軸相同')
plt.axis([-2,2,-2,2])
plt.show()


      
