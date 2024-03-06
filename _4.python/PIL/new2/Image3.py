from PIL import Image
img = Image.open("img01.jpg")
w,h=img.size #320 240

img1=img.resize((w*2,h))
img1.save("resize01.jpg")
img2=img.resize((w,h*2))
img2.save("resize02.jpg")