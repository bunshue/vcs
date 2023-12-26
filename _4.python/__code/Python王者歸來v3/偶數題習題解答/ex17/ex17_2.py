# ex17_2.py
from PIL import Image

hungPic = Image.open("hung.jpg")        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 600
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))
newImage.save("fig17_2.jpg")





