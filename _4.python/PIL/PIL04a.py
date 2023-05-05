'''
OCR，光學字元辨識(Optical Character Recognition) 意思是可以把照片中的文字轉化成文字檔

先 import pytesseract

到下面的網址下載並安裝 tesseract OCR
https://github.com/UB-Mannheim/tesseract/wiki

安裝 tesseract-ocr-w64-setup-5.3.1.20230401.exe

安裝好後找到 pytesseract.exe 的位置，並複製其絕對路徑，通常會在 C:\Program Files\Tesseract-OCR\tesseract.exe。
或是
C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe
'''

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


filename = 'C:/_git/vcs/_1.data/______test_files1/ocr04.jpg'

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/070601/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open(filename)
#img.show()
print(pytesseract.image_to_string(img, lang="chi_tra+eng"))    #中英混和
    
    

