# ch17_23.py
import qrcode

codeText = 'http://www.deepstone.com.tw'
img = qrcode.make(codeText)                 # 建立QR code 物件
print("檔案格式", type(img))
img.save("out17_23.jpg")


