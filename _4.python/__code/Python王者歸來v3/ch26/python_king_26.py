# ch26_1.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['jiinkwei@me.com']              # 設定收件人
msg = 'Subject: My first mail using Python\n\
Email from Python'                              # 信件標題與內容
mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                            # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_2.py

# ch26_2.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['jiinkwei@me.com']              # 設定收件人
msg = 'Subject: My first mail using Python\n\
To: jiinkwei@me.com\n\
Email from Python'                              # 信件標題與內容
mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_3.py

# ch26_3.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['service@deepwisdom.com.tw','jiinkwei@me.com']  # 設定收件人
msg = 'Subject: Send Email to mutiple users\n\
Multiple users will reveive this Email.'        # 信件標題與內容
mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_4.py

# ch26_4.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['service@deepwisdom.com.tw', 'jiinkwei@me.com'] # 設定收件人
msg = 'Subject: Send Email to mutiple users\n\
To: DeepWisdom AI Meeting Members\n\
Multiple users will reveive this Email.'        # 信件標題,收件人設定與內容
mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_5.py

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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_6.py

# ch26_6.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['service@deepwisdom.com.tw', 'jiinkwei@me.com'] # 設定收件人
msg = 'Subject: Assign the sender\n\
From: I Love Python\n\
To: service@deepwisdom.com.tw\n\
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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_7.py

# ch26_7.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['jiinkwei@me.com']              # 設定收件人
msg = 'Subject: Send the file contents\n\
To: jiinkwei@me.com'

with open('data26_7.txt') as fn:                # 讀取檔案內容
    mailContent = fn.read()
msg = msg + '\n' +  mailContent                 # 將msg與檔案內容結合

print("列印msg資料型態 : ", type(msg))          # 列印msg資料型態
print(msg)                                      # 列印msg內容

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                            # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_8.py

# ch26_8.py
import smtplib

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['jiinkwei@me.com']              # 設定收件人
msg = 'Subject: 中文信件標題\n\
To: jiinkwei@me.com'

with open('data26_7.txt') as fn:                # 讀取檔案內容
    mailContent = fn.read()
msg = msg + '\n' +  mailContent                 # 將msg與檔案內容結合

print("列印msg資料型態 : ", type(msg))          # 列印msg資料型態
print(msg)                                      # 列印msg內容

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                            # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg)  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch26\ch26_9.py

# ch26_9.py
import smtplib
from email.mime.text import MIMEText

from_addr = 'cshung1961@gmail.com'              # 設定發信帳號
pwd = 'Your_Password'                           # 密碼
to_addr_list = ['jiinkwei@me.com']              # 設定收件人

msg = MIMEText('傳送含中文字的郵件', 'plain', 'utf-8')
msg['Subject'] = 'Email using MIMEText'
msg['To'] = 'jiinkwei@me.com'

print(type(msg))                                # 列印msg的資料類型

mySMTP = smtplib.SMTP('smtp.gmail.com', 587)    # 執行連線
mySMTP.ehlo()                                   # 啟動對話
mySMTP.starttls()                               # 執行TLS加密               
mySMTP.login(from_addr, pwd)                    # 登入郵件伺服器
status = mySMTP.sendmail(from_addr, to_addr_list, msg.as_string())  # 執行發送信件
if status == {}:                                # 檢查是否發信成功
    print("發送郵件成功!")
mySMTP.quit()                                   # 結束連線


print("------------------------------------------------------------")  # 60個


