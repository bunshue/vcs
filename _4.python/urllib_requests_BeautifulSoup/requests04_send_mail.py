#發送e-mail

import requests

def get_mailgun_key():
    filename = 'C:/_git/vcs/_1.data/______test_files1/_key/mailgun_key.txt'

    import os
    filename = os.path.abspath(filename)
    if not os.path.exists(filename): #檢查檔案是否存在
        print('MAILGUN_KEY 檔案不存在, 離開, 檔案 : ' + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, 'r')
    mailgun_key = fo.read()
    fo.close()

    length = len(mailgun_key)
    if length != 50:
        print('MAILGUN_KEY 錯誤, 離開')
        return ""
    return mailgun_key

def send_simple_message(email_nicknane, email_from, email_to, subject, body):
    mailgun_key = get_mailgun_key()
    length = len(mailgun_key)
    if length != 50:
        print('MAILGUN_KEY 錯誤, 離開')
        return ""
    
    return requests.post(
        "https://api.mailgun.net/v3/sandboxbfcaff2ba2ce446eb4972796eabec7da.mailgun.org/messages",
        auth=("api", mailgun_key),
        data={"from": "%s <%s>" % (email_nicknane, email_from),
              "to": [email_to],
              "subject": subject,
              "text": body })

#共用的郵件資訊
email_addr_from = "bunshue@gmail.com"
email_addr_from_password = 'XXXXXXXXXX'
email_addr_from_nicknane = "王大頭"    #寄件者顯示的名稱
email_addr_to = "david@insighteyes.com"
email_addr_to_nicknane = "尊敬的收件者"   #收件者顯示的名稱
email_addr_cc = "bunshue@gmail.com"

mail_subject = '測試郵件標題' #郵件標題
mail_body = '測試郵件內容測試郵件內容測試郵件內容測試郵件內容'  #郵件內容

ret = send_simple_message(email_addr_from_nicknane, email_addr_from, email_addr_to, mail_subject, mail_body)
print(ret)
                    

