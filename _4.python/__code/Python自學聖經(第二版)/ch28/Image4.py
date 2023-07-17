from PIL import Image
img = Image.open("img01.jpg")

img1=img.rotate(90) #旋轉90度
img1.save("rotate01.jpg")
img.rotate(180).save("rotate02.jpg")#旋轉180度
img.rotate(45).save("rotate03.jpg") #旋轉45度