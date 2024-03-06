'''

PIL 圖片相關的處理

各種convert


使用函數convert()來進行轉換，它是圖像實例對象的一個方法，接受一個 mode 參數，用以指定一種色彩模式，mode 的取值可以是如下幾種：
· 1 (1-bit pixels, black and white, stored with one pixel per byte)
· L (8-bit pixels, black and white)
· P (8-bit pixels, mapped to any other mode using a colour palette)
· RGB (3x8-bit pixels, true colour)
· RGBA (4x8-bit pixels, true colour with transparency mask)
· CMYK (4x8-bit pixels, colour separation)
· YCbCr (3x8-bit pixels, colour video format)
· I (32-bit signed integer pixels)
· F (32-bit floating point pixels)


'''

import sys
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

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

"""
from PIL import Image,ImageDraw
image = Image.open("captcha.png").convert("L")	#轉換成灰階圖像
"""

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
pic=image.convert("1")
#pic.show()

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
pic = image.convert("1")
plt.imshow(pic)
plt.title('convert L')
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image
from matplotlib import patches
import matplotlib.pyplot as plt

#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'


image1 = Image.open(filename)
  
image = Image.open(filename)
image_1 = image.convert('1')	#轉換成二值化圖像

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image_1)

plt.show()

print('------------------------------------------------------------')	#60個

img = Image.open("data/img01.jpg")
imggray = img.convert('L') #轉換為灰階

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg")
w,h=img.size #320 240
img = img.convert('L')  #先轉換為灰階

for i in range(w):  #i為每一列
    for j in range(h):  #j為每一行
        if img.getpixel((i,j)) <100:  
            img.putpixel((i,j),(0))   #設為黑色
        else:
            img.putpixel((i,j),(255)) #設為白色

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





