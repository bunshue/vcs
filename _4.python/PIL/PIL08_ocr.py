"""
Pytesseract 辨識圖片中的文字

OCR，光學字元辨識(Optical Character Recognition) 意思是 可以把照片中的文字轉化成文字檔

1. pip install pytesseract
2. 到下面的網址下載並安裝 tesseract OCR

https://github.com/UB-Mannheim/tesseract/wiki

安裝 OCR 程式

64位元最新
tesseract-ocr-w64-setup-5.3.3.20231005.exe
32位元最新
tesseract-ocr-w32-setup-5.3.0.20221222.exe
安裝好後找到 pytesseract.exe 的位置，並複製其絕對路徑，通常會在

C:/Program Files/Tesseract-OCR/tesseract.exe
或
C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe

3. OCR 辨識繁體中文
其實和辨識英文一樣，只是我們要下載繁體中文的訓練資料，
到這邊 https://github.com/tesseract-ocr/tessdata_best/blob/master/chi_tra.traineddata
下載並將檔案放到
C:/Program Files/Tesseract-OCR/tessdata
或
C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tessdata
中
修改 lang 參數變成 chi_tra / chi_sim / jpn / eng 就可以了

按 RAW 才會下載
正中
https://github.com/tesseract-ocr/tessdata_best/tree/main/chi_tra.traineddata
簡中
https://github.com/tesseract-ocr/tessdata_best/tree/main/chi_sim.traineddata
日文
https://github.com/tesseract-ocr/tessdata_best/tree/main/jpn.traineddata
英文
https://github.com/tesseract-ocr/tessdata_best/blob/main/eng.traineddata
"""

print('------------------------------------------------------------')	#60個

import os
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

# pytesseract共同設定

#ocr_program = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
ocr_program = r"C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

import pytesseract
pytesseract.pytesseract.tesseract_cmd = ocr_program #設定OCR程式位置

print('------------------------------------------------------------')	#60個
'''
print("英文OCR")
filename = 'data/ocr/english02.jpg'
image = Image.open(filename)
text = pytesseract.image_to_string(image, lang="eng")
print(text)

print('------------------------------------------------------------')	#60個

print("中文OCR轉正中")
filename = 'data/ocr/red06.jpg'
image = Image.open(filename)
text = pytesseract.image_to_string(image, lang="chi_tra")
print(text)

print("------------------------------------------------------------")  # 60個

print("中文OCR轉簡中")
filename = 'data/ocr/red06.jpg'
image = Image.open(filename)
text = pytesseract.image_to_string(image, lang='chi_sim')
print(text)

print("------------------------------------------------------------")  # 60個

print("中文OCR轉正中 + 英文")
filename = 'data/ocr/red06.jpg'
image = Image.open(filename)
text = pytesseract.image_to_string(image, lang="chi_tra+eng")
print(text)

print('------------------------------------------------------------')	#60個

print("日文OCR")
filename = 'data/ocr/japanese02.jpg'
image = Image.open(filename)
text = pytesseract.image_to_string(image, lang="jpn")
print(text)

print("------------------------------------------------------------")  # 60個

print("車牌")
print("無指定OCR => 英文")
filename = 'data/ocr/carPlate01.jpg'
image = Image.open(filename)
text = pytesseract.image_to_string(image)
print(text)

print('------------------------------------------------------------')	#60個

import PIL.Image
import PIL.ImageDraw
from PIL import *
from PIL import ImageEnhance

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/captcha/captcha01.jpg'

#Code from https://stackoverflow.max-everyday.com/2019/06/python-opencv-denoising/

def getPixel(image,x,y,G,N):
    L = image.getpixel((x,y))  # 取得該點之像素值
    if L > G:
        L = True
    else:
        L = False
 
    nearDots = 0
    if L == (image.getpixel((x - 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y + 1)) > G):
        nearDots += 1
 
    if nearDots < N:
        return image.getpixel((x,y-1))
    else:
        return None

# 降噪 Function
def clearNoise(image,G,N,Z):
    draw = ImageDraw.Draw(image)
 
    for i in range(0,Z):
        for x in range(1,image.size[0] - 1):
            for y in range(1,image.size[1] - 1):
                color = getPixel(image,x,y,G,N)
                if color != None:
                    draw.point((x,y),color)

    return image

class CaptchaBroker():

    def decode(self,image_path):
        # open image

        print(image_path)
        image = Image.open(image_path)

        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(3.0)
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(10.0)

        im2 = image.convert('1')	#轉換成二值化圖像
        im2 = clearNoise(im2,50,4,6)

        w, h = image.size

        """
        code = pytesseract.image_to_string(im2, lang="eng")
        print(code)
        return code
        """

        image = Image.open(image_path)
        
        code = pytesseract.image_to_string(image, lang = "eng")
        print('解出來的資料 : ', code)

        return code

ccc = CaptchaBroker()
result = ccc.decode(filename)
print('結果')
print(result)

print('------------------------------------------------------------')	#60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



'''


print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

def getOCR_Data(filename, ocr_type):

    if ocr_type == "eng":
        print("英文OCR")
    elif ocr_type == "jpn":
        print("日文OCR")
    
    image = Image.open(filename)
    text = pytesseract.image_to_string(image, lang=ocr_type)
    return text

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="派圖 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)

filename = 'data/ocr/english02.jpg'
ocr_type = "eng"

text = getOCR_Data(filename, ocr_type)  
print(text)

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式
plt.imshow(image1)
plt.title(text)


plt.subplot(232)

filename = 'data/ocr/japanese01.jpg'
ocr_type = "jpn"

text = getOCR_Data(filename, ocr_type)  
print(text)

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式
plt.imshow(image1)
plt.title(text)


plt.show()


