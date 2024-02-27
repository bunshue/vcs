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

encode_text = 'https://www.google.com.tw/'

print('------------------------------------------------------------')	#60個

qrcode_image = qrcode.make(encode_text)
print("檔案格式", type(qrcode_image))

plt.imshow(qrcode_image)
plt.show()

print('------------------------------------------------------------')	#60個

#QR code 存 jpg/png 檔
qrcode_image = qrcode.make(encode_text)                 # 建立QR code 物件
qrcode_image.save("tmp_qrcode01.jpg")
qrcode_image.save('tmp_qrcode02.png')

#QR code 存 svg 檔
import qrcode.image.svg
qrcode_image = qrcode.make(encode_text, image_factory=qrcode.image.svg.SvgPathImage)
qrcode_image.save('tmp_qrcode03.svg')


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
img = qr.make_image(fill_color='blue', back_color='yellow')
img.save("tmp_qrcode05.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.bmp'

qr = qrcode.QRCode(version=5,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data(encode_text)
img = qr.make_image(fill_color='blue')
width, height = img.size            # QR code的寬與高
with Image.open(filename) as obj:
    obj_width, obj_height = obj.size
    img.paste(obj, ((width-obj_width)//2, (height-obj_height)//2))
img.save("tmp_qrcode06.jpg")

print('------------------------------------------------------------')	#60個


"""
qrcode_image.show()
qrcode_image.save('tmp_qrcode07.jpg')



"""






print("------------------------------------------------------------")  # 60個

import qrcode

img = qrcode.make(encode_text)  # 要轉換成 QRCode 的文字
img.show()  # 顯示圖片 ( Colab 不適用 )
img.save("tmp_qrcode08.png")  # 儲存圖片


print("------------------------------------------------------------")  # 60個

import qrcode

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
)
qr.add_data(encode_text)  # 要轉換成 QRCode 的文字
qr.make(fit=True)  # 根據參數製作為 QRCode 物件

img = qr.make_image()  # 產生 QRCode 圖片
img.show()  # 顯示圖片 ( Colab 不適用 )
img.save("tmp_qrcode09.png")  # 儲存圖片


print("------------------------------------------------------------")  # 60個

import qrcode
import qrcode.image.svg

img = qrcode.make(
    encode_text, image_factory=qrcode.image.svg.SvgPathImage
)  # 要轉換成 QRCode 的文字
# img.show()                # SVG 無法使用
img.save("tmp_qrcode10.svg")  # 儲存圖片，注意副檔名為 SVG

"""
下方的程式使用「進階設定」的方式產生 QRcode，額外載入 qrcode.image.svg，在 qrcode.QRCode 裡新增 image_factory=qrcode.image.svg.SvgPathImage 參數，就能產生 SVG 格式的 QRCode 圖片 ( 如果是 SVG 格式圖片無法改變顏色 )。
"""

import qrcode
import qrcode.image.svg

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    image_factory=qrcode.image.svg.SvgPathImage,
)
qr.add_data(encode_text)
qr.make(fit=True)

img = qr.make_image()
# img.show()               # SVG 無法使用
img.save("tmp_qrcode11.svg")  # 儲存圖片，注意副檔名為 SVG


print("------------------------------------------------------------")  # 60個

import qrcode
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

img1 = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
img2 = qr.make_image(
    image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer()
)
img3 = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
img4 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img5 = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
img6 = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
img1.save("tmp_qrcode21.png")
img2.save("tmp_qrcode22.png")
img3.save("tmp_qrcode23.png")
img4.save("tmp_qrcode24.png")
img5.save("tmp_qrcode25.png")
img6.save("tmp_qrcode26.png")


print("------------------------------------------------------------")  # 60個

import qrcode
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

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
)
qr.add_data(encode_text)
qr.make(fit=True)

img1 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SolidFillColorMask((255, 255, 255), (255, 0, 0)),
    module_drawer=RoundedModuleDrawer(),
)
img2 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=RadialGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)
img3 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SquareGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)
img4 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=VerticalGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)
img5 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=HorizontalGradiantColorMask((255, 255, 255), (255, 0, 0), (0, 0, 255)),
    module_drawer=RoundedModuleDrawer(),
)
img6 = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=ImageColorMask((255, 255, 255), "mona.jpg"),
    module_drawer=RoundedModuleDrawer(),
)

img1.save("tmp_qrcode31.png")
img2.save("tmp_qrcode32.png")
img3.save("tmp_qrcode33.png")
img4.save("tmp_qrcode34.png")
img5.save("tmp_qrcode35.png")


print("------------------------------------------------------------")  # 60個

import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
)
qr.add_data(encode_text)
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="mona.jpg")
img.save("tmp_qrcode12.png")


print("------------------------------------------------------------")  # 60個

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




