import numpy as np
import matplotlib.pyplot as plt
import cv2

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

img = cv2.imread('data/lena.png',0)  
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft) 
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('原始图像')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('级频谱')
plt.xticks([]), plt.yticks([])

plt.show()
