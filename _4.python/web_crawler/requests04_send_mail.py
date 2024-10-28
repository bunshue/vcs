# 發送e-mail

print("------------------------------------------------------------")  # 60個

import requests

'''
def get_mailgun_key():
    filename = "C:/_git/vcs/_1.data/______test_files1/_key/mailgun_key.txt"

    import os

    filename = os.path.abspath(filename)
    if not os.path.exists(filename):  # 檢查檔案是否存在
        print("MAILGUN_KEY 檔案不存在, 離開, 檔案 : " + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, "r")
    mailgun_key = fo.read()
    fo.close()

    length = len(mailgun_key)
    if length != 50:
        print("MAILGUN_KEY 錯誤, 離開")
        return ""
    return mailgun_key


def send_simple_message(email_nicknane, email_from, email_to, subject, body):
    mailgun_key = get_mailgun_key()
    length = len(mailgun_key)
    if length != 50:
        print("MAILGUN_KEY 錯誤, 離開")
        return ""

    return requests.post(
        "https://api.mailgun.net/v3/sandboxbfcaff2ba2ce446eb4972796eabec7da.mailgun.org/messages",
        auth=("api", mailgun_key),
        data={
            "from": "%s <%s>" % (email_nicknane, email_from),
            "to": [email_to],
            "subject": subject,
            "text": body,
        },
    )


# 共用的郵件資訊
email_addr_from = "bunshue@gmail.com"
email_addr_from_password = "XXXXXXXXXX"
email_addr_from_nicknane = "王大頭"  # 寄件者顯示的名稱
email_addr_to = "david@insighteyes.com"
email_addr_to_nicknane = "尊敬的收件者"  # 收件者顯示的名稱
email_addr_cc = "bunshue@gmail.com"

mail_subject = "測試郵件標題"  # 郵件標題
mail_body = "測試郵件內容測試郵件內容測試郵件內容測試郵件內容"  # 郵件內容

ret = send_simple_message(
    email_addr_from_nicknane, email_addr_from, email_addr_to, mail_subject, mail_body
)

print(ret)
"""
if ret == '<Response [200]>':
    print('信件已寄出')
else:
    print('寄信失敗')
"""

'''
print("------------------------------------------------------------")  # 60個
print("smtplib ST")
print("------------------------------------------------------------")  # 60個

import smtplib

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("你的信箱", "你的密碼")
from_addr = "你的信箱"
to_addr = "收件人信箱"
msg = "Subject:title\nHello\nWorld!"
status = smtp.sendmail(from_addr, to_addr, msg)
if status == {}:
    print("郵件傳送成功！")
else:
    print("郵件傳送失敗...")
smtp.quit()

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("你好呀！這是用 Python 寄的信～", "plain", "utf-8")  # 郵件內文
msg["Subject"] = "test測試"  # 郵件標題
msg["From"] = "oxxo"  # 暱稱或是 email
msg["To"] = "oxxo.studio@gmail.com"  # 收件人 email
msg["Cc"] = "oxxo.studio@gmail.com, XXX@gmail.com"  # 副本收件人 email ( 開頭的 C 大寫 )
msg["Bcc"] = "oxxo.studio@gmail.com, XXX@gmail.com"  # 密件副本收件人 email

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("你的信箱", "你的密碼")
status = smtp.send_message(msg)  # 改成 send_message
if status == {}:
    print("郵件傳送成功！")
else:
    print("郵件傳送失敗！")
smtp.quit()

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.text import MIMEText

html = """
<h1>hello</h1>
<div>這是 HTML 的內容</div>
<div style="color:red">紅色的字</div>
"""

