import monitor_module as m  # ←匯入自訂模組並更名為 m
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
m.send_gmail(gmail_addr, gmail_pwd, to_addrs, mime_text)  # ←寄出郵件
