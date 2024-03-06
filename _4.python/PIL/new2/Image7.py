from PIL import Image
img = Image.open("img01.jpg")
w,h=img.size #320 240
img = img.convert('L')  #先轉換為灰階

for i in range(w):  #i為每一列
    for j in range(h):  #j為每一行
        if img.getpixel((i,j)) <100:  
            img.putpixel((i,j),(0))   #設為黑色
        else:
            img.putpixel((i,j),(255)) #設為白色
img.save("thresh.jpg")
