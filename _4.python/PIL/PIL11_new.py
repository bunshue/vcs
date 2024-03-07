"""
PIL 新進


"""

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個
'''
from PIL import Image, ImageOps
from IPython.display import display

#利用圖片大小強調數量多寡
#載入圖片與顯示圖片的範例

im = Image.open(filename)
display(im)

print('------------------------------------------------------------')	#60個


from pathlib import Path
from PIL import Image

infolder = "testfolder"
value1 = "outputfolder4"
extlist = ["*.jpg","*.png"]

#【函數: 轉存為jpg檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)              #載入圖片檔
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        #-----------------------------------
        filename = Path(readfile).stem+".jpg"   #建立檔案名稱
        savepath = savedir.joinpath(filename)
        if img.format == "PNG":
            newimg = Image.new("RGB", img.size, "white")
            newimg.paste(img, mask=img.split()[3])  #在白底背景繪製圖片
            newimg.save(savepath, format="JPEG", quality=95)    #轉存為JPG圖檔
        elif img.format == "JPEG":
            img.save(savepath, format="JPEG", quality=95)   #轉存為JPG圖檔
        #-----------------------------------
        msg = "在"+savefolder + "轉存" + filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數: 處理資料夾之內的圖片檔】
def savefiles(infolder, savefolder):
    msg = ""
    for ext in extlist:                     #以多個副檔名調查
        filelist = []
        for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
            filelist.append(str(p))         #新增至列表
        for filename in sorted(filelist):   #再替每個檔案排序
            msg += savepng(filename, savefolder)
    return msg

#【執行函數】
msg = savefiles(infolder, value1)
print(msg)

print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageDraw

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename
savefile = "tmp_redline.png"

img = Image.open(infile)
draw = ImageDraw.Draw(img)  #在圖片畫線的準備
draw.line((0, 0, img.width, img.height), fill="RED", width=8) #畫線
img.save(savefile, format="PNG")

print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename#"earth.png"
savefile = "tmp_saveJPG2.jpg"

img = Image.open(infile)
if img.format == "PNG":
    newimg = Image.new("RGB", img.size, "WHITE")
    newimg.paste(img, mask=img)             # 將PNG檔壓在白底圖片上
    newimg.save(savefile, format="JPEG")    # JPG轉存檔案
elif img.format == "JPEG":
    img.save(savefile, format="JPEG")       # JPG轉存檔案

print("------------------------------------------------------------")  # 60個






print('------------------------------------------------------------')	#60個

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns #海生, 自動把圖畫得比較好看
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei

#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image

img1 = Image.new("RGB",(300,200),"rgb(0,0,255)") #藍色
img1.save("tmp_blue.jpg")

img2 = Image.new("RGBA",(300,200),"rgba(0,0,255,0)") #透明
img2.save("tmp_alpha.png")

print('------------------------------------------------------------')	#60個

#利用圖片的個數強調數量

#以人形圖示的個數強調數量的範例


# 要排列的圖示個數
num = 10

# 圖片之間的邊界
margin = 5

# 載入圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

im = Image.open(filename)#"human.png"
im_width, im_height = im.size

# 將圖片入作為畫布使用的Image
canvas = Image.new("RGBA", ((im_width + margin) * num, im_height))
for i in range(num):
    canvas.paste(im, ((im_width + margin) * i, 0))

canvas

print('------------------------------------------------------------')	#60個

from PIL import Image,ImageDraw
from PIL import ImageFont

img = Image.new("RGB",(400,300),"lightgray") #淡灰色
drawimg=ImageDraw.Draw(img)

#繪多邊形
drawimg.polygon([(200,100),(350,150),(50,150)],fill="blue",outline="red")#屋頂
#繪矩形
drawimg.rectangle((100,150,300,250),fill="green",outline="black") #房間
#繪圓
drawimg.ellipse((300,40,350,90),fill="red")#太陽 
#繪橢圓
drawimg.ellipse((60,80,100,100),fill="white") #白雲一   
drawimg.ellipse((100,60,130,80),fill="white") #白雲二 
#繪文字
drawimg.text((120,170),"e-happy",fill="orange")
font_filename = 'C:/Windows/Fonts/mingliu.ttc'
myfont=ImageFont.truetype(font_filename, 16)#文字一
drawimg.text((120,200),"文淵閣工作室",fill="red",font=myfont) #文字二 
img.show()
img.save("tmp_house.png")


print('------------------------------------------------------------')	#60個


from PIL import Image,ImageDraw
img = Image.new("RGB",(400,300),"lightgray") #淡灰色
drawimg=ImageDraw.Draw(img)
  
#繪點
for i in range(0,400,10):
    for j in range(0,300,10):    
        drawimg.point([(i,j)],fill="red")  
#繪直線
for i in range(0,400,10):
    drawimg.line([(i,300),(200,150)],width=2,fill="blue") 
img.show()




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





# 1 open save show

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
infile = filename#"earth.png"
savefile = "tmp_savePNG1.png"

img = Image.open(infile)      #載入圖片檔
img.save(savefile, format="PNG")    #PNG轉存檔案

print("------------------------------------------------------------")  # 60個



# 2 resize


print('------------------------------------------------------------')	#60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename#"earth.png"
savefile = "tmp_resize2.png"

img = Image.open(infile)
img = img.resize((100, 100), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")

print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
infile = filename#"earthH.png"
savefile = "tmp_resize1.png"

max_size = 100
img = Image.open(infile)
ratio = max_size / max(img.size)    #根據長寬較長的一邊決定縮放比率
w = int(img.width * ratio)
h = int(img.height * ratio)
img = img.resize((w, h), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")

#調整圖片大小的範例

mini_im = im.resize((int(im.size[0] * 0.2), int(im.size[1] * 0.2)))
display(mini_im)
print(mini_im.size)


print('------------------------------------------------------------')	#60個



# 3 crop 無
# 4 

'''

