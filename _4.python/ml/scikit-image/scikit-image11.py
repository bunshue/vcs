"""
scikit-image


"""

"""
圖像中的像素訪問

前面的一些例子中，我們都是利用Image.open()來打開一幅圖像，
然後直接對這個PIL對象進行操作。
如果只是簡單的操作還可以，但是如果操作稍微復雜一些，就比較吃力了。
因此，通常我們加載完圖片後，都是把圖片轉換成矩陣來進行更加復雜的操作。

python中利用numpy庫和scipy庫來進行各種數據操作和科學計算。
我們可以通過pip來直接安裝這兩個庫

pip install numpy
pip install scipy

"""

print('------------------------------------------------------------')	#60個

from PIL import Image
from PIL import ImageFilter

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

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

print("------------------------------------------------------------")  # 60個

from scipy.ndimage import gaussian_filter



print('------------------------------------------------------------')	#60個

print("de-noise")

import scipy.misc
import scipy.signal
import scipy.ndimage

#中值濾波函數
def medium_filter(im, x, y, step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return sum_s[(int(step*step/2)+1)]
#均值濾波函數
def mean_filter(im, x, y, step):
    sum_s = 0
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s += im[x+k][y+m] / (step*step)
    return sum_s

def convert_2d(r):
    n = 3
    # 3*3濾波器，每個系數都是1/9
    window = np.ones((n, n)) / n**2
    #使用濾波器卷積圖像
    # mode = same 表示輸出尺寸等于輸入尺寸
    # boundary 表示采用對稱邊界條件處理圖像邊緣
    s = scipy.signal.convolve2d(r, window, mode='same', boundary='symm')
    return s.astype(np.uint8)
#添加噪聲
def add_salt_noise(image):
    rows, cols, dims = image.shape 
    R = np.mat(image[:, :, 0])
    G = np.mat(image[:, :, 1])
    B = np.mat(image[:, :, 2])
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
    
    # 中值濾波
    Grey_sp_mf = scipy.ndimage.median_filter(Grey_sp, (8, 8))
    Grey_gs_mf = scipy.ndimage.median_filter(Grey_gs, (8, 8))
    
    # 均值濾波
    n = 3
    window = np.ones((n, n)) / n ** 2
    Grey_sp_me = convert_2d(Grey_sp)
    Grey_gs_me = convert_2d(Grey_gs)

    plt.subplot(231)
    plt.title('椒鹽噪聲')
    plt.imshow(Grey_sp, cmap='gray')

    plt.subplot(232)
    plt.title('高斯噪聲')
    plt.imshow(Grey_gs, cmap='gray')

    plt.subplot(233)
    plt.title('椒鹽噪聲的中值濾波')
    plt.imshow(Grey_sp_mf, cmap='gray')

    plt.subplot(234)
    plt.title('高斯噪聲的中值濾波')
    plt.imshow(Grey_gs_mf, cmap='gray')

    plt.subplot(235)
    plt.title('椒鹽噪聲的均值濾波')
    plt.imshow(Grey_sp_me, cmap='gray')

    plt.subplot(236)
    plt.title('高斯噪聲的均值濾波')
    plt.imshow(Grey_gs_me, cmap='gray')

    plt.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'

plt.figure(
    num="影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => PIL影像 => numpy陣列
image = np.array(Image.open(filename))
add_salt_noise(image)

print("------------------------------------------------------------")  # 60個

print("PIL_derivative")

import scipy.ndimage

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像 => 灰階 => numpy陣列
image=np.array(Image.open(filename).convert('L'))

plt.figure(
    num="PIL_derivative",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(141)
plt.title(u'(a)原圖')
plt.imshow(image)
# sobel算子
imagex=np.zeros(image.shape)
scipy.ndimage.sobel(image,1,imagex)

plt.subplot(142)
plt.title(u'(b)x方向差分')
plt.imshow(imagex)
imagey=np.zeros(image.shape)
scipy.ndimage.sobel(image,0,imagey)

plt.subplot(143)
plt.title(u'(c)y方向差分')
plt.imshow(imagey)
mag=255-np.sqrt(imagex**2+imagey**2)

plt.subplot(144)
plt.title(u'(d)梯度幅值')
plt.imshow(mag)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_fuzzy")

import scipy.ndimage
from matplotlib.font_manager import FontProperties

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像 => 灰階 => numpy陣列
image=np.array(Image.open(filename).convert('L'))

plt.figure(
    num="PIL_fuzzy",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(141)
plt.title(u'原圖')
plt.imshow(image)

for bi,blur in enumerate([2,4,8]):
    image2=np.zeros(image.shape)
    image2=scipy.ndimage.gaussian_filter(image,blur)
    image2=np.uint8(image2)
    imageNum=str(blur)
    plt.subplot(1,4,2+bi)
    plt.title(u'標準差為'+imageNum)
    plt.imshow(image2)

#如果是彩色圖像，則分別對三個通道進行模糊
#for bi, blur in enumerate([2,4,8]):
#  image2 = np.zeros(image.shape)
#  for i in range(3):
#    image2[:, :, i] = filters.gaussian_filter(image[:, :, i], blur)
#  image2 = np.uint8(image2)
#  plt.subplot(1, 4,  2 + bi)
#  plt.imshow(image2)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_gaussian")

import scipy.ndimage

def imx(image, sigma):
    imagex = np.zeros(image.shape)
    scipy.ndimage.gaussian_filter(image, sigma, (0, 1), imagex)
    return imagex
def imy(image, sigma):
    imagey = np.zeros(image.shape)
    scipy.ndimage.gaussian_filter(image, sigma, (1, 0), imagey)
    return imagey
def mag(image, sigma):
    # 還有gaussian_gradient_magnitude()
    imagemag = 255 - np.sqrt(imagex ** 2 + imagey ** 2)
    return imagemag

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open(filename).convert('L'))

plt.figure(
    num="PIL_gaussian",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
sigma = [2, 5, 10]
for i in  sigma:
    plt.subplot(3, 4, 4*(sigma.index(i))+1)
    plt.imshow(image)
    imagex=imx(image, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+2)
    plt.imshow(imagex)
    imagey=imy(image, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+3)
    plt.imshow(imagey)
    imagemag=mag(image, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+4)
    plt.imshow(imagemag)

plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個

print("PIL_opening")

#measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
import scipy.ndimage

# 加載圖像和閾值，以確保它是二進制的

plt.figure(
    num="PIL_opening",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open('data/castle.jpg').convert('L'))

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(221)
plt.imshow(image)
plt.title(u'原圖')
image = (image < 128)
labels, nbr_objects = scipy.ndimage.label(image) #圖像的灰度值表示對象的標簽
print ("Number of objects:", nbr_objects)

plt.subplot(222)
plt.imshow(labels)
plt.title(u'標記後的圖')
#形態學——使物體分離更好
image_open = scipy.ndimage.binary_opening(image, np.ones((9, 5)), iterations=4) #開操作，第二個參數為結構元素，iterations覺定執行該操作的次數

plt.subplot(223)
plt.imshow(image_open)
plt.title(u'開運算後的圖像')
labels_open, nbr_objects_open = scipy.ndimage.label(image_open)
print ("Number of objects:", nbr_objects_open)

plt.subplot(224)
plt.imshow(labels_open)
plt.title(u'開運算後進行標記後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_PCA")

#measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
import scipy.ndimage

# 加載圖像和閾值，以確保它是二進制的
# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open('data/castle.jpg').convert('L'))

plt.figure(
    num="PIL_PCA",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(221)
plt.imshow(image)
plt.title(u'原圖')
image = (image < 128)
labels, nbr_objects = scipy.ndimage.label(image) #圖像的灰度值表示對象的標簽
print ("Number of objects:", nbr_objects)

plt.subplot(222)
plt.imshow(labels)
plt.title(u'標記後的圖')
#形態學——使物體分離更好
image_open = scipy.ndimage.binary_opening(image, np.ones((9, 5)), iterations=4) #開操作，第二個參數為結構元素，iterations覺定執行該操作的次數

plt.subplot(223)
plt.imshow(image_open)
plt.title(u'開運算後的圖像')
labels_open, nbr_objects_open = scipy.ndimage.label(image_open)
print ("Number of objects:", nbr_objects_open)

plt.subplot(224)
plt.imshow(labels_open)
plt.title(u'開運算後進行標記後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_realROF")

import scipy.ndimage
#from scipy.misc import imsave
#from PCV.tools import rof

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open('data/gril.jpg').convert('L'))

#U,T = rof.denoise(image,image)
G = scipy.ndimage.gaussian_filter(image,10)

plt.figure(
    num="PIL_realROF",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(1,3,1)
plt.imshow(image)
#plt.axis('equal')
plt.title(u'原噪聲圖像')

plt.subplot(1,3,2)
plt.imshow(G)
#plt.axis('equal')
plt.title(u'高斯模糊後的圖像')

plt.subplot(1,3,3)
#plt.imshow(U)
#plt.axis('equal')
plt.title(u'ROF降噪後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_ROF")

import scipy.ndimage
#from scipy.misc import imsave
#from PCV.tools import rof

# 創建合成圖像與噪聲
image = np.zeros((500,500))
image[100:400,100:400] = 128
image[200:300,200:300] = 255
image = image + 30*np.random.standard_normal((500,500))
#roll()函數：循環滾動數組中的元素，計算領域元素的差異。linalg.norm()函數可以衡量兩個數組見得差異
#U,T = rof.denoise(image,image)  
G = scipy.ndimage.gaussian_filter(image,10)

plt.figure(
    num="PIL_ROF",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(1,3,1)
plt.imshow(image)
#plt.axis('equal')
plt.title(u'原噪聲圖像')

plt.subplot(1,3,2)
plt.imshow(G)
#plt.axis('equal')
plt.title(u'高斯模糊後的圖像')

plt.subplot(1,3,3)
#plt.imshow(U)
#plt.axis('equal')
plt.title(u'ROF降噪後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

im = np.array(Image.open(filename).convert('L'))
plt.gray()
plt.subplot(2,2,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(im)

for bi, blur in enumerate([2, 5, 10]):
    print("bi = ", bi)
    im2 = np.zeros(im.shape)
    im2 = scipy.ndimage.gaussian_filter(im, blur)
    im2 = np.uint8(im2)
    imNum = str(blur)
    plt.subplot(2, 2, 2 + bi)
    plt.axis('off')
    plt.title('GaussVar = ' + imNum)
    plt.imshow(im2)

plt.show()


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


