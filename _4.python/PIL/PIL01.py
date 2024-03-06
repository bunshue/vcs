"""

PIL 圖片相關的處理

無 影像處理

縮放 .resize
裁剪 .crop
複製 .copy
合成
旋轉 .rotate(
鏡射 .transpose(

拆分 .split() r, g, b = image1.split()   #r, g, b為三個通道的list
合併 .merge


"""

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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print('------------------------------------------------------------')	#60個
'''
print('測試 縮放 resize')

image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式
W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

print('寬度變2倍, 高度變一半')
W2, H2 = W * 2, H // 2
print('把原圖轉成', W2, 'X', H2, '大小')
image2 = image1.resize((W2, H2), Image.LANCZOS)

plt.imshow(image2)
plt.show()

print('------------------------------------------------------------')	#60個

print('測試 裁剪 crop')

image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式
W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

x_st = 20
y_st = 20
w = W - x_st * 2
h = H - y_st * 2

#                     x_st  y_st    x_sp     y_sp
image2 = image1.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間, 左上點到右下點

print('顯示一塊')
plt.imshow(image2)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('複製圖片')
image_copied = image.copy() #複製圖片
#plt.imshow(image_copied)
#plt.show()

x_st = 0
y_st = 0
w = 300 / 4
h = 400 / 4
#                             x_st  y_st    x_sp     y_sp
cropPict = image_copied.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間
image_copied.paste(cropPict, (20, 20))          # 第一次合成
image_copied.paste(cropPict, (20, 20 + 120))    # 第二次合成
image_copied.paste(cropPict, (20, 20 + 240))    # 第三次合成

print('合成圖片')
plt.imshow(image_copied)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('複製圖片')
image_copied = image.copy() #複製圖片

x_st = 0
y_st = 0
w = 300 / 4
h = 400 / 4
#                             x_st  y_st    x_sp     y_sp
cropPict = image_copied.crop((x_st, y_st, x_st + w, y_st + h))    # 裁切區間
cropW, cropH = cropPict.size           # 獲得裁切區間的寬與高

W, H = 600, 320                        # 新影像寬與高
image = Image.new('RGB', (W, H), "Yellow")  # 建立新影像
for x in range(20, W - 20, cropW):         # 雙層迴圈合成
    for y in range(20, H - 20, cropH):
        image.paste(cropPict, (x, y))        # 合成

print('合成圖片')
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('測試 旋轉 rotate')

image = Image.open(filename)     # 建立Pillow物件

print('旋轉90度')
image90 = image.rotate(90)

print('旋轉180度')
image180 = image.rotate(180)

print('旋轉270度')
image270 = image.rotate(270)

print('旋轉45度')
image45a = image.rotate(45)

print('旋轉45度 + 圖像擴充')
image45a = image.rotate(45, expand = True)


print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('左右相反')
image1 = image.transpose(Image.FLIP_LEFT_RIGHT)   # 左右

print('上下顛倒')
image2 = image.transpose(Image.FLIP_TOP_BOTTOM)   # 上下

print('旋轉90度')
rotate90 = image.transpose(Image.ROTATE_90)

'''
print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = Image.open(filename)

r, g, b = image.split()

plt.imshow(image)
plt.show()
"""
plt.imshow(r)
plt.show()

plt.imshow(g)
plt.show()

plt.imshow(b)
plt.show()
"""

print('RGB相反排列')
convert_image = Image.merge('RGB', (b, g, r))

plt.imshow(convert_image)
plt.show()



"""  ???
image = Image.open(filename)    #PIL讀取本機圖片
r, g, b = image.split()
convert_image = image.merge('RGB', (b, g, r))
convert_image.save('image_bgr.png')
"""



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

from PIL import Image, ImageFilter

filename1 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/bear_filter.jpg'

image = Image.open(filename1)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image)
plt.show()

#對圖形套用過濾器
im_sharp = image.filter(ImageFilter.SHARPEN)

