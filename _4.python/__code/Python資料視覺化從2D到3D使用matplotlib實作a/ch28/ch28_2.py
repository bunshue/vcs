# ch28_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
data = [[100,105,110,115],
        [58,61,66,72],
        [69,70,79,82],
        [50,52,35,55],
        [12,14,20,22]]
columns = ('2022年', '2023年', '2024年', '2025年')
rows = ("海外","聯合發行", "博客來", "天瓏", "Momo") 
# 建立長條圖的漸層色彩值
colors = plt.cm.Greens(np.linspace(0,0.6,len(data)))
n_rows = len(data)  
# 最初化堆疊長條圖資料的垂直位置, [0, 0, 0, 0]
y_bottom = np.zeros(len(columns)) 
# 繪製堆疊長條圖
index = np.arange(len(columns)) + 0.3
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row],width=0.5,bottom=y_bottom,
            color=colors[row])
    y_bottom = y_bottom + data[row]     # 計算堆疊位置
    cell_text.append(['%1.1f' % (x) for x in y_bottom])
# 反轉色彩和文字標籤, 下方資料在上方出現
colors = colors[::-1]
cell_text.reverse() 
# 在長條圖下方建立表格
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
plt.ylabel("各通路業績表")
plt.yticks(np.arange(0,500,step=100))
plt.xticks([])                          # 隱藏顯示 x 軸刻度
plt.title('深智業績表',fontsize=16,color='b')
plt.tight_layout() 
plt.show()





