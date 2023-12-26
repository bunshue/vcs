# ch26_5.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['service@deepwisdom.com.tw', 'jiinkwei@me.com'] # 設定收件人
msg = 'Subject: Email with Cc\n\
To: jiinkwei@me.com\n\
Cc: service@deepwisdom.com.tw\n\
Multiple users will reveive this Email.'        # 信件標題,收件人,副本與內容
mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線

