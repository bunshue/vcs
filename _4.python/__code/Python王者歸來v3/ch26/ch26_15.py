# ch26_15.py
import smtplib
import csv
from email.mime.text import MIMEText

# 設定發信帳號和密碼
from_addr = 'cshung1961@gmail.com'
pwd = 'Your_Password'

# SMTP 伺服器連線設定
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# 建立 SMTP 連線
mySMTP = smtplib.SMTP(smtp_server, smtp_port)
mySMTP.ehlo()
mySMTP.starttls()
mySMTP.login(from_addr, pwd)

# 讀取 CSV 檔案並提取未繳費會員的電子郵件地址
with open('member.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['會費'] != '已繳':
            to_addr = row['電子郵件']
            txt = '親愛的會員您好,提醒您尚未繳納會費,請於本月底前完成繳費,謝謝!'
            msg = MIMEText(txt, 'plain', 'utf-8')
            msg['Subject'] = '會費繳納提醒'
            msg['From'] = from_addr
            msg['To'] = to_addr
            
            status = mySMTP.sendmail(from_addr, [to_addr], msg.as_string())
            if status == {}:
                print(f"成功發送繳費提醒到 {to_addr}")
            else:
                print(f"發送繳費提醒到 {to_addr} 失敗")

mySMTP.quit()           # 結束 SMTP 連線
