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
