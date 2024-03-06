from PIL import Image
img = Image.open("img01.jpg")

img.transpose(Image.FLIP_LEFT_RIGHT).save("transpose01.jpg")#左右翻轉
img.transpose(Image.FLIP_TOP_BOTTOM).save("transpose02.jpg")#上下翻轉