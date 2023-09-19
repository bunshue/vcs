from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

#在圖上寫字 OK, 只能英文字

from PIL import Image, ImageDraw, ImageFont

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式

print("在圖上寫字")
dw = ImageDraw.Draw(image1)

mesg = '牡丹亭'
font = ImageFont.truetype(font_filename, 60)
#fn_w, fn_h = dw.textsize(unicode(mesg, 'utf-8'), font=font)
fn_w, fn_h = dw.textsize(str(mesg), font = font)

x = 100
y = 200
dw.text((x+5, y+5), str(mesg), font=font, fill=(25,25,25))
dw.text((x, y), str(mesg), font=font, fill=(128,255,255))

plt.imshow(image1)
plt.show()

print('------------------------------------------------------------')	#60個

image1 = Image.open(filename)        # 建立Pillow物件
newPic = image1.resize((350,500))

W, H = 450, 700
image2 = Image.new('RGB', (W, H), "Yellow")

image2.paste(newPic, (50,50))

drawObj = ImageDraw.Draw(image2)
name = "牡丹亭"
fontInfo = ImageFont.truetype(font_filename, 60)
drawObj.text((140,600), name, fill = 'Blue', font = fontInfo)

plt.imshow(image2)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖1')

W, H = 300, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(image)

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

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖2')

W, H = 300, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(image)

drawObj.rectangle((0,0,299,299), outline='Black')   # 影像外框線
drawObj.ellipse((30,60,130,100),outline='Black')    # 左眼外框
drawObj.ellipse((65,65,95,95),fill='Blue')          # 左眼
drawObj.ellipse((170,60,270,100),outline='Black')   # 右眼外框
drawObj.ellipse((205,65,235,95),fill='Blue')        # 右眼
drawObj.polygon([(150,120),(180,180),(120,180),(150,120)],fill='Aqua') # 鼻子
drawObj.rectangle((100,210,200,240), fill='Red')    # 嘴   

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖3')

W, H = 600, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立600*300黃色底的影像
drawObj = ImageDraw.Draw(image)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 
fontInfo = ImageFont.truetype('OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)

strCtext = '歡迎來到美國'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype(font_filename, 48)
drawObj.text((50,180), strCtext, fill = 'Blue', font = fontInfo)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖4')

W, H = 600, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立600*300黃色底的影像
drawObj = ImageDraw.Draw(image)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

fontInfo = ImageFont.truetype(font_filename, 48)
drawObj.text((50,180), strCtext, fill = 'Blue', font = fontInfo)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print("作業完成")

print('------------------------------------------------------------')	#60個
