from PIL import Image
img = Image.open("img01.jpg")
img.show()
w,h=img.size
print(w,h) #320 240
filename=img.filename
print(filename) #img01.jpg