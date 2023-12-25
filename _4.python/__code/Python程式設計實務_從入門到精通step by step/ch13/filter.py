from PIL import Image,ImageFilter
im=Image.open("pic/car.jpg")
new=im.filter(ImageFilter.EDGE_ENHANCE)
new.show()
