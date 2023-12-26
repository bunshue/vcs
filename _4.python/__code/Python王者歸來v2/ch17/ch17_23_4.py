# ch17_23_4.py
import qrcode

vc_str = '''
BEGIN:VCARD
FN:洪錦魁
TEL;CELL:0900123123
TEL;FAX:02-27320553
ORG:深智公司
TITLE:作者
EMAIL:jiinkwei@me.com
URL:https://www.deepmind.com.tw
ADR:台北市基隆路
END:VCARD
'''

img = qrcode.make(vc_str)
img.save("out17_23_4.jpg")




