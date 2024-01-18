import qrcode

codeText = 'https://www.google.com.tw/'
img = qrcode.make(codeText)
print("檔案格式", type(img))
img.save("tmp_qrcode01.jpg")

print("------------------------------------------------------------")  # 60個

import qrcode

codeText = 'https://www.google.com.tw/'
img = qrcode.make(codeText)
print("檔案格式", type(img))
img.save("tmp_qrcode02.jpg")

print("------------------------------------------------------------")  # 60個

import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("碧雲天黃葉地")
img = qr.make_image(fill_color='blue', back_color='yellow')
img.save("tmp_qrcode03.jpg")

print("------------------------------------------------------------")  # 60個

import qrcode
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.bmp'

qr = qrcode.QRCode(version=5,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("碧雲天黃葉地")
img = qr.make_image(fill_color='blue')
width, height = img.size            # QR code的寬與高
with Image.open(filename) as obj:
    obj_width, obj_height = obj.size
    img.paste(obj, ((width-obj_width)//2, (height-obj_height)//2))
img.save("tmp_qrcode04.jpg")

print("------------------------------------------------------------")  # 60個

import qrcode

vc_str = """
王之渙
涼州詞
黃河遠上白雲間
一片孤城萬仞山
羌笛何須怨楊柳
春風不度玉門關
"""

img = qrcode.make(vc_str)
img.save("tmp_qrcode05.jpg")

print("------------------------------------------------------------")  # 60個


