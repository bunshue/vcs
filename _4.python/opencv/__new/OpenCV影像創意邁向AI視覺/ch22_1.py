# ch22_1.py
import cv2
import numpy as np

src = cv2.imread("coin1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_1_1.py

# ch22_1.py
import cv2
import numpy as np

src = cv2.imread("coin2.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_2.py

# ch22_2.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_2_1.py

# ch22_2_1.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.5 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_2_2.py

# ch22_2_2.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("coin1.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_3.py

# ch22_3.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
plt.subplot(141)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(142)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(143)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.subplot(144)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_4.py

# ch22_4.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(133)
plt.title("標記區")
plt.imshow(markers)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_5.py

# ch22_5.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
# 先複製再標記修訂
sure_fg_copy = sure_fg.copy()
ret, markers_new = cv2.connectedComponents(sure_fg_copy)
markers_new += 1  # 標記修訂
markers_new[unknown == 255] = 0
plt.subplot(131)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(132)
plt.title("標記區")
plt.imshow(markers, cmap="jet")
plt.axis("off")
plt.subplot(133)
plt.title("標記修訂區")
plt.imshow(markers_new, cmap="jet")
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch22\ch22_6.py

# ch22_6.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
# 正式執行分水嶺函數
dst = rgb_src.copy()
markers = cv2.watershed(dst, markers)
dst[markers == -1] = [255, 0, 0]  # 使用紅色
plt.subplot(121)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(122)
plt.title("分割結果")
plt.imshow(dst)
plt.axis("off")
plt.show()


print("------------------------------------------------------------")  # 60個
