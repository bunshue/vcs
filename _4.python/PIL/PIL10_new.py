"""
PIL 新進

使用python進行數字圖片處理，還得安裝Pillow包。
雖然python里面自帶一個PIL（python images library), 但這個庫現在已經停止更新了，
所以使用Pillow, 它是由PIL發展而來的。

pip install Pillow
"""


"""
plot 集合 1
"""

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

print('------------------------------------------------------------')	#60個

from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

print('------------------------------------------------------------')	#60個

print('顯示原圖')

#建立Pillow物件 PIL讀取本機圖片, RGB模式, 存成PIL影像格式
img = Image.open(filename)

#img = img.convert('L')  #fail
print(type(img))
plt.imshow(img)
plt.show()

#PIL影像格式轉化為numpy陣列
img=np.array(img)
print(type(img))

#顯示方法相同

print('------------------------------------------------------------')	#60個

"""
圖像中的像素訪問

前面的一些例子中，我們都是利用Image.open（）來打開一幅圖像，然後直接對這個PIL對象進行操作。如果只是簡單的操作還可以，但是如果操作稍微復雜一些，就比較吃力了。因此，通常我們加載完圖片後，都是把圖片轉換成矩陣來進行更加復雜的操作。

python中利用numpy庫和scipy庫來進行各種數據操作和科學計算。我們可以通過pip來直接安裝這兩個庫

pip install numpy
pip install scipy

"""


"""
調用numpy中的array（）函數就可以將PIL對象轉換為數組對象。
如果是RGB圖片，那么轉換為array之後，就變成了一個rows*cols*channels的三維矩陣,因此，我們可以使用
img[i,j,k]
來訪問像素值。
例：打開圖片，並隨機添加一些椒鹽噪聲
"""

img=np.array(Image.open(filename))

#隨機生成5000個椒鹽
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255
    
plt.imshow(img)
plt.title('椒鹽效果')
plt.show()

print('------------------------------------------------------------')	#60個

print('將圖像二值化，像素值大于 threshold 的變為1，否則變為0')
img=np.array(Image.open(filename).convert('L'))

"""
plt.imshow(img)
plt.title('LLLL')
plt.show()
"""

print('圖像二值化, 要灰階圖像')
      
threshold=128

rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
        if (img[i,j]<=threshold):
            img[i,j]=0
        else:
            img[i,j]=1
            
plt.imshow(img,cmap='gray')
plt.title('二值化, threshold ='+ str(threshold))
plt.show()

"""
如果要對多個像素點進行操作，可以使用數組切片方式訪問。切片方式返回的是以指定間隔下標訪問 該數組的像素值。下面是有關灰度圖像的一些例子：

img[i,:] = im[j,:] # 將第 j 行的數值賦值給第 i 行
img[:,i] = 100 # 將第 i 列的所有數值設為 100
img[:100,:50].sum() # 計算前 100 行、前 50 列所有數值的和
img[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）
img[i].mean() # 第 i 行所有數值的平均值
img[:,-1] # 最後一列
img[-2,:] (or im[-2]) # 倒數第二行
"""
print('------------------------------------------------------------')	#60個

print("偽色彩圖像處理")

#filename = 'C:/_git/vcs/_1.data/______test_files1/pic_256X100.png'
#filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

image = Image.open(filename)

#彩色轉黑白
# 轉換為灰度圖像
gray_image = image.convert('L')

#3. 偽色彩處理

#偽色彩處理可以通過將灰度值映射到彩色值來實現。通常，我們使用一個顏色映射表（Color Map）來定義灰度和彩色之間的映射關系。
#在Python中，可以使用matplotlib庫來生成顏色映射表並將灰度圖像轉換為彩色圖像。

# 定義顏色映射表
cmap = plt.get_cmap('jet')

# 將灰度圖像轉換為彩色圖像
color_image = cmap(np.array(gray_image))

# 顯示彩色圖像
plt.imshow(color_image)
plt.title('偽色彩')

plt.show()

#上述代碼中，我們使用get_cmap方法獲取了一個名為’jet’的顏色映射表。然後，將灰度圖像轉換為NumPy數組，再將數組應用于顏色映射表，得到彩色圖像。

print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/red_300X300.bmp'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.bmp'

"""
平均雜湊（aHash）
ahash:          Average hash
hashfunc = imagehash.average_hash
感知雜湊（pHash）
phash:          Perceptual hash
hashfunc = imagehash.phash
差異雜湊（dHash）
dhash:          Difference hash
hashfunc = imagehash.dhash
小波雜湊（wHash）
whash-haar:     Haar wavelet hash
hashfunc = imagehash.whash
whash-db4:      Daubechies wavelet hash
imagehash.whash(img, mode='db4')
colorhash:      HSV color hash
hashmethod == 'crop-resistant':
crop-resistant: Crop-resistant hash
imagehash.crop_resistant_hash
"""
import imagehash

