# ch2_25.py
import matplotlib.pyplot as plt
import matplotlib.image as img

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
pict = img.imread('jk.jpg')
h, w, c = pict.shape
print(f"圖檔高度   = {h}")
print(f"圖檔寬度   = {w}")
print(f"圖檔通道数 = {c}")
plt.axis('off')
plt.title("洪錦魁",fontsize=24)
plt.imshow(pict)
plt.show()


