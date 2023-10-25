import sys
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

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
image = Image.open(filename)
print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

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
imfont = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf", 120)
draw = ImageDraw.Draw(image)
draw.text((100, 100), "Peony", font = imfont, fill = (0, 255, 255, 255))
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

