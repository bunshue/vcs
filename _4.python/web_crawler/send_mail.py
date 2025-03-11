import sys

print("------------------------------------------------------------")  # 60個

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人
msg = "Subject: My first mail using Python\n\
Email from Python"  # 信件標題與內容
mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

sys.exit()

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人
msg = "Subject: My first mail using Python\n\
To: david@insighteyes.com\n\
Email from Python"  # 信件標題與內容
mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["bunshue@yahoo.com.tw", "david@insighteyes.com"]  # 設定收件人
msg = "Subject: Send Email to mutiple users\n\
Multiple users will reveive this Email."  # 信件標題與內容
mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["bunshue@yahoo.com.tw", "david@insighteyes.com"]  # 設定收件人
msg = "Subject: Send Email to mutiple users\n\
To: Everyone\n\
Multiple users will reveive this Email."  # 信件標題,收件人設定與內容
mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["bunshue@yahoo.com.tw", "david@insighteyes.com"]  # 設定收件人
msg = "Subject: Email with Cc\n\
To: david@insighteyes.com\n\
Cc: bunshue@yahoo.com.tw\n\
Multiple users will reveive this Email."  # 信件標題,收件人,副本與內容
mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["bunshue@yahoo.com.tw", "david@insighteyes.com"]  # 設定收件人
msg = "Subject: Assign the sender\n\
From: I Love Python\n\
To: bunshue@yahoo.com.tw\n\
Cc: david@insighteyes.com\n\
Multiple users will reveive this Email."  # 信件標題,收件人,副本與內容
mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/涼州詞.txt"

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人
msg = "Subject: Send the file contents\n\
To: david@insighteyes.com"

with open(filename) as fn:  # 讀取檔案內容
    mailContent = fn.read()
msg = msg + "\n" + mailContent  # 將msg與檔案內容結合

print("列印msg資料型態 : ", type(msg))  # 列印msg資料型態
print(msg)  # 列印msg內容

mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/涼州詞.txt"

import smtplib

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人
msg = "Subject: 中文信件標題\n\
To: david@insighteyes.com"

with open(filename) as fn:  # 讀取檔案內容
    mailContent = fn.read()
msg = msg + "\n" + mailContent  # 將msg與檔案內容結合

print("列印msg資料型態 : ", type(msg))  # 列印msg資料型態
print(msg)  # 列印msg內容

mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.text import MIMEText

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人

msg = MIMEText("傳送含中文字的郵件", "plain", "utf-8")
msg["Subject"] = "Email using MIMEText"
msg["To"] = "david@insighteyes.com"

print(type(msg))  # 列印msg的資料類型

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
from email.mime.text import MIMEText

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人

# 定義HTML文件
htmlstr = """
<!doctype html>
<html>
<head>
   <meta charset="utf-8">
   <title>Test.html</title>
</head>
<body>
李白    月下獨酌
花間一壺酒，
獨酌無雙親；
舉杯邀明月，
對影成三人。
</body>
</html>
"""
msg = MIMEText(htmlstr, "html", "utf-8")
msg["Subject"] = "傳送HTML內容信件"
msg["To"] = "david@insighteyes.com"

mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/涼州詞.txt"

import smtplib
from email.mime.text import MIMEText

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人

with open(filename, "rb") as fn:  # 讀取檔案內容
    mailContent = fn.read()
msg = MIMEText(mailContent, "base64", "utf-8")
msg["Content-Type"] = "application/octet-stream"
msg["Content-Disposition"] = "attachment; filename=filename"
msg["Subject"] = "傳送附加檔案"
msg["To"] = "david@insighteyes.com"

mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/涼州詞.txt"

import smtplib
from email.mime.text import MIMEText

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人

with open(filename, "r") as fn:  # 讀取檔案內容
    mailContent = fn.read()
msg = MIMEText(mailContent, "plain", "utf-8")

msg["Content-Disposition"] = "attachment; filename=filename"
msg["Subject"] = "傳送附加檔案"
msg["To"] = "david@insighteyes.com"

mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
mySMTP.ehlo()  # 啟動對話
mySMTP.starttls()  # 執行TLS加密
mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:  # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()  # 結束連線

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "Your_Password"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人

with open(filename, "rb") as fn:  # 讀取圖片內容
    mailPict = fn.read()
msg = MIMEImage(mailPict)
msg["Content-Type"] = "application/octet-stream"
msg["Content-Disposition"] = "attachment; filename=filename"
msg["Subject"] = "傳送圖片附加檔案"
msg["To"] = "david@insighteyes.com"

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