plt.imshow(im_sharp)
plt.show()

#分解圖形顏色 例如RGB的紅綠藍
#看不出效果
r,g,b = im_sharp.split()

plt.imshow(r)
plt.show()

plt.imshow(g)
plt.show()

plt.imshow(b)
plt.show()

print('------------------------------------------------------------')	#60個


image = Image.open(filename)

gray_iamge = image.convert('L')

plt.imshow(gray_iamge)
plt.show()

print('------------------------------------------------------------')	#60個


image = Image.open(filename)

black_and_white = image.convert('1')

plt.imshow(black_and_white)
plt.show()

print('------------------------------------------------------------')	#60個





#調整資料夾內所有圖片檔影像寬度, 加logo
      
import sys, os, glob
from PIL import Image, ImageDraw
import shutil

source_dir = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
target_dir = 'C:/_git/vcs/_1.data/______test_files2/resized_pic'
#logo_filename = 'C:/_git/vcs/_1.data/______test_files1/burn.bmp'        #fail, bad transparency mask
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/logo.png'

#準備輸出資料夾 若已存在, 則先刪除再建立 若不存在, 則建立
if os.path.exists(target_dir):
        #os.remove(target_dir)  #存取被拒 不可用
        shutil.rmtree(target_dir)
if not os.path.exists(target_dir):
        os.mkdir(target_dir)

image_W = 800

print("將資料夾 " + source_dir + " 內所有圖片檔調整寬度成 " + str(image_W) + " 像素")

print('Processing: {}'.format(source_dir))

#單層
allfiles = glob.glob(source_dir + '/*.jpg') + glob.glob(source_dir + '/*.png')

logo = Image.open(logo_filename)    #PIL讀取本機圖片
logo = logo.resize((150, 150))   #調整圖像大小
#logo.show()

for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	image = Image.open(target_image)    #PIL讀取本機圖片
	W, H = image.size
	image = image.resize((800, int(800 / float(W) * H)))
	image.paste(logo, (0, 0), logo)
	image.save(target_dir + '/' + filename)
	image.close()

print("完成")
print('輸出圖片資料夾 : ', target_dir)

print('------------------------------------------------------------')	#60個

image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#print('顯示原圖')
#plt.imshow(image1)
#plt.show()

image1g = image1.convert('L')	#轉換成灰階圖像
plt.imshow(image1g)      #灰階圖
plt.show()

W, H = image1g.size
print('原圖大小 W =', W, ', H =', H)

x_st = 100
y_st = 200
w = 200
h = 200
image2 = image1g.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image2)
plt.show()

image2_hist = image2.histogram()

W2, H2 = 400, 200
print('把原圖轉成', W2, 'X', H2, '大小')
image3 = image1.resize((W2, H2), Image.LANCZOS)

plt.imshow(image3)
plt.show()

image1g = image3.convert('L')	#轉換成灰階圖像
hist = image1g.histogram()

r, g, b = image3.split()   #r, g, b為三個通道的list
print('r', r)
print('g', g)
print('b', b)
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

print('len = ', len(image2_hist))
ind = np.arange(0, len(image2_hist))

plt.plot(ind, image2_hist, color = 'cyan', label = 'cropped')
plt.plot(ind, hist, color = 'black', lw = 2, label = 'original')
plt.plot(ind, r_hist, color = 'red', label = 'Red Plane')
plt.plot(ind, g_hist, color = 'green', label = 'Green Plane')
plt.plot(ind, g_hist, color = 'blue', label = 'Blue Plane')
plt.xlim(0-10, 256+10)
plt.ylim(0, 8000)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

from PIL import ImageChops

def compare_images(filename1, filename2, threshold=0.8):
    #比較兩張圖像的相似度，返回相似度值（0~1之間的浮點數）
    image1 = Image.open(filename1).convert('RGBA')
    image2 = Image.open(filename2).convert('RGBA')
    diff = ImageChops.difference(image1, image2)
    histogram = diff.histogram()
    pixels = sum(histogram)
    similarity = 1 - (pixels / float(image1.size[0] * image1.size[1] * 3))
    print(similarity)
    return similarity >= threshold

