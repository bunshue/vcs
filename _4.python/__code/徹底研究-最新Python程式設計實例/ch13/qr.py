import qrcode
im = qrcode.make("http://www.grandtech.info/")
im.save("images/grand_qr.jpg")
