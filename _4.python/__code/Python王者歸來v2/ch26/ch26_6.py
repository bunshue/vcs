# ch26_6.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = input('請輸入 %s 的密碼 : ' % from_addr)  # 要求輸入發信密碼
to_addr_list = ['cshung@deepstone.com.tw', 'jiinkwei@me.com']   # 設定收件人
msg = 'Subject: Assign the sender\n\
From: I Love Python\n\
To: cshung@deepstone.com.tw\n\
Cc: jiinkwei@me.com\n\
Multiple users will reveive this Email.'        # 信件標題,收件人,副本與內容
mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                            # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線

