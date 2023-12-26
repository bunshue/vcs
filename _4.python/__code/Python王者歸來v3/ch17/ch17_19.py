# ch17_19.py
from PIL import Image
from PIL import ImageFilter
rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("out17_19_BLUR.jpg")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("out17_19_CONTOUR.jpg")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("out17_19_EMBOSS.jpg")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("out17_19_FIND_EDGES.jpg")







