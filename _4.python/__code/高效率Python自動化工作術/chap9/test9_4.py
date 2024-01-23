from PIL import Image
from PIL import ImageDraw

infile = "earth.png"
savefile = "redline.png"

img = Image.open(infile)
draw = ImageDraw.Draw(img)  #在圖片畫線的準備
draw.line((0, 0, img.width, img.height), fill="RED", width=8) #畫線
img.save(savefile, format="PNG")

