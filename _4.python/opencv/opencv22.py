import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('blur 效果 1')
r = cv2.blur(image, (5, 5))

plt.figure('blur 效果', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('blur 效果 1')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('blur 效果 2')
image_blur_05 = cv2.blur(image, (5, 5))      
image_blur_30 = cv2.blur(image, (30, 30))      

plt.figure('blur 效果', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('blur 效果 2')
plt.imshow(cv2.cvtColor(image_blur_05, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('blur 效果 2')
plt.imshow(cv2.cvtColor(image_blur_30, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('boxFilter 效果 1')
r=cv2.boxFilter(image, -1, (5, 5)) 

plt.figure('boxFilter 效果', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('boxFilter 效果 1')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('boxFilter 效果 2')
r = cv2.boxFilter(image, -1, (5, 5), normalize = 0)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('boxFilter 效果 2')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('boxFilter 效果 3')
r = cv2.boxFilter(image, -1, (2, 2), normalize = 0)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('boxFilter 效果 3')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('medianBlur 效果 1')
r = cv2.medianBlur(image,3)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('medianBlur 效果 1')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('bilateralFilter 效果')
r = cv2.bilateralFilter(image, 25, 100, 100)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('bilateralFilter 效果')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp'
image = cv2.imread(filename)

print('bilateralFilter 效果')
b = cv2.bilateralFilter(image, 55, 100, 100)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('bilateralFilter 效果')
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename)

print('filter2D 效果')
kernel = np.ones((9, 9), np.float32) / 81
r = cv2.filter2D(image, -1, kernel)

plt.figure('filter2D 效果', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('filter2D 效果')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'

image = cv2.imread(filename, cv2.COLOR_BGR2GRAY)

kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype = int)    #水平值一樣, 偵測水平的邊緣
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype = int)    #垂直值一樣, 偵測垂直的邊緣

print('filter2D 效果')

x = cv2.filter2D(image, cv2.CV_16S, kernel_x)
y = cv2.filter2D(image, cv2.CV_16S, kernel_y)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Prewitt_horizon')
#躺平的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absX, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Prewitt_vertical')
#直放的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absY, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

def saltpepper(image, n):
    m=int((image.shape[0] * image.shape[1]) * n)
    for a in range(m):
        i=int(np.random.random()*image.shape[1])
        j=int(np.random.random()*image.shape[0])
        if image.ndim==2:
            image[j,i]=255
        elif image.ndim==3:
            image[j,i,0]=255
            image[j,i,1]=255
            image[j,i,2]=255
    for b in range(m):
        i=int(np.random.random()*image.shape[1])
        j=int(np.random.random()*image.shape[0])
        if image.ndim==2:
            image[j,i]=0
        elif image.ndim==3:
            image[j,i,0]=0
            image[j,i,1]=0
            image[j,i,2]=0
    return image

#上面就是椒盐噪声函数，下面是使用方法，大家可以愉快的玩耍了
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename)

print('saltpepper 效果')
saltImage = saltpepper(image, 0.02)

plt.figure('saltpepper 效果', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('saltpepper 效果')
plt.imshow(cv2.cvtColor(saltImage, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

