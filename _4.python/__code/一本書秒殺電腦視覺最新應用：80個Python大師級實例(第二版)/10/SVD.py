"""
SVD

"""
print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# Gray

from PIL import Image

def svd_restore(sigma, u, v, K):
    K = min(len(sigma) - 1, K)  # 当K超过sigma的长度时会造成越界
    print("现在用%d等级恢复图像" % K)
    m = len(u)
    n = v[0].size
    SigRecon = np.zeros((m, n))  # 新建一int矩阵，储存恢复的灰度图像素
    for k in range(K + 1):  # 计算X=u*sigma*v
        for i in range(m):
            SigRecon[i] += sigma[k] * u[i][k] * v[k]
    # 计算得到的矩阵还是float型，需要将其转化为uint8以转为图片
    SigRecon = SigRecon.astype("uint8")
    Image.fromarray(SigRecon).save("svd_" + str(K) + "_" + image_file)  # 保存灰度图


image_file = "frog.jpg"

im = Image.open(image_file)  # 打开图像文件
im = im.convert("L")  # 将原图像转化为灰度图
im.save("Gray_" + image_file)  # 保存灰度图

w, h = im.size  # 得到原图的长与宽
# 新建一int矩阵，储存灰度图各像素点数据
dt = np.zeros((w, h), "uint8")
# 逐像素点复制，由于直接对im.getdata()进行数据类型转换会有偏差
for i in range(w):
    for j in range(h):
        dt[i][j] = im.getpixel((i, j))  # 取得該點之像素值
# 复制过来的图像是原图的翻转，因此将其再次翻转到正常角度
dt = dt.transpose()
u, sigma, v = np.linalg.svd(dt)  # 调用numpy库进行SVM
u = np.array(u)  # 转为array格式，方便进行乘法运算
v = np.array(v)  # 同上
for k in [1, 10, 30, 50, 80, 100, 150, 200, 300, 500]:
    svd_restore(sigma, u, v, k)  # 使用前k个奇异值进行恢复

print("------------------------------------------------------------")  # 60個
# RGB

from scipy import ndimage
from matplotlib.pyplot import imread
import imageio

# plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示


def pic_compress(k, pic_array):
    u, sigma, vt = np.linalg.svd(pic_array)
    sig = np.eye(k) * sigma[:k]
    new_pic = np.dot(np.dot(u[:, :k], sig), vt[:k, :])  # 还原图像
    size = u.shape[0] * k + sig.shape[0] * sig.shape[1] + k * vt.shape[1]  # 压缩后大小
    return new_pic, size


filename = "frog.jpg"
#ori_img = np.array(ndimage.imread(filename, flatten=True))
ori_img = np.array(imageio.imread(filename))
new_img, size = pic_compress(100, ori_img)
print("原始图像大小:" + str(ori_img.shape[0] * ori_img.shape[1]))
print("压缩后图像大小:" + str(size))
fig, ax = plt.subplots(1, 2)
ax[0].imshow(ori_img)
ax[0].set_title("压缩前")
ax[1].imshow(new_img)
ax[1].set_title("压缩后")

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
