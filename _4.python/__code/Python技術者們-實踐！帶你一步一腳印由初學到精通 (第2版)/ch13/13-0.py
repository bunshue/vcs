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


gmail_addr = '您的Gmail郵件地址'
gmail_pwd = '您的Gmail密碼'
to_addrs = ['第一個收件者的郵件網路', '第二個收件者的郵件網路']
send_gmail(gmail_addr, gmail_pwd, to_addrs, 'Subject:Hello\nTesting')
# ↑主旨   ↑內容