from_addr = "bunshue@gmail.com"  # 設定發信帳號
pwd = "abcde"  # 密碼
to_addr_list = ["david@insighteyes.com"]  # 設定收件人
msg = "Subject: My first mail using Python\n\
Email from Python"  # 信件標題與內容
try:
    mySMTP = smtplib.SMTP("smtp.gmail.com", 587)  # 執行連線
    mySMTP.ehlo()  # 啟動對話
    mySMTP.starttls()  # 執行TLS加密
    mySMTP.login(from_addr, pwd)  # 登入郵件伺服器
    mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
    print("發送郵件成功!")
    mySMTP.quit()  # 結束連線
except smtplib.SMTPException:
    print("發送郵件失敗!")

print("------------------------------------------------------------")  # 60個

import smtplib
from email.mime.text import MIMEText

# 設定發信帳號和密碼
from_addr = "bunshue@gmail.com"
pwd = "Your_Password"

to_addr_list = []

to_addr_list.append("mouse@taiwan.world")
to_addr_list.append("ox@taiwan.world")
to_addr_list.append("tiger@taiwan.world")

print(to_addr_list)

# SMTP 伺服器連線設定
smtp_server = "smtp.gmail.com"
smtp_port = 587

# 建立 SMTP 連線
mySMTP = smtplib.SMTP(smtp_server, smtp_port)
mySMTP.ehlo()
mySMTP.starttls()
mySMTP.login(from_addr, pwd)

# 發送郵件給所有會員
for to_addr in to_addr_list:
    msg = MIMEText("祝您2025年新年快樂!", "plain", "utf-8")
    msg["Subject"] = "2025年新年快樂"
    msg["From"] = from_addr
    msg["To"] = to_addr

    status = mySMTP.sendmail(from_addr, [to_addr], msg.as_string())
    if status == {}:
        print(f"成功發送到 {to_addr}")
    else:
        print(f"發送到 {to_addr} 失敗")

mySMTP.quit()  # 結束 SMTP 連線

print("------------------------------------------------------------")  # 60個

import imapclient
import pprint

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
pprint.pprint(imap.list_folders())

print("------------------------------------------------------------")  # 60個

import imapclient

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
imap.select_folder("INBOX", readonly=True)
UIDs = imap.search(["SINCE", "16-Nov-2023"])
print(UIDs)

print("------------------------------------------------------------")  # 60個

import imapclient
import pprint

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
imap.select_folder("INBOX", readonly=True)
UIDs = imap.search(["SINCE", "16-Nov-2023"])
raw_mail = imap.fetch(UIDs, ["BODY[]"])
pprint.pprint(raw_mail)

print("------------------------------------------------------------")  # 60個

import imapclient
from mailparser import parse_from_bytes

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
imap.select_folder("INBOX", readonly=True)
UIDs = imap.search(["SINCE", "16-Nov-2023"])
raw_mail = imap.fetch(UIDs, ["BODY[]"])

for uid, message_data in imap.fetch(raw_mail, "RFC822").items():
    email_message = parse_from_bytes(message_data[b"RFC822"])
    # 獲取寄件者和收件者訊息
    # 獲取寄件者訊息，假設寄件者是單一的
    from_email = email_message.from_  # 獲得寄件者郵件地址
    # 獲取收件者信息，可能有多個收件人
    to_emails = email_message.to

    print(f"Subject: {email_message.subject}")
    print(f"From: {from_email}")
    print(f"To: {to_emails}\n")  # to_emails內容是收件者的串列

print("------------------------------------------------------------")  # 60個

import imapclient
from mailparser import parse_from_bytes

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
imap.select_folder("INBOX", readonly=True)
UIDs = imap.search(["SINCE", "16-Nov-2023"])
raw_mail = imap.fetch(UIDs, ["BODY[]"])

for uid, message_data in imap.fetch(raw_mail, "RFC822").items():
    email_message = parse_from_bytes(message_data[b"RFC822"])
    # 獲取寄件者和收件者訊息
    # 獲取寄件者訊息，假設寄件者是單一的
    from_email = email_message.from_  # 獲得寄件者郵件地址
    # 獲取收件者信息，可能有多個收件人
    to_emails = email_message.to

    print(f"Subject: {email_message.subject}")
    print(f"From: {from_email[0][1]}")
    print(f"To: {to_emails[0][1]}\n")  # to_emails內容是收件者的串列

print("------------------------------------------------------------")  # 60個

import imapclient
from mailparser import parse_from_bytes

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
imap.select_folder("INBOX", readonly=True)
UIDs = imap.search(["SINCE", "16-Nov-2023"])
raw_mail = imap.fetch(UIDs, ["BODY[]"])

for uid, message_data in imap.fetch(raw_mail, "RFC822").items():
    email_message = parse_from_bytes(message_data[b"RFC822"])
    # 獲取寄件者和收件者訊息
    # 獲取寄件者訊息，假設寄件者是單一的
    from_email = email_message.from_  # 獲得寄件者郵件地址
    # 獲取收件者信息，可能有多個收件人
    to_emails = [to[1] for to in email_message.to]

    print(f"Subject: {email_message.subject}")
    print(f"From: {from_email[0][1]}")
    print(f"To: {', '.join(to_emails)}\n")  # to_emails內容是收件者的串列

