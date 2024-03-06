from PIL import ImageColor
print(ImageColor.getrgb("#0000ff"))         #(0, 0, 255)
print(ImageColor.getrgb("rgb(0,0,255)"))    #(0, 0, 255)
print(ImageColor.getrgb("rgb(0%,0%,100%)")) #(0, 0, 255)
print(ImageColor.getrgb("Blue"))            #(0, 0, 255)

print(ImageColor.getcolor("#0000ff","RGB"))      #(0, 0, 255)
print(ImageColor.getcolor("rgb(0,0,255)","RGB")) #(0, 0, 255)
print(ImageColor.getcolor("rgb(0,0,255)","RGBA"))#(0, 0, 255, 255)
print(ImageColor.getcolor("Blue","RGBA"))        #(0, 0, 255, 255)