"""


"""

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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

print('open-close')

import cv2
import numpy as np

original_img = cv2.imread('data/flower.png',0)
gray_res = cv2.resize(original_img,None,fx=0.8,fy=0.8,
                 interpolation = cv2.INTER_CUBIC)#图形太大了缩小一点
# B, G, img = cv2.split(res)
# _,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY) #设定红色通道阈值160（阈值影响开闭运算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))   #定义矩形结构元素
#闭运算1
closed1 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=1) 
#闭运算2   
closed2 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=3)  
#开运算1  
opened1 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel,iterations=1)  
#开运算2   
opened2 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel,iterations=3)   
#梯度  
gradient = cv2.morphologyEx(gray_res, cv2.MORPH_GRADIENT, kernel)      

#显示如下腐蚀后的图像
cv2.imshow("gray_res", gray_res)
cv2.imshow("Close1",closed1)
cv2.imshow("Close2",closed2)
cv2.imshow("Open1", opened1)
cv2.imshow("Open2", opened2)
cv2.imshow("gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()




print('------------------------------------------------------------')	#60個

print('morphology 形態學')


import cv2

original_img0 = cv2.imread('data/lena.png')
original_img = cv2.imread('data/lena.png',0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))                  #定义矩形结构元素
TOPHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_TOPHAT, kernel)     #顶帽运算
BLACKHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_BLACKHAT, kernel) #黒帽运算

#显示图像
cv2.imshow("original_img0", original_img0)
cv2.imshow("original_img", original_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)

cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('erode-dilate')

import cv2
import numpy as np

original_img = cv2.imread('data/flower.png')
res = cv2.resize(original_img,None,fx=0.6, fy=0.6,
                 interpolation = cv2.INTER_CUBIC) #图形太大了缩小一点
B, G, R = cv2.split(res)                    #获取红色通道
img = R
_,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
#OpenCV定义的结构矩形元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
eroded = cv2.erode(RedThresh,kernel)        #腐蚀图像
dilated = cv2.dilate(RedThresh,kernel)      #膨胀图像

cv2.imshow("original_img", res)             #原图像
cv2.imshow("R_channel_img", img)            #红色通道图
cv2.imshow("RedThresh", RedThresh)          #红色阈值图像
cv2.imshow("Eroded Image",eroded)           #显示腐蚀后的图像
cv2.imshow("Dilated Image",dilated)         #显示膨胀后的图像

#NumPy定义的结构元素
NpKernel = np.uint8(np.ones((3,3)))
Nperoded = cv2.erode(RedThresh,NpKernel)       #腐蚀图像

cv2.imshow("Eroded by NumPy kernel",Nperoded)  #显示腐蚀后的图像
cv2.waitKey(0)
cv2.destroyAllWindows()



print('------------------------------------------------------------')	#60個

print('Canny')


import cv2
import numpy 

image = cv2.imread("data/jianzhu.png",cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilate_img = cv2.dilate(image, kernel)
erode_img = cv2.erode(image, kernel) 
"""
将两幅图像相减获得边；cv2.absdiff参数：(膨胀后的图像，腐蚀后的图像)
上面得到的结果是灰度图，将其二值化以便观察结果
反色，对二值图每个像素取反
"""
absdiff_img = cv2.absdiff(dilate_img,erode_img);
retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY); 
result = cv2.bitwise_not(threshold_img); 
cv2.imshow("jianzhu",image)
cv2.imshow("dilate_img",dilate_img)
cv2.imshow("erode_img",erode_img)
cv2.imshow("absdiff_img",absdiff_img)
cv2.imshow("threshold_img",threshold_img)
cv2.imshow("result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('bitwise')

import cv2

original_img = cv2.imread('data/lena.png',0)
gray_img = cv2.resize(original_img,None,fx=0.8, fy=0.8,
                 interpolation = cv2.INTER_CUBIC) #图形太大了缩小一点

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))              #定义矩形结构元素(核大小为3效果好)
TOPHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_TOPHAT, kernel)     #顶帽运算
BLACKHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_BLACKHAT, kernel) #黒帽运算

bitwiseXor_gray = cv2.bitwise_xor(gray_img,TOPHAT_img)

#显示如下腐蚀后的图像
cv2.imshow("gray_img", gray_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)
cv2.imshow("bitwiseXor_gray",bitwiseXor_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('absdiff')

import cv2 

image = cv2.imread("data/jianzhu.png",0)
original_image = image.copy()
#构造5×5的结构元素，分别为十字形、菱形、方形和X型
cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
diamond = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0
square = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))  #构造方形结构元素
x = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))     

dilate_cross_img = cv2.dilate(image,cross)                #使用cross膨胀图像
erode_diamond_img = cv2.erode(dilate_cross_img, diamond)  #使用菱形腐蚀图像

dilate_x_img = cv2.dilate(image, x)                       #使用X膨胀原图像 
erode_square_img = cv2.erode(dilate_x_img,square)         #使用方形腐蚀图像 

result = cv2.absdiff(erode_square_img, erode_diamond_img)          #将两幅闭运算的图像相减获得角
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY) #使用阈值获得二值图

#在原图上用半径为5的圆圈将点标出。
for j in range(result.size):
    y = int(j / result.shape[0])
    x = int(j % result.shape[0])
    if result[x, y] == 255:                                        #result[] 只能传入整型
        cv2.circle(image,(y,x),5,(255,0,0))

cv2.imshow("original_image", original_image)
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


