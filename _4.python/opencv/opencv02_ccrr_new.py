"""
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from opencv_common import *


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# cv2.resize 的 5種 插值法

import cv2

"""
INTER_NEAREST | 最近邻插值
INTER_LINEAR | 双线性插值（默认设置）
INTER_AREA |  使用像素区域关系进行重采样。 它可能是图像抽取的首选方法，因为它会产生无云纹理的结果。 但是当图像缩放时，它类似于INTER_NEAREST方法。
INTER_CUBIC  | 4x4像素邻域的双三次插值
INTER_LANCZOS4 |  8x8像素邻域的Lanczos插值
"""

filename = 'D:/_git/vcs/_4.python/_data/picture1.jpg'

img = cv2.imread(filename)
height, width = img.shape[:2]

# 缩小图像
size = (int(width*0.8), int(height*0.7))
shrink_NEAREST = cv2.resize(img, size, interpolation=cv2.INTER_NEAREST)
shrink_LINEAR = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)
shrink_AREA = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
shrink_CUBIC = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
shrink_LANCZOS4 = cv2.resize(img, size, interpolation=cv2.INTER_LANCZOS4)

# 放大图像
fx = 1.2
fy = 1.1
enlarge_NEAREST = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_NEAREST)
enlarge_LINEAR = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
enlarge_AREA = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_AREA)
enlarge_CUBIC = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
enlarge_LANCZOS4 = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_LANCZOS4)

# 保存图像
cv2.imwrite("shrink_NEAREST.jpg", shrink_NEAREST)
cv2.imwrite("shrink_LINEAR.jpg", shrink_LINEAR)
cv2.imwrite("shrink_AREA.jpg", shrink_AREA)
cv2.imwrite("shrink_CUBIC.jpg", shrink_CUBIC)
cv2.imwrite("shrink_LANCZOS4.jpg", shrink_LANCZOS4)

cv2.imwrite("enlarge_NEAREST.jpg", enlarge_NEAREST)
cv2.imwrite("enlarge_LINEAR.jpg", enlarge_LINEAR)
cv2.imwrite("enlarge_AREA.jpg", enlarge_AREA)
cv2.imwrite("enlarge_CUBIC.jpg", enlarge_CUBIC)
cv2.imwrite("enlarge_LANCZOS4.jpg", enlarge_LANCZOS4)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


fname = "cccc.png"
image = cv2.imread(fname)  # 彩色讀取

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

image_resize1 = cv2.resize(image, (760, 384))  # resize 成 640x480 的圖
cv2.imshow("image", image_resize1)

cv2.waitKey()
cv2.destroyAllWindows()


image_resize0 = cv2.resize(image, (760, 384), interpolation=cv2.INTER_NEAREST)
image_resize1 = cv2.resize(image, (760, 384), interpolation=cv2.INTER_LINEAR)
image_resize2 = cv2.resize(image, (760, 384), interpolation=cv2.INTER_CUBIC)
image_resize3 = cv2.resize(image, (760, 384), interpolation=cv2.INTER_AREA)
image_resize4 = cv2.resize(image, (760, 384), interpolation=cv2.INTER_LANCZOS4)

pic_name = "tmp_pic0.png"
cv2.imwrite(pic_name, image_resize0)
pic_name = "tmp_pic1.png"
cv2.imwrite(pic_name, image_resize1)
pic_name = "tmp_pic2.png"
cv2.imwrite(pic_name, image_resize2)
pic_name = "tmp_pic3.png"
cv2.imwrite(pic_name, image_resize3)
pic_name = "tmp_pic4.png"
cv2.imwrite(pic_name, image_resize4)



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


