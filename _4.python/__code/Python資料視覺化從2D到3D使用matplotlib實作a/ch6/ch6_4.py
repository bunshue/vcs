# ch6_4.py
import matplotlib.pyplot as plt
import matplotlib.image as img

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

plt.figure(1)                       # 建立圖表 1
pict = img.imread('jk.jpg')
plt.axis('off')
plt.title("洪錦魁",fontsize=24)
plt.imshow(pict)

plt.figure(2)                       # 建立圖表 2
pict = img.imread('macau.jpg')
plt.axis('off')
plt.title("澳門",fontsize=24)
plt.imshow(pict)

plt.show()


