# ch2_23.py
import matplotlib.pyplot as plt
import matplotlib.image as img

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
pict = img.imread('jk.jpg')
plt.axis('off')
plt.title("洪錦魁",fontsize=24)
plt.imshow(pict)
plt.show()


