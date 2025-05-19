# ch24_1.py
import cv2
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

lisa = cv2.imread("lisaE1.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_NS)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


# ch24_2.py
import cv2
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

lisa = cv2.imread("lisaE2.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()
