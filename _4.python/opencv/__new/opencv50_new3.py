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

print("absolute")

import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape,dtype=np.int64)
    #确定拉普拉斯模板的形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    #计算每个像素点在经过高斯模板变换后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #条件语句为判断模板对应的值是否超出边界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i+ii-1][j+jj-1] * my_model[ii][jj]
    return result
    
original_image_test1 = cv2.imread('data/lena.png',0)
def my_laplace_result_add_abs(image, model):
    for i in range(model.shape[0]):
        for j in range(model.shape[1]):
            if model[i][j] < 0:
                model[i][j] = 0
            if model[i][j] > 255:
                model[i][j] = 255
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

# 调用自定义函数
result = my_laplace_sharpen(original_image_test1, my_type='big')
# 绘制结果
fig = plt.figure()
fig.add_subplot(121)
plt.title('原始图像')
plt.imshow(original_image_test1)
fig.add_subplot(122)
plt.title('锐化滤波')
plt.imshow(my_laplace_result_add_abs(original_image_test1,result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("Canny1")

import matplotlib.pyplot as plt
import numpy as np  

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

original_img = cv2.imread("data/lena.png", 0)
#canny(): 边缘检测
img1 = cv2.GaussianBlur(original_img, (3, 3), 0)   #執行高斯模糊化
canny = cv2.Canny(img1, 50, 150)

#形态学：边缘检测
_,Thr_img = cv2.threshold(original_img,210,255,cv2.THRESH_BINARY)#设定红色通道阈值210（阈值影响梯度运算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))         #定义矩形结构元素
gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel) #梯度

plt.subplot(131)
cv2.imshow("原始图像", original_img) 

plt.subplot(132)
cv2.imshow("梯度", gradient) 

plt.subplot(133)
cv2.imshow('Canny函数', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("CannyThreshold")

import numpy as np
 
def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0) #執行高斯模糊化
    detected_edges = cv2.Canny(detected_edges,
                               lowThreshold,
                               lowThreshold*ratio,
                               apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # 只需在原始图像的边缘添加一些颜色
    cv2.imshow('canny demo', dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3 
img = cv2.imread('data/lena.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.namedWindow('canny demo') 
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
 
CannyThreshold(0)  # 初始化
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("createCLAHE_image")

import numpy as np

img = cv2.imread('data/building.png',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('img',img)
cv2.imshow('cl1',cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("defogging")

import numpy as np

def zmMinFilterGray(src, r=7):
    '''最小值滤波，r是滤波器半径'''
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))

def guidedfilter(I, p, r, eps):
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (r, r))
    m_p = cv2.boxFilter(p, -1, (r, r))
    m_Ip = cv2.boxFilter(I * p, -1, (r, r))
    cov_Ip = m_Ip - m_I * m_p
    m_II = cv2.boxFilter(I * I, -1, (r, r))
    var_I = m_II - m_I * m_I

    a = cov_Ip / (var_I + eps)
    b = m_p - a * m_I
    m_a = cv2.boxFilter(a, -1, (r, r))
    m_b = cv2.boxFilter(b, -1, (r, r))
    return m_a * I + m_b

def Defog(m, r, eps, w, maxV1):                 #输入rgb图像，值范围[0,1]
    '''计算大气遮罩图像V1和光照值A, V1 = 1-t/A'''
    V1 = np.min(m, 2)                           #得到暗通道图像
    Dark_Channel = zmMinFilterGray(V1, 5)
    cv2.imshow('wu_Dark',Dark_Channel)    #查看暗通道
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    V1 = guidedfilter(V1, Dark_Channel, r, eps)  #使用引导滤波优化
    bins = 2000
    ht = np.histogram(V1, bins)                  #计算大气光照A
    d = np.cumsum(ht[0]) / float(V1.size)
    for lmax in range(bins - 1, 0, -1):
        if d[lmax] <= 0.999:
            break
    A = np.mean(m, 2)[V1 >= ht[1][lmax]].max()
    V1 = np.minimum(V1 * w, maxV1)               #对值范围进行限制
    return V1, A

def deHaze(m, r=81, eps=0.001, w=0.95, maxV1=0.80, bGamma=False):
    Y = np.zeros(m.shape)
    Mask_img, A = Defog(m, r, eps, w, maxV1)             #得到遮罩图像和大气光照

    for k in range(3):
        Y[:,:,k] = (m[:,:,k] - Mask_img)/(1-Mask_img/A)  #颜色校正
    Y = np.clip(Y, 0, 1)
    if bGamma:
        Y = Y ** (np.log(0.5) / np.log(Y.mean()))       #gamma校正,默认不进行该操作
    return Y

m = deHaze(cv2.imread('data/wu.jpg') / 255.0) * 255
cv2.imwrite('tmp_wu_2.png', m)

print("------------------------------------------------------------")  # 60個

print("equalizeHist_image")

import numpy as np

img = cv2.imread('data/wu_2.png',0)
equ = cv2.equalizeHist(img) #只能传入灰度图
res = np.hstack((img,equ))  #图像列拼接（用于显示）

cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("gaussion")

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

print('跑很久')

#高斯滤波函数
def my_function_gaussion(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2*sigma**2)) / (2*math.pi*sigma**2)

#产生高斯滤波矩阵
def my_get_gaussion_blur_retric(size, sigma):
    n = size // 2
    blur_retric = np.zeros([size, size])
    #根据尺寸和sigma值计算高斯矩阵
    for i in range(size):
        for j in range(size):
            blur_retric[i][j] = my_function_gaussion(i-n, j-n, sigma)
    #将高斯矩阵归一化
    blur_retric = blur_retric / blur_retric[0][0]
    #将高斯矩阵转换为整数
    blur_retric = blur_retric.astype(np.uint32)
    #返回高斯矩阵
    return blur_retric

#计算灰度图像的高斯滤波
def my_gaussion_blur_gray(image, size, sigma):
    blur_retric = my_get_gaussion_blur_retric(size, sigma)
    n = blur_retric.sum()
    sizepart = size // 2
    data = 0
    #计算每个像素点在经过高斯模板变换后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #条件语句为判断模板对应的值是否超出边界
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data += image[i+ii-sizepart][j+jj-sizepart] * blur_retric[ii][jj]
            image[i][j] = data / n
            data = 0
    #返回变换后的图像矩阵
    return image

#计算彩色图像的高斯滤波
def my_gaussion_blur_RGB(image, size, sigma):
    (b ,r, g) = cv2.split(image)
    blur_b = my_gaussion_blur_gray(b, size, sigma)
    blur_r = my_gaussion_blur_gray(r, size, sigma)
    blur_g = my_gaussion_blur_gray(g, size, sigma)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result

image_test1 = cv2.imread('data/lena.png')
#进行高斯滤波器比较
my_image_blur_gaussion = my_gaussion_blur_RGB(image_test1, 5, 0.75)
computer_image_blur_gaussion = cv2.GaussianBlur(image_test1, (5, 5), 0.75)  #執行高斯模糊化

fig = plt.figure(figsize = (20, 15))

fig.add_subplot(131)
plt.title('原始图像')
plt.imshow(image_test1)

fig.add_subplot(132)
plt.title('自定义高斯滤波器')
plt.imshow(my_image_blur_gaussion)

fig.add_subplot(133)
plt.title('库高斯滤波器')
plt.imshow(computer_image_blur_gaussion)

plt.show()

print("------------------------------------------------------------")  # 60個

print("gradient")

import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

# 输入图像，输出提取的边缘信息
def my_sobel_sharpen(image):
    result_x = np.zeros(image.shape,dtype=np.int64)
    result_y = np.zeros(image.shape, dtype=np.int64)
    result = np.zeros(image.shape, dtype=np.int64)
    # 确定拉普拉斯模板的形式
    my_model_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    my_model_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # 计算每个像素点在经过高斯模板变换后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    # 条件语句为判断模板对应的值是否超出边界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result_x[i][j] += image[i+ii-1][j+jj-1] * my_model_x[ii][jj]
                        result_y[i][j] += image[i+ii-1][j+jj-1] * my_model_y[ii][jj]
            result[i][j] = abs(result_x[i][j]) + abs(result_y[i][j])
            if result[i][j] > 255:
                result[i][j] = 255
    return result


# 将边缘信息按一定比例加到原始图像上
def my_result_add(image, model, k):
    result = image + k * model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result



original_image_lena= cv2.imread('data/lena.png', 0)

# 获得图像边界信息
edge_image_lena = my_sobel_sharpen(original_image_lena)

# 获得锐化图像
sharpen_image_lena = my_result_add(original_image_lena, edge_image_lena, -0.5)

# 显示结果
plt.subplot(131)
plt.title('原始图像')
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title('边缘检测')
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title('梯度处理')
plt.imshow(sharpen_image_lena)

plt.show()


print("------------------------------------------------------------")  # 60個

print("imaeg_laplace")

import matplotlib.pyplot as plt
import math
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

original_image_test1 = cv2.imread('data/lena.png',0)
#用原始图像减去拉普拉斯模板直接计算得到的边缘信息
def my_laplace_result_add(image, model):
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape,dtype=np.int64)
    #确定拉普拉斯模板的形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    #计算每个像素点在经过高斯模板变换后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #条件语句为判断模板对应的值是否超出边界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i+ii-1][j+jj-1] * my_model[ii][jj]
    return result

#将计算结果限制为正值
def my_show_edge(model):
    #这里一定要用copy函数，不然会改变原来数组的值
    mid_model = model.copy()
    for i in range(mid_model.shape[0]):
        for j in range(mid_model.shape[1]):
            if mid_model[i][j] < 0:
                mid_model[i][j] = 0
            if mid_model[i][j] > 255:
                mid_model[i][j] = 255
    return mid_model

#调用自定义函数
result = my_laplace_sharpen(original_image_test1, my_type='big')
#绘制结果
fig = plt.figure()
fig.add_subplot(131)
plt.title('原始图像')
plt.imshow(original_image_test1)
fig.add_subplot(132)
plt.title('边缘检测')
plt.imshow(my_show_edge(result))
fig.add_subplot(133)
plt.title('锐化处理')
plt.imshow(my_laplace_result_add(original_image_test1,result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_cv2")

from matplotlib import pyplot as plt

# 用原始图像减去拉普拉斯模板直接计算得到的边缘信息
def my_laplace_result_add(image, model):
    result = image-model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

original_image_test1 = cv2.imread('data/lena.png',0)
# 函数中的参数ddepth为输出图像的深度，也就是每个像素点是多少位的。
# CV_16S表示16位有符号数
computer_result = cv2.Laplacian(original_image_test1,ksize=3,ddepth=cv2.CV_16S)
plt.imshow(my_laplace_result_add(original_image_test1, computer_result))

plt.show()

print("------------------------------------------------------------")  # 60個

print("image_dft2")

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


print("------------------------------------------------------------")  # 60個

print("image_fft")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pylab import mpl

#mpl.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
#mpl.rcParams['axes.unicode_minus']=False       #显示负号

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

Fs=1200;  #采样频率
Ts=1/Fs;  #采样区间
x=np.arange(0,1,Ts)  #时间向量，1200个
y=5*np.sin(2*np.pi*600*x)
N=1200
frq=np.arange(N)            #频率数1200个数
half_x=frq[range(int(N/2))]  #取一半区间
fft_y=np.fft.fft(y)
abs_y=np.abs(fft_y)                #取复数的绝对值，即复数的模(双边频谱)
angle_y=180*np.angle(fft_y)/np.pi   #取复数的弧度,并换算成角度
gui_y=abs_y/N                       #归一化处理（双边频谱）                              
gui_half_y = gui_y[range(int(N/2))] #由于对称性，只取一半区间（单边频谱）
#画出原始波形的前50个点
plt.subplot(231)
plt.plot(frq[0:50],y[0:50])   
plt.title('原始波形')
#画出双边未求绝对值的振幅谱
plt.subplot(232)
plt.plot(frq,fft_y,'black')
plt.title('双边振幅谱(未求振幅绝对值)') 
#画出双边求绝对值的振幅谱
plt.subplot(233)
plt.plot(frq,abs_y,'r')
plt.title('双边振幅谱(未归一化)') 
#画出双边相位谱
plt.subplot(234)
plt.plot(frq[0:50],angle_y[0:50],'violet')
plt.title('双边相位谱(未归一化)')
#画出双边振幅谱(归一化)
plt.subplot(235)
plt.plot(frq,gui_y,'g')
plt.title('双边振幅谱(归一化)')

#画出单边振幅谱(归一化)
plt.subplot(236)
plt.plot(half_x,gui_half_y,'blue')
plt.title('单边振幅谱(归一化)')
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_ftt2")

import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

img = plt.imread('data/castle3.jpg')

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

print("------------------------------------------------------------")  # 60個

print("magnitude_spectrum")

import numpy as np
import matplotlib.pyplot as plt

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

print("------------------------------------------------------------")  # 60個

print("median")

import matplotlib.pyplot as plt
import math
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def get_median(data):
    data.sort()
    half = len(data) // 2
    return data[half]

#计算灰度图像的中值滤波
def my_median_blur_gray(image, size):
    data = []
    sizepart = int(size/2)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #首先判断所以是否超出范围，也可以事先对图像进行零填充
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data.append(image[i+ii-sizepart][j+jj-sizepart])
            #取每个区域内的中位数
            image[i][j] = int(get_median(data))
            data=[]
    return image

#计算彩色图像的中值滤波
def my_median_blur_RGB(image, size):
    (b ,r, g) = cv2.split(image)
    blur_b = my_median_blur_gray(b, size)
    blur_r = my_median_blur_gray(r, size)
    blur_g = my_median_blur_gray(g, size)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result

if __name__ == '__main__':
    image_test1 = cv2.imread('data/worm.jpg')
    #调用自定义函数
    my_image_blur_median = my_median_blur_RGB(image_test1, 5)
    #调用库函数
    computer_image_blur_median = cv2.medianBlur(image_test1, 5)
    fig = plt.figure()
    fig.add_subplot(131)
    plt.title('原图')
    plt.imshow(image_test1)
    fig.add_subplot(132)
    plt.title('自定义函数滤波')
    plt.imshow(my_image_blur_median)
    fig.add_subplot(133)
    plt.title('库函数滤波')
    plt.imshow(computer_image_blur_median)
    plt.show()

print("------------------------------------------------------------")  # 60個

print("optimize")

import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

def ComputeMinLevel(hist, pnum):
    index = np.add.accumulate(hist)
    return np.argwhere(index>pnum * 8.3 * 0.01)[0][0]

def ComputeMaxLevel(hist, pnum):
    hist_0 = hist[::-1]
    Iter_sum = np.add.accumulate(hist_0)
    index = np.argwhere(Iter_sum > (pnum * 2.2 * 0.01))[0][0]
    return 255-index

def LinearMap(minlevel, maxlevel):
    if (minlevel >= maxlevel):
        return []
    else:
        index = np.array(list(range(256)))
        screenNum = np.where(index<minlevel,0,index)
        screenNum = np.where(screenNum> maxlevel,255,screenNum)
        for i in range(len(screenNum)):
            if screenNum[i]> 0 and screenNum[i] < 255:
                screenNum[i] = (i - minlevel) / (maxlevel - minlevel) * 255
        return screenNum

def CreateNewImg(img):
    h, w, d = img.shape
    newimg = np.zeros([h, w, d])
    for i in range(d):
        imghist = np.bincount(img[:, :, i].reshape(1, -1)[0])
        minlevel = ComputeMinLevel(imghist,  h * w)
        maxlevel = ComputeMaxLevel(imghist, h * w)
        screenNum = LinearMap(minlevel, maxlevel)
        if (screenNum.size == 0):
            continue
        for j in range(h):
            newimg[j, :, i] = screenNum[img[j, :, i]]
    return newimg

img = cv2.imread('data/building.png')
newimg = CreateNewImg(img)
cv2.imshow('原始图像', img)
cv2.imshow('去雾后图像', newimg / 255)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("sharpening")

import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

# 图像锐化函数
def my_not_sharpen(image, k, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  #執行高斯模糊化
    # 注意不能直接用减法，对于图像格式结果为负时会自动加上256
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    # 两个矩阵中有一个不是图像格式，则结果就不会转换为图像格式
    sharpen_image = image + k * model   
    sharpen_image = cv2.convertScaleAbs(sharpen_image)
    return sharpen_image

# 提取图像边界信息函数
def my_get_model(image, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  #執行高斯模糊化
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    model = cv2.convertScaleAbs(model)
    return model

original_image_lena = cv2.imread('data/lena.png', 0)

# 获得图像边界信息
edge_image_lena = my_get_model(original_image_lena)

# 获得锐化图像
sharpen_image_lena = my_not_sharpen(original_image_lena, 3)

# 显示结果
plt.subplot(131)
plt.title('原始图像')
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title('边缘检测')
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title('非锐化')
plt.imshow(sharpen_image_lena)
plt.show()

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


