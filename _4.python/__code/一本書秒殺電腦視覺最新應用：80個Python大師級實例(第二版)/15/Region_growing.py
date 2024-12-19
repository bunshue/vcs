# 区域生长
from PIL import Image
import matplotlib.pyplot as plt  # plt用于显示图片
import numpy as np

im = Image.open("Marker.png")  # 读取图片
im_array = np.array(im)
print(im_array)
[m, n] = im_array.shape

a = np.zeros((m, n))  # 建立等大小空矩阵
a[70, 70] = 1  # 设立种子点
k = 40  # 设立区域判断生长阈值

flag = 1  # 设立是否判断的小红旗
while flag == 1:
    flag = 0
    lim = (np.cumsum(im_array * a)[-1]) / (np.cumsum(a)[-1])
    for i in range(2, m):
        for j in range(2, n):
            if a[i, j] == 1:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if a[i + x, j + y] == 0:
                            if abs(im_array[i + x, j + y] - lim) <= k:
                                flag = 1
                                a[i + x, j + y] = 1

data = im_array * a  # 矩阵相乘获取生长图像的矩阵
new_im = Image.fromarray(data)  # data矩阵转化为二维图片
# 画图展示
plt.subplot(1, 2, 1)
plt.imshow(im, cmap="gray")
plt.axis("off")  # 不显示坐标轴
plt.show()

plt.subplot(1, 2, 2)
plt.imshow(new_im, cmap="gray")
plt.axis("off")  # 不显示坐标轴
plt.show()
