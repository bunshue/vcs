import qrcode

encode_text = 'http://google.com'

img = qrcode.make(encode_text)

type(img)

img.show()
