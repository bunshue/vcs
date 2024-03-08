"""

OCR，光學字元辨識(Optical Character Recognition) 意思是可以把照片中的文字轉化成文字檔

先 import pytesseract

到下面的網址下載並安裝 tesseract OCR
https://github.com/UB-Mannheim/tesseract/wiki

安裝 tesseract-ocr-w64-setup-5.3.1.20230401.exe

安裝好後找到 pytesseract.exe 的位置，並複製其絕對路徑，通常會在 C:\Program Files\Tesseract-OCR\tesseract.exe。
或是
C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe
"""

print('------------------------------------------------------------')	#60個

from PIL import Image
import pytesseract

#filename = 'C:/_git/vcs/_1.data/______test_files1/ocr01.png'
filename = 'C:/_git/vcs/_1.data/______test_files1/ocr02.jpg'

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
image = Image.open(filename)
#image.show()
result = pytesseract.image_to_string(image, lang="eng")
print(result)

'''
OCR 辨識繁體中文

其實和辨識英文一樣，只是我們要下載繁體中文的訓練資料，
到這邊 https://github.com/tesseract-ocr/tessdata_best/blob/master/chi_tra.traineddata
下載並將檔案放到 C:\Program Files\Tesseract-OCR\tessdata 中，修改 lang 參數變成 chi_tra 就可以啦
'''

filename = 'C:/_git/vcs/_1.data/______test_files1/ocr03.jpg'

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open(filename)
#img.show()
print(pytesseract.image_to_string(img, lang="chi_tra"))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/ocr04.jpg'

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open(filename)
#img.show()
print(pytesseract.image_to_string(img, lang="chi_tra+eng"))    #中英混和
    
    
print('------------------------------------------------------------')	#60個

import pytesseract
import PIL.Image
import PIL.ImageDraw
from PIL import *
from PIL import ImageEnhance
from PIL import Image

# Important variables
user_tesseract_cmd = r'C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
show_image = False

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/captcha/captcha01.jpg'

#Code from https://stackoverflow.max-everyday.com/2019/06/python-opencv-denoising/

def getPixel(image,x,y,G,N):
    L = image.getpixel((x,y))
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

        if(show_image == True):
            im2.show()

        #Very important, tesseract-ocr path here
        pytesseract.pytesseract.tesseract_cmd = user_tesseract_cmd
        
        '''
        code = pytesseract.image_to_string(im2, lang="eng")
        print(code)
        return code
        '''

        image = Image.open(image_path)
        
        if(show_image == True):
            image.show()
            
        code = pytesseract.image_to_string(image, lang = "eng")
        print('解出來的資料 : ', code)

        return code

ccc = CaptchaBroker()
result = ccc.decode(filename)
print('結果')
print(result)





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