# 測試比較相似度
filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.bmp'
is_similar = compare_images(filename1, filename2)
print('相似度:', is_similar)

print('------------------------------------------------------------')	#60個

import torchvision.transforms as transforms

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sample.jpg'
image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image)
plt.show()

print("RGB圖像的維度：", np.array(image).shape)
image_dim_len = len(np.array(image).shape)
print("The dim of Image: ", image_dim_len)

# RGB轉換成灰階圖像
image_transforms = transforms.Compose([transforms.Grayscale(1)])

image = image_transforms(image)
# 輸出灰度圖像的維度
print("灰度圖像維度： ", np.array(image).shape)
image_dim_len = len(np.array(image).shape)
print("The dim of Image: ", image_dim_len)

#1
#轉為二值圖像，非黑即白。每個像素用8個bit表示，0表示黑，255表示白。
image_1 = image.convert('1')	#轉換成二值化圖像
plt.imshow(image_1)

plt.show()


"""
#L
#轉為灰度圖像，每個像素用8個bit表示，0表示黑，255表示白，其他數字表示不同的灰度。
#轉換公式：L = R * 299/1000 + G * 587/1000+ B * 114/1000。
image_L = image.convert('L')	#轉換成灰階圖像
plt.imshow(image_L)
plt.show()

#P
image_P = image.convert('P')
plt.imshow(image_P)
plt.show()

#RGB
image_RGB = image.convert('RGB')
plt.imshow(image_RGB)
plt.show()

#RGBA
image_RGBA = image.convert('RGBA')
plt.imshow(image_RGBA)
plt.show()

#CMYK
image_CMYK = image.convert('CMYK')
plt.imshow(image_CMYK)
plt.show()

#YCbCr
image_YCbCr = image.convert('YCbCr')
plt.imshow(image_YCbCr)
plt.show()

#I
image_I = image.convert('I')
plt.imshow(image_I)
plt.show()

#F
image_F = image.convert('F')
plt.imshow(image_F)
plt.show()

"""
print("------------------------------------------------------------")  # 60個

from PIL import Image

bg = Image.new("RGB", (1200, 800), "#000000")  # 產生一張 1200x800 的全黑圖片
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")  # 開啟圖片
    img = img.resize((300, 400))  # 縮小尺寸為 300x400
    x = (i - 1) % 4  # 根據開啟的順序，決定 x 座標
    y = (i - 1) // 4  # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(img, (x * 300, y * 400))  # 貼上圖片