from PIL import Image
plt.figure('影像處理1', figsize = (10, 6))

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = Image.open(filename)
plt.gray()  #這是什麼語法?

plt.subplot(121)
plt.title(u'原图')
plt.imshow(image)

image = Image.open(filename).convert('L')

plt.subplot(122)
plt.title(u'灰度图')
plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

print("PIL_hist")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from pylab import *

# 打开图像，并转成灰度图像
im = array(Image.open(filename).convert('L'))

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
plt.xlim([0-10,255+10])
plt.ylim([0,8000])

show()

print("------------------------------------------------------------")  # 60個

print("PIL_histeq")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from pylab import *
#from PCV.tools import imtools

# 添加中文字体支持
from matplotlib.font_manager import FontProperties

im = array(Image.open(filename).convert('L'))
# 打开图像，并转成灰度图像
#im2, cdf = imtools.histeq(im)
figure()
subplot(2, 2, 1)
axis('off')
gray()
title(u'原始图像')
imshow(im)
subplot(2, 2, 2)
axis('off')
title(u'直方图均衡化后的图像')
#imshow(im2)
subplot(2, 2, 3)
axis('off')
title(u'原始直方图')
hist(im.flatten(), 128, density=True)
subplot(2, 2, 4)
axis('off')
title(u'均衡化后的直方图')
#hist(im2.flatten(), 128, density=True)

show()

print("------------------------------------------------------------")  # 60個

#from numpy import *
from pylab import *

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im=array(Image.open(filename).convert('L'))
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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 读取图像到数组中
im = array(Image.open(filename))
figure()
imshow(im)
x = [100, 100, 200, 200]
y = [200, 400, 200, 400]
# 使用红色星状标记绘制点
plot(x, y, 'r*')
# 绘制连接两个点的线（默认为蓝色）
plot(x[:2], y[:2])
title('畫圖')

# show()命令首先打开图形用户界面（GUI），然后新建一个窗口，该图形用户界面会循环阻断脚本，然后暂停，
# 直到最后一个图像窗口关闭。每个脚本里，只能调用一次show()命令，通常相似脚本的结尾调用。
show()

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
fogfree_img.show()  

print("------------------------------------------------------------")  # 60個

print("PIL_operation")

from pylab import *

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

figure()
# 显示原图
image = Image.open(filename)
print(image.mode, image.size, image.format)
subplot(231)
title(u'原图')
axis('off')
imshow(image)

# 显示灰度图
image = Image.open(filename).convert('L')
gray()
subplot(232)
title(u'灰度图')
axis('off')
imshow(image)
# 复制并粘贴区域
image = Image.open(filename)
box = (100, 100, 200, 200)
region = image.crop(box)
region = region.transpose(Image.ROTATE_180)
image.paste(region, box)
subplot(233)
title(u'复制粘贴区域')
axis('off')
imshow(image)

# 缩略图
image = Image.open(filename)
size = 128, 128
image.thumbnail(size)
print(image.size)
subplot(234)
title(u'缩略图')
axis('off')
imshow(image)
#image.save('tmp_pic1.jpg')# 保存缩略图

#调整图像尺寸
image=Image.open(filename)
image=image.resize(size)
print(image.size)
subplot(235)
title(u'调整尺寸后的图像')
axis('off')
imshow(image)

#旋转图像45°
image=Image.open(filename)
image=image.rotate(45)
subplot(236)
title(u'旋转45°后的图像')
axis('off')
imshow(image)

show()

print("------------------------------------------------------------")  # 60個


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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'

img = np.array(Image.open(filename))  #导入图片
add_salt_noise(img)



print("------------------------------------------------------------")  # 60個



print("PIL_derivative")

from pylab import *
from scipy.ndimage import  filters
import numpy

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im=array(Image.open(filename).convert('L'))
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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
im=array(Image.open(filename).convert('L'))
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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
im = array(Image.open(filename).convert('L'))
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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im = array(Image.open(filename))
imshow(im)

print('请点击3个点')
x = ginput(3)
print('你已点击:', x)
show()

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


