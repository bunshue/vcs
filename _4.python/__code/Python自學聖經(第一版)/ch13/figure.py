import matplotlib.pyplot as plt
# 新增圖表區
plt.figure()
plt.plot([1,2,3])
# 新增圖表區並設定屬性
plt.figure(figsize=[8,4], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
plt.plot([1,2,3])

plt.show()