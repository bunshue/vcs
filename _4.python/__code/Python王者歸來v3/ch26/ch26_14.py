# ch26_14.py
import smtplib
import csv
from email.mime.text import MIMEText

# 設定發信帳號和密碼
from_addr = 'cshung1961@gmail.com'
pwd = 'Your_Password'                           

# 讀取 CSV 檔案並提取電子郵件地址
to_addr_list = []
with open('member.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        to_addr_list.append(row['電子郵件'])

# SMTP 伺服器連線設定
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# 建立 SMTP 連線
mySMTP = smtplib.SMTP(smtp_server, smtp_port)
mySMTP.ehlo()
mySMTP.starttls()
mySMTP.login(from_addr, pwd)

# 發送郵件給所有會員
for to_addr in to_addr_list:
    msg = MIMEText('祝您2025年新年快樂!', 'plain', 'utf-8')
    msg['Subject'] = '2025年新年快樂'
    msg['From'] = from_addr
    msg['To'] = to_addr
    
    status = mySMTP.sendmail(from_addr, [to_addr], msg.as_string())
    if status == {}:
        print(f"成功發送到 {to_addr}")
    else:
        print(f"發送到 {to_addr} 失敗")

mySMTP.quit()           # 結束 SMTP 連線
