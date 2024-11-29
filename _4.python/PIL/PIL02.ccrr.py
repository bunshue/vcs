"""

PIL 圖片相關的處理

無 影像處理

CCRR

裁剪 .crop
複製 .copy
縮放 .resize
旋轉 .rotate(

貼上 .paste

合成
鏡射 .transpose(

幾何變換 (1)
1. resize() 縮放
2. rotate() 旋轉
3. transpose()


"""

import time
import glob
import shutil

from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageFilter

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

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

print("裁剪 .crop ST------------------------------------------------------------")  # 60個

print("測試 裁剪 crop x, y, w, h")

# 檔案 => PIL影像
image1 = Image.open(filename)  # PIL讀取本機圖片, RGB模式

x_st, y_st, w, h = 140, 120, 70, 70
#                     x_st  y_st    x_sp     y_sp
image2 = image1.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間, 左上點到右下點

print("裁剪一塊 (x_sy, y_st, w, h), 大小 :", image2.size)
plt.imshow(image2)
plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("裁剪 .crop SP------------------------------------------------------------")  # 60個

print("複製 .copy ST------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("複製 .copy SP------------------------------------------------------------")  # 60個


print(
    "縮放 .resize ST------------------------------------------------------------"
)  # 60個

print("測試 縮放 resize")

# 檔案 => PIL影像
image1 = Image.open(filename)  # PIL讀取本機圖片, RGB模式
W, H = image1.size
print("原圖大小 W =", W, ", H =", H)

print("寬度變2倍, 高度變一半")
image2 = image1.resize((W * 2, H // 2), Image.LANCZOS)  # 使用 LANCZOS 調整影像大小

print("寬度變2倍, 高度不變")
image3 = image1.resize((W * 2, H))  # 寬度是2倍

print("寬度不變, 高度變2倍")
image4 = image1.resize((W, H * 2))  # 高度是2倍


""" resize new

image = image.resize((w, h), Image.LANCZOS)     # 使用 LANCZOS 調整影像大小
image = image.resize((100, 500), Image.LANCZOS)# 使用 LANCZOS 調整影像大小
image = image.resize((w*2,h), Image.LANCZOS)# 使用 LANCZOS 調整影像大小
image = image.resize((image.size[0]*2, image.size[1]*2), Image.LANCZOS)# 使用 LANCZOS 調整影像大小
image = image.resize((int(w / level), int(h / level)))  # 縮小圖片
image = image.resize((w, h), resample=Image.NEAREST)  # 放大圖片為原始大小


"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print(
    "縮放 .resize SP------------------------------------------------------------"
)  # 60個


print(
    "旋轉 .rotate ST------------------------------------------------------------"
)  # 60個

print("測試 旋轉 rotate")

# 檔案 => PIL影像
image = Image.open(filename)  # PIL讀取本機圖片, RGB模式

print("旋轉90度")
image90 = image.rotate(90)

print("旋轉180度")
image180 = image.rotate(180)

print("旋轉270度")
image270 = image.rotate(270)

print("旋轉45度")
image45a = image.rotate(45)

print("旋轉45度 + 圖像擴充")
image45b = image.rotate(45, expand=True)

print("旋轉60度 + xxx1")
image60a = image.rotate(60, Image.BILINEAR, 0, None, None, "#BBCC55")

print("旋轉60度 + xxx2")
image60b = image.rotate(60, Image.BILINEAR, 1, None, None, "#BBCC55")

image2 = image.rotate(30, Image.BILINEAR, 1, None, None, "#ffff66")
image2 = image.rotate(30, Image.BILINEAR, 0, None, None, "#ffff66")

print("保持圖片原始大小之旋轉")
image2 = image.rotate(60, Image.BILINEAR, 0, None, None, "#BBCC55")

print("保持圖片內容大小之旋轉")
image2 = image.rotate(60, Image.BILINEAR, 1, None, None, "#BBCC55")

print("------------------------------------------------------------")  # 60個

print("測試 旋轉 transpose")

print("左右相反")
image1 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 左右

print("上下顛倒")
image2 = image.transpose(Image.FLIP_TOP_BOTTOM)  # 上下

print("順時針旋轉90度")
rotate90 = image.transpose(Image.ROTATE_90)
rotate180 = image.transpose(Image.ROTATE_180)
rotate270 = image.transpose(Image.ROTATE_270)

transpose1 = image.transpose(Image.TRANSPOSE)
transpose2 = image.transpose(Image.TRANSVERSE)

# transpose()和rotate()沒有性能差別。

print(
    "旋轉 .rotate SP------------------------------------------------------------"
)  # 60個

print("------------------------------------------------------------")  # 60個

# 調整資料夾內所有圖片檔影像寬度, 加logo

source_dir = "C:/_git/vcs/_1.data/______test_files1/__pic/_book"
target_dir = "tmp_resized_pic"
logo_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_logo/matlab.png"

# 準備輸出資料夾 若已存在, 則先刪除再建立 若不存在, 則建立
if os.path.exists(target_dir):
    # os.remove(target_dir)  #存取被拒 不可用
    shutil.rmtree(target_dir)
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

image_W = 800

print("將資料夾 " + source_dir + " 內所有圖片檔調整寬度成 " + str(image_W) + " 像素")

print("Processing: {}".format(source_dir))

# 單層
allfiles = glob.glob(source_dir + "/*.jpg") + glob.glob(source_dir + "/*.png")

# 檔案 => PIL影像
logo = Image.open(logo_filename)  # PIL讀取本機圖片
logo = logo.resize((150, 150))  # 調整圖像大小

plt.imshow(logo)
plt.show()

for target_image in allfiles:
    pathname, filename = os.path.split(target_image)
    print(filename)
    # 檔案 => PIL影像
    image = Image.open(target_image)  # PIL讀取本機圖片
    W, H = image.size
    image = image.resize((800, int(800 / float(W) * H)))
    image.paste(logo, (0, 0), logo)
    image.save(target_dir + "/" + filename)
    image.close()

print("完成")
print("輸出圖片資料夾 : ", target_dir)

print("------------------------------------------------------------")  # 60個

print("合併圖 2 X 4 a")

bg = Image.new("RGB", (1200, 800), "#000000")  # 產生一張 1200x800 的全黑圖片
for i in range(1, 9):
    image = Image.open(
        f"C:/_git/vcs/_1.data/______test_files1/__pic/_MU/poster_0{i}.jpg"
    )  # 開啟圖片
    image2 = image.resize((300, 400))  # 縮小尺寸為 300x400
    x = (i - 1) % 4  # 根據開啟的順序，決定 x 座標
    y = (i - 1) // 4  # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(image2, (x * 300, y * 400))  # 貼上圖片

bg.save("tmp_compound2X4a.jpg")

print("------------------------------------------------------------")  # 60個

print("合併圖 2 X 4 b")
bg = Image.new("RGB", (1240, 840), "#000000")  # 因為擴張，所以將尺寸改成 1240x840
for i in range(1, 9):
    image = Image.open(
        f"C:/_git/vcs/_1.data/______test_files1/__pic/_MU/poster_0{i}.jpg"
    )  # 開啟圖片
    image2 = image.resize((300, 400))
    image3 = ImageOps.expand(image2, 20, "#ffffff")  # 擴張邊緣，產生邊框
    x = (i - 1) % 4
    y = (i - 1) // 4
    bg.paste(image3, (x * 300, y * 400))

bg.save("tmp_compound2X4b.jpg")

print("------------------------------------------------------------")  # 60個

print("撈出一個資料夾內的所有圖片")

images = glob.glob("./data/*.jpg")  # 讀取資料夾裡所有的圖片, 撈出一層

for i in images:
    # print(i)
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    # print(name)

    short_filename = os.path.basename(i)
    print("短檔名 :", short_filename)

print("------------------------------------------------------------")  # 60個

# 半透明貼上浮水印圖片
filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
logo_filename = "C:/_git/vcs/_1.data/______test_files1/_icon/唐.png"

# 檔案 => PIL影像
image = Image.open(filename)  # 準備合成浮水印的圖

# 檔案 => PIL影像
image2 = Image.open(filename)  # 底圖

# 檔案 => PIL影像
icon = Image.open(logo_filename)

image_w, image_h = image.size
icon_w, icon_h = icon.size
x = int((image_w - icon_w) / 2)
y = int((image_h - icon_h) / 2)
image.paste(icon, (x, y), icon)  # 合成浮水印
image.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
image.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
image2.paste(image, (0, 0), image)  # 合成底圖
image2.save("./tmp_elephant_add_watermark.jpg")

print("------------------------------------------------------------")  # 60個

# 製作馬賽克效果

filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

# 檔案 => PIL影像
image = Image.open(filename)

w, h = image.size
level = 5
image2 = image.resize((int(w / level), int(h / level)))
image2 = image2.resize((w, h), resample=Image.NEAREST)

x1, y1 = 60, 60  # 定義選取區域的左上角座標
x2, y2 = 250, 250  # 定義選取區域的右上角座標
area = image2.crop((x1, y1, x2, y2))  # 裁切區域
image.paste(area, (x1, y1))  # 在原本的圖片裡貼上馬賽克區域

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

print("圖片貼上logo")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"
filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

print("讀檔 => resize => paste")

# 檔案 => PIL影像(logo)
image1 = Image.open(logo_filename)

# resize
image1 = image1.resize((image1.size[0] // 2, image1.size[1] // 2))

# 檔案 => PIL影像(大圖)
image2 = Image.open(filename)

# 貼上位置, 將image1貼在image2之上
x_st = 250
y_st = 20
# 貼法一
image2.paste(image1, (x_st, y_st), image1)
# 貼法二
# image2.paste(image1, (x_st, y_st))

plt.imshow(image2)

plt.show()

print("------------------------------------------------------------")  # 60個


def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        time.sleep(1)  # 需延遲,否則會出錯
    os.mkdir(dirname)


image_dir = "data"
target_dir = "tmp_bmp_photo"
target_dir2 = "tmp_gray_photo"
emptydir(target_dir)
emptydir(target_dir2)
files = glob.glob(image_dir + "\*.jpg") + glob.glob(image_dir + "\*.png")
for i, f in enumerate(files):
    # 檔案 => PIL影像
    image = Image.open(f)
    image_new = image.resize((800, 600), Image.LANCZOS)  # 使用 LANCZOS 調整影像大小
    path, filename = f.split("\\")  # 路徑、檔名
    name, ext = filename.split(".")  # 主檔名、副檔名
    # 以bmp格式存檔
    image_new.save(target_dir + "/" + name + "aaa.bmp")

    # 轉換為灰階
    image_gray = image_new.convert("L")
    # gray001.jpg、gray002.jpg...
    outname = str("gray") + str("{:0>3d}").format(i + 1) + "aaa.jpg"
    image_gray.save(target_dir2 + "/" + outname)
    print("{} 複製完成!".format(f))
    image.close()

print("轉換尺寸及灰階處理結束！")

print("------------------------------------------------------------")  # 60個

print("生成縮略圖 thumbnail")

# 檔案 => PIL影像
image = Image.open(filename)

size = 128, 128
image.thumbnail(size)

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_operation")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
image = Image.open(filename)
print(image.mode, image.size, image.format)

plt.subplot(231)
plt.title("原圖")
plt.imshow(image)

# 顯示灰度圖
# 檔案 => PIL影像 => 灰階
image = Image.open(filename).convert("L")

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(232)
plt.title("灰度圖")
plt.imshow(image)
# 複製並粘貼區域

# 檔案 => PIL影像
image = Image.open(filename)
box = (100, 100, 200, 200)
region = image.crop(box)
region = region.transpose(Image.ROTATE_180)
image.paste(region, box)

plt.subplot(233)
plt.title("復制粘貼區域")
plt.imshow(image)

# 縮略圖
# 檔案 => PIL影像
image = Image.open(filename)

size = 128, 128
image.thumbnail(size)
print(image.size)

plt.subplot(234)
plt.title("縮略圖")
plt.imshow(image)

# 調整圖像尺寸
# 檔案 => PIL影像
image = Image.open(filename)

image = image.resize(size)
print(image.size)

plt.subplot(235)
plt.title("調整尺寸後的圖像")
plt.imshow(image)

plt.subplot(236)

plt.show()

print("------------------------------------------------------------")  # 60個

""" 處理資料夾有問題
foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'

allfiles = os.listdir(foldername)
print(allfiles)
for file in allfiles:
    print(file)
    filename, ext = os.path.splitext(file)
    filename = filename + "_s"
    targetfile = filename + ext
    #print(foldername, file)
    image = Image.open(os.path.join(foldername, file))
    thumbnail = image.resize((320,200))
    #thumbnail.save(os.path.join(target, targetfile))
    image.close()
    thumbnail.close()
    print("{}-->{}".format(file, targetfile))
"""
print("------------------------------------------------------------")  # 60個

from pathlib import Path

infolder = "testfolder"
value1 = "outputfolder4"
extlist = ["*.jpg", "*.png"]


# 【函數: 轉存為jpg檔案】
def savepng(readfile, savefolder):
    try:
        # 檔案 => PIL影像
        img = Image.open(readfile)  # 載入圖片檔
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        # -----------------------------------
        filename = Path(readfile).stem + ".jpg"  # 建立檔案名稱
        savepath = savedir.joinpath(filename)
        if img.format == "PNG":
            newimg = Image.new("RGB", img.size, "white")
            newimg.paste(img, mask=img.split()[3])  # 在白底背景繪製圖片
            # newimg.save(savepath, format="JPEG", quality=95)    #轉存為JPG圖檔
        elif img.format == "JPEG":
            # img.save(savepath, format="JPEG", quality=95)   #轉存為JPG圖檔
            pass
        # -----------------------------------
        msg = "在" + savefolder + "轉存" + filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數: 處理資料夾之內的圖片檔】
def savefiles(infolder, savefolder):
    msg = ""
    for ext in extlist:  # 以多個副檔名調查
        filelist = []
        for p in Path(infolder).glob(ext):  # 將這個資料夾的檔案
            filelist.append(str(p))  # 新增至列表
        for filename in sorted(filelist):  # 再替每個檔案排序
            msg += savepng(filename, savefolder)
    return msg


# 【執行函數】
msg = savefiles(infolder, value1)
print(msg)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
# 檔案 => PIL影像
image = Image.open(filename)
imagecopy = image.copy()  # 複製
# 切割貓熊並改變尺寸
image1 = imagecopy.crop((190, 184, 415, 350)).resize((160, 140))
imagecopy.paste(image1, (40, 30))  # 貼上
image2 = image1.transpose(Image.FLIP_LEFT_RIGHT)  # 左右翻轉
imagecopy.paste(image2, (220, 40))  # 貼上

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("綜合CCRR範例")
print("------------------------------------------------------------")  # 60個

print("複製範例一")
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# 檔案 => PIL影像
image = Image.open(filename)

# 複製圖片
image_copy = image.copy()

# 裁剪一塊 x, y ,w, h
x_st, y_st, w, h = 140, 120, 70, 70
#                             x_st  y_st    x_sp     y_sp
image_crop = image_copy.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間, 左上點到右下點
image_crop = image_copy.crop((140, 120, 210, 190))

# 貼上1
x_st, y_st = 220, 5
image_copy.paste(image_crop, (x_st, y_st))
# 貼上2
x_st, y_st = 220, 80
image_copy.paste(image_crop, (x_st, y_st))

plt.imshow(image_copy)
plt.show()

print("------------------------------------------------------------")  # 60個

print("複製範例二")
# 檔案 => PIL影像
image = Image.open(filename)

image_copied = image.copy()  # 複製圖片

x_st, y_st, w, h = 140, 120, 70, 70
#                               x_st  y_st    x_sp     y_sp
image_crop = image_copied.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間
cropW, cropH = image_crop.size  # 獲得裁切區間的寬與高

W, H = cropW * 8 + 10 * 9, cropH * 4 + 10 * 5  # 新影像寬與高
image = Image.new("RGB", (W, H), "Yellow")  # 建立新影像
for x in range(10, W - 50, cropW + 10):  # 雙層迴圈合成
    for y in range(10, H - 50, cropH + 10):
        image.paste(image_crop, (x, y))  # 合成

plt.imshow(image)
plt.show()


print("------------------------------------------------------------")  # 60個

# x_st, y_st, w, h = 140, 120, 70, 70
# roi = image.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間, 左上點到右下點

# 檔案 => PIL影像
image1 = Image.open(filename)
image2 = image1.copy()  # 複製
image3 = image2.crop((80, 30, 150, 100))  # 裁切區間
cropW, cropH = image3.size  # 獲得裁切區間的寬與高

W, H = 600, 320  # 新影像寬與高
image4 = Image.new("RGB", (W, H), "Yellow")  # 建立新影像
for x in range(20, W - 20, cropW):  # 雙層迴圈合成
    for y in range(20, H - 20, cropH):
        image4.paste(image3, (x, y))  # 合成

print("------------------------------------------------------------")  # 60個


# 使用pillow操作图像

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像
img = Image.open(filename)

# 檔案 => PIL影像
img2 = Image.open(filename)

# img3 = img2.crop((335, 435, 430, 615))
img3 = img2.crop((100, 100, 150, 150))
for x in range(4):
    for y in range(5):
        img2.paste(img3, (95 * y, 180 * x))

img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)

plt.imshow(img2)
plt.show()

print("------------------------------------------------------------")  # 60個

# 把同樣的圖片排列成 M X N

# 要排列的圖示個數
M = 5
N = 8

# 圖片之間的邊界
margin = 5

# 載入圖片
filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/AB_red.jpg"
# 檔案 => PIL影像
image = Image.open(filename)
print(image.size)

W, H = image.size

# 建立圖片 W*N X H*M
image_MXN = Image.new("RGBA", ((W + margin) * N, (H + margin) * M))

for j in range(M):
    for i in range(N):
        image_MXN.paste(image, ((W + margin) * i, (H + margin) * j))

plt.imshow(image_MXN)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""
# 存檔
# 檔案 => PIL影像 => 檔案
image.save("tmp_pic31_resize.jpg" )
image.save(savefile, format="PNG")
image.save('tmp_pic1.jpg')# 保存縮略圖
image.save(savefile, format="JPEG")       # JPG轉存檔案

"""