mail = MIMEText(html, "html", "utf-8")  # plain 換成 html，就能寄送 HTML 格式的信件
mail["Subject"] = "html 的信"
mail["From"] = "oxxo"
mail["To"] = "oxxo.studio@gmail.com"

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("你的信箱", "你的密碼")
status = smtp.send_message(mail)
print(status)
smtp.quit()

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html = """
<h1>hello</h1>
<div>這是 HTML 的內容</div>
<div style="color:red">紅色的字</div>
"""
msg = MIMEMultipart()  # 使用多種格式所組成的內容
msg.attach(MIMEText(html, "html", "utf-8"))  # 加入 HTML 內容
# 使用 python 內建的 open 方法開啟指定目錄下的檔案
with open("meme.jpg", "rb") as file:
    img = file.read()
attach_file = MIMEApplication(img, Name="meme.jpg")  # 設定附加檔案圖片
msg.attach(attach_file)  # 加入附加檔案圖片

msg["Subject"] = "附件是一張搞笑的圖"
msg["From"] = "oxxo"
msg["To"] = "oxxo.studio@gmail.com"

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("oxxo.studio@gmail.com", "你申請的應用程式密碼")
status = smtp.send_message(msg)
print(status)
smtp.quit()

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.text import MIMEText

from_addr = "cshung1961@gmail.com"  # 設定發信帳號
pwd = input("請輸入 %s 的密碼 : " % from_addr)  # 要求輸入發信帳號密碼
to_addr_list = ["cshung@deepwisdom.com.tw", "jiinkwei@me.com"]  # 設定收件人

with open("ex26_2.txt", "rb") as filename:  # 讀取檔案內容
    mailContent = filename.read()
msg = MIMEText(mailContent, "base64", "utf-8")
msg["Content-Type"] = "application/octet-stream"
msg["Content-Disposition"] = 'attachment; filename="ex26_2.txt"'
msg["Subject"] = "傳送Python學習心得附加檔案"
msg["From"] = "學生"
msg["To"] = "cshung@deepwisdom.com.tw"
msg["Cc"] = "jiinkwei@me.com"

mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

import smtplib


def send_gmail(gmail_addr, gmail_pwd, to_addrs, msg):
    smtp_gmail = smtplib.SMTP("smtp.gmail.com", 587)  # 建立 SMTP 物件
    print(smtp_gmail.ehlo())  # Say Hello
    print(smtp_gmail.starttls())  # 啟動 TLS 加密模式
    print(smtp_gmail.login(gmail_addr, gmail_pwd))  # 登入
    status = smtp_gmail.sendmail(gmail_addr, to_addrs, msg)  # 寄出
    if not status:
        print("寄信成功")
    else:
        print("寄信失敗", status)
    smtp_gmail.quit()  # 結束與郵件伺服器的連線


gmail_addr = "您的Gmail郵件地址"
gmail_pwd = "您的Gmail密碼"
to_addrs = ["第一個收件者的郵件網路", "第二個收件者的郵件網路"]
send_gmail(gmail_addr, gmail_pwd, to_addrs, "Subject:Hello\nTesting")
# ↑主旨   ↑內容

print("------------------------------------------------------------")  # 60個

try:  # 例外處理
    host = "hostname"  # 取得伺服器位址
    port = 25  # 取得通訊埠
    user = "david"  # 取得使用者名稱
    pw = "123456"  # 取得密碼
    fromaddr = "david@gmail.com"  # 取得發件人
    toaddr = "you@lion.mouse"  # 取得收件人
    subject = "Hello gmail"  # 取得主旨
    text = "aaaaaaaaa"
    msg = "From: %s\nTo: %s\nSubject: %s\n\n" % (  # 產生信件頭
        fromaddr,
        toaddr,
        subject,
    )
    msg = msg + text
    smtp = smtplib.SMTP(host, port)  # 連線伺服器
    smtp.set_debuglevel(1)  # 設定除錯等級
    smtp.login(user, pw)  # 登入伺服器
    smtp.sendmail(fromaddr, toaddr, msg)  # 傳送信件
    smtp.quit()  # 中斷伺服器
except Exception as e:
    print("傳送錯誤\n")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("smtplib SP")
print("------------------------------------------------------------")  # 60個
