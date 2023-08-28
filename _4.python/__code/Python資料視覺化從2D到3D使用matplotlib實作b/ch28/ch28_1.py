# ch28_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, ax =plt.subplots()
data=[[100,300],                        # 定義儲存格資料
      [400,600],
      [500,700]]
column_labels=["2023年", "2024年"]      # 定義欄位標題  
c_colors = ['lightyellow'] * 2          # 定義欄標題顏色
row_labels=['亞洲','歐洲','美洲']       # 定義列標題  
r_colors = ['lightgreen'] * 3           # 定義列標題顏色
ax.table(cellText=data,                 # 建立表格
         colLabels=column_labels,
         colColours=c_colors,
         rowLabels=row_labels,
         rowColours=r_colors,
         loc="upper left")              # 從左邊上方放置表格
ax.axis('off')
ax.set_title('深智軟件銷售表',fontsize=16,color='b')
plt.show()