bg.save("oxxostudio.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageOps

bg = Image.new("RGB", (1240, 840), "#000000")  # 因為擴張，所以將尺寸改成 1240x840
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")
    img = img.resize((300, 400))
    img = ImageOps.expand(img, 20, "#ffffff")  # 擴張邊緣，產生邊框
    x = (i - 1) % 4
    y = (i - 1) // 4
    bg.paste(img, (x * 300, y * 400))

bg.save("oxxostudio.jpg")

print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")  # 開啟風景圖
icon = Image.open("./oxxostudio-icon.png")  # 開啟浮水印 icon
img.paste(icon, (0, 0), icon)  # 將風景圖貼上 icon

print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")
icon = Image.open("./oxxostudio-icon.png")

img_w, img_h = img.size  # 取得風景圖尺寸
icon_w, icon_h = icon.size  # 取得 icon 尺寸
x = int((img_w - icon_w) / 2)  # 計算置中時 icon 左上角的 x 座標
y = int((img_h - icon_h) / 2)  # 計算置中時 icon 左上角的 y 座標

img.paste(icon, (x, y), icon)  # 設定 icon 左上角座標

print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

imgs = glob.glob("./demo/*.jpg")  # 讀取 demo 資料夾裡所有的圖片
icon = Image.open("./oxxostudio-icon.png")
for i in imgs:
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    img = Image.open(i)  # 開啟圖片
    img.paste(icon, (0, 0), icon)  # 加入浮水印
    img.save(f"./demo/watermark/{name}")  # 以原本的名稱存檔

print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")  # 準備合成浮水印的圖
img2 = Image.open("./watermark-photo.jpg")  # 底圖
icon = Image.open("./oxxostudio-icon.png")

img_w, img_h = img.size
icon_w, icon_h = icon.size
x = int((img_w - icon_w) / 2)
y = int((img_h - icon_h) / 2)
img.paste(icon, (x, y), icon)  # 合成浮水印
img.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img2.paste(img, (0, 0), img)  # 合成底圖
img2.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
w, h = img.size  # 讀取圖片長寬
level = 50  # 設定縮小程度
img2 = img.resize((int(w / level), int(h / level)))  # 縮小圖片
img2 = img2.resize((w, h), resample=Image.NEAREST)  # 放大圖片為原始大小
img2.save("tmp_pic01.jpg")  # 存檔

print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")
w, h = img.size
level = 20
img2 = img.resize((int(w / level), int(h / level)))
img2 = img2.resize((w, h), resample=Image.NEAREST)

x1, y1 = 60, 60  # 定義選取區域的左上角座標
x2, y2 = 250, 250  # 定義選取區域的右上角座標
area = img2.crop((x1, y1, x2, y2))  # 裁切區域
img.paste(area, (x1, y1))  # 在原本的圖片裡貼上馬賽克區域





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



image = Image.open(filename)           # 建立Pillow物件
width, height = image.size

newPict1 = image.resize((width*2, height))   # 寬度是2倍
plt.imshow(newPict1)
plt.show()

newPict2 = image.resize((width, height*2))   # 高度是2倍
plt.imshow(newPict2)
plt.show()


print("------------------------------------------------------------")  # 60個



"""

用plot繪制顯示出圖片后，將鼠標移動到圖片上，會在右下角出現當前點的坐標，以及像素值。

三、幾何變換 

Image類有resize()、rotate()和transpose()方法進行幾何變換。

　1、圖像的縮放和旋轉

dst = img.resize((128, 128))
dst = img.rotate(45) # 順時針角度表示

2、轉換圖像

dst = im.transpose(Image.FLIP_LEFT_RIGHT) #左右互換
dst = im.transpose(Image.FLIP_TOP_BOTTOM) #上下互換
dst = im.transpose(Image.ROTATE_90)  #順時針旋轉
dst = im.transpose(Image.ROTATE_180)
dst = im.transpose(Image.ROTATE_270)

transpose()和rotate()沒有性能差別。
"""


image = Image.open(filename)           # 建立Pillow物件
image090=image.rotate(90)  # 旋轉90度
image180=image.rotate(180)  # 旋轉180度
image270=image.rotate(270)  # 旋轉270度

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                       # 建立Pillow物件
image45a=image.rotate(45)  # 旋轉45度
image45b=image.rotate(45, expand=True)  # 旋轉45度圖像擴充

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                     # 建立Pillow物件
image_flip1 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 左右
image_flip2 = image.transpose(Image.FLIP_TOP_BOTTOM)  # 上下

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
cropPict = image.crop((80, 30, 150, 100))   # 裁切區間
cropPict.save("tmp_pic16.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
copyPict = image.copy()                      # 複製
copyPict.save("tmp_pic17.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
copyPict.paste(cropPict, (20, 20))              # 第一次合成
copyPict.paste(cropPict, (20, 100))             # 第二次合成
copyPict.save("tmp_pic18.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個




#PIL之基本設定


""" not ready
from PIL import Image, ImageDraw, ImageFont

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
im = Image.open(filename1)

filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'
image3 = image1.resize((100, 500), Image.ANTIALIAS)
image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片

"""





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





