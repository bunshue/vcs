# ch17_23_2.py
import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data("明志科技大學")
img = qr.make_image(fill_color='blue', back_color='yellow')
img.save("out17_23_2.jpg")




