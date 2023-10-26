import qrcode

print('------------------------------------------------------------')	#60個

encode_text = 'http://google.com'

img = qrcode.make(encode_text)

type(img)

img.show()
img.save('aaaa.jpg')

print('------------------------------------------------------------')	#60個

print('qrcode：qrcode產生器')

import qrcode
import qrcode.image.svg

text = '港町十三番地'
#存png檔
img = qrcode.make(text)
img.save('my_qrcode.png')
#存svg檔
img = qrcode.make(text, image_factory=qrcode.image.svg.SvgPathImage)
img.save('my_qrcode.svg')


qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save('my_qrcode2.png')


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



