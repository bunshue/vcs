# ch17_23_1.py
import qrcode

codeText = 'Python王者歸來'
img = qrcode.make(codeText)                 # 建立QR code 物件
print("檔案格式", type(img))
img.save("out17_23_1.jpg")




