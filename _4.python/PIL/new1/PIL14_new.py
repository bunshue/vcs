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

from PIL import Image

print('------------------------------------------------------------')	#60個

plt.figure('影像處理1', figsize = (10, 6))

pil_im = Image.open('house.jpg')
plt.gray()

plt.subplot(121)
plt.title(u'原图')
plt.axis('off')
plt.imshow(pil_im)

pil_im = Image.open('house.jpg').convert('L')

plt.subplot(122)
plt.title(u'灰度图')
plt.axis('off')
plt.imshow(pil_im)

plt.show()

print('------------------------------------------------------------')	#60個

print("PIL_hist")

from pylab import *

# 打开图像，并转成灰度图像
im = array(Image.open('house2.jpg').convert('L'))

# 新建一个图像
figure()
subplot(121)
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')
title(u'图像轮廓图')

subplot(122)
# 利用hist来绘制直方图
# 第一个参数为一个一维数组
# 因为hist只接受一维数组作为输入，所以要用flatten()方法将任意数组按照行优先准则转化成一个一维数组
# 第二个参数指定bin的个数
hist(im.flatten(), 128)
title(u'图像直方图')
#刻度
plt.xlim([0,250])
plt.ylim([0,12000])

show()

print("------------------------------------------------------------")  # 60個

print("PIL_histeq")

from pylab import *
from PCV.tools import imtools

# 添加中文字体支持
from matplotlib.font_manager import FontProperties

im = array(Image.open('house2.jpg').convert('L'))
# 打开图像，并转成灰度图像
im2, cdf = imtools.histeq(im)
figure()
subplot(2, 2, 1)
axis('off')
gray()
title(u'原始图像')
imshow(im)
subplot(2, 2, 2)
axis('off')
title(u'直方图均衡化后的图像')
imshow(im2)
subplot(2, 2, 3)
axis('off')
title(u'原始直方图')
hist(im.flatten(), 128, density=True)
subplot(2, 2, 4)
axis('off')
title(u'均衡化后的直方图')
hist(im2.flatten(), 128, density=True)

show()

print("------------------------------------------------------------")  # 60個

print("PIL_im")

print('------------------------------------------------------------')	#60個

#from numpy import *
from pylab import *

im=array(Image.open('house2.jpg').convert('L'))
print(int(im.min()),int(im.max()))

im2=255-im               #对图像进行反向处理
print('对图像进行反向处理:\n',int(im2.min()),int(im2.max())) #查看最大/最小元素

im3=(100.0/255)*im+100   #将图像像素值变换到100...200区间
print('将图像像素值变换到100...200区间:\n',int(im3.min()),int(im3.max()))

im4=255.0*(im/255.0)**2  #对像素值求平方后得到的图像
print('对像素值求平方后得到的图像:\n',int(im4.min()),int(im4.max()))

plt.figure('影像處理2', figsize = (10, 6))
gray()

subplot(131)
imshow(im2)
axis('off')
title(r'$f(x)=255-x$')

subplot(132)
imshow(im3)
axis('off')
title(r'$f(x)=\frac{100}{255}x+100$')

subplot(133)
imshow(im4)
axis('off')
title(r'$f(x)=255(\frac{x}{255})^2$')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_line")

from pylab import *

# 读取图像到数组中
im = array(Image.open('house2.jpg'))
figure()
# 绘制有坐标轴的
subplot(121)
imshow(im)
x = [100, 100, 200, 200]
y = [200, 400, 200, 400]
# 使用红色星状标记绘制点
plot(x, y, 'r*')
# 绘制连接两个点的线（默认为蓝色）
plot(x[:2], y[:2])
title(u'绘制house2.jpg')
# 不显示坐标轴的
subplot(122)
imshow(im)
x = [100, 100, 200, 200]
y = [200, 400, 200, 400]
plot(x, y, 'r*')
plot(x[:2], y[:2])
axis('off')
title(u'绘制house2.jpg')

# show()命令首先打开图形用户界面（GUI），然后新建一个窗口，该图形用户界面会循环阻断脚本，然后暂停，
# 直到最后一个图像窗口关闭。每个脚本里，只能调用一次show()命令，通常相似脚本的结尾调用。
show()

