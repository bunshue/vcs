# ch29_6.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
np.random.seed(10)
x_heights = np.random.randint(120,190,50)
y_weights = np.random.randint(30,100,50)
z_ages = np.random.randint(low=10,high=35,size=50)
# 性別標籤 1 是男生, 0 是女生
gender = np.random.choice([0, 1],50)   
# 建立軸物件
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# 繪製散點圖
ax.scatter(x_heights,y_weights,z_ages,c=gender)
ax.set_xlabel('身高 (單位 : 公分)',color='m')
ax.set_ylabel('體重 (單位 : 公斤)',color='m')
ax.set_zlabel('年齡 (單位 : 歲',color='m')
ax.set_title('不同年齡體重與身高分佈圖',fontsize=16,color='b')
plt.show()


 