print("------------------------------------------------------------")  # 60個

import imapclient
from mailparser import parse_from_bytes

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
imap.select_folder("INBOX", readonly=True)
UIDs = imap.search(["SINCE", "16-Nov-2023", "BODY", "Apple"])
raw_mail = imap.fetch(UIDs, ["BODY[]"])

for uid, message_data in imap.fetch(raw_mail, "RFC822").items():
    email_message = parse_from_bytes(message_data[b"RFC822"])
    # 獲取寄件者和收件者訊息
    # 獲取寄件者訊息，假設寄件者是單一的
    from_email = email_message.from_  # 獲得寄件者郵件地址
    # 獲取收件者信息，可能有多個收件人
    to_emails = [to[1] for to in email_message.to]

    print(f"Subject: {email_message.subject}")
    print(f"From: {from_email[0][1]}")
    print(f"To: {', '.join(to_emails)}\n")  # to_emails內容是收件者的串列

print("------------------------------------------------------------")  # 60個

import imapclient

imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login("bunshue@gmail.com", "Your_Password")
imap.select_folder("INBOX", readonly=False)
UIDs = imap.search(["SINCE", "16-Nov-2023", "BODY", "Apple"])
print(f"刪除前 : {UIDs}")
imap.delete_messages(UIDs)
print(f"執行delete_messages後 : {UIDs}")

print("------------------------------------------------------------")  # 60個

email_encoding = "utf-8"
email_addr_from = "david@insighteyes.com"
email_addr_from_password = ""
email_addr_from_nicknane = "王大頭"  # 寄件者顯示的名稱
email_addr_to = "david@insighteyes.com"
email_addr_to_nicknane = "尊敬的收件者"  # 收件者顯示的名稱
email_addr_cc = "bunshue@gmail.com"
mail_subject = "郵件標題"  # 郵件標題
mail_body = "郵件內容郵件內容郵件內容"  # 郵件內容

email_addr_from_password = ""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

# 附件
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    """
    # 無附件
    email_addr_from = 'david@insighteyes.com'
    receivers = ['david@insighteyes.com', 'david@insighteyes.com']
    message = MIMEText(mail_body, 'plain', 'utf-8')
    message['From'] = Header(email_addr_from_nicknane, 'utf-8')
    message['To'] = Header(email_addr_to_nicknane, 'utf-8')
    message['Subject'] = Header(mail_subject, 'utf-8')
    smtper = SMTP('www.hibox.hinet.net')
    smtper.login(email_addr_from, email_addr_from_password)
    smtper.sendmail(email_addr_from, receivers, message.as_string())
    """

    # 有附件
    # 創建一個帶附件的郵件消息對象
    message = MIMEMultipart()

    # 創建文本內容
    text_content = MIMEText(mail_body, "plain", "utf-8")
    message["Subject"] = Header(mail_subject, "utf-8")
    # 將文本內容添加到郵件消息對象中
    message.attach(text_content)

    # 讀取文件並將文件作為附件添加到郵件消息對象中
    with open("C:/_git/vcs/_4.python/_data/王之渙_涼州詞.txt", "rb") as f:
        txt = MIMEText(f.read(), "base64", "utf-8")
        txt["Content-Type"] = "text/plain"
        txt["Content-Disposition"] = "attachment; filename=王之渙_涼州詞.txt"
        message.attach(txt)
    # 讀取文件並將文件作為附件添加到郵件消息對象中
    with open(
        "C:/_git/vcs/_4.python/write_read_file/_4.office/data/python_add_chart1_line.xlsx",
        "rb",
    ) as f:
        xls = MIMEText(f.read(), "base64", "utf-8")
        xls["Content-Type"] = "application/vnd.ms-excel"
        xls["Content-Disposition"] = "attachment; filename=python_add_chart1_line.xlsx"
        message.attach(xls)

    # 創建SMTP對象
    smtper = SMTP("www.hibox.hinet.net")
    # 開啟安全連接
    # smtper.starttls()
    receivers = ["david@insighteyes.com", "david@insighteyes.com"]
    # 登錄到SMTP服務器
    # 請注意此處不是使用密碼而是郵件客戶端授權碼進行登錄
    # 對此有疑問的讀者可以聯繫自己使用的郵件服務器客服
    smtper.login(email_addr_from, email_addr_from_password)
    # 發送郵件
    smtper.sendmail(email_addr_from, receivers, message.as_string())
    # 與郵件服務器斷開連接
    smtper.quit()

    print("郵件發送完成!")


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
