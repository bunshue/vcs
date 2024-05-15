import cv2

ESC = 27
SPACE = 32

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

print("共用函數------------------------------------------------------------")  # 60個

from scipy import signal

# sobel 边缘检测
def sobel(image,winSize):
    rows,cols = image.shape
    pascalSmoothKernel = pascalSmooth(winSize)
    pascalDiffKernel = pascalDiff(winSize)
    # --- 与水平方向的卷积核卷积 ----
    image_sobel_x = np.zeros(image.shape,np.float32)
    #垂直方向上的平滑
    image_sobel_x = signal.convolve2d(image,pascalSmoothKernel.transpose(),mode='same')
    #水平方向上的差分
    image_sobel_x = signal.convolve2d(image_sobel_x,pascalDiffKernel,mode='same')
    # --- 与垂直方向上的卷积核卷积 --- 
    image_sobel_y = np.zeros(image.shape,np.float32)
    #水平方向上的平滑
    image_sobel_y = signal.convolve2d(image,pascalSmoothKernel,mode='same')
    #垂直方向上的差分
    image_sobel_y = signal.convolve2d(image_sobel_y,pascalDiffKernel.transpose(),mode='same')
    return (image_sobel_x,image_sobel_y)

#二项式展开式的系数，即平滑系数
def pascalSmooth(n):
    pascalSmooth = np.zeros([1,n],np.float32)
    for i in range(n):
        pascalSmooth[0][i] = math.factorial(n -1)/(math.factorial(i)*math.factorial(n-1-i))
    return pascalSmooth

#计算差分
def pascalDiff(n):
    pascalDiff = np.zeros([1,n],np.float32)
    pascalSmooth_previous = pascalSmooth(n-1)
    for i in range(n):
        if i ==0:
            #恒等于 1
            pascalDiff[0][i] = pascalSmooth_previous[0][i]
        elif i == n-1:
            #恒等于 -1
            pascalDiff[0][i] = -pascalSmooth_previous[0][i-1]
        else:
            pascalDiff[0][i] = pascalSmooth_previous[0][i] - pascalSmooth_previous[0][i-1]
    return pascalDiff

#通过平滑系数和差分系数的卷积运算计算卷积核
def getSobelKernel(winSize):
     pascalSmoothKernel = pascalSmooth(winSize)
     pascalDiffKernel = pascalDiff(winSize)
     #水平方向上的卷积核
     sobelKernel_x = signal.convolve2d(pascalSmoothKernel.transpose(),pascalDiffKernel,mode='full')
     #垂直方向上的卷积核
     sobelKernel_y = signal.convolve2d(pascalSmoothKernel,pascalDiffKernel.transpose(),mode='full')
     return (sobelKernel_x,sobelKernel_y)

print("------------------------------------------------------------")  # 60個

print('測試cv2視窗的Trackbar')

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename)

#调整对比度后，图像的效果显示窗口
cv2.namedWindow("TrackbarTest",cv2.WND_PROP_AUTOSIZE)

cv2.imshow("TrackbarTest", image)

MAX_VALUE = 80
MIN_VALUE = 30  # 無效，看起來最小值一定要0
initial_value = 40

#调整系数，观察图像的变化
def callback_trackbar_test(_value):
    print(_value, end = " ")

callback_trackbar_test(initial_value)#做一次

#cv2.createTrackbar('滑桿名稱', '視窗名稱', min, max, fn)
# min 最小值 ( 最小為 0，不可為負值 )
# max 最大值
# fn 滑桿數值改變時要執行的函式
cv2.createTrackbar("value", "TrackbarTest", MIN_VALUE, MAX_VALUE, callback_trackbar_test)  # callback function
cv2.setTrackbarPos('value', 'TrackbarTest', initial_value)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
img = cv2.imread(filename)
cv2.imshow('ImageProcessing', img)

contrast = 0    # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值
cv2.imshow('ImageProcessing', img)

# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c/100 + 1) - c + b    # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    cv2.imshow('ImageProcessing', output)

# 定義調整亮度函式
def brightness_fn(val):
    global img, contrast, brightness
    brightness = val - 100
    adjust(img, contrast, brightness)

# 定義調整對比度函式
def contrast_fn(val):
    global img, contrast, brightness
    contrast = val - 100
    adjust(img, contrast, brightness)

cv2.createTrackbar('brightness', 'ImageProcessing', 0, 200, brightness_fn)  # 加入亮度調整滑桿
cv2.setTrackbarPos('brightness', 'ImageProcessing', 100)

cv2.createTrackbar('contrast', 'ImageProcessing', 0, 200, contrast_fn)      # 加入對比度調整滑桿
cv2.setTrackbarPos('contrast', 'ImageProcessing', 100)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('測試 cv2.linearPolar')
print("空間變換 極座標變換 linearPolar_OpenCV3")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
src = cv2.imread(filename,cv2.IMREAD_ANYCOLOR)

#显示原图
cv2.imshow("src",src)

#图像的极坐标变换
dst = cv2.linearPolar(src,(508,503),550,cv2.INTER_LINEAR)

#显示极坐标变化的结果
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('測試 cv2.logPolar')

print("空間變換 極座標變換 logPolar")

src = cv2.imread(filename,cv2.IMREAD_ANYCOLOR)
#显示原图
cv2.imshow("src",src)
#图像的极坐标变换
M = 150
dst=cv2.logPolar(src,(508,503),M,cv2.WARP_FILL_OUTLIERS)
#显示极坐标变化的结果
print(src.shape)
print(dst.shape)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("空間變換 極座標變換 Polar")

#极坐标变换
def polar(I,center,r,theta=(0,360),rstep=1.0,thetastep=360.0/(180*8)):
    #得到距离的最小最大范围 
    minr,maxr = r
    #角度的最小范围
    mintheta,maxtheta = theta
    #输出图像的高，宽
    H = int((maxr-minr)/rstep)+1
    W =  int((maxtheta-mintheta)/thetastep)+1
    O = np.zeros((H,W),I.dtype)
    #极坐标变换
    r = np.linspace(minr,maxr,H)
    r = np.tile(r,(W,1))
    r = np.transpose(r)
    theta = np.linspace(mintheta,maxtheta,W)
    theta = np.tile(theta,(H,1))
    x,y=cv2.polarToCart(r,theta,angleInDegrees=True)
    #最近邻插值
    for i in range(H):
        for j in range(W):
            px = int(round(x[i][j])+cx)
            py = int(round(y[i][j])+cy)
            if(px>w-1 or py >h-1):
                O[i][j] = 125#灰色
            else:
                O[i][j] = I[py][px]
    return O
    
I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#图像的宽高
h,w = I.shape[:2]
print(w,h)
#极左标变换的中心
cx,cy = w/2.0,h/2.0+10
print(cx,cy)
cv2.circle(I,(int(cx),int(cy)),10,(255.0,0,0),3)
#距离的最小最大半径 #200 550 270,340
O = polar(I,(cx,cy),(270,340))
#旋转
O = cv2.flip(O,0)

#显示原图和输出图像
cv2.imshow("I",I)
cv2.imshow("O",O)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強1")

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename)
MAX_VALUE = 120
value = 120

#调整对比度后，图像的效果显示窗口
cv2.namedWindow("contrast",cv2.WND_PROP_AUTOSIZE)

#调整系数，观察图像的变化
def callback_contrast(_value):
    #通过线性运算，调整图像对比度
    a = float(_value)/40.0
    contrastImage = a*image
    contrastImage[contrastImage>255]=255
    contrastImage = np.round(contrastImage)
    contrastImage = contrastImage.astype(np.uint8)
    cv2.imshow("contrast",contrastImage)

callback_contrast(value)
cv2.createTrackbar("value","contrast",value,MAX_VALUE,callback_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強2")

#分段线性变换
def piecewiseLinear(image,point1,point2):
    #确保 point1 在 point2的左下角
    x1,y1 = point1
    x2,y2 = point2
    # 0 - point1.x
    a1 = float(y1)/x1
    b1 = 0
    # point1.x - point2.x
    a2 = float(y2-y1)/float(x2-x1)
    b2 = y1 - a2*x1
    print(a2)
    #point2.x - 255
    a3 = float(255 - y2)/(255-x2)
    b3 = 255 - a3*255
    #输出图像
    outPutImage = np.zeros(image.shape,np.uint8)
    #图像的宽高
    rows,cols = image.shape
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            if pixel <= x1:
                outPixel = a1*pixel + b1
            elif pixel>x1 and pixel < x2:
                outPixel = a2*pixel + b2
            else:
                outPixel = a3*pixel + b3
            outPixel = round(outPixel)
            outPutImage[r][c] = outPixel
    return outPutImage


image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
#分段线性变换
outPutImage = piecewiseLinear(image,(100,50),(150,230))
cv2.imshow("outPutImage",outPutImage)
#显示直方图正规化后图片的灰度直方图
#组数
numberBins = 256
#计算灰度直方图
rows,cols = outPutImage.shape
histSeq = outPutImage.reshape([rows*cols,])
histogram,bins,patch_image= plt.hist(histSeq,numberBins,facecolor='black',histtype='bar')
#设置坐标轴的标签
plt.xlabel(u"gray Level")
plt.ylabel(u"number of pixels")
#设置坐标轴的范围
y_maxValue = np.max(histogram)
print(y_maxValue)
plt.axis([0,255,0,y_maxValue])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強3 histNormalized")

#直方图正规化
#1、若输入是 8 位图 ，一般设置 O_min = 0，O_max = 255
#2、若输入的是归一化的图像，一般设置 O_min = 0，O_max = 1
def histNormalized(InputImage,O_min = 0,O_max = 255):
    #得到输入图像的最小灰度值
    I_min = np.min(InputImage)
    #得到输入图像的最大灰度值
    I_max = np.max(InputImage)
    #得到输入图像的宽高
    rows,cols = InputImage.shape
    #输出图像
    OutputImage = np.zeros(InputImage.shape,np.float32)
    #输出图像的映射
    cofficient = float(O_max - O_min)/float(I_max - I_min)
    for r in range(rows):
        for c in range(cols):
            OutputImage[r][c] = cofficient*( InputImage[r][c] - I_min) + O_min
    return OutputImage

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#直方图正规化
histNormResult = histNormalized(image)
#数据类型转换，灰度级显示
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)
#显示直方图正规化的图片
cv2.imshow("histNormlized",histNormResult)
"""
#如果输入图像是归一化的图像
image_0_1 = image/255.0
#直方图正规化
histNormResult = histNormalized(image_0_1,0,1)
#保存结果
histNormResult = 255.0*histNormResult
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)
"""
#显示直方图正规化后图片的灰度直方图
#组数
numberBins = 256
#计算灰度直方图
rows,cols = image.shape
histNormResultSeq = histNormResult.reshape([rows*cols,])
histogram,bins,patch_image= plt.hist(histNormResultSeq,numberBins,facecolor='black',histtype='bar')
#设置坐标轴的标签
plt.xlabel(u"gray Level")
plt.ylabel(u"number of pixels")
#设置坐标轴的范围
y_maxValue = np.max(histogram)
plt.axis([0,255,0,y_maxValue])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強4 gamma")

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename)

MAX_VALUE = 200
value = 40
segValue = float(value)
#伽马调整需要先将图像归一化
image_0_1 = image/255.0
#伽马调整后的图像显示窗口
cv2.namedWindow("gamma_contrast",cv2.WND_PROP_AUTOSIZE)

#调整 gamma 值，观察图像的变换
def callback_contrast(_value):
    gamma = float(_value)/segValue
    contrastImage = np.power(image_0_1,gamma)
    cv2.imshow("gamma_contrast",contrastImage)
    #保存伽马调整的结果
    contrastImage*=255
    contrastImage = np.round(contrastImage)
    contrastImage = contrastImage.astype(np.uint8)

callback_contrast(value)
cv2.createTrackbar("value","gamma_contrast",value,MAX_VALUE,callback_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強5 equalHist")

#计算图像灰度直方图
def calcGrayHist(image):
    #灰度图像矩阵的宽高
    rows,cols = image.shape
    #存储灰度直方图
    grayHist = np.zeros([256],np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] +=1
    return grayHist

#直方图均衡化
def equalHist(image):
    #灰度图像矩阵的宽高
    rows,cols = image.shape
    #计算灰度直方图
    grayHist = calcGrayHist(image)
    #计算累积灰度直方图
    zeroCumuMoment = np.zeros([256],np.uint32)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p-1] + grayHist[p]
    #根据直方图均衡化得到的输入灰度级和输出灰度级的映射
    outPut_q = np.zeros([256],np.uint8)
    cofficient = 256.0/(rows*cols)
    for p in range(256):
        q = cofficient* float(zeroCumuMoment[p]) -1
        if q >= 0:
            outPut_q[p] = math.floor(q)
        else:
            outPut_q[p] = 0
    #得到直方图均衡化后的图像
    equalHistImage  = np.zeros(image.shape,np.uint8)
    for r in range(rows):
        for c in range(cols):
            equalHistImage[r][c] = outPut_q[image[r][c]]
    return equalHistImage

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图像
cv2.imshow("image",image)
#直方图均衡化
result = equalHist(image)
cv2.imshow("equalHist",result)
#直方图均衡话后的灰度直方图
#组数
numberBins = 256
#计算灰度直方图
rows,cols = image.shape
histEqualResultSeq = result.reshape([rows*cols,])
histogram,bins,patch_image= plt.hist(histEqualResultSeq,numberBins,facecolor='black',histtype='bar')
#设置坐标轴的标签
plt.xlabel(u"gray Level")
plt.ylabel(u"number of pixels")
#设置坐标轴的范围
y_maxValue = np.max(histogram)
plt.axis([0,255,0,y_maxValue])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強6 CLAHE")

#第一步：读入图像
src = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#创建 CLAHE  对象
clahe = cv2.createCLAHE(clipLimit=1.0,tileGridSize=(28,28))
#限制对比度的自适应阈值均衡化
dst = clahe.apply(src)
#显示
cv2.imshow("src",src)
cv2.imshow("clahe",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖像平滑 copyMakeBorder")

src=np.array([[5,1,7],[1,5,9],[2,6,2]])
dst=cv2.copyMakeBorder(src,2,2,2,2,2)
print(dst)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 sameConv2d")

#输入矩阵
I = np.array([[1,2],[3,4]],np.float32)
# I 的高和宽
H1,W1 = I.shape[:2]
#卷积核
K = np.array([[-1,-2],[2,1]],np.float32)
# K 的高和宽
H2,W2 = K.shape[:2]
#计算 full 卷积
c_full = signal.convolve2d(I,K,mode='full')
#指定锚点的位置
kr,kc = 1,0
#根据锚点位置，从 full 卷积中截取得到 same 卷积
c_same = c_full[H2-kr-1:H1+H2-kr-1,W2-kc-1:W1+W2-kc-1]
print(c_same)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 sepConv")

from scipy import signal

kernel1 = np.array([[1,2,3]],np.float32)
kernel2 = np.array([[4],[5],[6]],np.float32)
#计算两个核的全卷积
kernel = signal.convolve2d(kernel1,kernel2,mode='full')

print("------------------------------------------------------------")  # 60個

print("圖像平滑 conv")

from scipy import signal

#图像矩阵
"""
I=np.array([[1,2,3,10,12],
            [32,43,12,4,190],
            [12,234,78,0,12],
            [43,90,32,8,90],
            [71,12,4,98,123]],np.float32)
"""
I = np.ones((10,10),np.float32)
I[1:3,3:5]=5
I[3:5,4:7]=3
#卷积核
"""
    kernel = np.array([[1,0,-1],
                   [1,0,-1],
                   [1,0,-1]])
"""
kernel1 = np.array([[1,3,4],[9,10,2],[-1,10,2]],np.float32)
kernel2 = np.array([[-1,2,3],[4,5,6],[10,9,10]],np.float32)
#kernel1 = np.array([[-1,2,3]],np.float32)
#kernel2 = np.array([[10],[43],[1]],np.float32)
kernel = signal.convolve2d(kernel1,kernel2,mode='full')
print(kernel)

#第一种方式:直接进行卷积运算得到的结果
I_Kernel = signal.convolve2d(I,kernel,mode='same',boundary = 'symm',fillvalue= 0)

#第二种方式:用可分离卷积核性质得到的结果
I_kernel1 = signal.convolve2d(I,kernel1,mode='same',boundary = 'wrap',fillvalue= 0)
I_kernel1_kernel2 = signal.convolve2d(I_kernel1,kernel2,mode='same',boundary = 'wrap',fillvalue= 0)

#print(I_Kernel)
print("*******************")
print(np.max(np.abs(I_Kernel - I_kernel1_kernel2)))
print("********************")
print(I_Kernel)
print(I_kernel1_kernel2)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 conv2")

from scipy import signal

#图像矩阵
I=np.array([[1,2,3,10,12],
            [32,43,12,4,190],
            [12,234,78,0,12],
            [43,90,32,8,90],
            [71,12,4,98,123]],np.float32)
#卷积核
kernel = np.array([[1,0,-1],
                   [1,0,-1],
                   [1,0,-1]])
# full 卷积
fullConv = signal.convolve2d(I,kernel,mode='full',boundary = 'fill',fillvalue= 0)
# same 卷积
sameConv = signal.convolve2d(I,kernel,mode='same',boundary = 'symm')
# valid 卷积
validConv = signal.convolve2d(I,kernel,mode='valid')
print(fullConv)
print(sameConv)
print(validConv)

print("------------------------------------------------------------")  # 60個

from scipy import signal

"""
得到高斯平滑算子：
getGaussKernel(sigma,H,W),使用过程中一般H和W一般为奇数，sigma大于零
"""

def getGaussKernel(sigma,H,W):
    """
        第一步：构建高斯矩阵gaussMatrix
    """
    gaussMatrix = np.zeros([H,W],np.float32)
    #得到中心点的位置
    cH = (H-1)/2
    cW = (W-1)/2
    #计算1/(2*pi*sigma^2)
    coefficient = 1.0/(2*np.pi*math.pow(sigma,2))
    #
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r-cH,2) + math.pow(c-cW,2)
            gaussMatrix[r][c] = coefficient*math.exp(-norm2/(2*math.pow(sigma,2)))
    """
        第二步：计算高斯矩阵的和
    """
    sumGM = np.sum(gaussMatrix)
    """
        第三步：归一化，gaussMatrix/sumGM
    """
    gaussKernel = gaussMatrix/sumGM
    return gaussKernel

