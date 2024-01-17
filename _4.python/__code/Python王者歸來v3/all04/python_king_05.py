# ch17_1.py
from PIL import ImageColor

print(ImageColor.getrgb("#0000ff"))
print(ImageColor.getrgb("rgb(0, 0, 255)"))
print(ImageColor.getrgb("rgb(0%, 0%, 100%)"))
print(ImageColor.getrgb("Blue"))
print(ImageColor.getrgb("red"))






#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_10.py

# ch17_10.py
from PIL import Image

pict = Image.open("rushmore.jpg")           # 建立Pillow物件
pict.rotate(90).save("out17_10_1.jpg")      # 旋轉90度
pict.rotate(180).save("out17_10_2.jpg")     # 旋轉180度
pict.rotate(270).save("out17_10_3.jpg")     # 旋轉270度









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_11.py

# ch17_11.py
from PIL import Image

pict = Image.open("rushmore.jpg")                       # 建立Pillow物件
pict.rotate(45).save("out17_11_1.jpg")                  # 旋轉45度
pict.rotate(45, expand=True).save("out17_11_2.jpg")     # 旋轉45度圖像擴充










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_12.py

# ch17_12.py
from PIL import Image

pict = Image.open("rushmore.jpg")                     # 建立Pillow物件
pict.transpose(Image.FLIP_LEFT_RIGHT).save("out17_12_1.jpg")    # 左右
pict.transpose(Image.FLIP_TOP_BOTTOM).save("out17_12_2.jpg")    # 上下










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_13.py

# ch17_13.py
from PIL import Image

newImage = Image.new('RGBA', (300, 100), "Yellow")
print(newImage.getpixel((150, 50)))      # 列印中心點的色彩
newImage.save("out17_13.png")














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_14.py

# ch17_14.py
from PIL import Image
from PIL import ImageColor

newImage = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):                                # x軸區間在50-250
    for y in range(50, 151):                            # y軸區間在50-150
        newImage.putpixel((x, y), (0, 255, 255, 255))   # 填青色
newImage.save("out17_14_1.png")                         # 第一階段存檔
for x in range(50, 251):                                # x軸區間在50-250            
    for y in range(151, 251):                           # y軸區間在151-250
        newImage.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))
newImage.save("out17_14_2.png")                         # 第一階段存檔


















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_15.py

# ch17_15.py
from PIL import Image

pict = Image.open("rushmore.jpg")           # 建立Pillow物件
cropPict = pict.crop((80, 30, 150, 100))   # 裁切區間
cropPict.save("out17_15.jpg")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_16.py

# ch17_16.py
from PIL import Image

pict = Image.open("rushmore.jpg")           # 建立Pillow物件
copyPict = pict.copy()                      # 複製
copyPict.save("out17_16.jpg")








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_17.py

# ch17_17.py
from PIL import Image

pict = Image.open("rushmore.jpg")               # 建立Pillow物件
copyPict = pict.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
copyPict.paste(cropPict, (20, 20))              # 第一次合成
copyPict.paste(cropPict, (20, 100))             # 第二次合成
copyPict.save("out17_17.jpg")                   # 儲存










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_18.py

# ch17_18.py
from PIL import Image

pict = Image.open("rushmore.jpg")               # 建立Pillow物件
copyPict = pict.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
cropWidth, cropHeight = cropPict.size           # 獲得裁切區間的寬與高

width, height = 600, 320                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
        newImage.paste(cropPict, (x, y))        # 合成

newImage.save("out17_18.jpg")                   # 儲存










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_19.py

# ch17_19.py
from PIL import Image
from PIL import ImageFilter
rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("out17_19_BLUR.jpg")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("out17_19_CONTOUR.jpg")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("out17_19_EMBOSS.jpg")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("out17_19_FIND_EDGES.jpg")








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_2.py

# ch17_2.py
from PIL import ImageColor

