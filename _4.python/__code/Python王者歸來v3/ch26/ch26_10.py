# ch26_10.py
import smtplib
from email.mime.text import MIMEText

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['jiinkwei@me.com']              # 設定收件人

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
msg = MIMEText(htmlstr, 'html', 'utf-8')
msg['Subject'] = '傳送HTML內容信件'
msg['To'] = 'jiinkwei@me.com'

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線

