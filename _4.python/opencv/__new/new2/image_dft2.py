import numpy as np
import matplotlib.pyplot as plt

print('跑不出來')

PI = 3.141591265

img = plt.imread('data/castle3.jpg')
#根据公式转成灰度图
img = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]

#显示原图
plt.subplot(131),plt.imshow(img,'gray'),plt.title('original')

#进行傅立叶变换，并显示结果
fft2 = np.fft.fft2(img)
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(132),plt.imshow(log_fft2,'gray'),plt.title('log_fft2')

h , w = img.shape
#生成一个同样大小的复数矩阵
F = np.zeros([h,w],'complex128')
for u in range(h):
    for v in range(w):
        res = 0
        for x in range(h):
            for y in range(w):
                res += img[x,y] * np.exp(-1.j * 2 * PI * (u * x / h + v * y / w))
        F[u,v] = res

log_F = np.log(1 + np.abs(F))
plt.subplot(133)
plt.imshow(log_F,'gray')
plt.title('log_F')

