# ch23_1.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch23\ch23_2.py

# ch23_2.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)
maskpict = cv2.imread("hung_mask.jpg")  # 讀取影像
newmask = cv2.imread("hung_mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask[newmask == 0] = 0  # 白色內容則確定是前景
mask[newmask == 255] = 1  # 黑色內容則確定是背景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")
dst = src * mask[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
maskpict_rgb = cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB)
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(maskpict_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch23\ch23_3.py

# ch23_3.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("lena.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch23\ch23_4.py

# ch23_4.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("lena.jpg")  # 讀取影像
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
mask[30:324, 30:300] = 3
mask[90:200, 90:200] = 1
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個
