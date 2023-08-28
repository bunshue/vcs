# ch12_18.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
farmers = ["張三","李四","大成","陳王", "李曉.","林邊"]
fruits = ["釋迦","番茄","鳳梨","蓮霧","香蕉","芭樂"]
# 建立收成表
harvest = np.array([[0.3, 2.1, 1.8, 3.5, 0.0, 2.0],
                    [2.1, 0.0, 3.0, 1.0, 2.3, 0.0],
                    [1.2, 2.6, 1.8, 4.1, 0.5, 3.6],
                    [0.5, 0.2, 0.7, 0.0, 2.3, 0.0],
                    [0.6, 1.5, 0.0, 2.1, 2.0, 4.2],
                    [0.3, 2.2, 0.0, 1.3, 0.0, 1.5]])

fig, ax = plt.subplots()
im = ax.imshow(harvest,cmap='YlGn')
ax.figure.colorbar(im, ax=ax)
# 依據農夫姓名建立 x 軸刻度標記和刻度標籤
ax.set_xticks(np.arange(len(farmers)))
ax.set_xticklabels(farmers)
# 依據水果名稱建立 y 軸刻度標記和刻度標籤
ax.set_yticks(np.arange(len(fruits)))
ax.set_yticklabels(fruits)
# 炫轉 x 軸刻度標籤
plt.setp(ax.get_xticklabels(), rotation=45)
# 使用雙層迴圈註記收成數量
for i in range(len(fruits)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i,j],
                        ha="center", va="center", color="b")
ax.set_title("農夫收成(噸 / 年)",fontsize=18)
ax.set_xlabel("姓名")
ax.set_ylabel("水果")
fig.tight_layout()
plt.show()


      
