# ch14_18.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("snow.jpg",cv2.IMREAD_GRAYSCALE)
plt.subplot(121)                    # 建立子圖 1
plt.imshow(src, 'gray')             # 灰度顯示第1張圖
plt.subplot(122)                    # 建立子圖 2
plt.hist(src.ravel(),256)           # 降維再繪製直方圖
plt.tight_layout()
plt.show()