print("------------------------------------------------------------")  # 60個

print("PIL_mean")

from PIL import ImageStat

def darkchannel(input_img,h,w):
    dark_img=Image.new("L",(h,w),0)
    for x in range(0,h-1):
        for y in range(0,w-1):
            dark_img.putpixel((x,y),min(input_img.getpixel((x,y))))
    return dark_img
  
def airlight(input_img,h,w):
    nMinDistance=65536    
    w=int(round(w/2))
    h=int(round(h/2))
    if h*w>200:
        lu_box = (0, 0, w, h) 
        ru_box = (w, 0, 2*w, h) 
        lb_box = (0, h, w, 2*h) 
        rb_box = (w, h, 2*h,2*w)  
               
        lu = input_img.crop(lu_box);
        ru = input_img.crop(ru_box);
        lb = input_img.crop(lb_box);
        rb = input_img.crop(rb_box);
        lu_m=ImageStat.Stat(lu)
        ru_m=ImageStat.Stat(ru)
        lb_m=ImageStat.Stat(lb)
        rb_m=ImageStat.Stat(rb)
        lu_mean = lu_m.mean
        ru_mean = ru_m.mean
        lb_mean = lb_m.mean
        rb_mean = rb_m.mean
        lu_stddev = lu_m.stddev
        ru_stddev = ru_m.stddev
        lb_stddev = lb_m.stddev
        rb_stddev = rb_m.stddev 
        score0 = lu_mean[0]+lu_mean[1]+lu_mean[2] - lu_stddev[0]-lu_stddev[1]-lu_stddev[2]
        score1 = ru_mean[0]+ru_mean[1]+lu_mean[2] - ru_stddev[0]-ru_stddev[1]-ru_stddev[2]  
        score2 = lb_mean[0]+lb_mean[1]+lb_mean[2] - lb_stddev[0]-lb_stddev[1]-lb_stddev[2]
        score3 = rb_mean[0]+rb_mean[1]+rb_mean[2] - rb_stddev[0]-rb_stddev[1]-rb_stddev[2]
        x =max(score0,score1,score2,score3)       
        if x == score0:
             air =airlight(lu,h,w)
        if x == score1:
             air =airlight(ru,h,w)
        if x == score2:
             air =airlight(lb,h,w)
        if x == score3:
             air =airlight(rb,h,w)
    else:
        for i in range(0,h-1):
            for j in range(0,w-1):
                temp=input_img.getpixel((i,j))            
                distance = ((255 - temp[0])**2 +  (255 - temp[1])**2 + (255 - temp[2])**2)**0.5
                if nMinDistance > distance:
                    nMinDistance = distance;
                    air = temp
    return air

def transmssion(air,dark_img,h,w,OMIGA):
    trans_map=np.zeros((h,w))
    A=max(air)
    for i in range(0,h-1):
        for j in range(0,w-1):
            temp=1-OMIGA*dark_img.getpixel((i,j))/A
            trans_map[i,j]=max(0.1,temp)  
    for i in range(1,h-1):
        for j in range(1,w-1):
                tempup=(trans_map[i-1][j-1]+2*trans_map[i][j-1]+trans_map[i+1][j-1])
                tempmid=2*(trans_map[i-1][j]+2*trans_map[i][j]+trans_map[i+1][j])
                tempdown=(trans_map[i-1][j+1]+2*trans_map[i][j+1]+trans_map[i+1][j+1])
                trans_map[i,j]=(tempup+tempmid+tempdown)/16
    return trans_map
                   
def defog(img,t_map,air,h,w):
    dehaze_img=Image.new("RGB",(h,w),0)
    for i in range(0,h-1):
        for j in range(0,w-1):
            R,G,B=img.getpixel((i,j))
            R=int((R-air[0])/t_map[i,j]+air[0])
            G=int((G-air[1])/t_map[i,j]+air[1])
            B=int((B-air[2])/t_map[i,j]+air[2])
            dehaze_img.putpixel((i,j),(R,G,B)) 
    return dehaze_img                       
                    
