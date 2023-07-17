from PIL import Image
img = Image.open("img01.jpg") # w,h=img.size #320 240
img1=img.crop((0,0,160,120))
img1.save("crop\crop01.jpg")
img.crop((161,0,320,120)).save("crop\crop02.jpg")
img.crop((0,121,160,240)).save("crop\crop03.jpg")
img.crop((161,121,320,240)).save("crop\crop04.jpg")
img.close()