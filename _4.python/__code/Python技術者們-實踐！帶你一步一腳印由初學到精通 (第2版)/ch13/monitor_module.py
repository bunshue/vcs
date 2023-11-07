from twilio.rest import Client
import cv2
from email.mime.image import MIMEImage
import smtplib


def send_gmail(gmail_addr, gmail_pwd, to_addrs, msg):
    smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)  # 建立 SMTP 物件
    print(smtp_gmail.ehlo())	    # Say Hello
    print(smtp_gmail.starttls())	 # 啟動 TLS 加密模式
    print(smtp_gmail.login(gmail_addr, gmail_pwd))  # 登入
    status = smtp_gmail.sendmail(gmail_addr, to_addrs, msg)	  # 寄出
    if not status:
        print('寄信成功')
    else:
        print('寄信失敗', status)
    smtp_gmail.quit()  # 結束與郵件伺服器的連線


#------------------------------------#


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


#------------------------------------#


def send_sms(text, sid, token, us_phone, tw_phone):
    client = Client(sid, token)    # 建立 Client 物件
    sms = client.messages.create(from_=us_phone,
                                 to=tw_phone,
                                 body=text)
    print('簡訊發送時間: ', sms.date_created)