if __name__== '__main__':
    img=Image.open("castle1.jpg")
    [h,w]=img.size
    OMIGA =0.8  
    dark_image=darkchannel(img,h,w)
    air=airlight(img,h,w)
    T_map=transmssion(air,dark_image,h,w,OMIGA)
    fogfree_img=defog(img,T_map,air,h,w)       
    fogfree_img.show()  

print("------------------------------------------------------------")  # 60個

print("PIL_opening")

from numpy import *
#measurements模块实现二值图像的计数和度量功能，morphology模块实现形态学操作
from scipy.ndimage import measurements, morphology  
from pylab import *

# 加载图像和阈值，以确保它是二进制的
figure()
gray()
im = array(Image.open('castle3.jpg').convert('L'))
subplot(221)
imshow(im)
axis('off')
title(u'原图')
im = (im < 128)
labels, nbr_objects = measurements.label(im) #图像的灰度值表示对象的标签
print ("Number of objects:", nbr_objects)
subplot(222)
imshow(labels)
axis('off')
title(u'标记后的图')
#形态学——使物体分离更好
im_open = morphology.binary_opening(im, ones((9, 5)), iterations=4) #开操作，第二个参数为结构元素，iterations觉定执行该操作的次数
subplot(223)
imshow(im_open)
axis('off')
title(u'开运算后的图像')
labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)
subplot(224)
imshow(labels_open)
axis('off')
title(u'开运算后进行标记后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_operation")

from pylab import *


figure()
# 显示原图
pil_im = Image.open('house.jpg')
print(pil_im.mode, pil_im.size, pil_im.format)
subplot(231)
title(u'原图')
axis('off')
imshow(pil_im)
# 显示灰度图
pil_im = Image.open('house.jpg').convert('L')
gray()
subplot(232)
title(u'灰度图')
axis('off')
imshow(pil_im)
# 复制并粘贴区域
pil_im = Image.open('house.jpg')
box = (100, 100, 400, 400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)
subplot(233)
title(u'复制粘贴区域')
axis('off')
imshow(pil_im)

# 缩略图
pil_im = Image.open('house.jpg')
size = 128, 128
pil_im.thumbnail(size)
print(pil_im.size)
subplot(234)
title(u'缩略图')
axis('off')
imshow(pil_im)
pil_im.save('house.jpg')# 保存缩略图

#调整图像尺寸
pil_im=Image.open('house.jpg')
pil_im=pil_im.resize(size)
print(pil_im.size)
subplot(235)
title(u'调整尺寸后的图像')
axis('off')
imshow(pil_im)

#旋转图像45°
pil_im=Image.open('house.jpg')
pil_im=pil_im.rotate(45)
subplot(236)
title(u'旋转45°后的图像')
axis('off')
imshow(pil_im)

show()

print("------------------------------------------------------------")  # 60個

print("PIL_PCA")

from numpy import *
#measurements模块实现二值图像的计数和度量功能，morphology模块实现形态学操作
from scipy.ndimage import measurements, morphology  
from pylab import *

# 加载图像和阈值，以确保它是二进制的
figure()
gray()
im = array(Image.open('castle3.jpg').convert('L'))
subplot(221)
imshow(im)
axis('off')
title(u'原图')
im = (im < 128)
labels, nbr_objects = measurements.label(im) #图像的灰度值表示对象的标签
print ("Number of objects:", nbr_objects)
subplot(222)
imshow(labels)
axis('off')
title(u'标记后的图')
#形态学——使物体分离更好
im_open = morphology.binary_opening(im, ones((9, 5)), iterations=4) #开操作，第二个参数为结构元素，iterations觉定执行该操作的次数
subplot(223)
imshow(im_open)
axis('off')
title(u'开运算后的图像')
labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)
subplot(224)
imshow(labels_open)
axis('off')
title(u'开运算后进行标记后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_realROF")

from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
from scipy.misc import imsave
from PCV.tools import rof

im = array(Image.open('gril.jpg').convert('L'))
U,T = rof.denoise(im,im)
G = filters.gaussian_filter(im,10)
figure()
gray()
subplot(1,3,1)
imshow(im)
#axis('equal')
axis('off')
title(u'原噪声图像')
subplot(1,3,2)
imshow(G)
#axis('equal')
axis('off')
title(u'高斯模糊后的图像')
subplot(1,3,3)
imshow(U)
#axis('equal')
axis('off')
title(u'ROF降噪后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_ROF")

from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
from scipy.misc import imsave
from PCV.tools import rof

# 创建合成图像与噪声
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im + 30*random.standard_normal((500,500))
#roll()函数：循环滚动数组中的元素，计算领域元素的差异。linalg.norm()函数可以衡量两个数组见得差异
U,T = rof.denoise(im,im)  
G = filters.gaussian_filter(im,10)
figure()
gray()
subplot(1,3,1)
imshow(im)
#axis('equal')
axis('off')
title(u'原噪声图像')

subplot(1,3,2)
imshow(G)
#axis('equal')
axis('off')
title(u'高斯模糊后的图像')

subplot(1,3,3)
imshow(U)
#axis('equal')
axis('off')
title(u'ROF降噪后的图像')

show()

print("------------------------------------------------------------")  # 60個

print("PIL_save")

def IsValidImage(img_path):
    """
    判断文件是否为有效（完整）的图片
    :param img_path:图片路径
    :return:True：有效 False：无效
    """
    bValid = True
    try:
        Image.open(img_path).verify()
    except:
        bValid = False
    return bValid


def transimg(img_path):
    """
    转换图片格式
    :param img_path:图片路径
    :return: True：成功 False：失败
    """
    if IsValidImage(img_path):
        try:
            str = img_path.rsplit(".", 1)
            output_img_path = str[0] + ".jpg"
            print(output_img_path)
            im = Image.open(img_path)
            im.save(output_img_path)
            return True
        except:
            return False
    else:
        return False


if __name__ == '__main__':
    img_path = 'lena.png'
    print(transimg(img_path))

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print("de_noise")

import random
import cv2
import scipy.misc
import scipy.signal
import scipy.ndimage

"""中值滤波函数"""
def medium_filter(im, x, y, step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return sum_s[(int(step*step/2)+1)]
"""均值滤波函数"""
def mean_filter(im, x, y, step):
    sum_s = 0
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s += im[x+k][y+m] / (step*step)
    return sum_s

def convert_2d(r):
    n = 3
    # 3*3滤波器，每个系数都是1/9
    window = np.ones((n, n)) / n**2
    #使用滤波器卷积图像
    # mode = same 表示输出尺寸等于输入尺寸
    # boundary 表示采用对称边界条件处理图像边缘
    s = scipy.signal.convolve2d(r, window, mode='same', boundary='symm')
    return s.astype(np.uint8)
"""添加噪声"""
def add_salt_noise(img):
    rows, cols, dims = img.shape 
    R = np.mat(img[:, :, 0])
    G = np.mat(img[:, :, 1])
    B = np.mat(img[:, :, 2])
    Grey_sp = R * 0.299 + G * 0.587 + B * 0.114
    Grey_gs = R * 0.299 + G * 0.587 + B * 0.114
    snr = 0.9
    mu = 0
    sigma = 0.12    
    noise_num = int((1 - snr) * rows * cols)

    for i in range(noise_num):
        rand_x = random.randint(0, rows - 1)
        rand_y = random.randint(0, cols - 1)
        if random.randint(0, 1) == 0:
            Grey_sp[rand_x, rand_y] = 0
        else:
            Grey_sp[rand_x, rand_y] = 255    
    Grey_gs = Grey_gs + np.random.normal(0, 48, Grey_gs.shape)
    Grey_gs = Grey_gs - np.full(Grey_gs.shape, np.min(Grey_gs))
    Grey_gs = Grey_gs * 255 / np.max(Grey_gs)
    Grey_gs = Grey_gs.astype(np.uint8)
    # 中值滤波
    Grey_sp_mf = scipy.ndimage.median_filter(Grey_sp, (8, 8))
    Grey_gs_mf = scipy.ndimage.median_filter(Grey_gs, (8, 8))
    # 均值滤波
    n = 3
    window = np.ones((n, n)) / n ** 2
    Grey_sp_me = convert_2d(Grey_sp)
    Grey_gs_me = convert_2d(Grey_gs)
    plt.subplot(231)
    plt.title('椒盐噪声')
    plt.imshow(Grey_sp, cmap='gray')
    plt.subplot(232)
    plt.title('高斯噪声')
    plt.imshow(Grey_gs, cmap='gray')
    plt.subplot(233)
    plt.title('椒盐噪声的中值滤波')
    plt.imshow(Grey_sp_mf, cmap='gray')
    plt.subplot(234)
    plt.title('高斯噪声的中值滤波')
    plt.imshow(Grey_gs_mf, cmap='gray')
    plt.subplot(235)
    plt.title('椒盐噪声的均值滤波')
    plt.imshow(Grey_sp_me, cmap='gray')
    plt.subplot(236)
    plt.title('高斯噪声的均值滤波')
    plt.imshow(Grey_gs_me, cmap='gray')
    plt.show()

def main():
    img = np.array(Image.open('LenaRGB.bmp'))  #导入图片
    add_salt_noise(img)

if __name__ == '__main__':
    main()

print("------------------------------------------------------------")  # 60個

print("PIL_derivative")

from pylab import *
from scipy.ndimage import  filters
import numpy

im=array(Image.open('house2.jpg').convert('L'))
gray()
subplot(141)
axis('off')
title(u'(a)原图')
imshow(im)
# sobel算子
imx=zeros(im.shape)
filters.sobel(im,1,imx)
subplot(142)
axis('off')
title(u'(b)x方向差分')
imshow(imx)
imy=zeros(im.shape)
filters.sobel(im,0,imy)
subplot(143)
axis('off')
title(u'(c)y方向差分')
imshow(imy)
mag=255-numpy.sqrt(imx**2+imy**2)
subplot(144)
title(u'(d)梯度幅值')
axis('off')
imshow(mag)

show()

print("------------------------------------------------------------")  # 60個

print("PIL_fuzzy")

from numpy import *
from pylab import *
from scipy.ndimage import filters
from matplotlib.font_manager import FontProperties

im=array(Image.open('house2.jpg').convert('L'))
figure()
gray()
axis('off')
subplot(141)
axis('off')
title(u'原图')
imshow(im)
for bi,blur in enumerate([2,4,8]):
    im2=zeros(im.shape)
    im2=filters.gaussian_filter(im,blur)
    im2=np.uint8(im2)
    imNum=str(blur)
    subplot(1,4,2+bi)
    axis('off')
    title(u'标准差为'+imNum)
    imshow(im2)

#如果是彩色图像，则分别对三个通道进行模糊
#for bi, blur in enumerate([2,4,8]):
#  im2 = zeros(im.shape)
#  for i in range(3):
#    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], blur)
#  im2 = np.uint8(im2)
#  subplot(1, 4,  2 + bi)
#  axis('off')
#  imshow(im2)

show()

print("------------------------------------------------------------")  # 60個

print("PIL_gaussian")

from pylab import *
from scipy.ndimage import filters
import numpy

def imx(im, sigma):
    imgx = zeros(im.shape)
    filters.gaussian_filter(im, sigma, (0, 1), imgx)
    return imgx
def imy(im, sigma):
    imgy = zeros(im.shape)
    filters.gaussian_filter(im, sigma, (1, 0), imgy)
    return imgy
def mag(im, sigma):
    # 还有gaussian_gradient_magnitude()
    imgmag = 255 - numpy.sqrt(imgx ** 2 + imgy ** 2)
    return imgmag

im = array(Image.open('castle3.jpg').convert('L'))
figure()
gray()
sigma = [2, 5, 10]
for i in  sigma:
    subplot(3, 4, 4*(sigma.index(i))+1)
    axis('off')
    imshow(im)
    imgx=imx(im, i)
    subplot(3, 4, 4*(sigma.index(i))+2)
    axis('off')
    imshow(imgx)
    imgy=imy(im, i)
    subplot(3, 4, 4*(sigma.index(i))+3)
    axis('off')
    imshow(imgy)
    imgmag=mag(im, i)
    subplot(3, 4, 4*(sigma.index(i))+4)
    axis('off')
    imshow(imgmag)
show()

print("------------------------------------------------------------")  # 60個

print("PIL_ginput")

from pylab import *

im = array(Image.open('house2.jpg'))
imshow(im)

print('请点击3个点')
x = ginput(3)
print('你已点击:', x)
show()

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


