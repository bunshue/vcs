# ch26_9.py
import smtplib
from email.mime.text import MIMEText

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = input('請輸入 %s 的密碼 : ' % from_addr)  # 要求輸入發信密碼
to_addr_list = ['cshung@deepstone.com.tw', 'jiinkwei@me.com']   # 設定收件人

msg = MIMEText('傳送含中文字的郵件', 'plain', 'utf-8')
msg['Subject'] = 'Email using MIMEText'
msg['From'] = '我愛Python'
msg['To'] = 'cshung@deepstone.com.tw'
msg['Cc'] = 'jiinkwei@me.com'

print(type(msg))                                # 列印msg的資料類型

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線

