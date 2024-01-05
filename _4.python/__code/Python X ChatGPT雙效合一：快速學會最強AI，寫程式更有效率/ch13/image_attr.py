from PIL import Image
im = Image.open("pic/1.jpg")
print(im.format)
print(im.mode)
print(im.width)
print(im.height)
print(im.size)
