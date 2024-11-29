import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

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
ori_img = np.array(ndimage.imread(filename, flatten=True))
new_img, size = pic_compress(100, ori_img)
print("原始图像大小:" + str(ori_img.shape[0] * ori_img.shape[1]))
print("压缩后图像大小:" + str(size))
fig, ax = plt.subplots(1, 2)
ax[0].imshow(ori_img)
ax[0].set_title("压缩前")
ax[1].imshow(new_img)
ax[1].set_title("压缩后")

plt.show()
