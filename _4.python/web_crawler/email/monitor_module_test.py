import monitor_module

print('------------------------------------------------------------')	#60個

#----------↓↓E-mail資料設定↓↓------------#
gmail_addr = '你的 Gmail 信箱'
gmail_pwd = '信箱密碼'
to_addrs = ['第一個收件者的 E-mail', '第二個收件者的 E-mail']
#----------↓↓簡訊資料設定↓↓------------#
sid = '你的 ACCOUNT SID'
token = '你的 AUTH TOKEN'
us_phone = '你的美國手機號碼'
tw_phone = '你的台灣手機號碼'

#img 影像
msg = monitor_module.get_mime_img('小偷入侵', '鷹眼防盜監視器', '警察局', img)
monitor_module.send_gmail(gmail_addr, gmail_pwd, to_addrs, msg)  # 以 gmail 寄出
monitor_module.send_sms('小偷來了', sid, token, us_phone, tw_phone)

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

import monitor_module
from email.mime.text import MIMEText

gmail_addr = '您的Gmail郵件地址'
gmail_pwd = '您的Gmail密碼'
to_addrs = ['第一個收件者的郵件網路', '第二個收件者的郵件網路']

mime_text = MIMEText('收信愉快', 'plain', 'utf-8')  # ←建立 MIMEText 物件
mime_text['Subject'] = '您好'
mime_text['From'] = '旗標科技'
mime_text['To'] = '親愛的讀者'
mime_text['Cc'] = '親愛的副本接收者'
mime_text = mime_text.as_string()  # ←轉為字串
monitor_module.send_gmail(gmail_addr, gmail_pwd, to_addrs, mime_text)  # ←寄出郵件

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

import monitor_module
from email.mime.image import MIMEImage
import cv2


def get_mime_img(subject, fr, to, img):
    # 將 img 編碼為 JPGE 格式，[1]為返回資料, [0]為返回是否成功
    img_encode = cv2.imencode('.jpg', img)[1]
    # 再將資料轉為 bytes, 此即為要傳送的資料
    img_bytes = img_encode.tobytes()
    mime_img = MIMEImage(img_bytes)   # 建立 MIMEImage 物件
    mime_img['Content-type'] = 'application/octet-stream'
    mime_img['Content-Disposition'] = 'attachment; filename="pic.jpg"'
    mime_img['Subject'] = subject
    mime_img['From'] = fr
    mime_img['To'] = to
    return mime_img.as_string()  # ←轉為字串後傳回


gmail_addr = '您的Gmail郵件地址'
gmail_pwd = '您的Gmail密碼'
to_addrs = ['第一個收件者的郵件網路', '第二個收件者的郵件網路']


msg = get_mime_img('小偷入侵', '鷹眼防盜監視器', '警察局', img)
monitor_module.send_gmail(gmail_addr, gmail_pwd, to_addrs, msg)  # 以 gmail 寄出郵件

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

from twilio.rest import Client

sid = '您的 ACCOUNT SID'
token = '您的 AUTH　TOKEN'
us_phone = '您的美國手機號碼'
tw_phone = '+您的台灣手機號碼'

#-----↓↓發送簡訊↓↓-----#
send_sms('注意！！家中有人闖入！！', sid, token, us_phone, tw_phone)    # 送出簡訊

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個


