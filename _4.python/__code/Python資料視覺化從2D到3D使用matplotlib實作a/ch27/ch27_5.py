# ch27_5.py
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.image as img

jk = img.imread('jk.jpg')               # 讀取原始圖像
fig, ax = plt.subplots()                # 建立 axes 軸物件
im = ax.imshow(jk)                      # 顯示 jk 影像物件
# 建立剪輯模式
patch = Circle((160,160),radius=150,transform=ax.transData)
im.set_clip_path(patch)                 # 建立剪輯結果
ax.axis('off')                          # 關閉軸標記與刻度
plt.show()






