# ex17_6.py
from PIL import Image, ImageDraw, ImageFont

hungPic = Image.open("hung.jpg")        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 700
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))

drawObj = ImageDraw.Draw(newImage)
name = "洪錦魁"
fontInfo = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 60)
drawObj.text((140,600), name, fill='Blue', font=fontInfo)


newImage.save("fig17_6.jpg")





