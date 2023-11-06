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
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 blur 效果 1')
r=cv2.blur(o,(5,5))
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 blur 效果 2')
r5=cv2.blur(o,(5,5))      
r30=cv2.blur(o,(30,30))      
cv2.imshow("result5",r5)
cv2.imshow("result30",r30)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 boxFilter 效果 1')
r=cv2.boxFilter(o,-1,(5,5)) 
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 boxFilter 效果 2')
r=cv2.boxFilter(o,-1,(5,5),normalize=0) 
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 boxFilter 效果 3')
r=cv2.boxFilter(o,-1,(2,2),normalize=0) 
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 medianBlur 效果 1')
r=cv2.medianBlur(o,3)
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 bilateralFilter 效果')
r=cv2.bilateralFilter(o,25,100,100)
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 bilateralFilter 效果')
b = cv2.bilateralFilter(o, 55, 100, 100)
cv2.imshow("bilateral", b)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 filter2D 效果')
kernel = np.ones((9,9),np.float32)/81
r = cv2.filter2D(o,-1,kernel)
cv2.imshow('filter2D', r)

cv2.waitKey()
cv2.destroyAllWindows()


filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'

o = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
print('顯示原圖')
cv2.imshow("original", o)

kernel_x = np.array([[1,1,1], [0,0,0], [-1,-1,-1]], dtype = int)    #水平值一樣, 偵測水平的邊緣
kernel_y = np.array([[-1,0,1], [-1,0,1], [-1,0,1]], dtype = int)    #垂直值一樣, 偵測垂直的邊緣

print('顯示 filter2D 效果')

x = cv2.filter2D(o, cv2.CV_16S, kernel_x)
y = cv2.filter2D(o, cv2.CV_16S, kernel_y)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

cv2.imshow('Prewitt_horizon', absX) #躺平的書本的邊緣有被強調出來
cv2.imshow('Prewitt_vertical', absY)#直放的書本的邊緣有被強調出來

cv2.waitKey()
cv2.destroyAllWindows()

sys.exit()

print('------------------------------------------------------------')	#60個

def saltpepper(img,n):
    m=int((img.shape[0]*img.shape[1])*n)
    for a in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=255
        elif img.ndim==3:
            img[j,i,0]=255
            img[j,i,1]=255
            img[j,i,2]=255
    for b in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=0
        elif img.ndim==3:
            img[j,i,0]=0
            img[j,i,1]=0
            img[j,i,2]=0
    return img

#上面就是椒盐噪声函数，下面是使用方法，大家可以愉快的玩耍了
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
print('顯示原圖')

print('顯示 saltpepper 效果')
saltImage=saltpepper(img,0.02)
cv2.imshow('saltImage',saltImage)

#cv2.imwrite('test.jpg',img) 偽寫入

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




