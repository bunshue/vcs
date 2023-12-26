# ex17_4.py
from PIL import Image
from PIL import ImageFilter
rushMore = Image.open("palace.png")       # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("fig17_4_BLUR.png")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("fig17_4_CONTOUR.png")
filterPict = rushMore.filter(ImageFilter.DETAIL)
filterPict.save("fig17_4_DETAIL.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE)
filterPict.save("fig17_4_EDGE_ENHANCE.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE_MORE)
filterPict.save("fig17_4_EDGE_ENHANCE_MORE.png")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("fig17_4_EMBOSS.png")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("fig17_4_FIND_EDGES.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH)
filterPict.save("fig17_4_SMOOTH.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH_MORE)
filterPict.save("fig17_4_SMOOTH_MORE.png")
filterPict = rushMore.filter(ImageFilter.SHARPEN)
filterPict.save("fig17_4_SHARPEN.png")





