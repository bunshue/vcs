# ch26_21.py
import imapclient
from mailparser import parse_from_bytes

imap = imapclient.IMAPClient('imap.gmail.com',ssl=True)
imap.login('cshung1961@gmail.com', 'Your_Password')
imap.select_folder('INBOX', readonly=True)
UIDs = imap.search(['SINCE', '16-Nov-2023'])
raw_mail = imap.fetch(UIDs, ['BODY[]'])

for uid, message_data in imap.fetch(raw_mail,'RFC822').items():
        email_message = parse_from_bytes(message_data[b'RFC822'])
        # 獲取寄件者和收件者訊息
        # 獲取寄件者訊息，假設寄件者是單一的
        from_email = email_message.from_        # 獲得寄件者郵件地址
        # 獲取收件者信息，可能有多個收件人
        to_emails = [to[1] for to in email_message.to]  
        
        print(f"Subject: {email_message.subject}")
        print(f"From: {from_email[0][1]}")
        print(f"To: {', '.join(to_emails)}\n")  # to_emails內容是收件者的串列