image1 = Image.open(filename1)
image2 = Image.open(filename2)
hash1 = imagehash.average_hash(image1)
hash2 = imagehash.average_hash(image2)

print('圖一的hash :', hash1)
print('圖二的hash :', hash2)

if hash1 == hash2:
    print('兩圖相同')
else:
    print('兩圖不同')

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
font_filename = 'C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf'

print('------------------------------------------------------------')	#60個

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
"""

post_html = """
</table>
</body>
</html>
"""
"""
table_html = ""

source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            image = Image.open(os.path.join(source, file))
            thumbnail = image.resize((320,200))
            #thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容            
            table_html += "<tr><td><a href='{}'><img src='{}'></a></td></tr>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
<tr>
"""

post_html = """
</tr>
</table>
</body>
</html>
"""


table_html = ""
"""
source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for index, file in enumerate(allfiles):
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            image = Image.open(os.path.join(source, file))
            thumbnail = image.resize((320,200))
            #thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容         
            table_html += "<td><a href='{}'><img src='{}'></a></td>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
            if (index+1) % 3 == 0:
                table_html += "</tr><tr>"
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

"""
def blue_to_red2(image_path):
    image = Image.open(image_path)
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            #若該點的藍色成分明顯超過紅色及綠色,我們便將之視為藍色
            if b > r and b > g:
                #將藍色分轉為紅色
                pixels[x, y] = (b, g, r)
    image.show()
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
blue_to_red2(filename)
"""    
print('------------------------------------------------------------')	#60個

import seaborn as sns #海生, 自動把圖畫得比較好看
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

print('------------------------------------------------------------')	#60個

