# ch12_8.py
import matplotlib.pyplot as plt
import matplotlib.image as img

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
macau = img.imread('macau.jpg')     # 讀取原始圖像
plt.figure()

plt.subplot(221)        # 原始圖像
plt.axis('off')
plt.title('原始圖像')
plt.imshow(macau)

plt.subplot(222)
r = macau.copy()        # 複製圖像
r[:,:,[1,2]] = 0        # 保留紅色元素, 設定綠色和藍色元素是 0
plt.axis('off')
plt.title('Red元素圖像')
plt.imshow(r)

plt.subplot(223)
g = macau.copy()        # 複製圖像
g[:,:,[0,2]] = 0        # 保留綠色元素, 設定紅色和藍色元素是 0
plt.axis('off')
plt.title('Green元素圖像')
plt.imshow(g)

plt.subplot(224)
b = macau.copy()        # 複製圖像
b[:,:,[0,1]] = 0        # 保留藍色元素, 設定紅色和綠色元素是 0
plt.axis('off')
plt.title('Blue元素圖像')
plt.imshow(b)
plt.show()


