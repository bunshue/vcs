import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签

img = plt.imread('castle3.jpg')
#根据公式转成灰度图
img = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]
#显示原图
plt.subplot(231)
plt.imshow(img,'gray')
plt.title('原始图像')
#进行傅立叶变换，并显示结果
fft2 = np.fft.fft2(img)
plt.subplot(232)
plt.imshow(np.abs(fft2),'gray')
plt.title('二维傅里叶变换')
#将图像变换的原点移动到频域矩形的中心，并显示效果
shift2center = np.fft.fftshift(fft2)
plt.subplot(233)
plt.imshow(np.abs(shift2center),'gray')
plt.title('频域矩形的中心')
#对傅立叶变换的结果进行对数变换，并显示效果
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(235)
plt.imshow(log_fft2,'gray')
plt.title('傅立叶变换对数变换')
#对中心化后的结果进行对数变换，并显示结果
log_shift2center = np.log(1 + np.abs(shift2center))
plt.subplot(236)
plt.imshow(log_shift2center,'gray')
plt.title('中心化的对数变化')
plt.show()
