"""
QR code

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

print('qrcode：qrcode產生器')

import qrcode
import qrcode.image.svg

encode_text = 'https://www.google.com.tw/'

print('qrcode.make 01------------------------------------------------------------')	#60個

qrcode_image = qrcode.make(encode_text)
print("檔案格式", type(qrcode_image))

plt.imshow(qrcode_image)
plt.show()

print('------------------------------------------------------------')	#60個

qrcode_image = qrcode.make(encode_text)  # 要轉換成 QRCode 的文字
qrcode_image.show()  # 顯示圖片
qrcode_image.save("tmp_qrcode08.png")  # 儲存圖片

print("------------------------------------------------------------")  # 60個

qrcode_image = qrcode.make(encode_text, image_factory = qrcode.image.svg.SvgPathImage)  # 要轉換成 QRCode 的文字
# qrcode_image.show()                # SVG 無法使用
qrcode_image.save("tmp_qrcode10.svg")  # 儲存圖片，注意副檔名為 SVG

print("------------------------------------------------------------")  # 60個

#QR code 存 jpg 檔
qrcode_image = qrcode.make(encode_text)                 # 建立QR code 物件
qrcode_image.save("tmp_qrcode01.jpg")

#QR code 存 png 檔
qrcode_image.save('tmp_qrcode02.png')

#QR code 存 svg 檔
qrcode_image = qrcode.make(encode_text, image_factory=qrcode.image.svg.SvgPathImage)
qrcode_image.save('tmp_qrcode03.svg')

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個





print('qrcode.QRCode 01------------------------------------------------------------')	#60個

print('紅色碼、藍色背景')
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encode_text)
qr.make(fit=True)
qrcode_image = qr.make_image(fill_color="red", back_color="blue")

qrcode_image.save('tmp_qrcode04.png')

print("------------------------------------------------------------")  # 60個

print('藍色碼、黃色背景')
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data(encode_text)
qrcode_image = qr.make_image(fill_color='blue', back_color='yellow')
qrcode_image.save("tmp_qrcode05.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.bmp'

qr = qrcode.QRCode(version=5,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data(encode_text)
qrcode_image = qr.make_image(fill_color='blue')
width, height = qrcode_image.size            # QR code的寬與高
with Image.open(filename) as obj:
    obj_width, obj_height = obj.size
    qrcode_image.paste(obj, ((width-obj_width)//2, (height-obj_height)//2))
qrcode_image.save("tmp_qrcode06.jpg")

print('------------------------------------------------------------')	#60個

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(encode_text)  # 要轉換成 QRCode 的文字
qr.make(fit=True)  # 根據參數製作為 QRCode 物件

qrcode_image = qr.make_image()  # 產生 QRCode 圖片
qrcode_image.show()  # 顯示圖片
qrcode_image.save("tmp_qrcode09.png")  # 儲存圖片

print("------------------------------------------------------------")  # 60個

"""
下方的程式使用「進階設定」的方式產生 QRcode，額外載入 qrcode.image.svg，
在 qrcode.QRCode 裡新增 image_factory=qrcode.image.svg.SvgPathImage 參數，
就能產生 SVG 格式的 QRCode 圖片 ( 如果是 SVG 格式圖片無法改變顏色 )。
"""

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    image_factory=qrcode.image.svg.SvgPathImage,
)
qr.add_data(encode_text)
qr.make(fit=True)

qrcode_image = qr.make_image()
# qrcode_image.show()               # SVG 無法使用
qrcode_image.save("tmp_qrcode11.svg")  # 儲存圖片，注意副檔名為 SVG

print("------------------------------------------------------------")  # 60個

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    VerticalBarsDrawer,
    RoundedModuleDrawer,
    HorizontalBarsDrawer,
    SquareModuleDrawer,
    GappedSquareModuleDrawer,
    CircleModuleDrawer,
)

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
)
qr.add_data(encode_text)
qr.make(fit=True)

qrcode_image1 = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
qrcode_image2 = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
qrcode_image3 = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
qrcode_image4 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
qrcode_image5 = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
qrcode_image6 = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
qrcode_image1.save("tmp_qrcode21.png")
qrcode_image2.save("tmp_qrcode22.png")
qrcode_image3.save("tmp_qrcode23.png")
qrcode_image4.save("tmp_qrcode24.png")
qrcode_image5.save("tmp_qrcode25.png")
qrcode_image6.save("tmp_qrcode26.png")

print("------------------------------------------------------------")  # 60個

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import (
    ImageColorMask,
    SolidFillColorMask,
    RadialGradiantColorMask,
    SquareGradiantColorMask,
    VerticalGradiantColorMask,
    HorizontalGradiantColorMask,
)

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(encode_text)
qr.make(fit=True)

qrcode_image1 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SolidFillColorMask((255, 255, 255), (255, 0, 0)),
    module_drawer=RoundedModuleDrawer(),
)
qrcode_image2 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=RadialGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)
qrcode_image3 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SquareGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)
qrcode_image4 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=VerticalGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)
qrcode_image5 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=HorizontalGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)

filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.bmp'
qrcode_image6 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=ImageColorMask((255, 255, 255), filename),
    module_drawer=RoundedModuleDrawer(),
)

qrcode_image1.save("tmp_qrcode31.png")
qrcode_image2.save("tmp_qrcode32.png")
qrcode_image3.save("tmp_qrcode33.png")
qrcode_image4.save("tmp_qrcode34.png")
qrcode_image5.save("tmp_qrcode35.png")

print("------------------------------------------------------------")  # 60個

from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(encode_text)
qr.make(fit=True)

filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.bmp'
qrcode_image = qr.make_image(image_factory=StyledPilImage, embeded_image_path=filename)
qrcode_image.save("tmp_qrcode12.png")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("barcode------------------------------------------------------------")  # 60個

from barcode import EAN13

number = "12345678987654321"  # 要轉換的數字
my_code = EAN13(number)  # 轉換成 barcode
my_code.save("tmp_qrcode13")  # 儲存為 SVG

print("------------------------------------------------------------")  # 60個

from barcode import EAN13
from barcode.writer import ImageWriter  # 載入 barcode.writer 的 ImageWriter

number = "12345678987654321"
my_code = EAN13(number, writer=ImageWriter())  # 添加 writer=ImageWriter()
my_code.save("tmp_qrcode14")

print("------------------------------------------------------------")  # 60個

print('barcode產生器')

#pip install python-barcode

import barcode
from barcode.writer import ImageWriter

print(barcode.PROVIDED_BARCODES)

EAN = barcode.get_barcode_class('ean13')

text = '123456789012'   #EAN僅能用數字, 必為12碼
#存svg檔
ean = EAN(text)
ean.save('ean13_barcode') 
#存png檔
ean = EAN(text, writer=ImageWriter())
ean.save('ean13_barcode')


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




"""
qrcode_image.show()
qrcode_image.save('tmp_qrcode07.jpg')

"""

print("------------------------------------------------------------")  # 60個

