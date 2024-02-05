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
qrcode_image.save('tmp_qrcode01.jpg')



"""


