# ch5_1.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_10.py

# ch5_10.py
import cv2
import numpy as np

height = 150  # 影像高
width = 300  # 影像寬
image = np.zeros((height, width, 3), np.uint8)
image[0:50, :, 0] = 255  # blue
image[50:100, :, 1] = 255  # green
image[100:150, :, 2] = 255  # red
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_2.py

# ch5_2.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
image.fill(255)  # 元素內容改為白色 255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_3.py

# ch5_3.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.ones((height, width), np.uint8) * 255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_4.py

# ch5_4.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_5.py

# ch5_5.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 建立GRAY影像陣列
image = np.zeros((height, width), np.uint8)
for y in range(0, height, 20):
    image[y : y + 10, :] = 255  # 白色厚度是10
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_6.py

# ch5_6.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256, size=[height, width], dtype=np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_7.py

# ch5_7.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
image[:, :, 0] = 255  # 建立 B 通道像素值
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_8.py

# ch5_8.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
blue_image = image.copy()
blue_image[:, :, 0] = 255  # 建立 B 通道像素值
cv2.imshow("blue image", blue_image)  # 顯示blue image影像

green_image = image.copy()
green_image[:, :, 1] = 255  # 建立 G 通道像素值
cv2.imshow("green image", green_image)  # 顯示green image影像

red_image = image.copy()
red_image[:, :, 2] = 255  # 建立 R 通道像素值
cv2.imshow("red image", red_image)  # 顯示red image影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\opencv\__new\OpenCV影像創意邁向AI視覺\ch05\ch5_9.py

# ch5_9.py
import cv2
import numpy as np

height = 160  # 影像高
width = 280  # 影像寬
# 使用random.randint()建立GRAY影像陣列
image = np.random.randint(256, size=[height, width, 3], dtype=np.uint8)
cv2.imshow("image", image)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
