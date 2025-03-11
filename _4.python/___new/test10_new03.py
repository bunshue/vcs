"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
"""
from threading import Thread


# 繼承Thread類創建自定義的線程類
class DownloadHanlder(Thread):

    def __init__(self, data):
        print(data)
        super().__init__()
        self.data = data

    def run(self):
        print("A")
        time.sleep(1000)


for _ in range(10):
    DownloadHanlder(_).start()

"""
print("------------------------------------------------------------")  # 60個

email_encoding = "utf-8"
email_addr_from = "david@insighteyes.com"
email_addr_from_password = ""
email_addr_from_nicknane = "王大頭"    # 寄件者顯示的名稱
email_addr_to = "david@insighteyes.com"
email_addr_to_nicknane = "尊敬的收件者"    # 收件者顯示的名稱
email_addr_cc = "bunshue@gmail.com"
mail_subject = "郵件標題"  # 郵件標題
mail_body = "郵件內容郵件內容郵件內容"    #郵件內容

email_addr_from_password = ""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

#附件
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
    text_content = MIMEText(mail_body, 'plain', 'utf-8')
    message['Subject'] = Header(mail_subject, 'utf-8')
    # 將文本內容添加到郵件消息對象中
    message.attach(text_content)

    # 讀取文件並將文件作為附件添加到郵件消息對象中
    with open('C:/_git/vcs/_4.python/_data/王之渙_涼州詞.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=王之渙_涼州詞.txt'
        message.attach(txt)
    # 讀取文件並將文件作為附件添加到郵件消息對象中
    with open('C:/_git/vcs/_4.python/write_read_file/_4.office/data/python_add_chart1_line.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=python_add_chart1_line.xlsx'
        message.attach(xls)
    
    # 創建SMTP對象
    smtper = SMTP('www.hibox.hinet.net')
    # 開啟安全連接
    # smtper.starttls()
    receivers = ['david@insighteyes.com', 'david@insighteyes.com']
    # 登錄到SMTP服務器
    # 請注意此處不是使用密碼而是郵件客戶端授權碼進行登錄
    # 對此有疑問的讀者可以聯繫自己使用的郵件服務器客服
    smtper.login(email_addr_from, email_addr_from_password)
    # 發送郵件
    smtper.sendmail(email_addr_from, receivers, message.as_string())
    # 與郵件服務器斷開連接
    smtper.quit()

    print('郵件發送完成!')


if __name__ == '__main__':
    main()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
