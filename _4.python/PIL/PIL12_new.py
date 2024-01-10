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

from PIL import Image, ImageDraw
image = Image.new("RGB", (400, 300))
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw
image = Image.new("RGB", (400, 300), '#00FF00')
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image
image = Image.open(filename)
print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

print('------------------------------------------------------------')	#60個

from PIL import Image
with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    w = 200
    h = 200
    new_image = image.crop((x, y, w, h))
    print(new_image.size)
    new_image.save('pic_crop.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageEnhance
with Image.open(filename) as image:
   new_image = ImageEnhance.Brightness(image).enhance(2.5)
   new_image.save('pic_brightness.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageFilter
image = Image.open(filename)
plt.imshow(image)
plt.title('原圖')
plt.show()

new = image.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(new)
plt.title('after filter')
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image
image = Image.open(filename)
pic = image.convert("1")
plt.imshow(pic)
plt.title('convert L')
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image
with Image.open(filename) as image:
    print(image.size)
    w = 200
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    new_image = image.resize((w, h))
    print(new_image.size)
    new_image.save('pic_resize.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image
with Image.open(filename) as image:
  new_image = image.rotate(180)
  new_image.save('pic_rotate.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image
with Image.open(filename) as image:
  new_image = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
  new_image.save('pic_rotate30.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image
with Image.open(filename) as image:
  new_image = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
  new_image.save('pic_rotate30_zero.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image
image = Image.open(filename)
image.save('pic_normal.jpg')
image.close()

print('------------------------------------------------------------')	#60個

from PIL import Image
image = Image.open(filename)
image.save('pic_high.jpg', quality = 95)
image.close()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw, ImageFont
image = Image.open(filename)
imfont = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf", 40)
draw = ImageDraw.Draw(image)
draw.text((100, 100), 'Peony', font = imfont, fill = (0, 255, 255, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image
with Image.open(filename) as image:
  new_image = image.transpose(Image.ROTATE_90)
  new_image.save('pic_rotate_90.jpg')
  new_image = image.transpose(Image.FLIP_LEFT_RIGHT)
  new_image.save('pic_flip.jpg')

print('------------------------------------------------------------')	#60個



from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
print(im.format)
print(im.mode)
print(im.width)
print(im.height)
print(im.size)

print("------------------------------------------------------------")  # 60個

print('保持圖片原始大小之旋轉')
with Image.open(filename) as im:
  new_im = im.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  new_im.save("pic_rotate60a.jpg")

print("------------------------------------------------------------")  # 60個

print('保持圖片內容大小之旋轉')
with Image.open(filename) as im:
  new_im = im.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  new_im.save("pic_rotate60b.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print('原圖片的尺寸大小:',im.size)
    x = 50
    y = 50
    x1 = 150
    y1 = 200
    new_im = im.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', new_im.size)
    new_im.save("pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print('原圖片的尺寸大小:',im.size)
    w=100
    r = w/im.size[0]
    h = int(im.size[1]*r)
    new_im = im.resize((w, h))
    print('圖片經縮放後的尺寸大小:',new_im.size)
    new_im.save("pic_resize.jpg" )

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as im:
    new_im = ImageEnhance.Contrast(im).enhance(0.3)
    new_im.save("pic_contrast.jpg") 

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as im:
    new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
    new_im.save("pic_transpose1.jpg")
    new_im = im.transpose(Image.FLIP_TOP_BOTTOM)
    new_im.save("pic_transpose2.jpg")
    new_im = im.transpose(Image.ROTATE_90)
    new_im.save("pic_transpose3.jpg")
    new_im = im.transpose(Image.ROTATE_180)
    new_im.save("pic_transpose4.jpg")
    new_im = im.transpose(Image.ROTATE_270)
    new_im.save("pic_transpose5.jpg")
    new_im = im.transpose(Image.TRANSPOSE)
    new_im.save("pic_transpose6.jpg")
    new_im = im.transpose(Image.TRANSVERSE)
    new_im.save("pic_transpose7.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter
im=Image.open(filename)
new=im.filter(ImageFilter.EDGE_ENHANCE)
#new.show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

