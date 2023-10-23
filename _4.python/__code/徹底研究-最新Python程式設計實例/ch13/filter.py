from PIL import Image,ImageFilter
im=Image.open("images/elephant.jpg")
new=im.filter(ImageFilter.EDGE_ENHANCE)
new.show()
