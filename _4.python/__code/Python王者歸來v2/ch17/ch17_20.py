# ch17_20.py
from PIL import Image, ImageDraw

newImage = Image.new('RGBA', (300, 300), "Yellow")  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

# 繪製點
for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        drawObj.point([(x,y)], fill='Green')

# 繪製線條, 繪外框線
drawObj.line([(0,0), (299,0), (299,299), (0,299), (0,0)], fill="Black")
# 繪製右上角美工線
for x in range(150, 300, 10):
    drawObj.line([(x,0), (300,x-150)], fill="Blue")
# 繪製左下角美工線
for y in range(150, 300, 10):
    drawObj.line([(0,y), (y-150,300)], fill="Blue")    
newImage.save("out17_20.png")








