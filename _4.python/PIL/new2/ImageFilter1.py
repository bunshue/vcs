from PIL import Image,ImageFilter

img = Image.open("panda.jpg")

imgFilter=img.filter(ImageFilter.BLUR)   #模擬
imgFilter.save("BLUR.jpg") 
imgFilter=img.filter(ImageFilter.CONTOUR)#輪廓
imgFilter.save("CONTOUR.jpg")
img.filter(ImageFilter.EMBOSS).save("EMBOSS.jpg")  #浮雕
img.filter(ImageFilter.SHARPEN).save("SHARPEN.jpg")#銳化
