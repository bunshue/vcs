import matplotlib.pyplot as plt

#新增圖表
plt.figure()
plt.figure(figsize=(8, 8))	#設定圖片視窗大小
plt.plot([1,2,3])
plt.grid(axis='y')  #加上y格線

#新增圖表 並 設定屬性
plt.figure(figsize=[8, 4], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
plt.plot([1,2,3])

plt.axis("off")  #隱藏坐標軸
_ = plt.title('image file', size="x-large", y=-0.1)  #顯示圖片描述

plt.axis("off")
plt.title('Picture Title', size=30, x=0.0, y=0.0)

plt.show()


