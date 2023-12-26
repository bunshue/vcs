# ch17_23_3.py
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=5,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("明志科技大學")
img = qr.make_image(fill_color='blue')
width, height = img.size            # QR code的寬與高
with Image.open('jhung.jpg') as obj:
    obj_width, obj_height = obj.size
    img.paste(obj, ((width-obj_width)//2, (height-obj_height)//2))
img.save("out17_23_3.jpg")




