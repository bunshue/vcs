# ch27_3.py
import matplotlib.pyplot as plt

figure, axes = plt.subplots()           # 建立子圖物件
circle = plt.Circle((0.5,0.5), 0.4, fill=False,
                    linewidth=3, edgecolor='m') # 繪製圓
axes.set_aspect('equal')                # 設定座標單位長度相同
plt.gca().add_artist(circle)            # 將物件加入圖表物件
plt.show()





