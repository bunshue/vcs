from PIL import Image,ImageDraw,ImageFont
im=Image.open("images/airport.jpg")
imfont=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(im)
draw.text((1400,100),"Tailand View",font=imfont,fill=(0,255,255,255))
im.show()
