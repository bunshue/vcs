from PIL import Image
img = Image.open("img01.jpg")
imggray = img.convert('L') #轉換為灰階

imggray.save("gray01.jpg")