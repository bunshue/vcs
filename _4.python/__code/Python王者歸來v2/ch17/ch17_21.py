# ch17_21.py
from PIL import Image, ImageDraw

newImage = Image.new('RGBA', (300, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

drawObj.rectangle((0,0,299,299), outline='Black')   # 影像外框線
drawObj.ellipse((30,60,130,100),outline='Black')    # 左眼外框
drawObj.ellipse((65,65,95,95),fill='Blue')          # 左眼
drawObj.ellipse((170,60,270,100),outline='Black')   # 右眼外框
drawObj.ellipse((205,65,235,95),fill='Blue')        # 右眼
drawObj.polygon([(150,120),(180,180),(120,180),(150,120)],fill='Aqua') # 鼻子
drawObj.rectangle((100,210,200,240), fill='Red')    # 嘴   
newImage.save("out17_21.png")








