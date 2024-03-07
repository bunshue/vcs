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


幾何變換 

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

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

image = Image.open(filename)           # 建立Pillow物件
width, height = image.size

newPict1 = image.resize((width*2, height))   # 寬度是2倍
plt.imshow(newPict1)
plt.show()

newPict2 = image.resize((width, height*2))   # 高度是2倍
plt.imshow(newPict2)
plt.show()

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r)
    image2 = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image2.size)
    image2.save("tmp_pic31_resize.jpg" )

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print(image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image_new = image.resize((w, h))
    print(image_new.size)
    image_new.save("tmp_pic_view_resize.jpg" )

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

with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 350
    image_new = image.crop((x, y, x1, y1))
    print(image_new.size)
    image_new.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

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
image_crop = image_copied.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間
image_copied.paste(image_crop, (20, 20))          # 第一次合成
image_copied.paste(image_crop, (20, 20 + 120))    # 第二次合成
image_copied.paste(image_crop, (20, 20 + 240))    # 第三次合成

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
image_crop = image_copied.crop((x_st, y_st, x_st + w, y_st + h))    # 裁切區間
cropW, cropH = image_crop.size           # 獲得裁切區間的寬與高

W, H = 600, 320                        # 新影像寬與高
image = Image.new('RGB', (W, H), "Yellow")  # 建立新影像
for x in range(20, W - 20, cropW):         # 雙層迴圈合成
    for y in range(20, H - 20, cropH):
        image.paste(image_crop, (x, y))        # 合成

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

#rotate0
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  image2.save("tmp_pic30.jpg")

print('------------------------------------------------------------')	#60個

# rotate1
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  image2.save( "tmp_pic31_rotate.jpg")

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(180)
    image_new.save("tmp_pic_rotate180.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    image_new.save("tmp_pic_rotate111.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    image_new.save("tmp_pic_rotate000.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)     # 建立Pillow物件

print('左右相反')
image1 = image.transpose(Image.FLIP_LEFT_RIGHT)   # 左右

print('上下顛倒')
image2 = image.transpose(Image.FLIP_TOP_BOTTOM)   # 上下

print('旋轉90度')
rotate90 = image.transpose(Image.ROTATE_90)

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image2 = image.transpose(Image.FLIP_LEFT_RIGHT)
    image2.save( "tmp_pic33b.jpg")
    image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image2.save( "tmp_pic33c.jpg")
    image2 = image.transpose(Image.ROTATE_90)
    image2.save( "tmp_pic33d.jpg")
    image2 = image.transpose(Image.ROTATE_180)
    image2.save( "tmp_pic33e.jpg")
    image2 = image.transpose(Image.ROTATE_270)
    image2.save( "tmp_pic33f.jpg")
    image2 = image.transpose(Image.TRANSPOSE)
    image2.save( "tmp_pic33g.jpg")
    image2 = image.transpose(Image.TRANSVERSE)
    image2.save( "tmp_pic33h.jpg")

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save("tmp_pic_transpose1.jpg")
    image_new = image.transpose(Image.FLIP_TOP_BOTTOM)
    image_new.save("tmp_pic_transpose2.jpg")
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save("tmp_pic_transpose3.jpg")
    image_new = image.transpose(Image.ROTATE_180)
    image_new.save("tmp_pic_transpose4.jpg")
    image_new = image.transpose(Image.ROTATE_270)
    image_new.save("tmp_pic_transpose5.jpg")
    image_new = image.transpose(Image.TRANSPOSE)
    image_new.save("tmp_pic_transpose6.jpg")
    image_new = image.transpose(Image.TRANSVERSE)
    image_new.save("tmp_pic_transpose7.jpg")

print("------------------------------------------------------------")  # 60個


with Image.open(filename) as image:
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save("tmp_pic_transpose90.jpg")
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save("tmp_pic_transposeLR.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save('tmp_pic_rotate_90.jpg')
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save('tmp_pic_flip.jpg')

print('------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = Image.open(filename)

r, g, b = image.split()

plt.imshow(image)
plt.title('image')
plt.show()

plt.imshow(r)
plt.title('r')
plt.show()

plt.imshow(g)
plt.title('g')
plt.show()

plt.imshow(b)
plt.title('b')
plt.show()


print('RGB相反排列')
convert_image = Image.merge('RGB', (b, g, r))

plt.imshow(convert_image)
plt.title('bgr')
plt.show()


image = Image.open(filename)    #PIL讀取本機圖片
r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))
convert_image.save('tmp_image_bgr_NG.png')


convert_image = Image.merge('RGB', (r, g, b))
convert_image.save('tmp_image_rgb_OK.png')

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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

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

print('合併圖 2 X 4 a')

bg = Image.new("RGB", (1200, 800), "#000000")  # 產生一張 1200x800 的全黑圖片
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")  # 開啟圖片
    img = img.resize((300, 400))  # 縮小尺寸為 300x400
    x = (i - 1) % 4  # 根據開啟的順序，決定 x 座標
    y = (i - 1) // 4  # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(img, (x * 300, y * 400))  # 貼上圖片

bg.save("tmp_compound2X4a.jpg")

print("------------------------------------------------------------")  # 60個

print('合併圖 2 X 4 b')
from PIL import Image, ImageOps

bg = Image.new("RGB", (1240, 840), "#000000")  # 因為擴張，所以將尺寸改成 1240x840
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")
    img = img.resize((300, 400))
    img = ImageOps.expand(img, 20, "#ffffff")  # 擴張邊緣，產生邊框
    x = (i - 1) % 4
    y = (i - 1) // 4
    bg.paste(img, (x * 300, y * 400))

bg.save("tmp_compound2X4b.jpg")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

img = Image.open(filename)  # 開啟風景圖
icon = Image.open(logo_filename)  # 開啟浮水印 icon
img.paste(icon, (0, 0), icon)  # 將風景圖貼上 icon

#img.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

img = Image.open(filename)
icon = Image.open(logo_filename)

img_w, img_h = img.size  # 取得風景圖尺寸
icon_w, icon_h = icon.size  # 取得 icon 尺寸
x = int((img_w - icon_w) / 2)  # 計算置中時 icon 左上角的 x 座標
y = int((img_h - icon_h) / 2)  # 計算置中時 icon 左上角的 y 座標

img.paste(icon, (x, y), icon)  # 設定 icon 左上角座標

#img.show()

print("------------------------------------------------------------")  # 60個

print('將一個資料夾內的所有圖片加上logo')

import glob
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

imgs = glob.glob("./*.jpg")  # 讀取 demo 資料夾裡所有的圖片, 撈出一層
icon = Image.open(logo_filename)
for i in imgs:
    print(i)
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    img = Image.open(i)  # 開啟圖片
    img.paste(icon, (0, 0), icon)  # 加入浮水印
    img.save(f"./tmp_watermark/{name}")  # 以原本的名稱存檔

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

img = Image.open(filename)  # 準備合成浮水印的圖
img2 = Image.open(filename)  # 底圖
icon = Image.open(logo_filename)

img_w, img_h = img.size
icon_w, icon_h = icon.size
x = int((img_w - icon_w) / 2)
y = int((img_h - icon_h) / 2)
img.paste(icon, (x, y), icon)  # 合成浮水印
img.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img2.paste(img, (0, 0), img)  # 合成底圖
#img2.save("./tmp_elephant_add_watermark.jpg")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

img = Image.open(filename)  # 開啟圖片
w, h = img.size  # 讀取圖片長寬
level = 5  # 設定縮小程度
img2 = img.resize((int(w / level), int(h / level)))  # 縮小圖片
img2 = img2.resize((w, h), resample=Image.NEAREST)  # 放大圖片為原始大小
#img2.save("tmp_elephant_50.jpg")  # 存檔

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

img = Image.open(filename)
w, h = img.size
level = 5
img2 = img.resize((int(w / level), int(h / level)))
img2 = img2.resize((w, h), resample=Image.NEAREST)

x1, y1 = 60, 60  # 定義選取區域的左上角座標
x2, y2 = 250, 250  # 定義選取區域的右上角座標
area = img2.crop((x1, y1, x2, y2))  # 裁切區域
img.paste(area, (x1, y1))  # 在原本的圖片裡貼上馬賽克區域

#img.show()

print('------------------------------------------------------------')	#60個


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
image_crop = image.crop((80, 30, 150, 100))   # 裁切區間
image_crop.save("tmp_pic16.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
image_copy = image.copy()                      # 複製
image_copy.save("tmp_pic17.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)               # 建立Pillow物件
image_copy = image.copy()                          # 複製
image_crop = image_copy.crop((80, 30, 150, 100))    # 裁切區間
image_copy.paste(image_crop, (20, 20))              # 第一次合成
image_copy.paste(image_crop, (20, 100))             # 第二次合成
image_copy.save("tmp_pic18.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

image1 = Image.open(filename1)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片

filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'
image3 = image1.resize((100, 500), Image.LANCZOS)



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image

image = Image.open(filename)

plt.imshow(image)

plt.show()

w,h = image.size

image1 = image.resize((w*2,h), Image.LANCZOS)

plt.imshow(image1)

plt.show()

image2 = image.convert('1')

plt.imshow(image2)

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image

hungPic = Image.open(filename)        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 600
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))
newImage.save("tmp_pic_2.jpg")

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


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img = Image.open(filename)
w,h=img.size #320 240

img1=img.resize((w*2,h))

img2=img.resize((w,h*2))

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
img = Image.open(filename)
imgcopy=img.copy() #複製
#切割貓熊並改變尺寸
img1=imgcopy.crop((190,184,415,350)).resize((160,140))
imgcopy.paste(img1,(40,30)) #貼上
img2=img1.transpose(Image.FLIP_LEFT_RIGHT)#左右翻轉
imgcopy.paste(img2,(220,40))#貼上

print("------------------------------------------------------------")  # 60個


def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(1)  #需延遲,否則會出錯
    os.mkdir(dirname)

import glob
import shutil, os
from time import sleep

image_dir="data"
target_dir = 'tmp_bmp_photo'
target_dir2 = 'tmp_gray_photo'
emptydir(target_dir)
emptydir(target_dir2)
files=glob.glob(image_dir+"\*.jpg") + glob.glob(image_dir+"\*.png")
for i, f in enumerate(files):
    img = Image.open(f)
    img_new = img.resize((800, 600), Image.LANCZOS)
    path,filename = f.split("\\") #路徑、檔名   
    name,ext = filename.split(".") #主檔名、副檔名
    #以bmp格式存檔
    img_new.save(target_dir+'/' + name + 'aaa.bmp')
    
    #轉換為灰階
    img_gray = img_new.convert('L')  
    # gray001.jpg、gray002.jpg...
    outname = str("gray") + str('{:0>3d}').format(i+1) + 'aaa.jpg'
    img_gray.save(target_dir2+'/'+outname)
    print("{} 複製完成!".format(f))
    img.close()   

print('轉換尺寸及灰階處理結束！')

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    w = 200
    h = 200
    image_new = image.crop((x, y, w, h))
    print(image_new.size)
    image_new.save('tmp_pic_crop.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print(image.size)
    w = 200
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image_new = image.resize((w, h))
    print(image_new.size)
    image_new.save('tmp_pic_resize.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 150
    y1 = 200
    image_new = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image_new.size)
    image_new.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r)
    image_new = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image_new.size)
    image_new.save("tmp_pic_resize.jpg" )

print("------------------------------------------------------------")  # 60個


print("縮放和黏貼圖像")

filename2 = "C:/_git/vcs/_1.data/______test_files1/bear.jpg"

image1 = Image.open(filename2)
image2 = Image.open(filename)
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

image1.show()

print("------------------------------------------------------------")  # 60個

print("剪裁圖像")

image = Image.open(filename)
rect = 80, 20, 310, 360
image.crop(rect).show()


print("------------------------------------------------------------")  # 60個


print("生成縮略圖")

image = Image.open(filename)
size = 128, 128
image.thumbnail(size)
image.show()

print('------------------------------------------------------------')	#60個


#crop
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 300
    image2 = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image2.size)
    image2.save("tmp_pic29.jpg")

print('------------------------------------------------------------')	#60個






with Image.open(filename) as image:
    image_new = image.rotate(180)
    image_new.save('tmp_pic_rotate.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    image_new.save('tmp_pic_rotate30.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    image_new.save('tmp_pic_rotate30_zero.jpg')

print('------------------------------------------------------------')	#60個

print('保持圖片原始大小之旋轉')
with Image.open(filename) as image:
  image_new = image.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  image_new.save("tmp_pic_rotate60a.jpg")

print("------------------------------------------------------------")  # 60個

print('保持圖片內容大小之旋轉')
with Image.open(filename) as image:
  image_new = image.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  image_new.save("tmp_pic_rotate60b.jpg")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img = Image.open(filename)

img1=img.rotate(45)#旋轉45度
img2=img.rotate(90) #旋轉90度
img3=img.rotate(180)#旋轉180度

print("------------------------------------------------------------")  # 60個


filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img = Image.open(filename)

img2=img.transpose(Image.FLIP_LEFT_RIGHT)#左右翻轉
img3=img.transpose(Image.FLIP_TOP_BOTTOM)#上下翻轉

print("------------------------------------------------------------")  # 60個




filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img = Image.open(filename) # w,h=img.size #320 240

img1=img.crop((0,0,160,120))
img2=img.crop((161,0,320,120))
img3=img.crop((0,121,160,240))
img4=img.crop((161,121,320,240))

img.close()

print("------------------------------------------------------------")  # 60個

#裁剪圖片
#從原圖片中裁剪感興趣區域（roi),裁剪區域由4-tuple決定，該tuple中信息為(left, upper, right, lower)。 Pillow左邊系統的原點（0，0）為圖片的左上角。坐標中的數字單位為像素點。


img=Image.open(filename)  #打開圖像
plt.figure('Peony')
plt.subplot(1,2,1)
plt.title('origin')
plt.imshow(img),plt.axis('off')

box=(80,100,260,300)
roi=img.crop(box)
plt.subplot(1,2,2)
plt.title('roi')
plt.imshow(roi),plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個


image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
cropWidth, cropHeight = cropPict.size           # 獲得裁切區間的寬與高

width, height = 600, 320                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
        newImage.paste(cropPict, (x, y))        # 合成

newImage.save("tmp_pic19.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個



"""

image = Image.open(filename)
print(image.format, image.size, image.mode)

#image.show()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個

"""


print("------------------------------------------------------------")  # 60個


