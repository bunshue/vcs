from PIL import Image,ImageDraw
from PIL import ImageFont

img = Image.new("RGB",(400,300),"lightgray") #淡灰色
drawimg=ImageDraw.Draw(img)

#繪多邊形
drawimg.polygon([(200,100),(350,150),(50,150)],fill="blue",outline="red")#屋頂
#繪矩形
drawimg.rectangle((100,150,300,250),fill="green",outline="black") #房間
#繪圓
drawimg.ellipse((300,40,350,90),fill="red")#太陽 
#繪橢圓
drawimg.ellipse((60,80,100,100),fill="white") #白雲一   
drawimg.ellipse((100,60,130,80),fill="white") #白雲二 
#繪文字
drawimg.text((120,170),"e-happy",fill="orange")
myfont=ImageFont.truetype("C:\Windows\Fonts\mingliu.ttc",16)#文字一
drawimg.text((120,200),"文淵閣工作室",fill="red",font=myfont) #文字二 
img.show()
img.save("house.png")
