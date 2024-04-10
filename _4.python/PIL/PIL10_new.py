"""
PIL 新進

使用python進行數字圖片處理，還得安裝Pillow包。
雖然python里面自帶一個PIL（python images library), 但這個庫現在已經停止更新了，
所以使用Pillow, 它是由PIL發展而來的。

pip install Pillow


PIL中所涉及的基本概念有如下几个：
通道（bands）
模式（mode）
尺寸（size）
坐标系统（coordinate system）
调色板（palette）
信息（info）
滤波器（filters）

1、  通道
彩色圖片 RGB 3通道
灰階圖片 1通道

2、  模式

图像的模式定义了图像的类型和像素的位宽。当前支持如下模式：

1：1位像素，表示黑和白，但是存储的时候每个像素存储为8bit。
L：8位像素，表示黑和白。
P：8位像素，使用调色板映射到其他模式。
RGB：3x8位像素，为真彩色。
RGBA：4x8位像素，有透明通道的真彩色。
CMYK：4x8位像素，颜色分离。
YCbCr：3x8位像素，彩色视频格式。
I：32位整型像素。
F：32位浮点型像素。

3、  尺寸
4、  坐标系统

PIL使用笛卡尔像素坐标系统，坐标(0，0)位于左上角。
注意：坐标值表示像素的角；位于坐标（0，0）处的像素的中心实际上位于（0.5，0.5）。
坐标经常用于二元组（x，y）。
长方形则表示为四元组，前面是左上角坐标。
例如，一个覆盖800x600的像素图像的长方形表示为（0，0，800，600）。

5、  调色板

调色板模式 ("P")使用一个颜色调色板为每个像素定义具体的颜色值

6、  信息

使用info属性可以为一张图片添加一些辅助信息。这个是字典对象。
加载和保存图像文件时，多少信息需要处理取决于文件格式。

7、  滤波器

对于将多个输入像素映射为一个输出像素的几何操作，PIL提供了4个不同的采样滤波器：

NEAREST：最近滤波。从输入图像中选取最近的像素作为输出像素。它忽略了所有其他的像素。
BILINEAR：双线性滤波。在输入图像的2x2矩阵上进行线性插值。注意：PIL的当前版本，做下采样时该滤波器使用了固定输入模板。
BICUBIC：双立方滤波。在输入图像的4x4矩阵上进行立方插值。注意：PIL的当前版本，做下采样时该滤波器使用了固定输入模板。
ANTIALIAS：平滑滤波。这是PIL 1.1.3版本中新的滤波器。
对所有可以影响输出像素的输入像素进行高质量的重采样滤波，以计算输出像素值。
在当前的PIL版本中，这个滤波器只用于改变尺寸和缩略图方法。

注意：在当前的PIL版本中，ANTIALIAS滤波器是下采样（例如，将一个大的图像转换为小图）时唯一正确的滤波器。
BILIEAR和BICUBIC滤波器使用固定的输入模板，用于固定比例的几何变换和上采样是最好的。

Image模块中的方法resize()和thumbnail()用到了滤波器。

PIL 之 resize()

image.resize(size, filter=None)

>>>im_resize = im.resize((256,256))

对参数filter不赋值的话，方法resize()默认使用NEAREST滤波器。

>>>im_resize0 = im.resize((256,256), Image.BILINEAR)
>>>im_resize1 = im.resize((256,256), Image.BICUBIC)
>>>im_resize2 = im.resize((256,256), Image.ANTIALIAS)

PIL 之 thumbnail()

image.thumbnail(size, filter=None)

>>>im.thumbnail((200,200))

这里需要说明的是，方法thumbnail()需要保持宽高比，对于size=(200,200)的输入参数，其最终的缩略图尺寸为(200, 112)。
对参数filter不赋值的话，方法thumbnail()默认使用NEAREST滤波器。如果要使用其他滤波器可以通过下面的方法来实现：

>>> im.thumbnail((200,200),Image.BILINEAR)
>>> im.thumbnail((200,200), Image.BICUBIC)
>>> im.thumbnail((200,200), Image.ANTIALIAS)



"""

print("------------------------------------------------------------")  # 60個

import PIL
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

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

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/red_300X300.bmp'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.bmp'
'''
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
imagehash.whash(image, mode='db4')
colorhash:      HSV color hash
hashmethod == 'crop-resistant':
crop-resistant: Crop-resistant hash
imagehash.crop_resistant_hash
"""
import imagehash

# 檔案 => PIL影像
image1 = Image.open(filename1)

# 檔案 => PIL影像
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

'''
print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

