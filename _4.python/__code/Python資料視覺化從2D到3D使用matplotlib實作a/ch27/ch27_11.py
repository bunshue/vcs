# ch27_11.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.image as img

jk = img.imread('jk.jpg')               # 讀取原始圖像
fig, ax = plt.subplots()                # 建立 axes 軸物件
im = ax.imshow(jk)                      # 顯示 jk 影像物件
ax.add_patch(Rectangle((60,30),         # 矩形 xy
                       200, 200,        # 寬與高
                       fc ='none',      # 內部顏色
                       ec = 'g',        # 矩形框的顏色
                       lw = 5) )        # 矩形線寬
ax.axis('off')                          # 關閉軸標記與刻度
plt.show()






