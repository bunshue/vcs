from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

im = Image.new("RGB", (400,300), '#00FF00')
draw=ImageDraw.Draw(im)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
im.show()



print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

im = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(im)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
im.show()


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\convert.py

from PIL import Image
im = Image.open("images/食物1.jpg")
pic=im.convert("1")
pic.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\crop.py

from PIL import Image
with Image.open("images/elephant.jpg") as im:
    print(im.size)
    x = 1000
    y = 0
    x1 = 2100
    y1 = 1600
    new_im = im.crop((x, y, x1, y1))
    print(new_im.size)
    new_im.save( "images/elephant _crop.jpg")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\enhance.py

from PIL import Image,ImageEnhance
with Image.open("images/tailand.jpg") as im:
   new_im = ImageEnhance.Brightness(im).enhance(2.5)
   new_im.save( "images/tailand_Brightness.jpg")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\filter.py

from PIL import Image,ImageFilter
im=Image.open("images/elephant.jpg")
new=im.filter(ImageFilter.EDGE_ENHANCE)
new.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\info.py

from PIL import Image
im = Image.open("images/cute.jpg")
print('圖檔格式: ',im.format)
print('圖檔的色彩模式: ',im.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ',im.size)
print('圖片的寬度，單位像素(pixels): ',im.width)
print('圖片的高度，單位像素(pixels): ',im.height)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\resize.py

from PIL import Image
with Image.open("images/view.jpg") as im:
    print(im.size)
    w=200
    r = w/im.size[0]
    h = int(im.size[1]*r) #依縮放比例計算高度
    new_im = im.resize((w, h))
    print(new_im.size)
    new_im.save( "images/view_resize.jpg" )

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\rotate.py

from PIL import Image
with Image.open("images/building.jpg") as im:
  new_im = im.rotate(180)
  new_im.save( "images/building_rotate.jpg")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\rotate30.py

from PIL import Image
with Image.open("images/view.jpg") as im:
  new_im = im.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
  new_im.save( "images/view30.jpg")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\rotate30_zero.py

from PIL import Image
with Image.open("images/view.jpg") as im:
  new_im = im.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
  new_im.save( "images/view30_zero.jpg")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch13\transpose.py

from PIL import Image
with Image.open("images/building.jpg") as im:
  new_im = im.transpose(Image.ROTATE_90)
  new_im.save( "images/building_90.jpg")
  new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
  new_im.save( "images/building_flip.jpg")

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

from PIL import Image
im = Image.open("images/cute.jpg")
im.save("images/kid_high.jpg", quality=95 )
im.close()




print("------------------------------------------------------------")  # 60個


from PIL import Image
im = Image.open("images/cute.jpg")
im.save( "images/kid.jpg" )
im.close()



print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageDraw,ImageFont
im=Image.open("images/airport.jpg")
imfont=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(im)
draw.text((1400,100),"Tailand View",font=imfont,fill=(0,255,255,255))
im.show()


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