print(ImageColor.getcolor("#0000ff", "RGB"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB"))
print(ImageColor.getcolor("Blue", "RGB"))
print(ImageColor.getcolor("#0000ff", "RGBA"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))
print(ImageColor.getcolor("Blue", "RGBA"))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_20.py

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









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_21.py

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









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_22.py

# ch17_22.py
from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Ming-Chi Institute of Technology'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 處理中文字體
strCtext = '明志科技大學'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype('C:\Windows\Fonts\DFZongYiStd-W9.otf', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)
newImage.save("out17_22.png")









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_22_1.py

# ch17_22_1.py
from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Ming-Chi Institute of Technology'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 使用Microsoft所提供的新細明體中文字型處理中文字體
strCtext = '明志科技大學'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)
newImage.save("out17_22_1.png")









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_23.py

# ch17_23.py
import qrcode

codeText = 'http://deepwisdom.com.tw'
img = qrcode.make(codeText)                 # 建立QR code 物件
print("檔案格式", type(img))
img.save("out17_23.jpg")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_23_1.py

# ch17_23_1.py
import qrcode

codeText = 'Python王者歸來'
img = qrcode.make(codeText)                 # 建立QR code 物件
print("檔案格式", type(img))
img.save("out17_23_1.jpg")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_23_2.py

# ch17_23_2.py
import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("明志科技大學")
img = qr.make_image(fill_color='blue', back_color='yellow')
img.save("out17_23_2.jpg")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_23_3.py

# ch17_23_3.py
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=5,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("明志科技大學")
img = qr.make_image(fill_color='blue')
width, height = img.size            # QR code的寬與高
with Image.open('jhung.jpg') as obj:
    obj_width, obj_height = obj.size
    img.paste(obj, ((width-obj_width)//2, (height-obj_height)//2))
img.save("out17_23_3.jpg")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_23_4.py

# ch17_23_4.py
import qrcode

vc_str = '''
BEGIN:VCARD
FN:洪錦魁
TEL;CELL:0900123123
TEL;FAX:02-27320553
ORG:深智公司
TITLE:作者
EMAIL:jiinkwei@me.com
URL:https://deepmind.com.tw
ADR:台北市基隆路
END:VCARD
'''

img = qrcode.make(vc_str)
img.save("out17_23_4.jpg")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_24.py

# ch17_24.py
from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('d:\\Python\\ch17\\atq9305.jpg'))
print(type(text), "   ", text)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_25.py

# ch17_25.py
from PIL import Image
import pytesseract
import time

carDict = {}
myPath = "d:\\Python\\ch17\\"
while True:
    carPlate = input("請掃描或輸入車牌(Q/q代表結束) : ")
    if carPlate == 'Q' or carPlate == 'q':
        break
    carPlate = myPath + carPlate
    keyText = pytesseract.image_to_string(Image.open(carPlate))    
    if keyText in carDict:
        exitTime = time.asctime()
        print("車輛出場時間 : ", keyText, ":", exitTime)
        del carDict[keyText]
    else:
        entryTime = time.asctime()
        print("車輛入場時間 : ", keyText, ":", entryTime)
        carDict[keyText] = entryTime




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_26.py

# ch17_26.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('d:\\Python\\ch17\\data17_26.jpg'),
                                    lang='chi_tra')
print(text)
with open('d:\\Python\\ch17\\out17_26.txt', 'w') as fn:
    fn.write(text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_27.py

# ch17_27.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('d:\\Python\\ch17\\data17_27.jpg'),
                                               lang='chi_sim')
print(text)
with open('d:\\Python\\ch17\\out17_27.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_28.py

# ch17_28.py
from PIL import Image
import os

def batch_resize_images(input_folder, output_folder, size=(300, 300)):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷輸入資料夾中的所有影像檔案
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png')):
            # 打開影像
            img = Image.open(os.path.join(input_folder, filename))
            # 調整影像尺寸
            img = img.resize(size, Image.ANTIALIAS)
            # 保存調整尺寸後的影像到輸出資料夾
            img.save(os.path.join(output_folder, filename))

# 假設有一個包含原始圖片的資料夾 'input_images' 和
# 一個用於存放調整後圖片的資料夾 'output_images'
input_folder = 'input_images'
output_folder = 'output_images'

# 呼叫函數，將所有圖片調整為300x300大小
batch_resize_images(input_folder, output_folder)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_29.py

# ch17_29.py
from PIL import Image
import os

def batch_convert_images(directory, target_format='.jpg'):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            img = Image.open(path)
            rgb_im = img.convert('RGB')  # 轉換為RGB模式以便保存為JPEG
            rgb_im.save(path.replace('.png', target_format), quality=95)

# 呼叫批次更改函數
batch_convert_images('images_directory')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_3.py

# ch17_3.py
from PIL import Image

rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
print("列出物件型態 : ", type(rushMore))
width, height = rushMore.size               # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_30.py

# ch17_30.py
from PIL import Image, ImageDraw, ImageFont

def generate_product_image(product_img_path, background_img_path, promo_text):
    # 加載產品和背景影像
    product_img = Image.open(product_img_path).resize((200, 200))
    background_img = Image.open(background_img_path)
    # 在背景影像上放置產品影像
    background_img.paste(product_img, (50, 50), product_img)
    # 在影像上添加促銷文字
    draw = ImageDraw.Draw(background_img)
    font = ImageFont.truetype("arial.ttf", size=45)
    draw.text((50, 260), promo_text, font=font, fill="white")
    # 保存或返回影像
    background_img.save('output_promo_image.jpg')

generate_product_image('product.png', 'background.jpg', '特價促銷!')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_4.py

# ch17_4.py
from PIL import Image

rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
print("列出物件檔名 : ", rushMore.filename)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_5.py

# ch17_5.py
from PIL import Image

rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
print("列出物件副檔名 : ", rushMore.format)
print("列出物件描述   : ", rushMore.format_description)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_6.py

# ch17_6.py
from PIL import Image

rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
rushMore.save("out17_6.png")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_6_1.py

# ch17_6_1.py
from PIL import Image

rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
rushMore.show()






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_7.py

# ch17_7.py
from PIL import Image

pictObj = Image.new("RGB", (300, 180), "aqua")  # 建立aqua顏色影像
pictObj.save("out17_7.jpg")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_8.py

# ch17_8.py
from PIL import Image

pictObj = Image.new("RGBA", (300, 180))     # 建立完全透明影像
pictObj.save("out17_8.png")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all04\ch17_9.py

# ch17_9.py
from PIL import Image

pict = Image.open("rushmore.jpg")           # 建立Pillow物件
width, height = pict.size
newPict1 = pict.resize((width*2, height))   # 寬度是2倍
newPict1.save("out17_9_1.jpg")
newPict2 = pict.resize((width, height*2))   # 高度是2倍
newPict2.save("out17_9_2.jpg")




print("------------------------------------------------------------")  # 60個

