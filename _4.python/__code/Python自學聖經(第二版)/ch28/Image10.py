from PIL import Image
img = Image.open("panda.jpg")
imgcopy=img.copy() #複製
#切割貓熊並改變尺寸
img1=imgcopy.crop((190,184,415,350)).resize((160,140))
imgcopy.paste(img1,(40,30)) #貼上
img2=img1.transpose(Image.FLIP_LEFT_RIGHT)#左右翻轉
imgcopy.paste(img2,(220,40))#貼上
# imgcopy.show()
imgcopy.save("panda_paste.jpg")