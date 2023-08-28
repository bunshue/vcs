# ch14_19.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("springfield.jpg",cv2.IMREAD_GRAYSCALE)
plt.subplot(121)                        # 建立子圖 1
plt.imshow(src, 'gray')                 # 灰階顯示第1張圖
plt.subplot(122)                        # 建立子圖 2
plt.hist(src.ravel(),256)               # 降維再繪製直方圖
plt.tight_layout()
plt.show()


