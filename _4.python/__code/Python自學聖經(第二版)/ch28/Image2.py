from PIL import Image
img1 = Image.new("RGB",(300,200),"rgb(0,0,255)") #藍色
img1.save("blue.jpg")

img2 = Image.new("RGBA",(300,200),"rgba(0,0,255,0)") #透明
img2.save("alpha.png")