plt.figure(
    num="影像處理1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = Image.open(filename)
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(121)
plt.title(u'原圖')
plt.imshow(image)

image = Image.open(filename).convert('L')

plt.subplot(122)
plt.title(u'灰度圖')
plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

image0 = Image.open(filename)
image0 = image0.convert('L')
image1 = np.array(image0)
print('原圖 灰階最小值 :', int(image1.min()),', 灰階最大值 :', int(image1.max()))

image2=255-image1               #對圖像進行反向處理
print('反相 灰階最小值 :', int(image2.min()),', 灰階最大值 :', int(image2.max()))

image3=(100.0/255)*image1+100   #將圖像像素值變換到100...200區間
print('壓縮到100~200 灰階最小值 :', int(image3.min()),', 灰階最大值 :', int(image3.max()))

image4=255.0*(image1/255.0)**2  #對像素值求平方後得到的圖像
print('相素值平方 灰階最小值 :', int(image4.min()),', 灰階最大值 :', int(image4.max()))

plt.figure(
    num="影像處理2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(221)
plt.imshow(image0)
plt.title('原圖轉灰階')

plt.subplot(222)
plt.imshow(image2)
plt.title(r'反相 $f(x)=255-x$')

plt.subplot(223)
plt.imshow(image3)
plt.title(r'壓縮到100~200 $f(x)=\frac{100}{255}x+100$')

plt.subplot(224)
plt.imshow(image4)
plt.title(r'相素值平方 $f(x)=255(\frac{x}{255})^2$')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_mean")

from PIL import ImageStat

def darkchannel(input_img,h,w):
    dark_img = Image.new("L",(h,w),0)
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
    dehaze_img = Image.new("RGB",(h,w),0)
    for i in range(0,h-1):
        for j in range(0,w-1):
            R,G,B=img.getpixel((i,j))
            R=int((R-air[0])/t_map[i,j]+air[0])
            G=int((G-air[1])/t_map[i,j]+air[1])
            B=int((B-air[2])/t_map[i,j]+air[2])
            dehaze_img.putpixel((i,j),(R,G,B)) 
    return dehaze_img                       
                    
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img=Image.open(filename)
[h,w]=img.size
OMIGA =0.8  
dark_image=darkchannel(img,h,w)
air=airlight(img,h,w)
T_map=transmssion(air,dark_image,h,w,OMIGA)
fogfree_img=defog(img,T_map,air,h,w)

#把結果顯示出來
plt.imshow(fogfree_img)

plt.show()

print("------------------------------------------------------------")  # 60個

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

img = np.array(Image.open(filename))  #導入圖片
add_salt_noise(img)

print("------------------------------------------------------------")  # 60個

print("PIL_derivative")

from scipy.ndimage import filters

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

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
filters.sobel(image,1,imagex)

plt.subplot(142)
plt.title(u'(b)x方向差分')
plt.imshow(imagex)
imagey=np.zeros(image.shape)
filters.sobel(image,0,imagey)

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

from scipy.ndimage import filters
from matplotlib.font_manager import FontProperties

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
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
    image2=filters.gaussian_filter(image,blur)
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

from scipy.ndimage import filters

def imx(image, sigma):
    imgx = np.zeros(image.shape)
    filters.gaussian_filter(image, sigma, (0, 1), imgx)
    return imgx
def imy(image, sigma):
    imgy = np.zeros(image.shape)
    filters.gaussian_filter(image, sigma, (1, 0), imgy)
    return imgy
def mag(image, sigma):
    # 還有gaussian_gradient_magnitude()
    imgmag = 255 - np.sqrt(imgx ** 2 + imgy ** 2)
    return imgmag

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
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
    imgx=imx(image, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+2)
    plt.imshow(imgx)
    imgy=imy(image, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+3)
    plt.imshow(imgy)
    imgmag=mag(image, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+4)
    plt.imshow(imgmag)

plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個

print("PIL_opening")

#measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
from scipy.ndimage import measurements, morphology  

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

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
image = np.array(Image.open('data/castle.jpg').convert('L'))

plt.subplot(221)
plt.imshow(image)
plt.title(u'原圖')
image = (image < 128)
labels, nbr_objects = measurements.label(image) #圖像的灰度值表示對象的標簽
print ("Number of objects:", nbr_objects)

plt.subplot(222)
plt.imshow(labels)
plt.title(u'標記後的圖')
#形態學——使物體分離更好
image_open = morphology.binary_opening(image, np.ones((9, 5)), iterations=4) #開操作，第二個參數為結構元素，iterations覺定執行該操作的次數

plt.subplot(223)
plt.imshow(image_open)
plt.title(u'開運算後的圖像')
labels_open, nbr_objects_open = measurements.label(image_open)
print ("Number of objects:", nbr_objects_open)

plt.subplot(224)
plt.imshow(labels_open)
plt.title(u'開運算後進行標記後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_PCA")

#measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
from scipy.ndimage import measurements, morphology  

# 加載圖像和閾值，以確保它是二進制的
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
labels, nbr_objects = measurements.label(image) #圖像的灰度值表示對象的標簽
print ("Number of objects:", nbr_objects)

plt.subplot(222)
plt.imshow(labels)
plt.title(u'標記後的圖')
#形態學——使物體分離更好
image_open = morphology.binary_opening(image, np.ones((9, 5)), iterations=4) #開操作，第二個參數為結構元素，iterations覺定執行該操作的次數

plt.subplot(223)
plt.imshow(image_open)
plt.title(u'開運算後的圖像')
labels_open, nbr_objects_open = measurements.label(image_open)
print ("Number of objects:", nbr_objects_open)

plt.subplot(224)
plt.imshow(labels_open)
plt.title(u'開運算後進行標記後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_realROF")

from scipy.ndimage import filters
#from scipy.misc import imsave
#from PCV.tools import rof

image = np.array(Image.open('data/gril.jpg').convert('L'))
#U,T = rof.denoise(image,image)
G = filters.gaussian_filter(image,10)

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

from scipy.ndimage import filters
#from scipy.misc import imsave
#from PCV.tools import rof

# 創建合成圖像與噪聲
image = np.zeros((500,500))
image[100:400,100:400] = 128
image[200:300,200:300] = 255
image = image + 30*np.random.standard_normal((500,500))
#roll()函數：循環滾動數組中的元素，計算領域元素的差異。linalg.norm()函數可以衡量兩個數組見得差異
#U,T = rof.denoise(image,image)  
G = filters.gaussian_filter(image,10)

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

print("PIL_save")

def IsValidImage(img_path):
    """
    判斷文件是否為有效（完整）的圖片
    :param img_path:圖片路徑
    :return:True：有效 False：無效
    """
    bValid = True
    try:
        Image.open(img_path).verify()
    except:
        bValid = False
    return bValid


def transimg(img_path):
    """
    轉換圖片格式
    :param img_path:圖片路徑
    :return: True：成功 False：失敗
    """
    if IsValidImage(img_path):
        try:
            str = img_path.rsplit(".", 1)
            output_img_path = "tmp_" + str[0] + ".jpg"
            print(output_img_path)
            im = Image.open(img_path)
            #im.save(output_img_path)
            return True
        except:
            return False
    else:
        return False


img_path = 'lena.png'
print(transimg(img_path))

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

from PIL import Image, ImageFilter

print('PIL模糊處理 GaussianBlur')
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

guido_img = Image.open(open(filename, 'rb'))
guido2_img = guido_img.filter(ImageFilter.GaussianBlur)
guido2_img.save(open('tmp_elephant_blur.jpg', 'wb'))


print('二值化')
img1 = Image.open(open(filename, 'rb'))
img2 = img1.point(lambda x: 0 if x < 128 else 255)

img2.save(open('tmp_elephant_binary.png', 'wb'))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個

"""
print("PIL_ginput")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im = np.array(Image.open(filename))
plt.imshow(im)

print('請點擊3個點')
x = plt.ginput(3)
print('你已點擊:', x)
plt.show()
"""

print('------------------------------------------------------------')	#60個



