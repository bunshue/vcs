import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r=cv2.blur(o,(5,5))
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r5=cv2.blur(o,(5,5))      
r30=cv2.blur(o,(30,30))      
cv2.imshow("result5",r5)
cv2.imshow("result30",r30)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r=cv2.boxFilter(o,-1,(5,5)) 
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r=cv2.boxFilter(o,-1,(5,5),normalize=0) 
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r=cv2.boxFilter(o,-1,(2,2),normalize=0) 
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r=cv2.GaussianBlur(o,(5,5),0,0)
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r=cv2.medianBlur(o,3)
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('lena_noise.png')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
r=cv2.bilateralFilter(o,25,100,100)
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o=cv2.imread('bilTest.bmp')
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
g=r=cv2.GaussianBlur(o,(55,55),0,0)
cv2.imshow("Gaussian",g)

print('顯示xxxx')
b=cv2.bilateralFilter(o,55,100,100)
cv2.imshow("bilateral",b)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示xxxx')
kernel = np.ones((9,9),np.float32)/81
r = cv2.filter2D(o,-1,kernel)
cv2.imshow("Gaussian",r)

cv2.waitKey()
cv2.destroyAllWindows()

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

print('顯示xxxx')
saltImage=saltpepper(img,0.02)
cv2.imshow('saltImage',saltImage)

#cv2.imwrite('test.jpg',img) 偽寫入

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