# 打開圖像，并轉成灰度圖像
# 檔案 => PIL影像 => 灰階 => np陣列
image = np.array(Image.open(filename).convert('L'))#L為8位像素黑白圖

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.contour(image, origin='image')
plt.axis('equal')
plt.title(u'圖像輪廓圖')

plt.show()

print("------------------------------------------------------------")  # 60個

gif_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cat.gif"

print("gif轉jpg")
from PIL import Image,ImageSequence

gif = Image.open(gif_filename)                # 讀取動畫圖檔

i = 0                                      # 設定編號變數
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGB')           # 取出每一格轉換成 RGB
    #frame.save(f'tmp_frame{i}.jpg', quality=65, subsampling=0)  # 儲存為 jpg
    i = i + 1                              # 編號增加 1

print("------------------------------------------------------------")  # 60個
print("用cv視窗播放gif檔案")

gif_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cat.gif"

from PIL import Image,ImageSequence

gif = Image.open(gif_filename)

img_list = []                                      # 建立儲存影格的空串列
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')                  # 轉換成 RGBA
    opencv_img = np.array(frame, dtype=np.uint8)   # 轉換成 numpy 陣列
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)  # 顏色從 RGBA 轉換為 BGRA
    img_list.append(opencv_img)                    # 利用串列儲存該圖片資訊

loop = True                                        # 設定 loop 為 True
while loop:
    for i in img_list:
        cv2.imshow('image', i)                # 不斷讀取並顯示串列中的圖片內容
        if cv2.waitKey(200) == ord('q'):
            loop = False                           # 停止時同時也將 while 迴圈停止
            break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageSequence

gif_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cat.gif"

gif = Image.open(gif_filename)

img_list = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')
    opencv_img = np.array(frame, dtype=np.uint8)
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)

    # 在圖形中間繪製黑色方塊
    x_st, y_st, w, h = 10, 10, 120, 40
    cv2.rectangle(opencv_img,(x_st, y_st),(x_st+w, y_st+h),(0,0,0),-1)

    # 在黑色方塊上方加入文字, 文字基準是左下角
    text = 'My Cat'
    org = (x_st, y_st+30)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255,255,255)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(opencv_img, text, org, fontFace, fontScale, color, thickness, lineType)

    img_list.append(opencv_img)

loop = True
while loop:
    for i in img_list:
        cv2.imshow('image', i)
        if cv2.waitKey(200) == ord('q'):
            loop = False
            break
# 建立要輸出的影格串列
output = []
for i in img_list:
    img = i
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # 因為 OpenCV 為 BGRA，要轉換成 RGBA
    img = Image.fromarray(img)    # 轉換成 PIL 格式
    img = img.convert('RGB')      # 轉換成 RGB ( 如果是 RGBA 會自動將黑色白色變成透明色 )
    output.append(img)            # 加入 output
# 儲存為 gif 動畫圖檔
output[0].save("tmp_image.gif", save_all=True, append_images=output[1:], duration=200, loop=0, disposal=0)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("多個jpg組成一個gif檔")

from PIL import Image,ImageSequence

gif = []
for i in range(1, 6):
    img = Image.open(f'C:/_git/vcs/_1.data/______test_files1/__pic/_scenery/ggb{i}.jpg')  # 開啟圖片
    gif.append(img)                    # 加入串列
# 儲存為 gif
gif[0].save("tmp_image.gif", save_all=True, append_images=gif[1:], duration=2000, loop=0, disposal=0)

print("------------------------------------------------------------")  # 60個

"""

n = 0
for i in source:                  # source 為要轉存的所有圖片陣列 ( opencv 格式，色彩為 RGBA )
    img = Image.fromarray(i)      # 轉換成 PIL 格式
    img.save(f'tmp_gif{n}.gif')  # 儲存為 gif
    n = n + 1                     # 改變儲存的檔名編號

output = []                       # 建立空串列
for i in range(n):
    img = Image.open(f'tmp_gif{i}.gif')  # 依序開啟每張 gif
    img = img.convert("RGBA")             # 轉換為 RGBA
    output.append(img)                    # 記錄每張圖片內容

# 轉存為 gif 動畫，設定 disposal=2
output[0].save("tmp_image.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)
"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個

"""
print("PIL_ginput")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像 => numpy陣列
im = np.array(Image.open(filename))
plt.imshow(im)

print('請點擊3個點')
x = plt.ginput(3)
print('你已點擊:', x)
plt.show()
"""

print('------------------------------------------------------------')	#60個



