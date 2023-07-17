from PIL import Image,ImageDraw
img = Image.new("RGB",(400,300),"lightgray") #淡灰色
drawimg=ImageDraw.Draw(img)
  
#繪點
for i in range(0,400,10):
    for j in range(0,300,10):    
        drawimg.point([(i,j)],fill="red")  
#繪直線
for i in range(0,400,10):
    drawimg.line([(i,300),(200,150)],width=2,fill="blue") 
img.show()