gaussKernel = getGaussKernel(2,3,3)
print(gaussKernel)
#高斯核gaussKernel是可分解的，可以分解为水平方向和垂直方向的卷积核
gaussKernel_x = getGaussKernel(2,1,3)
print(gaussKernel_x)
gaussKernel_y = getGaussKernel(2,3,1)
print(gaussKernel_y)
"""
水平方向和垂直方向的卷积核进行卷积运算,注意：mode='full',boundary = 'fill',fillvalue=0
这样的参数设置，得到的结果才和gaussKernel完全相等，否则，边界不相等
"""
gaussKernel_xy = signal.convolve2d(gaussKernel_x,gaussKernel_y,mode='full',boundary ='fill',fillvalue=0)
print(gaussKernel_xy)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 gaussBlur")

from scipy import signal

#高斯平滑，返回的数据类型为浮点型
def gaussBlur(image,sigma,H,W,_boundary = 'fill',_fillvalue = 0):

    #构建HxW的高斯平滑算子
    #gaussKernelxy = getGaussKernel(sigma,H,W)
    #图像矩阵和高斯卷积核卷积
    #gaussBlur_xy = signal.convolve2d(image,gaussKernelxy,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    #return gaussBlur_xy

    #因为高斯核是可分解的，根据卷积的结合律
    #先进行水平方向的卷积，然后再进行垂直方向的卷积
    gaussKenrnel_x = getGaussKernel(sigma,1,W)
    gaussBlur_x = signal.convolve2d(image,gaussKenrnel_x,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    gaussKenrnel_y = getGaussKernel(sigma,H,1)
    gaussBlur_xy = signal.convolve2d(gaussBlur_x,gaussKenrnel_y,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    return gaussBlur_xy

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",image)
# 3 11 11 9 25 25
blurImage = gaussBlur(image,5,51,51,'symm')
#如果输入的图像是8位图,输出的
blurImage = np.round(blurImage)
blurImage = blurImage.astype(np.uint8)
cv2.imshow("gaussBlur",blurImage)
#如果输入的图像数据类型是浮点型，且像素值归一到[0,1]
image_0_1 = image/255.0
blurImage_0_1 = gaussBlur(image_0_1,4,5,5,'symm')
#cv2.imshow("gaussBlur-0-1",blurImage_0_1)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖像平滑 fastMeanBlur")

#图像积分
def integral(image):
    rows,cols = image.shape
    #行积分运算
    inteImageC = np.zeros((rows,cols),np.float32)
    for r in range(rows):
        for c in range(cols):
            if c == 0:
                inteImageC[r][c] = image[r][c]
            else:
                inteImageC[r][c] = inteImageC[r][c-1] + image[r][c]
    #列积分运算
    inteImage = np.zeros(image.shape,np.float32)
    for c in range(cols):
        for r in range(rows):
            if r == 0:
                inteImage[r][c] = inteImageC[r][c]
            else:
                inteImage[r][c] = inteImage[r-1][c] + inteImageC[r][c]
    #为了在快速均值平滑使用中省去判断边界的问题
    #上边和左边进行补零
    inteImage_0 = np.zeros((rows+1,cols+1),np.float32)
    inteImage_0[1:rows+1,1:cols+1] = inteImage
    return inteImage_0

#快速均值平滑：返回数组的数据类型是浮点型，winSize = ( 高，宽 )
def fastMeanBlur(image,winSize,borderType = cv2.BORDER_DEFAULT):
    halfH = (winSize[0]-1)/2
    halfW = (winSize[1]-1)/2
    ratio = 1.0/(winSize[0]*winSize[1])
    #边缘扩充
    paddImage = cv2.copyMakeBorder(image,halfH,halfH,halfW,halfW,borderType)
    #图像积分
    paddIntegral = integral(paddImage)
    #图像的宽高
    rows,cols = image.shape
    #均值滤波后的结果
    meanBlurImage = np.zeros(image.shape,np.float32)
    r,c = 0,0
    for h in range(halfH,halfH+rows,1):
        for w in range(halfW,halfW+cols,1):
            meanBlurImage[r][c] = (paddIntegral[h+halfH+1][w+halfW+1] + paddIntegral[h-halfH][w-halfW]
                                    -paddIntegral[h+halfH+1][w-halfW]-paddIntegral[h-halfH][w+halfW+1])*ratio
            c+=1
        r+=1
        c=0
    return meanBlurImage

""" fail
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

#快速均值平滑
meanBlurImage = fastMeanBlur(image,(15,15),cv2.BORDER_DEFAULT)

#数据类型转换
meanBlurImage = np.round(meanBlurImage)
meanBlurImage = meanBlurImage.astype(np.uint8)

cv2.imshow("fastMeanBlur",meanBlurImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("圖像平滑 meanBlur")

from scipy import signal

#均值平滑
def meanBlur(image,H,W,_boundary='fill',_fillvalue=0):
    #H、W均不为零
    if H==0 or W==0:
        print('W or H is not zero')
        return image
    
    #-------没有对均值平滑算子进行分离
    #meanKernel = 1.0/(H*W)*np.ones([H,W],np.float32)
    #result = signal.convolve2d(image,meanKernel,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    #-----卷积后进行数据类型转换,得到均值平滑的结果
    #result = result.astype(np.uint8)
    #return result
    
    #因为均值算子是可分离的卷积核，根据卷积运算的结合律
    #可以先进行水平方向的卷积，
    #再进行垂直方向的卷积
    #首先水平方向的均值平滑
    meanKernel_x = 1.0/W*np.ones([1,W],np.float32)
    i_conv_mk_x = signal.convolve2d(image,meanKernel_x,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    #然后对得到的水平卷积的结果再进行垂直方向的卷积
    meanKernel_y = 1.0/H*np.ones([H,1],np.float32)
    i_conv_xy = signal.convolve2d(i_conv_mk_x,meanKernel_y,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    i_conv_xy = np.round(i_conv_xy)
    #卷积后的结果进行数据类型转换，得到均值平滑的结果
    result = i_conv_xy.astype(np.uint8)
    return result

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#均值滤波卷积核的宽高均设为 2*halfWinSize+1
halfWinSize = 1
MAX_HALFWINSIZE = 20
cv2.namedWindow("meanBlur",1)

#回调函数，均值滤波
def callback_meanBlur(_halfWinSize):
    result = meanBlur(image,2*_halfWinSize+1,2*_halfWinSize+1,_boundary='symm',_fillvalue=0)
    cv2.imshow("meanBlur",result)

callback_meanBlur(halfWinSize)
cv2.createTrackbar("winSize/2","meanBlur",halfWinSize,MAX_HALFWINSIZE,callback_meanBlur)

latexImage = meanBlur(image,29,29,'symm')

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖像平滑 medianBlur")

#中值滤波 
def medianBlur(image,winSize):
    #图像的宽高
    rows,cols = image.shape
    #窗口的宽高，均为奇数
    winH,winW = winSize
    halfWinH = (winH-1)/2
    halfWinW = (winW-1)/2
    #中值滤波后的输出图像
    medianBlurImage = np.zeros(image.shape,image.dtype)
    for r in range(rows):
        for c in range(cols):
            #判断边界
            rTop = 0 if r-halfWinH < 0 else r-halfWinH
            rBottom = rows-1 if r+halfWinH > rows-1 else r+halfWinH
            cLeft = 0 if c-halfWinW < 0 else c-halfWinW
            cRight = cols-1 if c+halfWinW > cols-1 else c+halfWinW
            #取中值的区域
            region = image[rTop:rBottom+1,cLeft:cRight+1]
            #求中值
            medianBlurImage[r][c] = np.median(region)
    return medianBlurImage

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#中值滤波
medianBlurImage = medianBlur(image,(3,3))
#显示中值滤波后的结果
cv2.imshow("medianBlurImage",medianBlurImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("圖像平滑 salt")

#模拟椒盐噪声，number 指添加椒盐噪声的数量
def salt(image,number):
    #图像的宽高
    rows,cols = image.shape
    #加入椒盐噪声后的图像
    saltImage = np.copy(image)
    for i in range(number):
        randR = random.randint(0,rows-1)
        randC = random.randint(0,cols-1)
        saltImage[randR][randC] = 0
    return saltImage

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#添加椒盐噪声
saltImage = salt(image,2000)
cv2.imshow("saltImage",saltImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖像平滑 BFilter")

#基于空间距离的权重因子 ( 和计算高斯算子的过程是一样的 )
def getClosenessWeight(sigma_g,H,W):
    #第一步：构建高斯矩阵gaussMatrix
    gaussMatrix = np.zeros([H,W],np.float32)
    #得到中心点的位置
    cH = (H-1)/2
    cW = (W-1)/2
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r-cH,2.0) + math.pow(c-cW,2.0)
            gaussMatrix[r][c] = math.exp(-norm2/(2*math.pow(sigma_g,2.0)))
    #第二步：计算高斯矩阵的和
    sumGM = np.sum(gaussMatrix)
    #第三步：归一化，gaussMatrix/sumGM
    gaussMatrix = gaussMatrix/sumGM
    return gaussMatrix

# BilateralFiltering 双边滤波，返回的数据类型为浮点型
def bfltGray(image,winH,winW,sigma_g,sigma_d):
    #构建空间距离的权重因子
    closenessWeight = getClosenessWeight(sigma_g,winH,winW)
    #得到卷积核的中心点坐标
    halfWinH = (winH -1)/2
    halfWinW = (winW -1)/2
    #图像矩阵的行数和列数
    rows,cols = image.shape
    #双边滤波后的结果
    bfltGrayImage = np.zeros(image.shape,np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            #判断边界
            rTop = 0 if r-halfWinH < 0 else r-halfWinH
            rBottom = rows-1 if r+halfWinH > rows-1 else r+halfWinH
            cLeft = 0 if c-halfWinW < 0 else c-halfWinW
            cRight = cols-1 if c+halfWinW > cols-1 else c+halfWinW
            #核作用的区域
            region = image[rTop:rBottom+1,cLeft:cRight+1]
            #构建灰度值相似性的权重因子
            similarityWeightTemp = np.exp(-0.5*pow(region -pixel,2.0)/pow(sigma_d,2.0))#错误
            closenessWeightTemp = closenessWeight[rTop-r+halfWinH:rBottom-r+halfWinH+1,cLeft-c+halfWinW:cRight-c+halfWinW+1]
            #两个核相乘
            weightTemp = similarityWeightTemp*closenessWeightTemp
            weightTemp = weightTemp/np.sum(weightTemp)
            bfltGrayImage[r][c] = np.sum(region*weightTemp)
    return bfltGrayImage

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#双边滤波
image = image.astype(np.float32)
bfltImage = bfltGray(image,21,21,30,30)
bfltImage = bfltImage/255.0
#显示双边滤波的结果
bfltImage = bfltImage.astype(np.float32)
cv2.imshow("BilateralFiltering",bfltImage)
#因为双边滤波返回的是数据类型是浮点型的,可以转换为 8 位图
# bfltImage = bfltImage*255.0
#bfltImage = np.round(bfltImage)
#bfltImage = bfltImage.astype(np.uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("圖像平滑 BilateralFiltering")


#基于空间距离的权重模板 ( 和计算高斯算子的过程是一样的 )
def getClosenessWeight(sigma_g,H,W):
    r,c = np.mgrid[0:H:1, 0:W:1]
    r -= (H-1)/2
    c -= (W-1)/2
    closeWeight = np.exp(-0.5*(np.power(r,2)+np.power(c,2))/math.pow(sigma_g,2))
    return closeWeight

# BilateralFiltering 双边滤波，返回的数据类型为浮点型
def bfltGray(I,H,W,sigma_g,sigma_d):
    #构建空间距离的权重模板
    closenessWeight = getClosenessWeight(sigma_g,H,W)
    #模板的中心点位置
    cH = (H -1)/2
    cW = (W -1)/2
    #图像矩阵的行数和列数
    rows,cols = I.shape
    #双边滤波后的结果
    bfltGrayImage = np.zeros(I.shape,np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = I[r][c]
            #判断边界
            rTop = 0 if r-cH < 0 else r-cH
            rBottom = rows-1 if r+cH > rows-1 else r+cH
            cLeft = 0 if c-cW < 0 else c-cW
            cRight = cols-1 if c+cW > cols-1 else c+cW
            #权重模板作用的区域
            region = I[rTop:rBottom+1,cLeft:cRight+1]
            #构建灰度值相似性的权重因子
            similarityWeightTemp = np.exp(-0.5*np.power(region -pixel,2.0)/math.pow(sigma_d,2))        
            closenessWeightTemp = closenessWeight[rTop-r+cH:rBottom-r+cH+1,cLeft-c+cW:cRight-c+cW+1]
            #两个权重模板相乘
            weightTemp = similarityWeightTemp*closenessWeightTemp
            weightTemp = weightTemp/np.sum(weightTemp)
            bfltGrayImage[r][c] = np.sum(region*weightTemp)
    return bfltGrayImage

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#将灰度值归一化
image = image/255.0
#双边滤波
bfltImage = bfltGray(image,33,33,10,0.8)
#显示双边滤波的结果
cv2.imshow("BilateralFiltering",bfltImage)
bfltImage = bfltImage*255.0
bfltImage = np.round(bfltImage)
bfltImage = bfltImage.astype(np.uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("圖像平滑 blfFilterColor")

#基于空间距离的权重因子 ( 和计算高斯核的过程类似 )
def getClosenessWeight(sigma_d,H,W):
    #构建距离权重因子
    closenessWeight = np.zeros([H,W],np.float32)
    #得到中心点的位置
    cH = (H-1)/2
    cW = (W-1)/2
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r-cH,2.0) + math.pow(c-cW,2.0)
            closenessWeight[r][c] = math.exp(-norm2/(2*math.pow(sigma_d,2.0)))
    return closenessWeight

# BilateralFiltering 双边滤波，返回的数据类型为浮点型
def blFilter(image,winH,winW,sigma_d,sigma_s):
    #构建空间距离的权重因子
    closenessWeight = getClosenessWeight(sigma_d,winH,winW)
    #得到卷积核的中心点坐标
    halfWinH = (winH -1)/2
    halfWinW = (winW -1)/2
    #图像矩阵的行数和列数
    rows,cols = image.shape
    #双边滤波后的结果
    blfImage = np.zeros(image.shape,np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            #判断边界
            rTop = 0 if r-halfWinH < 0 else r-halfWinH
            rBottom = rows-1 if r+halfWinH > rows-1 else r+halfWinH
            cLeft = 0 if c-halfWinW < 0 else c-halfWinW
            cRight = cols-1 if c+halfWinW > cols-1 else c+halfWinW
            #核作用的区域
            region = image[rTop:rBottom+1,cLeft:cRight+1]
            #构建灰度值相似性的权重因子
            similarityWeightTemp = np.exp(-0.5*np.power(region -pixel,2.0)/np.power(sigma_s,2.0))
            closenessWeightTemp = closenessWeight[rTop-r+halfWinH:rBottom-r+halfWinH+1,cLeft-c+halfWinW:cRight-c+halfWinW+1]
            #两个权重因子对应位置相乘
            weightTemp = similarityWeightTemp*closenessWeightTemp
            #归一化
            weightTemp = weightTemp/np.sum(weightTemp)
            blfImage[r][c] = np.sum(region*weightTemp)
    return blfImage

#彩色双边滤波 返回的是浮点型
def blFilterColor(colorImage,winH,winW,sigma_d,sigma_s):
    #分别对三个颜色通道进行双边滤波
    blfColorImage = np.zeros(colorImage.shape,np.float32)
    for c in range(3):
        blfColorImage[:,:,c] =  blFilter(colorImage[:,:,c],winH,winW,sigma_d,sigma_s)
    return blfColorImage

""" fail
image = cv2.imread(filename, cv2.IMREAD_COLOR)
#显示原图
cv2.imshow("image",image)
#彩色双边滤波
image = image.astype(np.float32)#注意首先转换为浮点型
blfColorImage = blFilterColor(image,27,27,100,30)
#显示结果
blfColorImage = np.round(blfColorImage)
blfColorImage = blfColorImage.astype(np.uint8)
cv2.imshow("blfFilterColor",blfColorImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""

print("------------------------------------------------------------")  # 60個

print("圖像平滑 JointBilterFilter")

#基于空间距离的权重模板 ( 和计算高斯算子的过程是一样的 )
def getClosenessWeight(sigma_g,H,W):
    r,c = np.mgrid[0:H:1, 0:W:1]
    r -= (H-1)/2
    c -= (W-1)/2
    closeWeight = np.exp(-0.5*(np.power(r,2.0)+np.power(c,2.0))/math.pow(sigma_g,2.0))
    return closeWeight
def jointBLF(I,H,W,sigma_g,sigma_d,borderType=cv2.BORDER_DEFAULT):
    #构建空间距离的权重模板
    closenessWeight = getClosenessWeight(sigma_g,H,W)
    #对 I 进行高斯平滑
    Ig = cv2.GaussianBlur(I, (W,H), sigma_g)    #執行高斯模糊化
    #模板的中心点位置
    cH = (H -1)/2
    cW = (W -1)/2
    #对原图和高斯平滑的结果扩充边界
    Ip=cv2.copyMakeBorder(I,cH,cH,cW,cW,borderType)
    Igp=cv2.copyMakeBorder(Ig,cH,cH,cW,cW,borderType)
    #图像矩阵的行数和列数
    rows,cols = I.shape
    i,j=0,0
    #联合双边滤波结果
    jblf = np.zeros(I.shape,np.float64)        
    for r in np.arange(cH,cH+rows,1):
        for c in np.arange(cW,cW+cols,1):
            #当前位置的值
            pixel = Igp[r][c]
            #当前位置的邻域
            rTop,rBottom = r-cH,r+cH
            cLeft,cRight = c-cW,c+cW
            #从 Igp 中截取该邻域，用于构建相似性权重
            region= Igp[rTop:rBottom+1,cLeft:cRight+1]
            #通过上述邻域,构建该位置的相似性权重模板
            similarityWeight = np.exp(-0.5*np.power(region -pixel,2.0)/math.pow(sigma_d,2.0))
            #相似性权重模板和空间距离权重模板形成
            weight = closenessWeight*similarityWeight
            #将权重模板归一化
            weight = weight/np.sum(weight)
            #权重模板和邻域对应位置相乘并求和
            jblf[i][j] = np.sum(Ip[rTop:rBottom+1,cLeft:cRight+1]*weight)
            j += 1
        j = 0
        i += 1
    return jblf

""" fail
I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#将 8 位图转换为 浮点型
fI = I.astype(np.float64)
#联合双边滤波，返回值的数据类型为浮点型
jblf = jointBLF(fI,33,33,7,2)
#转换为 8 位图
jblf = np.round(jblf)
jblf = jblf.astype(np.uint8)
cv2.imshow("jblf",jblf)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("圖像平滑 fastGuidedFilter")

#快速导向滤波，输入的图像数据类型为归一到[0,1]的浮点型
#s属于(0,1] ,
#建议 r>=4, 1/r=<s<=4/r 
def fastGuidedFilter(I,p,r,eps,s):
    #输入图像的宽高
    rows,cols = I.shape
    #缩小图像
    small_I = cv2.resize(I,dsize=(int(round(s*cols)),int(round(s*rows))),interpolation=cv2.INTER_CUBIC)
    small_p = cv2.resize(p,dsize=(int(round(s*cols)),int(round(s*rows))),interpolation=cv2.INTER_CUBIC)
    #缩放均值平滑的窗口半径
    small_r = int(round(r*s))#确保是整型
    winSize = (2*small_r+1,2*small_r+1)
    # small_I 的均值平滑
    mean_small_I = fastMeanBlur(small_I,winSize,cv2.BORDER_DEFAULT)
    # small_p 的均值平滑
    mean_small_p = fastMeanBlur(small_p,winSize,cv2.BORDER_DEFAULT)
    # small_I.*small_p 的均值平滑
    small_Ip = small_I*small_p
    mean_small_Ip = fastMeanBlur(small_Ip,winSize,cv2.BORDER_DEFAULT)
    #协方差
    cov_small_Ip = mean_small_Ip - mean_small_I*mean_small_p
    mean_small_II = fastMeanBlur(small_I*small_I,winSize,cv2.BORDER_DEFAULT)
    #方差
    var_small_I = mean_small_II - mean_small_I*mean_small_I
    small_a = cov_small_Ip/(var_small_I+eps)
    small_b = mean_small_p - small_a*mean_small_I
    #对 small_a 和 small_b 进行均值平滑
    mean_small_a = fastMeanBlur(small_a,winSize,cv2.BORDER_DEFAULT)
    mean_small_b = fastMeanBlur(small_b,winSize,cv2.BORDER_DEFAULT)
    #放大 small_a 和 small_b
    mean_a = cv2.resize(mean_small_a,dsize=(cols,rows),interpolation=cv2.INTER_LINEAR)
    mean_b = cv2.resize(mean_small_b,dsize=(cols,rows),interpolation=cv2.INTER_LINEAR)
    q = mean_a*I + mean_b
    return q

#彩色快速导向滤波（平滑）
def fGFColorSmooth(I,r,eps,s):
    q_color = np.zeros(I.shape,np.float64)
    #对每一个通道进行导向滤波
    for c in range(3):
        q_color[:,:,c] = fastGuidedFilter(I[:,:,c],I[:,:,c],r,eps,s)
    return q_color

#细节增强
def fGFEnchance(I,r,eps,s):
    #导向平滑处理
    qColor = fGFColorSmooth(I,r,eps,s)
    #细节增强处理
    enchanced = (I - qColor)*5 + qColor
    """
    for c in range(3):
        enchanced[:,:,c] = cv2.normalize(enchanced[:,:,c],alpha = 1,beta = 0,norm_type = cv2.NORM_MINMAX)
    """
    enchanced = cv2.normalize(enchanced,alpha = 1,beta = 0,norm_type = cv2.NORM_MINMAX)
    return enchanced

""" fail
image = cv2.imread(filename, cv2.IMREAD_COLOR)
#显示原图
cv2.imshow("image",image)
#快速导向滤波（彩色图像平滑）
image_0_1 = image/255.0
result = fGFColorSmooth(image_0_1,5,pow(0.1,2.0),1.0/3)
cv2.imshow("fastGuidedFilter",result)
#细节增强
enchanced = fGFEnchance(image_0_1,5,pow(0.2,2.0),1.0/3)
cv2.imshow("fGFEnchance",enchanced)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("圖像平滑 fastMeanBlur")

#图像积分
def integral(image):
    rows,cols = image.shape
    #行积分运算
    inteImageC = np.zeros((rows,cols),np.float32)
    for r in range(rows):
        for c in range(cols):
            if c == 0:
                inteImageC[r][c] = image[r][c]
            else:
                inteImageC[r][c] = inteImageC[r][c-1] + image[r][c]
    #列积分运算
    inteImage = np.zeros(image.shape,np.float32)
    for c in range(cols):
        for r in range(rows):
            if r == 0:
                inteImage[r][c] = inteImageC[r][c]
            else:
                inteImage[r][c] = inteImage[r-1][c] + inteImageC[r][c]
    #为了在快速均值平滑使用中省去判断边界的问题
    #上边和左边进行补零
    inteImage_0 = np.zeros((rows+1,cols+1),np.float32)
    inteImage_0[1:rows+1,1:cols+1] = inteImage
    return inteImage_0

#快速均值平滑：返回数组的数据类型是浮点型，winSize = ( 高，宽 )
def fastMeanBlur(image,winSize,borderType = cv2.BORDER_DEFAULT):
    halfH = (winSize[0]-1)/2
    halfW = (winSize[1]-1)/2
    ratio = 1.0/(winSize[0]*winSize[1])
    #边缘扩充
    paddImage = cv2.copyMakeBorder(image,halfH,halfH,halfW,halfW,borderType)
    #图像积分
    paddIntegral = integral(paddImage)
    #图像的宽高
    rows,cols = image.shape
    #均值滤波后的结果
    meanBlurImage = np.zeros(image.shape,np.float32)
    r,c = 0,0
    for h in range(halfH,halfH+rows,1):
        for w in range(halfW,halfW+cols,1):
            meanBlurImage[r][c] = (paddIntegral[h+halfH+1][w+halfW+1] + paddIntegral[h-halfH][w-halfW]
                                    -paddIntegral[h+halfH+1][w-halfW]-paddIntegral[h-halfH][w+halfW+1])*ratio
            c+=1
        r+=1
        c=0
    return meanBlurImage

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#快速均值平滑
meanBlurImage = fastMeanBlur(image,(15,15),cv2.BORDER_DEFAULT)
#数据类型转换
meanBlurImage = np.round(meanBlurImage)
meanBlurImage = meanBlurImage.astype(np.uint8)
cv2.imshow("fastMeanBlur",meanBlurImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("圖像平滑 guidedFilter")

#导向滤波
def guidedFilter(I,p,winSize,eps):
    #输入图像的宽高
    rows,cols = I.shape
    # I 的均值平滑
    mean_I = fastMeanBlur(I,winSize,cv2.BORDER_DEFAULT)
    # p 的均值平滑
    mean_p = fastMeanBlur(p,winSize,cv2.BORDER_DEFAULT)
    # I.*p 的均值平滑
    Ip = I*p
    mean_Ip = fastMeanBlur(Ip,winSize,cv2.BORDER_DEFAULT)
    #协方差
    cov_Ip = mean_Ip - mean_I*mean_p
    mean_II = fastMeanBlur(I*I,winSize,cv2.BORDER_DEFAULT)
    #方差
    var_I = mean_II - mean_I*mean_I
    a = cov_Ip/(var_I+eps)
    b = mean_p - a*mean_I
    # 对 a 和 b进行均值平滑
    mean_a = fastMeanBlur(a,winSize,cv2.BORDER_DEFAULT)
    mean_b = fastMeanBlur(b,winSize,cv2.BORDER_DEFAULT)
    q = mean_a*I + mean_b
    return q

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#将图像归一化
image_0_1 = image/255.0
#显示原图
cv2.imshow("image",image)
#导向滤波
result = guidedFilter(image_0_1,image_0_1,(17,17),pow(0.2,2.0))
cv2.imshow("guidedFilter",result)
#保存导向滤波的结果
result = result*255
result[result>255] = 255
result = np.round(result)
result = result.astype(np.uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
print("------------------------------------------------------------")  # 60個

print("圖像平滑 guidedFilter_color cccc")

#导向滤波
def guidedFilter(I,p,winSize,eps):
    #输入图像的宽高
    rows,cols = I.shape
    # I 的均值平滑
    mean_I = fastMeanBlur(I,winSize,cv2.BORDER_DEFAULT)
    # p 的均值平滑
    mean_p = fastMeanBlur(p,winSize,cv2.BORDER_DEFAULT)
    # I.*p 的均值平滑
    Ip = I*p
    mean_Ip = fastMeanBlur(Ip,winSize,cv2.BORDER_DEFAULT)
    #协方差
    cov_Ip = mean_Ip - mean_I*mean_p
    mean_II = fastMeanBlur(I*I,winSize,cv2.BORDER_DEFAULT)
    #方差
    var_I = mean_II - mean_I*mean_I
    a = cov_Ip/(var_I+eps)
    b = mean_p - a*mean_I
    # 对 a 和 b进行均值平滑
    mean_a = fastMeanBlur(a,winSize,cv2.BORDER_DEFAULT)
    mean_b = fastMeanBlur(b,winSize,cv2.BORDER_DEFAULT)
    q = mean_a*I + mean_b
    return q

""" fail
filename1 = 'C:/_git/vcs/_4.python/_data/pic_brightness1.bmp'
filename2 = 'C:/_git/vcs/_4.python/_data/pic_brightness2.bmp'

I = cv2.imread(filename1, cv2.IMREAD_COLOR)
p = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
#将图像归一化
image_0_1 = I/255.0
p = p/255.0
#显示原图
cv2.imshow("image_0_1",image_0_1)
#导向滤波
result = np.zeros(I.shape)
result[:,:,0] = guidedFilter(image_0_1[:,:,0],image_0_1[:,:,0],(17,17),pow(0.2,2.0))
result[:,:,1] = guidedFilter(image_0_1[:,:,1],image_0_1[:,:,1],(17,17),pow(0.2,2.0))
result[:,:,2] = guidedFilter(image_0_1[:,:,2],image_0_1[:,:,2],(17,17),pow(0.2,2.0))
cv2.imshow("guidedFilter",result)
#保存导向滤波的结果
result = result*255
result[result>255] = 255
result = np.round(result)
result = result.astype(np.uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("閾值分割 threshold_OpenCV3")

src = np.array([[123,234,68],[33,51,17],[48,98,234], [129,89,27],[45,167,134]],np.uint8)
#手动设置阈值
the = 150
maxval = 255
dst = cv2.threshold(src,the,maxval,cv2.THRESH_BINARY)
# Otsu 阈值处理 
otsuThe = 0
otsuThe,dst_Otsu = cv2.threshold(src,otsuThe,maxval,cv2.THRESH_OTSU)
print(otsuThe,dst_Otsu)
# TRIANGLE 阈值处理
triThe = 0
triThe,dst_tri = cv2.threshold(src,triThe,maxval,cv2.THRESH_TRIANGLE)
print(triThe,dst_tri)

print("------------------------------------------------------------")  # 60個

print("閾值分割 threshTwoPeaks")

#计算图像灰度直方图
def calcGrayHist(image):
    #灰度图像矩阵的宽高
    rows,cols = image.shape
    #存储灰度直方图
    grayHist = np.zeros([256],np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] +=1
    return grayHist

#返回阈值和二值图
def threshTwoPeaks(image):
    #计算回复直方图
    histogram = calcGrayHist(image)
    #找到灰度直方图的最大峰值对应的灰度值
    maxLoc = np.where(histogram==np.max(histogram))
    firstPeak = maxLoc[0]
    print(maxLoc[0])
    #寻找灰度直方图的 " 第二个峰值 " 对应的灰度值
    measureDists = np.zeros([256],np.float32)
    for k in range(256):
        measureDists[k] = pow(k-firstPeak,2)*histogram[k]
    maxLoc2 = np.where(measureDists==np.max(measureDists))
    secondPeak = maxLoc2[0]
    #找到两个峰值之间的最小值对应的灰度值，作为阈值
    thresh = 0
    if firstPeak > secondPeak:
        temp = histogram[int(secondPeak):int(firstPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = secondPeak + minLoc[0]+1
    else:
        temp = histogram[int(firstPeak):int(secondPeak)]
        minLoc = np.where( temp == np.min(temp))
        thresh = firstPeak + minLoc[0]+1
    #找到阈值后进行阈值处理，得到二值图
    threshImage_out = image.copy()
    threshImage_out[threshImage_out > thresh] = 255
    threshImage_out[threshImage_out <= thresh] = 0
    return (thresh,threshImage_out)

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
thresh,threshImage_out = threshTwoPeaks(image)
#输出直方图技术得到的阈值
print(thresh)
#显示原图和阈值化得到的二值图
cv2.imshow("image",image)
cv2.imshow("threshTwoPeaks",threshImage_out)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("閾值分割 threshEntroy")

#计算图像灰度直方图
def calcGrayHist(image):
    #灰度图像矩阵的宽高
    rows,cols = image.shape
    #存储灰度直方图
    grayHist = np.zeros([256],np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] +=1
    return grayHist
#熵阈值法
def threshEntroy(image):
    rows,cols = image.shape
    #求灰度直方图
    grayHist = calcGrayHist(image)
    #归一化灰度直方图
    normGrayHist = grayHist/float(rows*cols)
    #计算累加直方图，也称零阶累加矩
    zeroCumuMoment = np.zeros([256],np.float32)
    for k in range(256):
        if k==0:
            zeroCumuMoment[k] = normGrayHist[k]
        else:
            zeroCumuMoment[k] = zeroCumuMoment[k-1] + normGrayHist[k]
    #计算各个灰度级的熵
    entropy = np.zeros([256],np.float32)
    for k in range(256):
        if k==0:
            if normGrayHist[k] ==0:
                entropy[k] = 0
            else:
                entropy[k] = - normGrayHist[k]*math.log10(normGrayHist[k])
        else:
            if normGrayHist[k] ==0:
                entropy[k] = entropy[k-1]
            else:
               entropy[k] = entropy[k-1] - normGrayHist[k]*math.log10(normGrayHist[k])
    #找阈值
    fT = np.zeros([256],np.float32)
    ft1,ft2 = 0.0,0.0
    totalEntroy = entropy[255]
    for k in range(255):
        #找最大值
        maxFront = np.max(normGrayHist[0:k+1])
        maxBack = np.max(normGrayHist[k+1:256])
        if(maxFront == 0 or zeroCumuMoment[k] == 0 or maxFront==1 or zeroCumuMoment[k]==1 or totalEntroy==0):
            ft1 = 0
        else:
            ft1 =entropy[k]/totalEntroy*(math.log10(zeroCumuMoment[k])/math.log10(maxFront))
        if(maxBack == 0 or 1 - zeroCumuMoment[k]==0 or maxBack == 1 or 1-zeroCumuMoment[k] ==1):
            ft2 = 0
        else:
            if totalEntroy==0:
                ft2 = (math.log10(1-zeroCumuMoment[k])/math.log10(maxBack))
            else:
                ft2 = (1-entropy[k]/totalEntroy)*(math.log10(1-zeroCumuMoment[k])/math.log10(maxBack))
        fT[k] = ft1+ft2
    #找最大值的索引，作为得到的阈值
    threshLoc = np.where(fT==np.max(fT))
    thresh = threshLoc[0][0]
    #阈值处理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return (threshold,thresh)

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#阈值处理
threshold,thresh = threshEntroy(image);
#显示阈值后的二值化图像
cv2.imshow("threshEntroy",threshold)
print(thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("閾值分割 otsu")

#计算图像灰度直方图
def calcGrayHist(image):
    #灰度图像矩阵的宽高
    rows,cols = image.shape
    #存储灰度直方图
    grayHist = np.zeros([1,256],np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[0][image[r][c]] +=1
    return grayHist         

def ostu(image):
    rows,cols = image.shape
    #计算图像的灰度直方图
    grayHist = calcGrayHist(image)
    #归一化灰度直方图
    uniformGrayHist = grayHist/float(rows*cols)
    #计算零阶累积矩和一阶累积矩
    zeroCumuMoment = np.zeros([1,256],np.float32)
    oneCumuMoment = np.zeros([1,256],np.float32)
    for k in range(256):
        if k == 0:
            zeroCumuMoment[0][k] = uniformGrayHist[0][0]
            oneCumuMoment[0][k] = (k+1)*uniformGrayHist[0][0]
        else:
            zeroCumuMoment[0][k] = zeroCumuMoment[0][k-1] + uniformGrayHist[0][k]
            oneCumuMoment[0][k] = oneCumuMoment[0][k-1] + k*uniformGrayHist[0][k]
    #计算类间方差  
    variance = np.zeros([1,256],np.float32)
    for k in range(255):
        if zeroCumuMoment[0][k] == 0:
            variance[0][k] = 0
        else:
            variance[0][k] = math.pow(oneCumuMoment[0][255]*zeroCumuMoment[0][k] - oneCumuMoment[0][k],2)/(zeroCumuMoment[0][k]*(1.0-zeroCumuMoment[0][k]))
    #找到阈值
    threshLoc = np.where(variance[0][0:255] == np.max(variance[0][0:255]))
    thresh = threshLoc[0]
    #阈值处理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return threshold

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

#显示原图
cv2.imshow("image",image)

#阈值算法
ostu_threshold = ostu(image)

#显示阈值处理的结果
cv2.imshow("ostu_threshold", ostu_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("閾值分割 adaptive")

#图像积分
def integral(image):
    rows,cols = image.shape
    #行积分运算
    inteImageC = np.zeros(image.shape,np.float32)
    for r in range(rows):
        for c in range(cols):
            if c == 0:
                inteImageC[r][c] = image[r][c]
            else:
                inteImageC[r][c] = inteImageC[r][c-1] + image[r][c]
    #列积分运算
    inteImage = np.zeros(image.shape,np.float32)
    for c in range(cols):
        for r in range(rows):
            if r == 0:
                inteImage[r][c] = inteImageC[r][c]
            else:
                inteImage[r][c] = inteImage[r-1][c] + inteImageC[r][c]
    return inteImage

#阈值处理
def threshAdaptive(image,winSize,ratio):
    #图像的宽高
    rows,cols = image.shape
    #窗口的宽高
    winH,winW = winSize
    h = (winH-1)/2
    w = (winW-1)/2
    #阈值处理后的二值化图像
    threshImage = np.zeros(image.shape,np.uint8)
    #图像的积分
    inteImage = integral(image)
    for r in range(rows):
        for c in range(cols):
            # top left 
            tl_r = (r-h) if r-h > 0 else 0
            tl_c = (c-w) if c-w > 0 else 0
            #bottom right
            br_r = (r+h) if (r+h) < rows else rows -1
            br_c = (c+w) if (c+w) < cols else cols -1
            #计算区域和
            regionSum = inteImage[br_r][br_c] + inteImage[tl_r][tl_c] - inteImage[tl_r][br_c] - inteImage[br_r][tl_c]
            count = (br_r - tl_r + 1)*(br_c - tl_c + 1)
            if(image[r][c]*count < (1 - ratio)*regionSum):
                threshImage[r][c] = 0
            else:
                threshImage[r][c] = 255
    return threshImage

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
threshImage = threshAdaptive(image,(41,41),0.15)
#显示自适应阈值后二值化图像
cv2.imshow("threshImage",threshImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("閾值分割 adaptiveThresh")

def adaptiveThresh(I,winSize,ratio=0.15):
    #第一步：对图像矩阵进行均值平滑
    I_smooth = cv2.boxFilter(I,cv2.CV_32FC1,winSize)
    #I_smooth = cv2.medianBlur(I,winSize)
    #第二步：原图像矩阵与平滑结果做差
    out = I - (1.0-ratio)*I_smooth
    #第三步：对 out 进行全局阈值处理，差值大于等于零，输出值为255，反之为零
    out[out>=0] = 255
    out[out<0] = 0
    out = out.astype(np.uint8)
    return out


image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
out = adaptiveThresh(image,(31,31),0.15)
cv2.imshow("out",out)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("閾值分割 bitwise_and")

src1 = np.array([[255,0,255]])
src2 = np.array([[255,0,0]])
#与运算
dst_and = cv2.bitwise_and(src1,src2)
#或运算
dst_or = cv2.bitwise_or(src1,src2)
print("与运算的结果：")
print(dst_and)
print("或运算的结果：")
print(dst_or)

print("------------------------------------------------------------")  # 60個

print("形態學處理 erode")

I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#创建结构元
s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#腐蚀图像
r = cv2.erode(I,s)
#显示原图和腐蚀后的结果
cv2.imshow("I",I)
cv2.imshow("erode",r)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("形態學處理 dilate")

""" fail
if __name__ =="__main__":
    #第一步：读入图像
    I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #显示原图
    cv2.imshow("I",I)
    #结构元半径,迭代次数
    r,i = 1,1
    MAX_R,MAX_I = 20,20
    #显示膨胀效果的窗口
    cv2.namedWindow("dilate",1)
    def nothing(*arg):
        pass
    #调节结构元半径
    cv2.createTrackbar("r","dilate",r,MAX_R,nothing)
    #调节迭代次数
    cv2.createTrackbar("i","dilate",i,MAX_I,nothing)
    while True:
        #得到当前的r值
        r = cv2.getTrackbarPos('r', 'dilate')
        #得到当前的i值
        i= cv2.getTrackbarPos('i','dilate')
        #创建结构元
        s = cv2.getStructuringElement(cv2.MORPH_GRADIENT,(2*r+1,2*r+1))
        #膨胀图像
        d = cv2.erode(I,s,iterations=i)
        #显示膨胀效果
        cv2.imshow("dilate",d)

        k = cv2.waitKey(5)
        if k == ESC:
            break
    cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("形態學處理 open")

#第一步：读入图像
I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#创建结构元
s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#腐蚀图像
d = cv2.morphologyEx(I,cv2.MORPH_OPEN,s,iterations=1)
#显示原图和腐蚀后的结果
cv2.imshow("I",I)
cv2.imshow("open",d)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# fail

print("形態學處理 mor")
print('按 ESC 離開')

#第一步：读入图像
I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

#显示原图
cv2.imshow("I",I)

#结构元半径，迭代次数
r, i= 1,1
MAX_R,MAX_I = 20,20

#显示形态学处理的效果的窗口
cv2.namedWindow("morphology",1)

def nothing(*arg):
    pass

#调节结构元半径
cv2.createTrackbar("r","morphology",r,MAX_R,nothing)

#调节迭代次数
cv2.createTrackbar("i","morphology",i,MAX_I,nothing)

while True:
    #得到当前的r值
    r = cv2.getTrackbarPos('r', 'morphology')
    #得到当前的i值
    i = cv2.getTrackbarPos('i','morphology')
    #创建结构元
    s = cv2.getStructuringElement(cv2.MORPH_RECT,(2*r+1,2*r+1))
    #形态学处理
    d = cv2.morphologyEx(I,cv2.MORPH_GRADIENT,s,iterations=i)
    #显示效果
    cv2.imshow("morphology",d)

    k = cv2.waitKey(5)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 roberts")

from scipy import signal

def roberts(I,_boundary='fill',_fillvalue=0):
    #图像的高、宽
    H1,W1=I.shape[0:2]
    #卷积核的尺寸
    H2,W2=2,2
    #卷积核 1 及 锚点的位置
    R1 = np.array([[1,0],[0,-1]],np.float32)
    kr1,kc1=0,0
    #计算 fuLl 卷积
    IconR1 = signal.convolve2d(I,R1,mode='full',boundary = _boundary,fillvalue=_fillvalue)
    IconR1=IconR1[H2-kr1-1:H1+H2-kr1-1,W2-kc1-1:W1+W2-kc1-1]
    #卷积核2
    R2 = np.array([[0,1],[-1,0]],np.float32)
    #先计算 full 卷积
    IconR2 = signal.convolve2d(I,R2,mode='full',boundary = _boundary,fillvalue=_fillvalue)
    #锚点的位置
    kr2,kc2 = 0,1
    #根据锚点的位置，截取 full卷积，从而得到 same 卷积
    IconR2=IconR2[H2-kr2-1:H1+H2-kr2-1,W2-kc2-1:W1+W2-kc2-1]
    return (IconR1,IconR2)


image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#卷积，注意边界扩充一般采用 " symm "
IconR1,IconR2 = roberts(image,'symm')
#45度方向上的边缘强度的灰度级显示
IconR1 = np.abs(IconR1)
edge_45 = IconR1.astype(np.uint8)
cv2.imshow("edge_45",edge_45)
#135度方向上的边缘强度
IconR2 = np.abs(IconR2)
edge_135 = IconR2.astype(np.uint8)
cv2.imshow("edge_135",edge_135)
#用平方和的开方衡量最后的输出边缘
edge = np.sqrt(np.power(IconR1,2.0) + np.power(IconR2,2.0))
edge = np.round(edge)
edge[edge>255] = 255
edge = edge.astype(np.uint8)
#显示边缘
cv2.imshow("edge",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Marr_Hildreth")

from scipy import signal

#构建 LoG 算子
def createLoGKernel(sigma,kSize):
    # LoG 算子的宽高，且两者均为奇数
    winH,winW = kSize
    logKernel = np.zeros(kSize,np.float32)
    #方差
    sigmaSquare = pow(sigma,2.0)
    # LoG 算子的中心
    centerH = (winH-1)/2
    centerW = (winW-1)/2
    for r in range(winH):
        for c in range(winW):
            norm2 = pow(r-centerH,2.0) + pow(c-centerW,2.0)
            logKernel[r][c] = 1.0/sigmaSquare*(norm2/sigmaSquare - 2)*math.exp(-norm2/(2*sigmaSquare))
    return logKernel
#零交叉点：方法1
def zero_cross_default(img_conv_log):
    zero_cross = np.zeros(img_conv_log.shape,np.uint8)
    rows,cols = img_conv_log.shape
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            # 左 / 右方向
            if img_conv_log[r][c-1]*img_conv_log[r][c+1] < 0:
                zero_cross[r][c] = 255
                continue
            #上 / 下方向
            if img_conv_log[r-1][c]*img_conv_log[r+1][c] < 0:
                zero_cross[r][c] = 255
                continue
            #左上 / 右下方向
            if img_conv_log[r-1][c-1]*img_conv_log[r+1][c+1] < 0:
                zero_cross[r][c] = 255
                continue
            #右上 / 左下方向
            if img_conv_log[r-1][c+1]*img_conv_log[r+1][c-1] < 0:
                zero_cross[r][c] = 255
                continue
    return zero_cross
#零交叉点：方法2
def zero_cross_mean(img_conv_log):
    zero_cross = np.zeros(img_conv_log.shape,np.uint8)
    #存储左上，右上，左下，右下方向
    fourMean = np.zeros(4,np.float32)
    rows,cols = img_conv_log.shape
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            #左上方的均值
            leftTopMean = np.mean(img_conv_log[r-1:r+1,c-1:c+1])
            fourMean[0] = leftTopMean
            #右上方的均值
            rightTopMean = np.mean(img_conv_log[r-1:r+1,c:c+2])
            fourMean[1] = rightTopMean
            #左下方的均值
            leftBottomMean = np.mean(img_conv_log[r:r+2,c-1:c+1])
            fourMean[2] = leftBottomMean
            #右下方的均值
            rightBottomMean = np.mean(img_conv_log[r:r+2,c:c+2])
            fourMean[3] = rightBottomMean
            if(np.min(fourMean)*np.max(fourMean)<0):
                zero_cross[r][c] = 255
    return zero_cross
# Marr_Hildreth 边缘检测算法
def Marr_Hildreth(image,loGSize,sigma,crossType="ZERO_CROSS_DEFAULT"):
    #第一步：创建 LoG 算子
    loGKernel = createLoGKernel(sigma,loGSize)
    #第二步：图像与 LoG 算子的卷积
    img_conv_log = signal.convolve2d(image,loGKernel,'same','symm')
    #第三步：过零点
    if crossType == "ZERO_CROSS_DEFAULT":
        zero_cross = zero_cross_default(img_conv_log)
    elif  crossType == "ZERO_CROSS_MEAN":
        zero_cross = zero_cross_mean(img_conv_log)
    else:
        print("no crossType")
    return zero_cross


image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
# Marr-Hilreth 边缘检测算法
result = Marr_Hildreth(image,(13,13),2,"ZERO_CROSS_MEAN")
result = 255 - result
cv2.imshow("Marr-Hildreth",result)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Marr_Hildreth")

from scipy import signal

#非归一化的高斯卷积
def gaussConv(I,size,sigma):
    #卷积核的高和宽
    H,W = size
    #构造水平方向上非归一化的高斯卷积核
    xr,xc = np.mgrid[0:1,0:W]
    xc -= (W-1)/2
    xk = np.exp(-np.power(xc,2.0)/(2.0*pow(sigma,2)))
    # I 与 xk 卷积
    I_xk = signal.convolve2d(I,xk,'same','symm')
    #构造垂直方向上的非归一化的高斯卷积核
    yr,yc = np.mgrid[0:H,0:1]
    yr -= (H-1)/2
    yk = np.exp(-np.power(yr,2.0)/(2.0*pow(sigma,2.0)))
    # I_xk 与 yk 卷积
    I_xk_yk = signal.convolve2d(I_xk,yk,'same','symm')
    I_xk_yk *= 1.0/(2*np.pi*pow(sigma,2.0))
    return I_xk_yk

#高斯差分
def DoG(I,size,sigma,k=1.1):
    #标准差为 sigma 的非归一化的高斯卷积
    Is = gaussConv(I,size,sigma)
    #标准差为 k*sigma 的非归一化高斯卷积
    Isk = gaussConv(I,size,k*sigma)
    #两个高斯卷积的差分
    doG = Isk - Is
    doG /= (pow(sigma,2.0)*(k-1))
    return doG

#零交叉点：方法1
def zero_cross_default(doG):
    zero_cross = np.zeros(doG.shape,np.uint8)
    rows,cols = doG.shape
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            # 左 / 右方向
            if doG[r][c-1]*doG[r][c+1] < 0:
                zero_cross[r][c] = 255
                continue
            #上 / 下方向
            if doG[r-1][c]*doG[r+1][c] < 0:
                zero_cross[r][c] = 255
                continue
            #左上 / 右下方向
            if doG[r-1][c-1]*doG[r+1][c+1] < 0:
                zero_cross[r][c] = 255
                continue
            #右上 / 左下方向
            if doG[r-1][c+1]*doG[r+1][c-1] < 0:
                zero_cross[r][c] = 255
                continue
    return zero_cross

#零交叉点：方法2
def zero_cross_mean(doG):
    zero_cross = np.zeros(doG.shape,np.uint8)
    #存储左上，右上，左下，右下方向
    fourMean = np.zeros(4,np.float32)
    rows,cols = doG.shape
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            #左上方的均值
            leftTopMean = np.mean(doG[r-1:r+1,c-1:c+1])
            fourMean[0] = leftTopMean
            #右上方的均值
            rightTopMean = np.mean(doG[r-1:r+1,c:c+2])
            fourMean[1] = rightTopMean
            #左下方的均值
            leftBottomMean = np.mean(doG[r:r+2,c-1:c+1])
            fourMean[2] = leftBottomMean
            #右下方的均值
            rightBottomMean = np.mean(doG[r:r+2,c:c+2])
            fourMean[3] = rightBottomMean
            if(np.min(fourMean)*np.max(fourMean)<0):
                zero_cross[r][c] = 255
    return zero_cross

# Marr_Hildreth 边缘检测算法
def Marr_Hildreth(image,size,sigma,k=1.1,crossType="ZERO_CROSS_DEFAULT"):
    #高斯差分
    doG = DoG(image,size,sigma,k)
    #过零点
    if crossType == "ZERO_CROSS_DEFAULT":
        zero_cross = zero_cross_default(doG)
    elif  crossType == "ZERO_CROSS_MEAN":
        zero_cross = zero_cross_mean(doG)
    else:
        print("no crossType")
    return zero_cross

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
# Marr-Hilreth 边缘检测算法
result = Marr_Hildreth(image,(19,19),2,1.1,"ZERO_CROSS_MEAN")
cv2.imshow("Marr-Hildreth",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("邊緣檢測 prewitt")

from scipy import signal

#prewtt卷积
def prewitt(I,_boundary='symm',):
    #因为prewitt_X是可分离卷积核,根据卷积运算的结合律,可以分两次小卷积核运算
    #1：垂直方向的 " 均值平滑 "
    ones_y = np.array([[1],[1],[1]],np.float32)
    i_conv_pre_x = signal.convolve2d(I,ones_y,mode='same',boundary = _boundary)
    #2：水平方向的差分
    diff_x = np.array([[1,0,-1]],np.float32)
    i_conv_pre_x = signal.convolve2d(i_conv_pre_x,diff_x,mode='same',boundary = _boundary)
    #因为prewitt_y是可分离卷积核，根据卷积运算的结合律，可以分两次小卷积核运算
    #1：水平方向的"均值平滑 "
    ones_x = np.array([[1,1,1]],np.float32)
    i_conv_pre_y = signal.convolve2d(I,ones_x,mode='same',boundary = _boundary)
    #2：垂直方向的差分
    diff_y = np.array([[1],[0],[-1]],np.float32)
    i_conv_pre_y = signal.convolve2d(i_conv_pre_y,diff_y,mode='same',boundary = _boundary)
    return (i_conv_pre_x,i_conv_pre_y)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#图像矩阵 和 两个 prewitt算子 的卷积
i_conv_pre_x,i_conv_pre_y = prewitt(image)
#取绝对值,分别得到水平方向和垂直方向的边缘强度
abs_i_conv_pre_x = np.abs(i_conv_pre_x)
abs_i_conv_pre_y = np.abs(i_conv_pre_y)    
#水平方向和垂直方向的边缘强度的灰度级显示
edge_x = abs_i_conv_pre_x.copy()
edge_y = abs_i_conv_pre_y.copy()
edge_x[edge_x>255]=255
edge_y[edge_y>255]=255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
cv2.imshow("edge_x",edge_x)
cv2.imshow("edge_y",edge_y)

#利用 abs_i_conv_pre_x 和 abs_i_conv_pre_y 求最终的边缘强度
#求边缘强度，有多重方式，这里使用的是插值法
edge = 0.5*abs_i_conv_pre_x + 0.5*abs_i_conv_pre_y
#边缘强度的灰度级显示
edge[edge>255]=255
edge = edge.astype(np.uint8)
cv2.imshow('edge',edge)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 sobel")

from scipy import signal

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

#得到卷积核
sobelKernel3 = getSobelKernel(3)
sobelKernel5 = getSobelKernel(5)
print(sobelKernel3)
print(sobelKernel5)

#卷积
image_sobel_x,image_sobel_y = sobel(image,3)
edge_x = np.abs(image_sobel_x)
edge_x[ edge_x>255]=255
edge_x=edge_x.astype(np.uint8)
edge_y = np.abs(image_sobel_y)
edge_y[ edge_y>255]=255
edge_y=edge_y.astype(np.uint8)

""" fail
#边缘强度：两个卷积结果对应位置的平方和
edge = np.sqrt(np.power(image_sobel_x,2.0) + np.power(image_sobel_y,2.0))
#边缘强度的灰度级显示
edge[edge>255] = 255
edge = np.round(edge)
edge = edge.astype(np.uint8)
cv2.imshow("sobel edge",edge)

#模拟素描
pencilSketch = edge.copy()
pencilSketch = 255 - pencilSketch
pencilSketch[pencilSketch < 80] = 80
cv2.imshow("pencilSketch",pencilSketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Sobel_normalize")

from scipy import signal

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

#卷积
image_sobel_x,image_sobel_y = sobel(image,7)
#平方和开方的方式
edge = np.sqrt(np.power(image_sobel_x,2.0) + np.power(image_sobel_y,2.0))
#边缘强度的灰度级显示
edge =edge/np.max(edge)
edge = np.power(edge,0.8)
edge*=255
edge = edge.astype(np.uint8)
cv2.imshow("sobel edge",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 scharr")

from scipy import signal

def scharr(I,_boundary='symm'):
    # I 与 scharr_x 的 same 卷积
    scharr_x = np.array([[3,0,-3],[10,0,-10],[3,0,-3]],np.float32)
    I_x = signal.convolve2d(I,scharr_x,mode='same',boundary='symm')
    # I 与 scharr_y 的same 卷积
    scharr_y = np.array([[3,10,3],[0,0,0],[-3,-10,-3]],np.float32)
    I_y = signal.convolve2d(I,scharr_y,mode='same',boundary='symm')
    return (I_x,I_y)

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#求卷积
i_conv_sch_x = scharr(image,1,0,_boundary='symm')
i_conv_sch_y = scharr(image,0,1,_boundary='symm')
#取绝对值,分别得到水平方向和垂直方向的边缘强度
abs_i_conv_sch_x = np.abs(i_conv_sch_x)
abs_i_conv_sch_y = np.abs(i_conv_sch_y)
#水平方向和垂直方向的边缘强度的灰度级显示
edge_x = abs_i_conv_sch_x.copy()
edge_y = abs_i_conv_sch_y.copy()
edge_x[edge_x>255]=255
edge_y[edge_y>255]=255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)
cv2.imshow("edge_x",edge_x)
cv2.imshow("edge_y",edge_y)
#根据水平方向和垂直方向的边缘强度,求最终的边缘强度
#有多种方式，这里使用平方根形式
edge = np.sqrt(np.power(abs_i_conv_sch_x,2)+np.power(abs_i_conv_sch_y,2))
#最终的边缘强度的灰度级显示
edge[edge>255]=255
edge = np.round(edge)
edge = edge.astype(np.uint8)
cv2.imshow('edge',edge)
#经过阈值处理的边缘显示
cv2.namedWindow("thresh_edge",1)
MAX_THRESH = 255
thresh = 255

#回调函数，阈值处理
def callback_thresh(_thresh):
    threshEdge = edge.copy()
    threshEdge[threshEdge < _thresh] = 0
    threshEdge[threshEdge >= _thresh] = 255
    cv2.imshow("thresh_edge",threshEdge)

callback_thresh(thresh)
cv2.createTrackbar("thresh","thresh_edge",thresh,MAX_THRESH,callback_thresh)

#模拟铅笔素描
pencilSketch = edge.copy()
pencilSketch = 255 - pencilSketch
pencilSketch[pencilSketch < 100] = 100
cv2.imshow("pencilSketch",pencilSketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Kirsch")

from scipy import signal

"""
    Krisch边缘检测算法:
    krisch(image,_boundary='fill',_fillvalue=0)
    其中:边缘处理的方式_boundary包括：'symm','wrap','fill',
    且当__boundary='fill'时,填充值默认为零_fillvalue=0
"""

def krisch(image,_boundary='fill',_fillvalue=0):
    """
    第一步:8个krisch边缘卷积算子分别和图像矩阵进行卷积,然后分别取绝对值得到边缘强度
    """
    #存储8个方向的边缘强度
    list_edge=[]
    #图像矩阵和k1进行卷积,然后取绝对值（即:得到边缘强度）
    k1 = np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]])
    image_k1 = signal.convolve2d(image,k1,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k1))
    #图像矩阵和k2进行卷积,然后取绝对值（即:得到边缘强度）
    k2 = np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]])
    image_k2 = signal.convolve2d(image,k2,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k2))
    #图像矩阵和k3进行卷积,然后取绝对值（即:得到边缘强度）
    k3 = np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]])
    image_k3 = signal.convolve2d(image,k3,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k3))
    #图像矩阵和k4进行卷积,然后取绝对值（即:得到边缘强度）
    k4 = np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]])
    image_k4 = signal.convolve2d(image,k4,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k4))
    #图像矩阵和k5进行卷积,然后取绝对值（即:得到边缘强度）
    k5 = np.array([[-3,-3,5],[-3,0,5],[-3,-3,5]])
    image_k5 = signal.convolve2d(image,k5,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k5))
    #图像矩阵和k6进行卷积,然后取绝对值（即:得到边缘强度）
    k6 = np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]])
    image_k6 = signal.convolve2d(image,k6,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k6))
    #图像矩阵和k7进行卷积,然后取绝对值（即:得到边缘强度）
    k7 = np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]])
    image_k7 = signal.convolve2d(image,k7,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k7))
    #图像矩阵和k8进行卷积,然后取绝对值（即:得到边缘强度）
    k8 = np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]])
    image_k8 = signal.convolve2d(image,k8,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    list_edge.append(np.abs(image_k8))
    """
    第二步：对上述8个方向的边缘强度,对应位置取最大值，作为图像最后的边缘强度
    """
    edge = list_edge[0]
    for i in range(len(list_edge)):
        edge = edge*(edge>=list_edge[i]) + list_edge[i]*(edge < list_edge[i])
    return edge

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
edge = krisch(image,_boundary='symm')
#边缘强度的灰度级显示
rows,cols = edge.shape
for r in range(rows):
    for c in range(cols):
        if edge[r][c] >255:
            edge[r][c] = 255
edge = edge.astype(np.uint8)
cv2.imshow("edge",edge)
#经过阈值处理的边缘显示
cv2.namedWindow("thresh_edge",1)
MAX_THRESH = 255
thresh = 255

#回调函数，阈值处理
def callback_thresh(_thresh):
    threshEdge = edge.copy()
    threshEdge[threshEdge < _thresh] = 0
    threshEdge[threshEdge >= _thresh] = 255
    cv2.imshow("thresh_edge",threshEdge)

callback_thresh(thresh)
cv2.createTrackbar("thresh","thresh_edge",thresh,MAX_THRESH,callback_thresh)

#模拟素描
pencilSketch = edge.copy()
pencilSketch = 255 - pencilSketch
pencilSketch[pencilSketch<50] = 50
cv2.imshow("pencilSketch",pencilSketch)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 canny")

#sobel边缘检测

#边缘检测
#非极大值抑制
def non_maximum_suppression_default(dx,dy):
    #边缘强度
    edgeMag = np.sqrt(np.power(dx,2.0) + np.power(dy,2.0))
    #宽、高
    rows,cols = dx.shape
    #梯度方向
    gradientDirection = np.zeros(dx.shape)
    #边缘强度非极大值抑制
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            #angle 的范围 [0,180] [-180,0]
            angle = math.atan2(dy[r][c],dx[r][c])/math.pi*180
            gradientDirection[r][c] = angle
            #左 / 右方向
            if(abs(angle)<22.5 or abs(angle) >157.5):
                if(edgeMag[r][c]>edgeMag[r][c-1] and edgeMag[r][c] > edgeMag[r][c+1]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #左上 / 右下方向  
            if(angle>=22.5 and angle < 67.5 or(-angle > 112.5 and -angle <= 157.5)):
                if(edgeMag[r][c] > edgeMag[r-1][c-1] and edgeMag[r][c]>edgeMag[r+1][c+1]):
                     edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #上 / 下方向
            if((angle>=67.5 and angle<=112.5) or (angle>=-112.5 and angle<=-67.5)):
                if(edgeMag[r][c] > edgeMag[r-1][c] and edgeMag[r][c] > edgeMag[r+1][c]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            #右上 / 左下方向
            if((angle>112.5 and angle<=157.5) or(-angle>=22.5 and -angle< 67.5 )):
                if(edgeMag[r][c]>edgeMag[r-1][c+1] and edgeMag[r][c] > edgeMag[r+1][c-1]):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup

#非极大值抑制：插值比较
def non_maximum_suppression_Inter(dx,dy):
    #边缘强度
    edgeMag = np.sqrt(np.power(dx,2.0)+np.power(dy,2.0))
    #宽、高
    rows,cols = dx.shape
    #梯度方向
    gradientDirection = np.zeros(dx.shape)
    #边缘强度的非极大值抑制
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            if dy[r][c] ==0 and dx[r][c] == 0:
                continue
            #angle的范围 [0,180],[-180,0]
            angle = math.atan2(dy[r][c],dx[r][c])/math.pi*180
            gradientDirection[r][c] = angle
            #左上方和上方的插值 右下方和下方的插值
            if (angle > 45 and angle <=90) or (angle > -135 and angle <=-90):
                ratio = dx[r][c]/dy[r][c]
                leftTop_top = ratio*edgeMag[r-1][c-1]+(1-ratio)*edgeMag[r-1][c]
                rightBottom_bottom = (1-ratio)*edgeMag[r+1][c] + ratio*edgeMag[r+1][c+1]
                if edgeMag[r][c] >  leftTop_top and edgeMag[r][c] > rightBottom_bottom:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
            #右上方和上方的插值 左下方和下方的插值
            if (angle>90 and angle<=135) or (angle>-90 and angle <= -45):
                ratio = abs(dx[r][c]/dy[r][c])
                rightTop_top = ratio*edgeMag[r-1][c+1] + (1-ratio)*edgeMag[r-1][c]
                leftBottom_bottom = ratio*edgeMag[r+1][c-1] + (1-ratio)*edgeMag[r+1][c]
                if edgeMag[r][c] > rightTop_top and edgeMag[r][c] > leftBottom_bottom:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
            #左上方和左方的插值 右下方和右方的插值
            if (angle>=0 and angle <=45) or (angle>-180 and angle <= -135):
                ratio = dy[r][c]/dx[r][c]
                rightBottom_right = ratio*edgeMag[r+1][c+1]+(1-ratio)*edgeMag[r][c+1]
                leftTop_left = ratio*edgeMag[r-1][c-1]+(1-ratio)*edgeMag[r][c-1]
                if edgeMag[r][c] > rightBottom_right and edgeMag[r][c] > leftTop_left:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
            #右上方和右方的插值 左下方和左方的插值
            if(angle>135 and angle<=180) or (angle>-45 and angle <=0):
                ratio = abs(dy[r][c]/dx[r][c])
                rightTop_right = ratio*edgeMag[r-1][c+1]+(1-ratio)*edgeMag[r][c+1]
                leftBottom_left = ratio*edgeMag[r+1][c-1]+(1-ratio)*edgeMag[r][c-1]
                if edgeMag[r][c] > rightTop_right and edgeMag[r][c] > leftBottom_left:
                    edgeMag_nonMaxSup[r][c]  = edgeMag[r][c]
    return edgeMag_nonMaxSup

#判断一个点的坐标是否在图像范围内
def checkInRange(r,c,rows,cols):
    if r>=0 and r<rows and c>=0 and c<cols:
        return True
    else:
        return False

def trace(edgeMag_nonMaxSup,edge,lowerThresh,r,c,rows,cols):
    #大于阈值为确定边缘点
    if edge[r][c] == 0:
        edge[r][c]=255
        for i in range(-1,2):
            for j in range(-1,2):
                if checkInRange(r+i,c+j,rows,cols) and edgeMag_nonMaxSup[r+i][c+j] >= lowerThresh:
                    trace(edgeMag_nonMaxSup,edge,lowerThresh,r+i,c+j,rows,cols)

#滞后阈值
def hysteresisThreshold(edge_nonMaxSup,lowerThresh,upperThresh):
    #宽高
    rows,cols = edge_nonMaxSup.shape
    edge = np.zeros(edge_nonMaxSup.shape,np.uint8)
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            #大于高阈值，设置为确定边缘点，而且以该点为起始点延长边缘
            if edge_nonMaxSup[r][c] >= upperThresh:
                trace(edgeMag_nonMaxSup,edge,lowerThresh,r,c,rows,cols)
            #小于低阈值，被剔除
            if edge_nonMaxSup[r][c]< lowerThresh:
                edge[r][c] = 0
    return edge

if __name__ =="__main__":
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    # ------- canny 边缘检测 -----------
    #第一步： 基于 sobel 核的卷积
    image_sobel_x,image_sobel_y = sobel(image,3)
    #边缘强度：两个卷积结果对应位置的平方和
    edge = np.sqrt(np.power(image_sobel_x,2.0) + np.power(image_sobel_y,2.0))
    #边缘强度的灰度级显示
    edge[edge>255] = 255
    edge = edge.astype(np.uint8)
    cv2.imshow("sobel edge",edge)
    #第二步：非极大值抑制
    edgeMag_nonMaxSup = non_maximum_suppression_default(image_sobel_x,image_sobel_y)
    edgeMag_nonMaxSup[edgeMag_nonMaxSup>255] =255
    edgeMag_nonMaxSup = edgeMag_nonMaxSup.astype(np.uint8)
    cv2.imshow("edgeMag_nonMaxSup",edgeMag_nonMaxSup)
    #第三步：双阈值滞后阈值处理，得到 canny 边缘
    #滞后阈值的目的就是最后决定处于高阈值和低阈值之间的是否为边缘点
    edge = hysteresisThreshold(edgeMag_nonMaxSup,60,180)
    lowerThresh = 40
    upperThresh = 150
    cv2.imshow("canny",edge)
    # -------以下是为了单阈值与滞后阈值的结果比较 ------
    #大于高阈值 设置为白色 为确定边缘
    EDGE = 255
    #小于低阈值的设置为黑色 表示不是边缘，被剔除
    NOEDGE = 0
    #而大于等于低阈值 小于高阈值的设置为灰色，标记为可能的边缘
    POSSIBLE_EDGE = 128
    tempEdge = np.copy(edgeMag_nonMaxSup)
    rows,cols = tempEdge.shape
    for r in range(rows):
        for c in range(cols):
            if tempEdge[r][c]>=upperThresh:
                tempEdge[r][c] = EDGE
            elif tempEdge[r][c]<lowerThresh:
                tempEdge[r][c] = NOEDGE
            else:
                tempEdge[r][c] = POSSIBLE_EDGE
    cv2.imshow("tempEdge",tempEdge)
    lowEdge = np.copy(edgeMag_nonMaxSup)
    lowEdge[lowEdge>60] = 255
    lowEdge[lowEdge<60] = 0
    cv2.imshow("lowEdge",lowEdge)
    upperEdge = np.copy(edgeMag_nonMaxSup)
    upperEdge[upperEdge>180]=255
    upperEdge[upperEdge<=180]=0
    cv2.imshow("upperEdge",upperEdge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 laplacian")
from scipy import signal

#laplacian 边缘检测算法:
#laplacian(image,_boundary='fill',_fillvalue=0)
#其中：边缘处理的方式_boundary包括：'symm','wrap','fill',
#且当__boundary='fill'时，填充值默认为零_fillvalue=0

def laplacian(image,_boundary='fill',_fillvalue=0):
    #拉普拉斯卷积核
    #laplacianKernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
    laplacianKernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],np.float32)
    #图像矩阵和拉普拉斯算子卷积
    i_conv_lap = signal.convolve2d(image,laplacianKernel,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    return i_conv_lap

if __name__ =="__main__":
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #显示原图
    cv2.imshow("image.jpg",image)
    # ----- 第一种情形 ------
    #图像矩阵和拉普拉斯核进行卷积，然后进行阈值处理
    i_conv_lap = laplacian(image,'symm')
    i_conv_lap_copy = np.copy(i_conv_lap)
    #i_conv_lap_copy[i_conv_lap_copy>0] = 255
    #i_conv_lap_copy[i_conv_lap_copy<=0] = 150
    i_conv_lap_copy = np.abs(i_conv_lap_copy)
    i_conv_lap_copy += 125
    i_conv_lap_copy[i_conv_lap_copy>255]=255
    i_conv_lap_copy = i_conv_lap_copy.astype(np.uint8)
    cv2.imshow("i_conv_lap",i_conv_lap_copy)
    #第五种情形
    
    # ---- 第二种情形 ------
    #对卷积结果取绝对值
    i_conv_lap_abs = np.abs(i_conv_lap)
    i_conv_lap_abs = np.round(i_conv_lap_abs)
    i_conv_lap_abs[i_conv_lap_abs>255]=255
    i_conv_lap_abs = i_conv_lap_abs.astype(np.uint8)
    cv2.imshow("i_conv_lap_abs",i_conv_lap_abs)
    # ---- 第三种情形 -----
    #先对图像进行高斯平滑，再进行拉普拉斯卷积，然后阈值处理
    imageBlur = gaussBlur(image,3,19,19,'symm')
    imageBlur_conv_lap = laplacian(imageBlur,'symm')
    threshEdge = np.copy(imageBlur_conv_lap)
    threshEdge = np.abs(threshEdge)
    threshEdge[threshEdge>255] = 255
    #threshEdge[threshEdge>0] = 255
    #threshEdge[threshEdge<=0] = 0
    threshEdge = threshEdge.astype(np.uint8)
    cv2.imshow("threshEdge",threshEdge)
    # ---- 第四种情形 ----
    #图像抽象化
    rows,cols = imageBlur_conv_lap.shape
    imageAbstraction = np.copy(imageBlur_conv_lap)
    for r in range(rows):
        for c in range(cols):
            if imageAbstraction[r][c] > 0:
                imageAbstraction[r][c] = 1
            else:
                imageAbstraction[r][c] = 1+math.tanh(imageAbstraction[r][c])
    cv2.imshow("imageAbstraction",imageAbstraction)
    #转换为 8 位图，保存结果
    imageAbstraction = 255*imageAbstraction
    imageAbstraction = np.round(imageAbstraction)
    imageAbstraction = imageAbstraction.astype(np.uint8)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 LoG_edge")

from scipy import signal

#构建 LoG 算子
def createLoGKernel(sigma,kSize):
    # LoG 算子的宽高，且两者均为奇数
    winH,winW = kSize
    logKernel = np.zeros(kSize,np.float32)
    #方差
    sigmaSquare = pow(sigma,2.0)
    # LoG 算子的中心
    centerH = (winH-1)/2
    centerW = (winW-1)/2
    for r in range(winH):
        for c in range(winW):
            norm2 = pow(r-centerH,2.0) + pow(c-centerW,2.0)
            logKernel[r][c] = 1.0/sigmaSquare*(norm2/sigmaSquare - 2)*math.exp(-norm2/(2*sigmaSquare))
    return logKernel

#高斯拉普拉斯卷积，一般取 _boundary = 'symm'
def LoG(image,sigma,kSize,_boundary='fill',_fillValue = 0):
    #构建 LoG 卷积核
    loGKernel = createLoGKernel(sigma,kSize)
    #图像与 LoG 卷积核卷积
    img_conv_log = signal.convolve2d(image,loGKernel,'same',boundary =_boundary)
    return img_conv_log

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#高斯拉普拉斯卷积
img_conv_log = LoG(image,2,(13,13),'symm')
#边缘的二值化显示
edge_binary = np.copy(img_conv_log)
edge_binary[edge_binary>=0]=0
edge_binary[edge_binary<0]=255
edge_binary = edge_binary.astype(np.uint8)
cv2.imshow("edge_binary",edge_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 LoG")

from scipy import signal

def createLoGKernel(sigma,size):
    # LoG 算子的高和宽，且两者均为奇数
    H,W = size
    r,c = np.mgrid[0:H:1,0:W:1]
    r-=(H-1)/2
    c-=(W-1)/2
    #方差
    sigma2 = pow(sigma,2.0)
    # LoG 核
    norm2 = np.power(r,2.0)+np.power(c,2.0)
    #LoGKernel=1.0/sigma2*(norm2/sigma2 -2)*np.exp(-norm2/(2*sigma2))
    LoGKernel=(norm2/sigma2 -2)*np.exp(-norm2/(2*sigma2))
    return LoGKernel
def LoG(image,sigma,size,_boundary='symm'):
    #构建 LoG 卷积核
    loGKernel = createLoGKernel(sigma,size)
    #图像与 LoG 卷积核卷积
    img_conv_log = signal.convolve2d(image,loGKernel,'same',boundary =_boundary)
    return img_conv_log

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#高斯拉普拉斯卷积
img_conv_log = LoG(image,6,(37,37),'symm')
#边缘的二值化显示
edge_binary = np.copy(img_conv_log)
edge_binary[edge_binary>0]=255
edge_binary[edge_binary<=0]=0
edge_binary = edge_binary.astype(np.uint8)
cv2.imshow("edge_binary",edge_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("邊緣檢測 DoG")

from scipy import signal


#非归一化的高斯卷积
def gaussConv(I,size,sigma):
    #卷积核的高和宽
    H,W = size
    #构造水平方向上非归一化的高斯卷积核
    xr,xc = np.mgrid[0:1,0:W]
    xc -= (W-1)/2
    xk = np.exp(-np.power(xc,2.0)/(2.0*pow(sigma,2)))
    # I 与 xk 卷积
    I_xk = signal.convolve2d(I,xk,'same','symm')
    #构造垂直方向上的非归一化的高斯卷积核
    yr,yc = np.mgrid[0:H,0:1]
    yr -= (H-1)/2
    yk = np.exp(-np.power(yr,2.0)/(2.0*pow(sigma,2.0)))
    # I_xk 与 yk 卷积
    I_xk_yk = signal.convolve2d(I_xk,yk,'same','symm')
    I_xk_yk *= 1.0/(2*np.pi*pow(sigma,2.0))
    return I_xk_yk
    #
#高斯差分
def DoG(I,size,sigma,k=1.1):
    #标准差为 sigma 的非归一化的高斯卷积
    Is = gaussConv(I,size,sigma)
    #标准差为 k*sigma 的非归一化高斯卷积
    Isk = gaussConv(I,size,k*sigma)
    #两个高斯卷积的差分
    doG = Isk - Is
    doG /= (pow(sigma,2.0)*(k-1))
    return doG

""" fail
image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#显示原图
cv2.imshow("image",image)
#高斯差分边缘检测
sigma = 4
k = 0.9
size = (25,25)
imageDoG = DoG(image,size,sigma,k)
#二值化边缘，对 imageDoG 阈值处理
edge = np.copy(imageDoG)
edge[edge>0] = 255
edge[edge<=0] = 0
edge = edge.astype(np.uint8)
cv2.imshow("edge",edge)

#图像边缘抽象化
asbstraction = -np.copy(imageDoG)
asbstraction = asbstraction.astype(np.float32)
asbstraction[asbstraction>=0]=1.0
asbstraction[asbstraction<0] = 1.0+ np.tanh(asbstraction[asbstraction<0])
cv2.imshow("asbstraction",asbstraction)
asbstraction = asbstraction*255
asbstraction = asbstraction.astype(np.uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 boxPoints_OpenCV3")

#旋转矩形
vertices = cv2.boxPoints(((200, 200), (90, 150), -60.0))
#四个顶点
print(vertices.dtype)#打印数据类型
print(vertices)#打印四个顶点
#根据四个顶点在黑色画板上画出该矩形
img = np.zeros((400,400),np.uint8)

for i in range(4):
    #相邻的点
    p1 = vertices[i,:]
    j = (i+1)%4
    p2 = vertices[j,:]
    #画出直线
    cv2.line(img, (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1])), (255, 255, 255), 5, lineType=cv2.LINE_AA)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 convexHull")

#黑色画板 400 x 400
s = 400
I = np.zeros((s,s),np.uint8)
#随机生成 横纵坐标均在 100 至 300 的坐标点
n=80#随机生成 n 个坐标点，每一行存储一个坐标
points = np.random.randint(100,300,(n,2),np.int32)
#把上述点集处的灰度值设置为 255,单个白色像素点不容易观察，用一个小圆标注一下
for i in range(n):
    cv2.circle(I,(points[i,0],points[i,1]),2,255,2)
#求点集 points 的凸包
convexhull = cv2.convexHull(points,clockwise=False)
# ----- 打印凸包的信息 ----
print(type(convexhull))
print(convexhull.shape)
#连接凸包的各个点
k = convexhull.shape[0]
for i in range(k-1):
    cv2.line(I,(convexhull[i,0,0],convexhull[i,0,1]),(convexhull[i+1,0,0],convexhull[i+1,0,1]),255,2)
#首尾相接
cv2.line(I,(convexhull[k-1,0,0],convexhull[k-1,0,1]),(convexhull[0,0,0],convexhull[0,0,1]),255,2)
#显示图片
cv2.imshow("I",I)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 minEnclosingTriangle")

points = np.array ([[[1,1]],[[5,10]],[[5,1]],[[1,10]],[[2,5]]] ,np.float32)
#points = np.array ([[1,1],[5,10],[5,1],[1,10],[2,5]] ,np.float32)
#最小外包直立矩形
area,triangle = cv2.minEnclosingTriangle(points)
#cv2.boundingRect(points)
#打印面积
print(area)
#打印三角形的三个顶点
print(triangle)
# print(type(triangle))
# print(triangle.dtype)

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 HTLine")

from mpl_toolkits.mplot3d import Axes3D

#霍夫极坐标变换：直线检测
def HTLine (image,stepTheta=1,stepRho=1):
    #宽、高
    rows,cols = image.shape
    #图像中可能出现的最大垂线的长度
    L =  round(math.sqrt(pow(rows-1,2.0)+pow(cols-1,2.0)))+1
    #初始化投票器
    numtheta = int(180.0/stepTheta)
    numRho = int(2*L/stepRho + 1)
    accumulator = np.zeros((numRho,numtheta),np.int32)
    #建立字典
    accuDict={}
    for k1 in range(numRho):
        for k2 in range(numtheta):
            accuDict[(k1,k2)]=[]
    #投票计数
    for y in range(rows):
        for x  in range(cols):
            if(image[y][x] == 255):#只对边缘点做霍夫变换
                for m in range(numtheta):
                    #对每一个角度，计算对应的 rho 值
                    rho = x*math.cos(stepTheta*m/180.0*math.pi)+y*math.sin(stepTheta*m/180.0*math.pi)
                    #计算投票哪一个区域
                    n = int(round(rho+L)/stepRho)
                    #投票加 1
                    accumulator[n,m] += 1
                    #记录该点
                    accuDict[(n,m)].append((x,y))
    return accumulator,accuDict

"""
if __name__ == "__main__":
    #输入图像
    I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #canny 边缘检测
    edge = cv2.Canny(I,50,200)
    #显示二值化边缘
    cv2.imshow("edge",edge)
    #霍夫直线检测
    accumulator,accuDict = HTLine(edge,1,1)
    #计数器的二维直方图方式显示
    rows,cols = accumulator.shape
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X,Y = np.mgrid[0:rows:1, 0:cols:1]
    surf = ax.plot_wireframe(X,Y,accumulator,cstride=1, rstride=1,color='gray')
    ax.set_xlabel(u"$\\rho$")
    ax.set_ylabel(u"$\\theta$")
    ax.set_zlabel("accumulator")
    ax.set_zlim3d(0,np.max(accumulator))
    #计数器的灰度级显示
    grayAccu = accumulator/float(np.max(accumulator))
    grayAccu = 255*grayAccu
    grayAccu = grayAccu.astype(np.uint8)
    #只画出投票数大于 60 直线
    voteThresh = 60
    for r in range(rows):
        for c in range(cols):
            if accumulator[r][c] > voteThresh:
                points = accuDict[(r,c)]
                cv2.line(I,points[0],points[len(points)-1],(255),2)
    cv2.imshow('accumulator',grayAccu)
    
    #显示原图
    cv2.imshow("I",I)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 HTCircle")
""" 跑不完
#标准霍夫圆检测
def HTCircle (I,minR,maxR,voteThresh = 100):
    #宽、高
    H,W = I.shape
    #归为整数
    minr = round(minR)+1
    maxr = round(maxR)+1
    #初始化三维的计数器
    r_num = int(maxr-minr+1)
    a_num = int(W-1+maxr+maxr+1)
    b_num = int(H-1+maxr+maxr+1)
    accumulator = np.zeros((r_num,b_num,a_num),np.int32)
    #投票计数
    for y in range(H):
        for x  in range(W):
            if(I[y][x] == 255):#只对边缘点做霍夫变换
                for k in range(r_num):# r 变化的步长为 1 
                    for theta in np.linspace(0,360,360):
                        #计算对应的 a 和 b
                        a = x - (minr+k)*math.cos(theta/180.0*math.pi)
                        b = y - (minr+k)*math.sin(theta/180.0*math.pi)
                        #取整
                        a = int(round(a))
                        b = int(round(b))
                        #投票
                        accumulator[k,b,a]+=1
    #筛选投票数 大于 voteThresh的圆
    circles = []
    for k in range(r_num):
        for b in range(b_num):
            for a in range(a_num): 
                if(accumulator[k,b,a]>voteThresh):
                    circles.append((k+minr,b,a))
    return circles

I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#canny 边缘检测
edge = cv2.Canny(I,50,200)
cv2.imshow("edge",edge)
#霍夫圆检测
circles = HTCircle(edge,60,80,80)
#画圆
for i in range(len(circles)):
    cv2.circle(I,(int(circles[i][2]),int(circles[i][1])),int(circles[i][0]),(255),2)
cv2.imshow("I",I)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 arcLength")

#点集
points = np.array ([[[0,0]],[[50,30]],[[100,0]],[[100,100]]] ,np.float32)
print(points.shape)
#points = np.array ([[0,0],[50,30],[100,0],[100,100]] ,np.float32)
#计算点集的所围区域的周长
length1 = cv2.arcLength(points,False)#首尾不相连
length2 = cv2.arcLength(points,True)#首尾相连
#计算点集所围区域的面积
area = cv2.contourArea(points)
#打印周长和面积
print(length1,length2,area)

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 contours")

#输入图像
img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#边缘检测或阈值分割的二值化
binaryImg = cv2.Canny(img,50,200)
#寻找轮廓
contours,h = cv2.findContours(binaryImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#打印 contoures 的类型
print(type(contours))
# contours 是列表类型，打印每一元素的类型
print(type(contours[0]))
#打印轮廓（点集）个数
print(len(contours))
#对这些点集，求每一个点集最小
#最小外包凸包
contoursImg = np.zeros(img.shape,np.uint8)
cv2.drawContours(contoursImg,contours,7,255,3)
circle = cv2.minEnclosingCircle(contours[7])
cv2.circle(contoursImg,(int(circle[0][0]),int(circle[0][1])),int(circle[1]),255,2)
convexhull = cv2.convexHull(contours[7])
cv2.drawContours(contoursImg,contours,7,255,3)
for i in range(len(contours)):
    # ----- 最小外包圆 -------
    circle = cv2.minEnclosingCircle(contours[i])
    #画圆
    #cv2.circle(img,(int(circle[0][0]),int(circle[0][1])),int(circle[1]),255,2)
    # ---- 最小直立矩形 ----
    rect = cv2.boundingRect(contours[i])
    #cv2.rectangle(img,(rect[0],rect[1]),(rect[2],rect[3]),255,2)
    # ---- 最小外包的旋转矩形 -----
    convexhull = cv2.convexHull(contours[i])

#最小直立矩形
cv2.imshow("img",img)
#显示轮廓
cv2.imshow("contoursImg",contoursImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 convexityDefects")

#轮廓
contour = np.array([[20,20],[50,70],[20,120],[120,120],[100,70],[120,20]],np.int32)
#轮廓的凸包
hull = cv2.convexHull(contour,returnPoints=False)
defects = cv2.convexityDefects(contour,hull)
#打印凸包
print(hull)
#打印凸包的缺陷
print(defects)

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 drawContours")

img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#第二步：边缘检测 或者 阈值处理 生成一张二值图
img = cv2.GaussianBlur(img, (3, 3), 0.5)#高斯平滑处理    #執行高斯模糊化
binaryImg = cv2.Canny(img,50,200)
cv2.imshow("binaryImg",binaryImg)
#第三步：边缘的轮廓，返回的 contours 是一个 list 列表
contours, h= cv2.findContours(binaryImg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#轮廓的数量
n =  len(contours)
contoursImg = []
#画出找到的轮廓
for i in range(n):
    #创建一个黑色画布
    temp = np.zeros(binaryImg.shape,np.uint8)
    contoursImg.append(temp)
    #在第 i 个黑色画布上，画第 i 个轮廓
    cv2.drawContours(contoursImg[i],contours,i,255,2)
    cv2.imshow("contour-"+str(i),contoursImg[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
""" fail
print("幾何形狀的檢測和擬合 findContours_OpenCV3")

#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

#第一步：阈值化，生成二值图
#图像平滑
dst = cv2.GaussianBlur(img, (3, 3), 0.5)   #執行高斯模糊化
# Otsu 阈值分割
OtsuThresh = 0
OtsuThresh,dst = cv2.threshold(dst,OtsuThresh,255,cv2.THRESH_OTSU)
# --- 形态学开运算（ 消除细小白点 ）
#创建结构元
s = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dst = cv2.morphologyEx(dst,cv2.MORPH_OPEN,s,iterations=2)

#第二步：寻找二值图的轮廓，返回值是一个元组，hc[1] 代表轮廓
hc= cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = hc[1]
#打印轮廓的属性
print(type(contours))
#第三步：画出找到的轮廓并用多边形拟合轮廓
#轮廓的数量
n =  len(hc[1])
#将轮廓画在该黑板上
contoursImg = np.zeros(img.shape,np.uint8)
for i in range(n):
    #画出轮廓
    cv2.drawContours(contoursImg,contours,i,255,2)
    #画出轮廓的最小外包圆
    circle = cv2.minEnclosingCircle(contours[i])
    cv2.circle(img,(int(circle[0][0]),int(circle[0][1])),int(circle[1]),0,5)
    #多边形逼近（注意与凸包区别）
    approxCurve = cv2.approxPolyDP(contours[i],0.3,True)
    #多边形顶点个数
    k = approxCurve.shape[0]
    #顶点连接，绘制多边形
    for i in range(k-1):
        cv2.line(img,(approxCurve[i,0,0],approxCurve[i,0,1]),(approxCurve[i+1,0,0],approxCurve[i+1,0,1]),0,5)
    #首尾相接
    cv2.line(img,(approxCurve[k-1,0,0],approxCurve[k-1,0,1]),(approxCurve[0,0,0],approxCurve[0,0,1]),0,5)

#显示轮廓
cv2.imshow("contours",contoursImg)
#显示拟合的多边形
cv2.imshow("dst",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 pointPolygonTest")

#点集
contour = np.array([[0,0],[50,30],[100,100],[100,0]],np.float32)
#判断三个点和点集构成的轮廓的关系
dist1 = cv2.pointPolygonTest(contour,(80,40),False)
dist2 = cv2.pointPolygonTest(contour,(50,0),False)
dist3 = cv2.pointPolygonTest(contour,(40,80),False)
#打印结果
print(dist1,dist2,dist3)

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 fft2")

#快速傅里叶变换
def fft2Image(src):
    #得到行、列
    r,c = src.shape[:2]
    #得到快速傅里叶变换最优扩充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    #边缘扩充，下边缘和右边缘扩充值为零
    fft2 = np.zeros((rPadded,cPadded,2),np.float32)
    fft2[:r,:c,0]=src
    #快速傅里叶变换
    cv2.dft(fft2,fft2,cv2.DFT_COMPLEX_OUTPUT)
    return fft2

image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
#计算图像矩阵的快速傅里叶变换
fft2 = fft2Image(image)
#傅里叶逆变换
ifft2 = np.zeros(fft2.shape[:2],np.float32)
cv2.dft(fft2,ifft2,cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)
#裁剪
img = np.copy(ifft2[:image.shape[0],:image.shape[1]])
#裁剪后的结果 img 等于 image，两个相减的最大值为零
print(np.max(image - img))

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 spectrum")

#快速傅里叶变换
def fft2Image(src):
    #得到行、列
    r,c = src.shape[:2]
    #得到快速傅里叶变换最优扩充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    #边缘扩充，下边缘和右边缘扩充值为零
    fft2 = np.zeros((rPadded,cPadded,2),np.float32)
    fft2[:r,:c,0]=src
    #快速傅里叶变换
    cv2.dft(fft2,fft2,cv2.DFT_COMPLEX_OUTPUT)
    return fft2

#傅里叶幅度谱
def amplitudeSpectrum(fft2):
    #求幅度
    real2 = np.power(fft2[:,:,0],2.0)
    Imag2 = np.power(fft2[:,:,1],2.0)
    amplitude = np.sqrt(real2+Imag2)
    return amplitude

#幅度谱的灰度级显示
def graySpectrum(amplitude):
    #对比度拉伸
    #cv2.log(amplitude+1.0,amplitude)
    amplitude = np.log(amplitude+1.0)
    #归一化,傅里叶谱的灰度级显示
    spectrum = np.zeros(amplitude.shape,np.float32)
    cv2.normalize(amplitude,spectrum,0,1,cv2.NORM_MINMAX)
    return spectrum

#相位谱
def phaseSpectrum(fft2):
    #得到行数、列数
    rows,cols = fft2.shape[:2]
    #计算相位角
    phase = np.arctan2(fft2[:,:,1],fft2[:,:,0])
    #相位角转换为 [ -180 , 180]
    spectrum = phase/math.pi*180
    return spectrum

if __name__ =="__main__":
    #第一步：读入图像
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #显示原图
    cv2.imshow("image",image)
    #快速傅里叶变换
    fft2 = fft2Image(image)
    #求幅度谱
    amplitude = amplitudeSpectrum(fft2)
    amc = np.copy(amplitude)
    amc[amc>255]=255
    amc = amc.astype(np.uint8)
   # cv2.imshow("originam",amc)
    #幅度谱的灰度级显示
    ampSpectrum = graySpectrum(amplitude)
    ampSpectrum *=255
    ampSpectrum = ampSpectrum.astype(np.uint8)
    cv2.imshow("amplitudeSpectrum",ampSpectrum)
    #相位谱的灰度级显示
    phaseSpe = phaseSpectrum(fft2)
    cv2.imshow("phaseSpectrum",phaseSpe)
    """
    傅里叶幅度谱的中心化
    """
    #第一步：图像乘以(-1)^(r+c)
    rows,cols = image.shape
    fimg = np.copy(image)
    fimg = fimg.astype(np.float32)
    for r in range(rows):
        for c in range(cols):
            if (r+c)%2:
                fimg[r][c] =-1*image[r][c]
            else:
                fimg[r][c] = image[r][c]
    #第二步：快速傅里叶变换
    imgfft2 = fft2Image(fimg)
    #第三步：傅里叶的幅度谱
    amSpe = amplitudeSpectrum(imgfft2)
    #幅度谱的灰度级显示
    graySpe = graySpectrum(amSpe)
    cv2.imshow("amSpe",graySpe)
    graySpe *=255
    graySpe = graySpe.astype(np.uint8)
    #第四步：相位谱的灰度级显示
    phSpe = phaseSpectrum(imgfft2)
    cv2.imshow("phSpe",phSpe)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 saliencyMap")

#快速傅里叶变换
def fft2Image(src):
    #得到行、列
    r,c = src.shape[:2]
    #得到快速傅里叶变换最优
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    #边缘扩充，下边缘和右边缘扩充值为零
    fft2 = np.zeros((rPadded,cPadded,2),np.float32)
    fft2[:r,:c,0]=src
    #快速傅里叶变换
    cv2.dft(fft2,fft2,cv2.DFT_COMPLEX_OUTPUT)
    return fft2
 #傅里叶幅度谱
def amplitudeSpectrum(fft2):
    #求幅度
    real,Imag = cv2.split(fft2)
    amplitude = cv2.magnitude(real,Imag)
    #amplitude = cv2.magnitude(fft2[:,:,0],fft2[:,:,1])
    return amplitude
#幅度谱的灰度级显示
def graySpectrum(amplitude):
    #对比度拉伸
    #cv2.log(amplitude+1.0,amplitude)
    amplitude = np.log(amplitude+1.0)
    #归一化,傅里叶谱的灰度级显示
    spectrum = np.zeros(amplitude.shape,np.float32)
    cv2.normalize(amplitude,spectrum,0,1,cv2.NORM_MINMAX)
    return spectrum
#相位谱
def phaseSpectrum(fft2):
    #得到行数、列数
    rows,cols = fft2.shape[:2]
    #计算相位角
    phase = np.arctan2(fft2[:,:,1],fft2[:,:,0])
    #显示该相位谱时，首先需要将相位角转换为 [ -180 , 180]
    #spectrum = phase/math.pi*180
    return phase    


image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

#第一步：计算图像的快速傅里叶变换
fft2 = fft2Image(image)

#第二步：计算傅里叶幅度谱的灰度级
#求幅度谱
amplitude = amplitudeSpectrum(fft2)
#幅度谱的灰度级
logAmplitude = graySpectrum(amplitude)

#第三步：计算相位
phase = phaseSpectrum(fft2)
#余弦谱（用于计算实部）
cosSpectrum = np.cos(phase)
#正弦谱（用于计算虚部）
sinSectrum = np.sin(phase)

#第四步：计算残差（Spectral Residual）
#对幅度谱的灰度级进行均值平滑
meanLogAmplitude = cv2.boxFilter(logAmplitude,cv2.CV_32FC1,(3,3))
#残差
spectralResidual = logAmplitude - meanLogAmplitude

#第五步：计算傅里叶逆变换,显著性
#残差的指数
expSR = np.exp(spectralResidual)
#分别计算实部和虚部
real = expSR*cosSpectrum
imaginary = expSR*sinSectrum
#合并实部和虚部
com = np.zeros((real.shape[0],real.shape[1],2),np.float32)
com[:,:,0]=real
com[:,:,1]=imaginary
#逆变换
ifft2=np.zeros(com.shape,np.float32)
cv2.dft(com,ifft2,cv2.DFT_COMPLEX_OUTPUT+cv2.DFT_INVERSE)
#显著性
saliencymap = np.power(ifft2[:,:,0],2)+np.power(ifft2[:,:,1],2)
#对显著性进行高斯平滑
saliencymap = cv2.GaussianBlur(saliencymap, (11, 11), 2.5) #執行高斯模糊化
#显示检测到的显著性
#cv2.normalize(saliencymap,saliencymap,0,1,cv2.NORM_MINMAX)
saliencymap  = saliencymap/np.max(saliencymap)
#提高对比度，进行伽马变换
saliencymap = np.power(saliencymap,0.5)
saliencymap = np.round(saliencymap*255)
saliencymap = saliencymap.astype(np.uint8)
cv2.imshow("saliencymap",saliencymap)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 fft2Conv")

from scipy import signal

if __name__ =="__main__":
    #图像矩阵
    I = np.array([
                  [34,56,1,0,255,230,45,12],
                  [0,201,101,125,52,12,124,12],
                  [3,41,42,40,12,90,123,45],
                  [5,245,98,32,34,234,90,123],
                  [12,12,10,41,56,89,189,5],
                  [112,87,12,45,78,45,10,1],
                  [42,123,234,12,12,21,56,43],
                  [1,2,45,123,10,44,123,90]
                  ],np.float64)
    #卷积核
    kernel = np.array([[1,0,-1],[1,0,1],[1,0,-1]],np.float64)
    # I 与 kernel 进行全卷积
    confull = signal.convolve2d(I,kernel,mode='full',boundary = 'fill',fillvalue=0)
    # I 的傅里叶变换
    FT_I = np.zeros((I.shape[0],I.shape[1],2),np.float64)
    cv2.dft(I,FT_I,cv2.DFT_COMPLEX_OUTPUT)
    # kernel 的傅里叶变换
    FT_kernel = np.zeros((kernel.shape[0],kernel.shape[1],2),np.float64)
    cv2.dft(kernel,FT_kernel,cv2.DFT_COMPLEX_OUTPUT)
    # 傅里叶变换
    fft2= np.zeros((confull.shape[0],confull.shape[1]),np.float64)
    #对 I 进行右侧和下侧补 0
    I_Padded = np.zeros((I.shape[0]+kernel.shape[0]-1,I.shape[1]+kernel.shape[1]-1),np.float64)
    I_Padded[:I.shape[0],:I.shape[1]] = I
    FT_I_Padded = np.zeros((I_Padded.shape[0],I_Padded.shape[1],2),np.float64)
    cv2.dft(I_Padded,FT_I_Padded,cv2.DFT_COMPLEX_OUTPUT)
    #对 kernel 进行右侧和下侧补 0 
    kernel_Padded = np.zeros((I.shape[0]+kernel.shape[0]-1,I.shape[1]+kernel.shape[1]-1),np.float64)
    kernel_Padded[:kernel.shape[0],:kernel.shape[1]] = kernel
    FT_kernel_Padded = np.zeros((kernel_Padded.shape[0],kernel_Padded.shape[1],2),np.float64)
    cv2.dft(kernel_Padded,FT_kernel_Padded,cv2.DFT_COMPLEX_OUTPUT)
    #两个傅里叶变换相乘
    FT_Ikernel = cv2.mulSpectrums(FT_I_Padded,FT_kernel_Padded,cv2.DFT_ROWS)
    #利用傅里叶变换求全 ( full ) 卷积
    ifft2 = np.zeros(FT_Ikernel.shape[:2],np.float64)
    cv2.dft(FT_Ikernel,ifft2,cv2.DFT_REAL_OUTPUT+cv2.DFT_INVERSE+cv2.DFT_SCALE)
    print(np.max(ifft2 - confull))
    
    # 全卷积进行傅里叶变换等于两个傅里叶变换的点乘
    FT_confull = np.zeros((confull.shape[0],confull.shape[1],2),np.float64)
    cv2.dft(confull,FT_confull,cv2.DFT_COMPLEX_OUTPUT)
    print(FT_confull-FT_Ikernel)
    print(np.max(FT_confull-FT_Ikernel))

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 fft2toConv")

from scipy import signal

#利用傅里叶变换计算离散的二维卷积
def fft2Conv(I,kernel,borderType=cv2.BORDER_DEFAULT):
    #图像矩阵的高、宽
    R,C = I.shape[:2]
    #卷积核的高、宽
    r,c = kernel.shape[:2]
    #卷积核的半径
    tb = (r-1)/2
    lr = (c-1)/2
    #第一步：扩充边界
    I_padded = cv2.copyMakeBorder(I,tb,tb,lr,lr,borderType)
    #第二步：对 I_padded 和 kernel 右侧和下侧补零
    #满足二维快速傅里叶变换的行数、列数
    rows = cv2.getOptimalDFTSize(I_padded.shape[0]+r-1)
    cols = cv2.getOptimalDFTSize(I_padded.shape[1]+c-1)
    #补零
    I_padded_zeros = np.zeros((rows,cols),np.float64)
    I_padded_zeros[:I_padded.shape[0],:I_padded.shape[1]] = I_padded
    kernel_zeros = np.zeros((rows,cols),np.float64)
    kernel_zeros[:kernel.shape[0],:kernel.shape[1]] = kernel
    #第三步：快速傅里叶变换
    fft2_Ipz = np.zeros((rows,cols,2),np.float64)
    cv2.dft(I_padded_zeros,fft2_Ipz,cv2.DFT_COMPLEX_OUTPUT)
    fft2_kz = np.zeros((rows,cols,2),np.float64)
    cv2.dft(kernel_zeros,fft2_kz,cv2.DFT_COMPLEX_OUTPUT)
    #第四步：两个快速傅里叶变换点乘
    Ipz_rz = cv2.mulSpectrums(fft2_Ipz,fft2_kz,cv2.DFT_ROWS)
    #第五步：傅里叶逆变换，并只取实部
    ifft2FullConv = np.zeros((rows,cols),np.float64)
    cv2.dft(Ipz_rz,ifft2FullConv,cv2.DFT_REAL_OUTPUT+cv2.DFT_INVERSE+cv2.DFT_SCALE)
    print(np.max(ifft2FullConv))
    #第六步：裁剪，同输入的图像矩阵尺寸一样
    sameConv = np.copy(ifft2FullConv[r-1:R+r-1,c-1:C+c-1])
    return sameConv

#图像矩阵
I = np.array([
    [34,56,1,0,255,230,45,12],
    [0,201,101,125,52,12,124,12],
    [3,41,42,40,12,90,123,45],
    [5,245,98,32,34,234,90,123],
    [12,12,10,41,56,89,189,5],
    [112,87,12,45,78,45,10,1],
    [42,123,234,12,12,21,56,43],
    [1,2,45,123,10,44,123,90]
    ],np.float32)

#卷积核
kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]],np.float32)
# same 卷积
consame = signal.convolve2d(I,kernel,mode='same',boundary = 'symm')
print(consame)
""" fail
# 利用傅里叶变换计算卷积
sameConv = fft2Conv(I,kernel,cv2.BORDER_REFLECT)
print(sameConv)
"""

print("------------------------------------------------------------")  # 60個

print("頻率域濾波 LPFilter")

#截止频率
radius = 50
MAX_RADIUS = 100
#低通滤波类型
lpType = 0
MAX_LPTYPE = 2

#快速傅里叶变换
def fft2Image(src):
    #得到行、列
    r,c = src.shape[:2]
    #得到快速傅里叶变换最优
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    #边缘扩充，下边缘和右边缘扩充值为零
    fft2 = np.zeros((rPadded,cPadded,2),np.float32)
    fft2[:r,:c,0]=src
    #快速傅里叶变换
    cv2.dft(fft2,fft2,cv2.DFT_COMPLEX_OUTPUT)
    return fft2

#傅里叶幅度谱
def amplitudeSpectrum(fft2):
    #求幅度
    real2 = np.power(fft2[:,:,0],2.0)
    Imag2 = np.power(fft2[:,:,1],2.0)
    amplitude = np.sqrt(real2+Imag2)
    return amplitude

#幅度谱的灰度级显示
def graySpectrum(amplitude):
    #对比度拉伸
    #cv2.log(amplitude+1.0,amplitude)
    amplitude = np.log(amplitude+1.0)
    #归一化,傅里叶谱的灰度级显示
    spectrum = np.zeros(amplitude.shape,np.float32)
    cv2.normalize(amplitude,spectrum,0,1,cv2.NORM_MINMAX)
    return spectrum

#构建低通滤波器    
def createLPFilter(shape,center,radius,lpType=0,n=2):
    #滤波器的高和宽
    rows,cols = shape[:2]
    r,c = np.mgrid[0:rows:1,0:cols:1]
    c-=center[0]
    r-=center[1]
    d = np.power(c,2.0)+np.power(r,2.0)
    #构造低通滤波器
    lpFilter = np.zeros(shape,np.float32)
    if(radius<=0):
        return lpFilter
    if(lpType == 0):#理想低通滤波
        lpFilter = np.copy(d)
        lpFilter[lpFilter<pow(radius,2.0)]=1
        lpFilter[lpFilter>=pow(radius,2.0)]=0
    elif(lpType == 1): #巴特沃斯低通滤波
        lpFilter = 1.0/(1.0+np.power(np.sqrt(d)/radius,2*n))
    elif(lpType == 2): #高斯低通滤波
        lpFilter = np.exp(-d/(2.0*pow(radius,2.0)))
    return lpFilter

if __name__ =="__main__":
    #第一步：读入图像
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #显示原图
    cv2.imshow("image",image)
    #第二步：每一元素乘以 (-1)^(r+c)
    fimage = np.zeros(image.shape,np.float32)
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            if (r+c)%2:
                fimage[r][c] = -1*image[r][c]
            else:
                fimage[r][c] = image[r][c]
    #第三和四步：补零和快速傅里叶变换
    fImagefft2 = fft2Image(fimage)
    #傅里叶谱
    amplitude = amplitudeSpectrum(fImagefft2)
    #傅里叶谱的灰度级显示
    spectrum = graySpectrum(amplitude)
    cv2.imshow("originalSpectrum",spectrum)
    #找到傅里叶谱最大值的位置
    minValue,maxValue,minLoc,maxLoc = cv2.minMaxLoc(amplitude)
    #低通傅里叶谱灰度级的显示窗口
    cv2.namedWindow("lpFilterSpectrum",1)
    def nothing(*arg):
        pass
    #调节低通滤波类型
    cv2.createTrackbar("lpType","lpFilterSpectrum",lpType,MAX_LPTYPE,nothing)
    #调节截断频率
    cv2.createTrackbar("radius","lpFilterSpectrum",radius,MAX_RADIUS,nothing)
    #低通滤波结果
    result = np.zeros(spectrum.shape,np.float32)
    while True:
        #得到当前的截断频率、低通滤波类型
        radius = cv2.getTrackbarPos("radius","lpFilterSpectrum")
        lpType = cv2.getTrackbarPos("lpType","lpFilterSpectrum")
        #第五步：构建低通滤波器
        lpFilter = createLPFilter(spectrum.shape,maxLoc,radius,lpType)
        #第六步：低通滤波器和快速傅里叶变换对应位置相乘（点乘）
        rows,cols = spectrum.shape[:2]
        fImagefft2_lpFilter = np.zeros(fImagefft2.shape,fImagefft2.dtype)
        for i in range(2):
            fImagefft2_lpFilter[:rows,:cols,i] = fImagefft2[:rows,:cols,i]*lpFilter
        #低通傅里叶变换的傅里叶谱
        lp_amplitude = amplitudeSpectrum(fImagefft2_lpFilter)
        #显示低通滤波后的傅里叶谱的灰度级
        lp_spectrum = graySpectrum(lp_amplitude)
        cv2.imshow("lpFilterSpectrum", lp_spectrum)
        #第七和八步：对低通傅里叶变换执行傅里叶逆变换,并只取实部
        cv2.dft(fImagefft2_lpFilter,result,cv2.DFT_REAL_OUTPUT+cv2.DFT_INVERSE+cv2.DFT_SCALE)
        #第九步：乘以(-1)^(r+c)
        for r in range(rows):
            for c in range(cols):
                if (r+c)%2:
                    result[r][c]*=-1
        #第十步：数据类型转换,并进行灰度级显示，截取左上角，大小和输入图像相等
        for r in range(rows):
            for c in range(cols):
                if result[r][c] < 0:
                    result[r][c] = 0
                elif result[r][c] > 255:
                    result[r][c] = 255
        lpResult = result.astype(np.uint8)
        lpResult = lpResult[:image.shape[0],:image.shape[1]]
        cv2.imshow("LPFilter",lpResult)
        
        k = cv2.waitKey(5)
        if k == ESC:
            break
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("頻率域濾波 HomomorphicFilter")

#快速傅里叶变换
def fft2Image(src):
    #得到行、列
    r,c = src.shape[:2]
    #得到快速傅里叶变换最优
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    #边缘扩充，下边缘和右边缘扩充值为零
    fft2 = np.zeros((rPadded,cPadded,2),np.float32)
    fft2[:r,:c,0]=src
    #快速傅里叶变换
    cv2.dft(fft2,fft2,cv2.DFT_COMPLEX_OUTPUT)
    return fft2

#傅里叶幅度谱
def amplitudeSpectrum(fft2):
    #求幅度
    real2 = np.power(fft2[:,:,0],2.0)
    Imag2 = np.power(fft2[:,:,1],2.0)
    amplitude = np.sqrt(real2+Imag2)
    return amplitude

if __name__ =="__main__":
    #第一步：读入图像
    I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    cv2.imshow("I",I)
    #第二步：取对数
    lI = np.log(I+1.0)
    lI = lI.astype(np.float32)
    #第三步：每一元素乘以 (-1)^(r+c)
    fI = np.copy(lI)
    for r in range(I.shape[0]):
        for c in range(I.shape[1]):
            if (r+c)%2:
                fI[r][c] = -1*fI[r][c]
    #第四、五步：补零和快速傅里叶变换
    fft2 = fft2Image(fI)
    #第六步：构造高频增强滤波器（ high-emphasis Filter）
    #找到傅里叶谱中的最大值的位置
    amplitude = amplitudeSpectrum(fft2)
    minValue,maxValue,minLoc,maxLoc = cv2.minMaxLoc(amplitude)
    #滤波器的高和宽
    rows,cols = fft2.shape[:2]
    r,c = np.mgrid[0:rows:1,0:cols:1]
    c-=maxLoc[0]
    r-=maxLoc[1]
    d = np.power(c,2.0)+np.power(r,2.0)
    high,low,k,radius = 2.5,0.5,1,300
    heFilter =(high-low)*(1-np.exp(-k*d/(2.0*pow(radius,2.0))))+low
    #第七步：快速傅里叶变换与高频增强滤波器的点乘
    fft2Filter = np.zeros(fft2.shape,fft2.dtype)
    for i in range(2):
        fft2Filter[:rows,:cols,i] = fft2[:rows,:cols,i]*heFilter
    #第八、九步：高频增强傅里叶变换执行傅里叶逆变换,并只取实部
    ifft2 = cv2.dft(fft2Filter,flags=cv2.DFT_REAL_OUTPUT+cv2.DFT_INVERSE+cv2.DFT_SCALE)
    #第十步：裁剪，和输入图像的尺寸一样
    ifI = np.copy(ifft2[:I.shape[0],:I.shape[1]])
    #第十一步：每一元素乘以 (-1)^(r+c)
    for i in range(ifI.shape[0]):
        for j in range(ifI.shape[1]):
            if (i+j)%2:
                ifI[i][j] = -1*ifI[i][j]
    #第十二步：取指数
    eifI = np.exp(ifI)-1
    #第十三步：归一化，并进行数据类型转换
    eifI = (eifI-np.min(eifI))/(np.max(eifI)-np.min(eifI))
    eifI = 255*eifI
    eifI = eifI.astype(np.uint8)
    cv2.imshow("homomorphicFilter",eifI)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("將一彩圖做RGB分離")

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'

image = cv2.imread(filename,cv2.IMREAD_COLOR)

#得到三个颜色通道
b = image[:,:,0]
g = image[:,:,1]
r = image[:,:,2]

#显示三个颜色通道
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)

#8位图转换为 浮点型
fImg = image/255.0
fb = fImg[:,:,0]
fg = fImg[:,:,1]
fr = fImg[:,:,2]

#显示三个颜色
cv2.imshow("f B",fb)
cv2.imshow("f G",fg)
cv2.imshow("f R",fr)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#HLS.py

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'

image = cv2.imread(filename,cv2.IMREAD_COLOR)

#显示原图
cv2.imshow("image",image)
#图像归一化，且转换为浮点型
fImg = image.astype(np.float32)
fImg = fImg/255.0
#颜色空间转换
hlsImg = cv2.cvtColor(fImg,cv2.COLOR_BGR2HLS)
l = 100 
s = 100
MAX_VALUE = 100
cv2.namedWindow("l and s",cv2.WINDOW_AUTOSIZE)

def nothing(*arg):
    pass

cv2.createTrackbar("l","l and s",l,MAX_VALUE,nothing)
cv2.createTrackbar("s","l and s",s,MAX_VALUE,nothing)
#调整饱和度和亮度后的效果
lsImg = np.zeros(image.shape,np.float32)
#调整饱和度和亮度

while True:
    #复制
    hlsCopy = np.copy(hlsImg)
    #得到 l 和 s 的值
    l = cv2.getTrackbarPos('l', 'l and s')
    s = cv2.getTrackbarPos('s', 'l and s')
    #调整亮度和饱和度（线性变换）
    hlsCopy[:,:,1] = (1.0+l/float(MAX_VALUE))*hlsCopy[:,:,1]
    hlsCopy[:,:,1][hlsCopy[:,:,1]>1] = 1
    hlsCopy[:,:,2] = (1.0+s/float(MAX_VALUE))*hlsCopy[:,:,2]
    hlsCopy[:,:,2][hlsCopy[:,:,2]>1] = 1
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsCopy,cv2.COLOR_HLS2BGR)
    #显示调整后的效果
    cv2.imshow("l and s",lsImg)
    #保存结果
    lsImg = lsImg*255
    lsImg = lsImg.astype(np.uint8)
    
    k = cv2.waitKey(5)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

