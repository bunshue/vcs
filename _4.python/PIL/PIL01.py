'''

PIL 圖片相關的處理

無 影像處理

縮放
裁剪
複製
合成
旋轉
鏡射


'''

import sys
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print('測試 縮放 resize')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式
W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

print('寬度變2倍, 高度變一半')
W2, H2 = W * 2, H // 2
print('把原圖轉成', W2, 'X', H2, '大小')
image2 = image1.resize((W2, H2), Image.ANTIALIAS)

plt.imshow(image2)
plt.show()

print('------------------------------------------------------------')	#60個

print('測試 裁剪 crop')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式
W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

x_st = 100
y_st = 200
w = 200
h = 200
#                     x_st  y_st    x_sp     y_sp
image2 = image1.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間

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
w = 305 / 4
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
w = 305 / 4
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
plt.imshow(image.rotate(90))
plt.show()

print('旋轉180度')
plt.imshow(image.rotate(180))
plt.show()

print('旋轉270度')
plt.imshow(image.rotate(270))
plt.show()

print('旋轉90度')
rotate_image = image.transpose(Image.ROTATE_90)
plt.imshow(rotate_image)
plt.show()

print('旋轉45度')
plt.imshow(image.rotate(45))
plt.show()

print('旋轉45度 + 圖像擴充')
plt.imshow(image.rotate(45, expand = True))
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('左右相反')
plt.imshow(image.transpose(Image.FLIP_LEFT_RIGHT))   # 左右
plt.show()

print('上下顛倒')
plt.imshow(image.transpose(Image.FLIP_TOP_BOTTOM))   # 上下
plt.show()

print('------------------------------------------------------------')	#60個




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

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sample.jpg'
filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
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
image3 = image1.resize((W2, H2), Image.ANTIALIAS)

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

ind = np.arange(0, len(image2_hist))

plt.plot(ind, image2_hist, color = 'cyan', label = 'cropped')
plt.plot(ind, hist, color = 'black', lw = 2, label = 'original')
plt.plot(ind, r_hist, color = 'red', label = 'Red Plane')
plt.plot(ind, g_hist, color = 'green', label = 'Green Plane')
plt.plot(ind, g_hist, color = 'blue', label = 'Blue Plane')
plt.xlim(0, 255)
plt.ylim(0, 8000)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

import sys

import matplotlib.pyplot as plt
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/flower.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))

plt.imshow(convert_image)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

black_and_white = image.convert('1')

plt.imshow(black_and_white)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

gray_iamge = image.convert('L')

plt.imshow(gray_iamge)
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


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


import numpy as np
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

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


'''
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

'''

'''  ???
image = Image.open(filename)    #PIL讀取本機圖片
r, g, b = image.split()
convert_image = image.merge('RGB', (b, g, r))
convert_image.save('image_bgr.png')
'''

print('------------------------------------------------------------')	#60個

# PIL 測試 1

from PIL import Image
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

print('完成')

