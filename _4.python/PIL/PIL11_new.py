"""
PIL 新進


"""

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageOps
from IPython.display import display

#利用圖片大小強調數量多寡
#載入圖片與顯示圖片的範例

im = Image.open(filename)
display(im)

print('------------------------------------------------------------')	#60個


from pathlib import Path
from PIL import Image

infolder = "testfolder"
value1 = "outputfolder4"
extlist = ["*.jpg","*.png"]

#【函數: 轉存為jpg檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)              #載入圖片檔
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        #-----------------------------------
        filename = Path(readfile).stem+".jpg"   #建立檔案名稱
        savepath = savedir.joinpath(filename)
        if img.format == "PNG":
            newimg = Image.new("RGB", img.size, "white")
            newimg.paste(img, mask=img.split()[3])  #在白底背景繪製圖片
            newimg.save(savepath, format="JPEG", quality=95)    #轉存為JPG圖檔
        elif img.format == "JPEG":
            img.save(savepath, format="JPEG", quality=95)   #轉存為JPG圖檔
        #-----------------------------------
        msg = "在"+savefolder + "轉存" + filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數: 處理資料夾之內的圖片檔】
def savefiles(infolder, savefolder):
    msg = ""
    for ext in extlist:                     #以多個副檔名調查
        filelist = []
        for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
            filelist.append(str(p))         #新增至列表
        for filename in sorted(filelist):   #再替每個檔案排序
            msg += savepng(filename, savefolder)
    return msg

#【執行函數】
msg = savefiles(infolder, value1)
print(msg)

print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageDraw

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename
savefile = "tmp_redline.png"

img = Image.open(infile)
draw = ImageDraw.Draw(img)  #在圖片畫線的準備
draw.line((0, 0, img.width, img.height), fill="RED", width=8) #畫線
img.save(savefile, format="PNG")

print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename#"earth.png"
savefile = "tmp_saveJPG2.jpg"

img = Image.open(infile)
if img.format == "PNG":
    newimg = Image.new("RGB", img.size, "WHITE")
    newimg.paste(img, mask=img)             # 將PNG檔壓在白底圖片上
    newimg.save(savefile, format="JPEG")    # JPG轉存檔案
elif img.format == "JPEG":
    img.save(savefile, format="JPEG")       # JPG轉存檔案

print("------------------------------------------------------------")  # 60個






print('------------------------------------------------------------')	#60個

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns #海生, 自動把圖畫得比較好看
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei

#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image

img1 = Image.new("RGB",(300,200),"rgb(0,0,255)") #藍色
img1.save("tmp_blue.jpg")

img2 = Image.new("RGBA",(300,200),"rgba(0,0,255,0)") #透明
img2.save("tmp_alpha.png")

print('------------------------------------------------------------')	#60個

#利用圖片的個數強調數量

#以人形圖示的個數強調數量的範例


# 要排列的圖示個數
num = 10

# 圖片之間的邊界
margin = 5

# 載入圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

im = Image.open(filename)#"human.png"
im_width, im_height = im.size

# 將圖片入作為畫布使用的Image
canvas = Image.new("RGBA", ((im_width + margin) * num, im_height))
for i in range(num):
    canvas.paste(im, ((im_width + margin) * i, 0))

canvas

print('------------------------------------------------------------')	#60個

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
font_filename = 'C:/Windows/Fonts/mingliu.ttc'
myfont=ImageFont.truetype(font_filename, 16)#文字一
drawimg.text((120,200),"文淵閣工作室",fill="red",font=myfont) #文字二 
img.show()
img.save("tmp_house.png")


print('------------------------------------------------------------')	#60個


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




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





# 1 open save show

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
infile = filename#"earth.png"
savefile = "tmp_savePNG1.png"

img = Image.open(infile)      #載入圖片檔
img.save(savefile, format="PNG")    #PNG轉存檔案

print("------------------------------------------------------------")  # 60個



# 2 resize


print('------------------------------------------------------------')	#60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename#"earth.png"
savefile = "tmp_resize2.png"

img = Image.open(infile)
img = img.resize((100, 100), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")

print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
infile = filename#"earthH.png"
savefile = "tmp_resize1.png"

max_size = 100
img = Image.open(infile)
ratio = max_size / max(img.size)    #根據長寬較長的一邊決定縮放比率
w = int(img.width * ratio)
h = int(img.height * ratio)
img = img.resize((w, h), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")

#調整圖片大小的範例

mini_im = im.resize((int(im.size[0] * 0.2), int(im.size[1] * 0.2)))
display(mini_im)
print(mini_im.size)


print('------------------------------------------------------------')	#60個



# 3 crop 無
# 4 



