# ch28_3.py
import numpy as np
import matplotlib.pyplot as plt
 
plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
data = [[100,105,110,115],
        [58,61,66,72],
        [69,70,79,82],
        [50,52,35,55],
        [12,14,20,22]]
 
columns = ('2022年', '2023年', '2024年', '2025年')
rows = ("Momo","天瓏", "博客來", "聯合發行", "海外")  

colors = ['r', 'g', 'b', 'm', 'orange']     # 建立色彩
index = np.arange(len(columns)) + 0.3
n_rows = len(data)
# 繪製折線圖圖
for row in range(n_rows):                  
    plt.plot(index, data[row], color=colors[row])
# 在折線圖下方建立表格 
plt.table(cellText=data,
          rowLabels=rows,
          rowColours=colors,
          colLabels=columns,
          loc='bottom')
plt.ylabel("各通路業績表")
plt.yticks(np.arange(0,130,step=10))
plt.xticks([])
plt.title('深智業績表',fontsize=16,color='b')
plt.tight_layout()  
plt.show()




