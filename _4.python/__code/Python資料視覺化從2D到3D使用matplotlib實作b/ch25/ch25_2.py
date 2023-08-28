# ch25_2.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x_pos = 0
y_pos = 0
x_direct = 1
y_direct = 1
plt.quiver(x_pos,y_pos,x_direct,y_direct,color='b')
plt.title('Quiver()函數繪製單一藍色箭頭')
plt.xlim([-1,10])
plt.ylim([-1,10])
plt.show()


      
