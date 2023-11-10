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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/erode.bmp'
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('erode 效果 1')
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(image, kernel)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('erode 效果 1')
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/erode.bmp'
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('erode 效果 2')
kernel = np.ones((9, 9), np.uint8)
erosion = cv2.erode(image, kernel,iterations = 5)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('erode 效果 2')
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/dilation.bmp'
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('dilate 效果 1')
kernel = np.ones((9, 9), np.uint8)
dilation = cv2.dilate(image, kernel)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('dilate 效果 1')
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/dilation.bmp'
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('dilate 效果 2')
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(image, kernel, iterations = 9)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('dilate 效果 2')
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opening.bmp'
img1 = cv2.imread(filename)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opening2.bmp'
img2 = cv2.imread(filename)

print('morphologyEx 效果 1')
k = np.ones((10, 10), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
r2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, k)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 1')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 1')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/closing.bmp'
img1 = cv2.imread(filename)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/closing2.bmp'
img2 = cv2.imread(filename)

print('morphologyEx 效果 2')
k = np.ones((10, 10), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, k, iterations = 3)
r2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k, iterations = 3)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 2')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 2')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/gradient.bmp'
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('morphologyEx 效果 3')
k=np.ones((5, 5), np.uint8)
r=cv2.morphologyEx(image, cv2.MORPH_GRADIENT, k)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('morphologyEx 效果 3')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/tophat.bmp'
image1 = cv2.imread(filename,cv2.IMREAD_UNCHANGED)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image2=cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('morphologyEx 效果 4')
k = np.ones((5,5),np.uint8)
r1 = cv2.morphologyEx(image1, cv2.MORPH_TOPHAT, k)
r2 = cv2.morphologyEx(image2, cv2.MORPH_TOPHAT, k)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 4')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 4')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/blackhat.bmp'
image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('morphologyEx 效果 5')
k = np.ones((5,5), np.uint8)
r1 = cv2.morphologyEx(image1, cv2.MORPH_BLACKHAT, k)
r2 = cv2.morphologyEx(image2, cv2.MORPH_BLACKHAT, k)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 5')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 5')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print("kernel1 =\n", kernel1)
print("kernel2 =\n", kernel2)
print("kernel3 =\n", kernel3)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/kernel.bmp'
o = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('dilate 效果')
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59,59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (59,59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (59,59))
dst1 = cv2.dilate(o,kernel1)
dst2 = cv2.dilate(o,kernel2)
dst3 = cv2.dilate(o,kernel3)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('dilate 效果')
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('dilate 效果')
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('dilate 效果')
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('作業完成')


