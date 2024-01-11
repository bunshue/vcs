from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

im = Image.new("RGB", (400,300), '#00FF00')
draw=ImageDraw.Draw(im)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#im.show()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

im = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(im)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#im.show()

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
pic=im.convert("1")
#pic.show()

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print(im.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 350
    new_im = im.crop((x, y, x1, y1))
    print(new_im.size)
    new_im.save("pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as im:
    new_im = ImageEnhance.Brightness(im).enhance(2.5)
    new_im.save("pic_brightness.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter

im=Image.open(filename)
new=im.filter(ImageFilter.EDGE_ENHANCE)
#new.show()

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
print('圖檔格式: ',im.format)
print('圖檔的色彩模式: ',im.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ',im.size)
print('圖片的寬度，單位像素(pixels): ',im.width)
print('圖片的高度，單位像素(pixels): ',im.height)

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print(im.size)
    w=100
    r = w/im.size[0]
    h = int(im.size[1]*r) #依縮放比例計算高度
    new_im = im.resize((w, h))
    print(new_im.size)
    new_im.save("pic_view_resize.jpg" )

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.rotate(180)
    new_im.save("pic_rotate180.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    new_im.save("pic_rotate111.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    new_im.save("pic_rotate000.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.transpose(Image.ROTATE_90)
    new_im.save("pic_transpose90.jpg")
    new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
    new_im.save("pic_transposeLR.jpg")

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
im.save("pic_quality95.jpg", quality=95 )
im.close()

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
im.save("pic_quality_default.jpg")
im.close()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageDraw,ImageFont
im=Image.open(filename)
imfont=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(im)
draw.text((50,50),"牡丹亭",font=imfont,fill=(0,255,255,255))
im.show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
